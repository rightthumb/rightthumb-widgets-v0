"""
autoproj: Autonomous project manager framework.

Core components:
- Mode / capability configuration
- Environment detection
- Structured logging
- Memory & metacognition
- Session / sprint / task management
- OS and web-search tools
- Agent orchestrator and CLI
"""

from pathlib import Path
from typing import Optional

from .config import (
    ModeConfig,
    RuntimeConfig,
    CapabilityFlags,
    load_runtime_config,
)
from .logging_system import BaseLogger, FileLogger
from .env_detection import EnvironmentInfo, detect_environment
from .memory import MemoryStore, JsonMemoryStore, SQLiteMemoryStore
from .meta_cognition import MetaCognitionEngine
from .session import Task, Sprint, Session, SessionManager
from .tools.os_tools import OSExecutor
from .tools.web_search import WebSearchClient
from .agent import Agent

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
