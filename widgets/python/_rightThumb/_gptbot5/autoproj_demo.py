#!/usr/bin/env python3
"""
autoproj_demo.py

Small end-to-end demo for the autoproj framework:

- Creates (or reuses) a session for the goal:
    "Prototype threaded video/mp3 conversion helper"

- Ensures a simple sprint with 3 tasks exists for that session
- Runs tasks one by one using a pluggable executor
- Stops when the sprint is complete
- Prints a summary of all sessions at the end
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path
from typing import Callable, Any, Optional, Tuple

# These imports assume the package layout we’ve been using:
# autoproj/
#   __init__.py
#   models.py
#   storage.py
#   agent.py
#   modes.py
try:
    from autoproj.storage import ProjectStore
    from autoproj.agent import AutoProjectAgent
    from autoproj.modes import ExecutionMode
    from autoproj.models import Task, GPTSession
except ImportError as e:
    print("[ERROR] Could not import autoproj package:", e, file=sys.stderr)
    print("Make sure this file lives next to the 'autoproj' package folder.")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Simple “executor” – this is the only piece you need to swap later
# to hook in GPT, shell commands, etc.
# ---------------------------------------------------------------------------

def simple_executor(task: Task, ctx: dict[str, Any]) -> str:
    """
    Very dumb executor used for this demo.

    It just returns a text summary. In a real build, this is where you’d:
    - build a GPT prompt
    - call your GPT client
    - save any files from the GPT response
    - run shell commands if mode allows
    - log everything to SQLite / Mongo / whatever
    """
    print("\n=== Executing task ===")
    print(f"Session: {ctx['session'].id}")
    print(f"Goal:    {ctx['session'].goal}")
    print(f"Task:    {task.description}")
    print("======================\n")

    # This is where “real stuff” would happen.
    # For now, just echo.
    time.sleep(0.3)
    return f"Task executed: {task.description}"


# ---------------------------------------------------------------------------
# Helpers for this demo
# ---------------------------------------------------------------------------

GOAL = "Prototype threaded video/mp3 conversion helper"


def ensure_demo_session(agent: AutoProjectAgent, store: ProjectStore) -> GPTSession:
    """
    Find an existing session for GOAL or create a new one.
    Uses FILES_ONLY mode by default.
    """
    existing = None
    for s in store.list_sessions():
        if s.goal == GOAL:
            existing = s
            break

    if existing:
        print(f"[INFO] Reusing existing session: {existing.id}")
        return existing

    print("[INFO] Creating new session...")
    session = agent.create_session(
        goal=GOAL,
        mode=ExecutionMode.FILES_ONLY,
        parent_id=None,
    )
    print(f"[INFO] New session id: {session.id}")
    return session


def ensure_demo_sprint(agent: AutoProjectAgent, store: ProjectStore, session: GPTSession) -> None:
    """
    Ensure there is at least one sprint for the session.
    If no sprints exist, create a new one with 3 simple tasks.
    """
    sprints = store.list_sprints(session.id)
    if sprints:
        print(f"[INFO] Session {session.id} already has {len(sprints)} sprint(s).")
        return

    print(f"[INFO] Creating initial sprint for session {session.id}...")

    sprint_title = "Initial threaded video/mp3 conversion sprint"
    tasks = [
        "Scan current folder for .mp4 and .mkv files.",
        "Design a Python interface for threaded video->mp3 conversion using ffmpeg.",
        "Outline error logging and retry strategy for failed ffmpeg runs.",
    ]

    agent.create_sprint_with_tasks(
        session_id=session.id,
        title=sprint_title,
        task_descriptions=tasks,
    )

    print("[INFO] Sprint created with 3 tasks.")


def run_demo_loop(agent: AutoProjectAgent, store: ProjectStore, session: GPTSession) -> None:
    """
    Run tasks until the active sprint completes.

    Uses `agent.run_next_task` which is assumed to:
    - find the active sprint for the session
    - pick the next pending task
    - call the executor
    - mark task as done
    - mark sprint as done when no more pending tasks
    """
    print("\n=== Running demo task loop ===\n")

    # keep a simple safety guard so we don’t loop forever if something is wrong
    max_iterations = 50
    iterations = 0

    while iterations < max_iterations:
        iterations += 1

        ctx = {"session": session}

        task, result = agent.run_next_task(
            session_id=session.id,
            executor=simple_executor,
            context=ctx,
        )

        print("=== Task result ===")
        print(result)
        print()

        if task is None:
            # agent signals there is no active sprint / nothing to do
            print("(exiting because there is no active sprint)\n")
            break

    else:
        print("[WARN] Hit max_iterations safety guard; exiting loop.\n")


def print_sessions_summary(store: ProjectStore) -> None:
    """
    Print a JSON-ish summary of all sessions known to the store.
    """
    print("=== Sessions summary ===")
    for s in store.list_sessions():
        row = {
            "id": s.id,
            "goal": s.goal,
            "parent_id": s.parent_id,
            "mode_name": getattr(s.mode, "name", getattr(s.mode, "value", None)),
            "created_at": s.created_at,
            "updated_at": s.updated_at,
            "sprints": len(store.list_sprints(s.id)),
        }
        print(json.dumps(row, indent=2))


# ---------------------------------------------------------------------------
# main()
# ---------------------------------------------------------------------------

def main() -> None:
    # By default ProjectStore will use its own path (e.g. ~/.autoproj),
    # but if your implementation takes a base_dir you can do:
    #
    #   base_dir = Path.home() / ".autoproj"
    #   store = ProjectStore(base_dir=base_dir)
    #
    # For now we assume the no-arg constructor works (as in the CLI).
    store = ProjectStore()
    agent = AutoProjectAgent(store)

    session = ensure_demo_session(agent, store)
    ensure_demo_sprint(agent, store, session)
    run_demo_loop(agent, store, session)
    print_sessions_summary(store)


if __name__ == "__main__":
    main()
