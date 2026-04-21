from __future__ import annotations

import json
import threading
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Protocol


@dataclass
class LogEvent:
    timestamp: float
    level: str
    component: str
    message: str
    data: Dict[str, Any]

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)


class BaseLogger(Protocol):
    """
    Abstract logger interface. Implementations should be thread-safe.
    """

    def log(self, level: str, component: str, message: str, **data: Any) -> None:
        ...

    def debug(self, component: str, message: str, **data: Any) -> None:
        self.log("DEBUG", component, message, **data)

    def info(self, component: str, message: str, **data: Any) -> None:
        self.log("INFO", component, message, **data)

    def warning(self, component: str, message: str, **data: Any) -> None:
        self.log("WARNING", component, message, **data)

    def error(self, component: str, message: str, **data: Any) -> None:
        self.log("ERROR", component, message, **data)


class FileLogger(BaseLogger):
    """
    Simple JSONL file logger.
    """

    def __init__(self, log_file: Path):
        self.log_file = log_file
        self._lock = threading.Lock()
        self.log_file.parent.mkdir(parents=True, exist_ok=True)

    def log(self, level: str, component: str, message: str, **data: Any) -> None:
        event = LogEvent(
            timestamp=time.time(),
            level=level,
            component=component,
            message=message,
            data=data,
        )
        line = event.to_json()
        with self._lock:
            with self.log_file.open("a", encoding="utf-8") as f:
                f.write(line + "\n")


class NullLogger(BaseLogger):
    """
    Logger that discards all events.
    """

    def log(self, level: str, component: str, message: str, **data: Any) -> None:
        return


class SQLiteLogger(FileLogger):
    """
    Minimal placeholder that reuses FileLogger behavior.
    Replace with real SQLite logging if needed.
    """

    def __init__(self, db_path: Path):
        super().__init__(db_path.with_suffix(".log.jsonl"))
