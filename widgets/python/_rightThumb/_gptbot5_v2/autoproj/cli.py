### filename: autoproj/cli.py
from __future__ import annotations

import argparse
import json
from typing import Any, Optional

from .agent import Agent, AgentContext
from .session import Task


def make_executor(agent: Agent):
    """
    Build an executor function that can:
      - handle normal "Analyze goal..." style tasks
      - interpret special "tool:NAME {json}" tasks and route to tools
    """

    def executor(task: Task, ctx: AgentContext) -> str:
        text = task.description.strip()

        # Tool invocation syntax:
        #   tool:python_snippet.run {"name": "hello", "code": "print('hi')"}

        if text.startswith("tool:"):
            parts = text.split(" ", 1)
            tool_spec = parts[0]
            tool_name = tool_spec[len("tool:") :].strip()
            arg_json = parts[1].strip() if len(parts) > 1 else ""

            tool = agent.tools.get(tool_name)
            if not tool:
                return f"[ERROR] Tool not found: {tool_name}"

            kwargs = json.loads(arg_json) if arg_json else {}
            result = tool.func(ctx=ctx, **kwargs)
            return f"[TOOL {tool_name}] {result}"


        # if text.startswith("tool:"):
        #     parts = text.split(" ", 1)
        #     tool_spec = parts[0]
        #     tool_name = tool_spec[len("tool:") :].strip()
        #     arg_json = parts[1].strip() if len(parts) > 1 else ""

        #     tool = agent.tools.get(tool_name)
        #     if not tool:
        #         return f"[ERROR] Tool not found: {tool_name}"

        #     kwargs: dict[str, Any] = {}
        #     if arg_json:
        #         try:
        #             kwargs = json.loads(arg_json)
        #         except Exception as e:
        #             return f"[ERROR] Failed to parse tool arguments as JSON: {e}"

        #     # Call the tool; convention: func(*, ctx=..., **kwargs)
        #     result = tool.func(ctx=ctx, **kwargs)
        #     return f"[TOOL {tool_name}] {result}"

        # Default behavior: simple echo-style executor
        return f"Task executed: {task.description}"

    return executor


def cmd_init(agent: Agent, goal: str) -> int:
    ctx = agent.init_project(goal)
    print(
        json.dumps(
            {
                "session_id": ctx.session.id,
                "goal": ctx.session.goal,
            },
            indent=2,
        )
    )
    return 0


def cmd_list(agent: Agent) -> int:
    sessions = agent.list_sessions_summary()
    print(json.dumps(sessions, indent=2))
    return 0


def cmd_run_next(agent: Agent, session_id: str, loop: bool) -> int:
    ctx = agent.load_session(session_id)
    if not ctx:
        print(f"Session {session_id} not found")
        return 1

    exec_fn = make_executor(agent)

    def run_once() -> str:
        result = agent.run_next_task(ctx, exec_fn)
        # result is expected to be a string from the executor, or some status
        print("\n=== Task result ===")
        print(result)
        print()
        return str(result)

    if not loop:
        run_once()
        return 0

    # loop mode: keep going until sprint is done / no active sprint
    while True:
        result_text = run_once()
        # Very simple stop condition – refine if your Agent returns richer data
        if "No active sprint" in result_text:
            print("(exiting because there is no active sprint)")
            break

    # Optional: summarize at the end
    print("\n=== Sessions summary ===")
    for s in agent.list_sessions_summary():
        print(s)
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="autoproj",
        description="Autonomous project manager framework (Agent-based CLI).",
    )
    sub = parser.add_subparsers(dest="command")

    # autoproj init "Build threaded video conversion pipeline"
    p_init = sub.add_parser("init", help="Initialize a new project")
    p_init.add_argument("goal", help="Project goal (natural language)")

    # autoproj list
    sub.add_parser("list", help="List existing sessions")

    # autoproj run-next SESSION_ID [--loop]
    p_run = sub.add_parser("run-next", help="Run next task in a session")
    p_run.add_argument("session_id", help="Session ID to operate on")
    p_run.add_argument(
        "--loop",
        action="store_true",
        help="Keep running tasks until the sprint completes / no active sprint.",
    )

    args = parser.parse_args(argv)

    # For now, Agent is our high-level orchestrator
    agent = Agent()

    if args.command == "init":
        return cmd_init(agent, args.goal)

    if args.command == "list":
        return cmd_list(agent)

    if args.command == "run-next":
        return cmd_run_next(agent, args.session_id, args.loop)

    # No subcommand
    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
