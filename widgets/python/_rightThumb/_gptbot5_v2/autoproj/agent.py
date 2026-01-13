### filename: autoproj/agent.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Optional, List, Any, Dict

from .config import RuntimeConfig, load_runtime_config, ModeName
from .env_detection import detect_environment
from .logging_system import BaseLogger, FileLogger
from .memory import JsonMemoryStore, SQLiteMemoryStore, MemoryStore
from .meta_cognition import MetaCognitionEngine
from .session import SessionManager, Session, Sprint, Task
from .tools.os_tools import OSExecutor
from .tools.web_search import WebSearchClient
from .tools.registry import Tool, ToolRegistry
from .codegen_store import CodeSnippetStore, PythonSnippetExecutor


@dataclass
class AgentContext:
    """
    Lightweight struct for per-session context.
    """
    session: Session
    env_summary: str


class Agent:
    """
    Core orchestrator for autonomous project management.

    This is intentionally generic: you can plug in your own GPT client / terminal
    proxy / socket server on top of this.
    """

    def __init__(
        self,
        runtime_config: Optional[RuntimeConfig] = None,
        logger: Optional[BaseLogger] = None,
        state_dir: Optional[Path] = None,
        memory_store: Optional[MemoryStore] = None,
    ):
        # Load runtime config (modes, capabilities, paths, etc.)
        self.config: RuntimeConfig = runtime_config or load_runtime_config()

        # Decide where to store sessions / memory / logs
        if state_dir is not None:
            self.state_dir = Path(state_dir)
        elif getattr(self.config, "state_dir", None) is not None:
            self.state_dir = Path(self.config.state_dir)
        else:
            self.state_dir = Path.home() / ".autoproj"

        self.state_dir.mkdir(parents=True, exist_ok=True)

        # Session manager
        self.session_manager = SessionManager(self.state_dir)

        # Memory + meta-cognition
        self.memory_store: MemoryStore = memory_store or self._make_memory_store()
        self.meta = MetaCognitionEngine(self.memory_store)

        # Logging
        self.logger: BaseLogger = logger or FileLogger(self.state_dir / "autoproj.log")

        # Environment detection
        self.env_info = detect_environment()

        # OS + web tools – used by your higher-level executor
        self.os = OSExecutor(
            capabilities=self.config.capabilities,
            logger=self.logger,
            project_root=self.config.project_root,
        )
        self.web = WebSearchClient(
            api_key=self.config.web_search_api_key,
            endpoint=self.config.web_search_endpoint,
            capabilities=self.config.capabilities,
            logger=self.logger,
        )

        # Tool registry
        self.tools = ToolRegistry()
        self._register_builtin_tools()

        # Code generation store + executor (GOD_MODE-only execution)
        self.code_store = CodeSnippetStore(self.state_dir / "codegen.sqlite")
        self.python_executor = PythonSnippetExecutor(
            store=self.code_store,
            os_executor=self.os,
            logger=self.logger,
            meta=self.meta,
            mode_name=self.config.mode.name,
            state_dir=self.state_dir,
        )

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #

    def _make_memory_store(self) -> MemoryStore:
        backend = getattr(self.config, "memory_backend", "json")
        if backend == "sqlite":
            return SQLiteMemoryStore(self.state_dir / "memory.sqlite")
        # default JSON (append-only log)
        return JsonMemoryStore(self.state_dir / "memory.jsonl")

    def _register_builtin_tools(self) -> None:
        """
        Register a small set of built-in tools.

        You can expand this over time; for now we include:
          - python_snippet.run: store+execute generated Python code (GOD_MODE only)
        """

        def run_python_snippet_tool(
            *,
            ctx: AgentContext,
            name: str,
            code: str,
            description: Optional[str] = None,
            notes: Optional[str] = None,
        ) -> Dict[str, Any]:
            """
            Store & execute a Python snippet via the codegen subsystem.
            """
            result = self.run_generated_python(
                ctx=ctx,
                name=name,
                code=code,
                description=description,
                notes=notes,
            )
            return {
                "returncode": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr,
            }

        self.tools.register(
            Tool(
                name="python_snippet.run",
                description="Store and execute a generated Python snippet (GOD_MODE only).",
                func=run_python_snippet_tool,
                requires_god_mode=True,
            )
        )

    # ------------------------------------------------------------------ #
    # Public helpers for code generation
    # ------------------------------------------------------------------ #

    def run_generated_python(
        self,
        ctx: AgentContext,
        name: str,
        code: str,
        description: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> CommandResult:
        """
        Convenience wrapper around PythonSnippetExecutor.

        Stores the snippet in the codegen DB and executes it (GOD_MODE only),
        recording executions and meta-cognition events.
        """
        return self.python_executor.run_snippet(
            name=name,
            code=code,
            session_id=ctx.session.id,
            project_goal=ctx.session.goal,
            task_description=None,
            description=description,
            notes=notes,
        )

    # ------------------------------------------------------------------ #
    # Session lifecycle
    # ------------------------------------------------------------------ #

    def init_project(self, goal: str) -> AgentContext:
        # Mode name can be an enum, string, etc. – normalize to string
        mode_name = getattr(self.config.mode, "name", None)
        if hasattr(mode_name, "value"):
            mode_name_str = mode_name.value
        elif isinstance(mode_name, str):
            mode_name_str = mode_name
        else:
            mode_name_str = "FILES_ONLY"

        session = self.session_manager.create_session(
            goal=goal,
            mode_name=mode_name_str,
        )

        env_summary = (
            f"os={self.env_info.platform} "
            f"wsl={self.env_info.is_wsl} "
            f"docker={self.env_info.is_docker} "
            f"distro={self.env_info.distro_id}"
        )

        self.logger.info(
            "agent",
            "Initialized project",
            goal=goal,
            session_id=session.id,
        )

        self.meta.record_event(
            kind="project_init",
            session_id=session.id,
            project_goal=goal,
            language=None,
            summary=f"Project created with goal: {goal}",
            env=env_summary,
        )

        return AgentContext(session=session, env_summary=env_summary)

    def load_session(self, session_id: str) -> Optional[AgentContext]:
        session = self.session_manager.load_session(session_id)
        if not session:
            return None

        env_summary = (
            f"os={self.env_info.platform} "
            f"wsl={self.env_info.is_wsl} "
            f"docker={self.env_info.is_docker} "
            f"distro={self.env_info.distro_id}"
        )
        return AgentContext(session=session, env_summary=env_summary)

    def list_sessions_summary(self) -> List[dict]:
        out: List[dict] = []
        for s in self.session_manager.list_sessions():
            out.append(
                {
                    "id": s.id,
                    "goal": s.goal,
                    "parent_id": s.parent_id,
                    "mode_name": s.mode_name,
                    "created_at": s.created_at,
                    "updated_at": s.updated_at,
                    "sprints": len(s.sprints),
                }
            )
        return out

    # ------------------------------------------------------------------ #
    # Sprint / task logic
    # ------------------------------------------------------------------ #

    def create_sprint_from_text(self, session: Session, title: str) -> Sprint:
        """
        Very simple initial sprint decomposition based on the project goal.
        You can later swap this for a GPT-based planner.
        """
        goal = session.goal
        default_tasks = [
            f"Analyze goal: {goal}",
            f"Design initial plan for: {goal}",
            f"Implement first working prototype for: {goal}",
        ]
        sprint = Sprint(
            title=title,
            status="active",
            tasks=[Task(description=t) for t in default_tasks],
        )
        return sprint

    def run_next_task(
        self,
        ctx: AgentContext,
        executor: Callable[[Task, AgentContext], str],
    ) -> str:
        """
        Run the next pending task for this session.

        Behavior:
        - If there is no active sprint, automatically create an initial sprint
          from the project goal and attach it to the session.
        - If the active sprint has no pending tasks, mark it done and report completion.
        - Otherwise, run the first pending task via the provided executor.
        """
        session = ctx.session

        # 1) Ensure there is an active sprint
        sprint = self.session_manager.get_active_sprint(session)
        if sprint is None:
            sprint = self.create_sprint_from_text(
                session,
                f"Initial sprint for goal: {session.goal}",
            )
            self.session_manager.add_sprint(session, sprint)
            self.session_manager.save_session(session)
            sprint = self.session_manager.get_active_sprint(session)

        if sprint is None:
            # Should basically never happen now
            return "No active sprint (even after auto-create)."

        # 2) Find pending task
        pending = [t for t in sprint.tasks if getattr(t, "status", "pending") == "pending"]
        if not pending:
            sprint.status = "done"
            self.session_manager.complete_sprint_if_done(session)
            self.session_manager.save_session(session)
            return f"Sprint '{sprint.title}' completed. No remaining tasks."

        task = pending[0]

        self.logger.info(
            "agent",
            "Running task",
            session_id=session.id,
            sprint=sprint.title,
            task=task.description,
        )

        # 3) Execute the task via provided executor
        try:
            result = executor(task, ctx)
        except Exception as e:
            self.logger.error(
                "agent",
                "Task execution failed",
                error=str(e),
                task=task.description,
                session_id=session.id,
            )
            self.meta.record_error(
                session_id=session.id,
                project_goal=session.goal,
                language=None,
                error_message=f"Error while executing task: {task.description}",
                error=str(e),
            )
            raise

        # 4) Mark task done and persist
        task.status = "done"
        if hasattr(task, "notes") and isinstance(task.notes, list):
            task.notes.append(str(result))

        self.session_manager.save_session(session)

        self.meta.record_solution(
            session_id=session.id,
            project_goal=session.goal,
            language=None,
            summary=f"Completed task: {task.description}",
            result=str(result),
        )
        self.session_manager.complete_sprint_if_done(session)

        return f"Task executed: {task.description}\n\n{result}"
