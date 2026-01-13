from __future__ import annotations

import argparse
import json
from typing import Any, Optional

from .agent import Agent, AgentContext
from .session import Task


def _dummy_executor(task: Task, ctx: AgentContext) -> str:
    """
    Simple executor used by the CLI for now.

    Later you can swap this out for a real GPT-backed executor that:
    - Plans detailed steps
    - Modifies files via OSExecutor
    - Runs shell commands safely
    - Uses web search when allowed
    - Logs everything to your meta-cognition / memory systems
    """
    return f"Task executed: {task.description}"


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

    def run_once() -> str:
        result = agent.run_next_task(ctx, _dummy_executor)
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
