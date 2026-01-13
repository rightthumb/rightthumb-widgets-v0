# autoproj/core.py

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Callable, Any
from pathlib import Path

from .storage import Storage
from .env import EnvConfig, EnvMode
from .executors import ExecutionBroker
from .models.session import Session
from .models.sprint import Sprint
from .models.task import Task


class AutoProjectManager:
    """
    Main orchestrator that:
    - manages sessions
    - creates sprints
    - runs tasks
    - calls GPT
    - coordinates environment + execution rules
    """

    def __init__(
        self,
        client,                   # your GPT client
        store: Storage,           # session/sprint/task store
        env: Optional[EnvConfig] = None,
        executor: Optional[ExecutionBroker] = None,
    ):
        self.client = client
        self.store = store

        self.env = env or EnvConfig(
            mode=EnvMode.NO_OS,
            project_root=Path.cwd(),
            allow_web=False,
            allow_package_install=False,
            allow_virtualization=False,
            env_label="default",
        )

        self.executor = executor or ExecutionBroker(self.env)

    # ----------------------------------------------------------------------------------

    def ensure_session(self, goal: str) -> Session:
        """Find existing matching session or create a new one."""
        sess = self.store.find_session_by_goal(goal)
        if sess:
            return sess
        return self.store.create_session(goal)

    # ----------------------------------------------------------------------------------

    def ensure_initial_sprint(self, session: Session) -> Sprint:
        """If the session has no sprint, create a default one."""
        sprints = self.store.get_sprints(session.id)
        if sprints:
            return sprints[0]

        # Create a simple default sprint (3 example tasks)
        tasks = [
            Task(description="Scan current folder for video files"),
            Task(description="Design threaded conversion interface"),
            Task(description="Outline retry strategy for failures"),
        ]
        return self.store.create_sprint(session.id, title="Initial Sprint", tasks=tasks)

    # ----------------------------------------------------------------------------------

    def run_next_task(self, session: Session, executor_fn: Callable[[Task], Any]) -> Optional[str]:
        """Run the next pending task from the first active sprint."""
        sprint = self.store.get_active_sprint(session.id)
        if not sprint:
            return None

        task = sprint.next_pending_task()
        if not task:
            # sprint complete
            sprint.status = "done"
            self.store.update_sprint(sprint)
            return None

        # Execute task
        result_text = executor_fn(task)

        # Log task result
        self.store.append_history(session.id, task.description, result_text)

        # Mark complete
        task.status = "done"
        self.store.update_sprint(sprint)

        return result_text
