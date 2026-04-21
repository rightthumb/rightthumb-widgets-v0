from __future__ import annotations

import json
import sqlite3
import threading
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol


@dataclass
class MemoryEvent:
    """
    A single learning event for metacognition.
    """

    timestamp: float
    kind: str
    session_id: Optional[str]
    project_goal: Optional[str]
    language: Optional[str]
    summary: str
    metadata: Dict[str, Any]


class MemoryStore(Protocol):
    """
    Abstract interface for memory storage.
    """

    def record(self, event: MemoryEvent) -> None:
        ...

    def query(
        self,
        kind: Optional[str] = None,
        limit: int = 50,
        session_id: Optional[str] = None,
    ) -> List[MemoryEvent]:
        ...


class JsonMemoryStore(MemoryStore):
    """
    File-based JSONL memory store. Simple but robust.
    """

    def __init__(self, path: Path):
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()

    def record(self, event: MemoryEvent) -> None:
        line = json.dumps(asdict(event), ensure_ascii=False)
        with self._lock:
            with self.path.open("a", encoding="utf-8") as f:
                f.write(line + "\n")

    def query(
        self,
        kind: Optional[str] = None,
        limit: int = 50,
        session_id: Optional[str] = None,
    ) -> List[MemoryEvent]:
        results: List[MemoryEvent] = []
        if not self.path.exists():
            return results
        with self.path.open("r", encoding="utf-8") as f:
            for line in reversed(list(f)):
                try:
                    obj = json.loads(line)
                    ev = MemoryEvent(**obj)
                    if kind and ev.kind != kind:
                        continue
                    if session_id and ev.session_id != session_id:
                        continue
                    results.append(ev)
                    if len(results) >= limit:
                        break
                except Exception:
                    continue
        return results


class SQLiteMemoryStore(MemoryStore):
    """
    SQLite-based memory store. Good for simple relational queries.
    """

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._lock = threading.Lock()
        self._init_db()

    def _init_db(self) -> None:
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS memory_events (
                    ts REAL,
                    kind TEXT,
                    session_id TEXT,
                    project_goal TEXT,
                    language TEXT,
                    summary TEXT,
                    metadata TEXT
                )
                """
            )

    def record(self, event: MemoryEvent) -> None:
        with self._lock, sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT INTO memory_events (
                    ts, kind, session_id, project_goal, language, summary, metadata
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    event.timestamp,
                    event.kind,
                    event.session_id,
                    event.project_goal,
                    event.language,
                    event.summary,
                    json.dumps(event.metadata, ensure_ascii=False),
                ),
            )

    def query(
        self,
        kind: Optional[str] = None,
        limit: int = 50,
        session_id: Optional[str] = None,
    ) -> List[MemoryEvent]:
        sql = "SELECT ts, kind, session_id, project_goal, language, summary, metadata FROM memory_events"
        clauses = []
        params: List[Any] = []
        if kind:
            clauses.append("kind = ?")
            params.append(kind)
        if session_id:
            clauses.append("session_id = ?")
            params.append(session_id)
        if clauses:
            sql += " WHERE " + " AND ".join(clauses)
        sql += " ORDER BY ts DESC LIMIT ?"
        params.append(limit)

        results: List[MemoryEvent] = []
        with sqlite3.connect(self.db_path) as conn:
            for row in conn.execute(sql, params):
                ts, k, sid, goal, lang, summary, metadata_json = row
                try:
                    metadata = json.loads(metadata_json) if metadata_json else {}
                except Exception:
                    metadata = {}
                results.append(
                    MemoryEvent(
                        timestamp=ts,
                        kind=k,
                        session_id=sid,
                        project_goal=goal,
                        language=lang,
                        summary=summary,
                        metadata=metadata,
                    )
                )
        return results
