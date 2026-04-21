"""
autoproj: Autonomous project manager framework.

Provides:
- Mode / capability configuration
- Environment detection
- Logging system
- Memory & metacognition
- Session / sprint / task management
- OS and web-search tools
- Core Agent orchestrator
"""

from .config import ModeConfig, RuntimeConfig, CapabilityFlags, load_runtime_config
from .logging_system import BaseLogger, FileLogger
from .env_detection import EnvironmentInfo, detect_environment
from .memory import MemoryStore, JsonMemoryStore, SQLiteMemoryStore
from .meta_cognition import MetaCognitionEngine
from .session import Task, Sprint, Session, SessionManager
from .tools.os_tools import OSExecutor
from .tools.web_search import WebSearchClient
from .agent import Agent

from .env import EnvConfig, EnvMode
from .executors import ExecutionBroker
from typing import Optional

class AutoProjectManager:
    def __init__(
        self,
        client,            # your GPTClient / OpenAI client
        store,             # your Storage / SessionStore
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



__all__ = [
    "ModeConfig",
    "RuntimeConfig",
    "CapabilityFlags",
    "load_runtime_config",
    "BaseLogger",
    "FileLogger",
    "EnvironmentInfo",
    "detect_environment",
    "MemoryStore",
    "JsonMemoryStore",
    "SQLiteMemoryStore",
    "MetaCognitionEngine",
    "Task",
    "Sprint",
    "Session",
    "SessionManager",
    "OSExecutor",
    "WebSearchClient",
    "Agent",
]
