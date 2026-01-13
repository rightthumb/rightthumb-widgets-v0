### filename: autoproj/codegen_store.py
from __future__ import annotations

import hashlib
import json
import sqlite3
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional

from .logging_system import BaseLogger
from .memory import MemoryStore
from .meta_cognition import MetaCognitionEngine
from .config import ModeName
from .tools.os_tools import OSExecutor, CommandResult


@dataclass
class CodeSnippet:
    """
    A single generated code snippet stored in the codegen database.
    """

    id: int
    name: str
    language: str
    code: str
    code_hash: str
    created_at: float
    description: Optional[str]
    created_by: Optional[str]
    last_used_at: Optional[float]
    use_count: int
    tags_json: Optional[str]


class CodeSnippetStore:
    """
    SQLite-backed store for generated code snippets and their executions.

    Schema:
      - code_snippets: one row per unique (name, code_hash)
      - snippet_executions: one row per execution of a snippet
    """

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._init_db()

    # ------------------------------------------------------------------ #
    # Internal helpers
    # ------------------------------------------------------------------ #

    def _connect(self) -> sqlite3.Connection:
        return sqlite3.connect(self.db_path)

    def _init_db(self) -> None:
        with self._connect() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS code_snippets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    language TEXT NOT NULL,
                    code TEXT NOT NULL,
                    code_hash TEXT NOT NULL,
                    created_at REAL NOT NULL,
                    description TEXT,
                    created_by TEXT,
                    tags_json TEXT,
                    last_used_at REAL,
                    use_count INTEGER NOT NULL DEFAULT 0,
                    UNIQUE(name, code_hash)
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS snippet_executions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    snippet_id INTEGER NOT NULL,
                    session_id TEXT,
                    task_description TEXT,
                    mode_name TEXT NOT NULL,
                    started_at REAL NOT NULL,
                    finished_at REAL NOT NULL,
                    returncode INTEGER NOT NULL,
                    stdout TEXT,
                    stderr TEXT,
                    notes TEXT,
                    FOREIGN KEY(snippet_id) REFERENCES code_snippets(id)
                )
                """
            )

    @staticmethod
    def _hash_code(code: str) -> str:
        return hashlib.sha256(code.encode("utf-8")).hexdigest()

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #

    def get_or_create_snippet(
        self,
        name: str,
        language: str,
        code: str,
        description: Optional[str] = None,
        created_by: Optional[str] = None,
        tags: Optional[Dict[str, Any]] = None,
    ) -> int:
        """
        Return an existing snippet id for (name, code_hash) or insert a new record.
        """
        code_hash = self._hash_code(code)
        now = time.time()
        tags_json = json.dumps(tags, ensure_ascii=False) if tags is not None else None

        with self._connect() as conn:
            cur = conn.execute(
                """
                SELECT id FROM code_snippets
                WHERE name = ? AND code_hash = ?
                """,
                (name, code_hash),
            )
            row = cur.fetchone()
            if row:
                return int(row[0])

            cur = conn.execute(
                """
                INSERT INTO code_snippets (
                    name, language, code, code_hash, created_at,
                    description, created_by, tags_json, last_used_at, use_count
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, NULL, 0)
                """,
                (name, language, code, code_hash, now, description, created_by, tags_json),
            )
            return int(cur.lastrowid)

    def record_execution(
        self,
        snippet_id: int,
        *,
        session_id: Optional[str],
        task_description: Optional[str],
        mode_name: ModeName,
        result: CommandResult,
        notes: Optional[str] = None,
    ) -> None:
        """
        Record one execution of a snippet and bump use_count / last_used_at.
        """
        started_at = result.started_at
        finished_at = result.finished_at
        with self._connect() as conn:
            conn.execute(
                """
                INSERT INTO snippet_executions (
                    snippet_id, session_id, task_description, mode_name,
                    started_at, finished_at, returncode, stdout, stderr, notes
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    snippet_id,
                    session_id,
                    task_description,
                    mode_name.value,
                    started_at,
                    finished_at,
                    result.returncode,
                    result.stdout,
                    result.stderr,
                    notes,
                ),
            )
            conn.execute(
                """
                UPDATE code_snippets
                SET last_used_at = ?, use_count = COALESCE(use_count, 0) + 1
                WHERE id = ?
                """,
                (finished_at, snippet_id),
            )


class PythonSnippetExecutor:
    """
    Handles execution of generated Python snippets.

    - Stores snippet in SQLite.
    - Writes it to a .py file under state_dir/generated_code.
    - Executes via OSExecutor.
    - Logs execution in CodeSnippetStore + MetaCognitionEngine.

    Guardrail:
    - Only allowed when mode_name == ModeName.GOD_MODE.
    """

    def __init__(
        self,
        store: CodeSnippetStore,
        os_executor: OSExecutor,
        logger: BaseLogger,
        meta: MetaCognitionEngine,
        mode_name: ModeName,
        state_dir: Path,
    ):
        self.store = store
        self.os_executor = os_executor
        self.logger = logger
        self.meta = meta
        self.mode_name = mode_name
        self.state_dir = state_dir
        self.generated_dir = self.state_dir / "generated_code"
        self.generated_dir.mkdir(parents=True, exist_ok=True)

    def run_snippet(
        self,
        *,
        name: str,
        code: str,
        session_id: Optional[str],
        project_goal: Optional[str],
        task_description: Optional[str] = None,
        description: Optional[str] = None,
        notes: Optional[str] = None,
    ) -> CommandResult:
        if self.mode_name != ModeName.GOD_MODE:
            raise PermissionError("Python snippet execution is only allowed in GOD_MODE")

        snippet_id = self.store.get_or_create_snippet(
            name=name,
            language="python",
            code=code,
            description=description,
            created_by="autoproj",
            tags={"kind": "generated_python"},
        )

        # Persist code to file under generated_code/
        safe_name = "".join(ch if ch.isalnum() or ch in ("_", "-") else "_" for ch in name).strip("_") or f"snippet_{snippet_id}"
        file_path = self.generated_dir / f"{safe_name}_{snippet_id}.py"
        file_path.write_text(code, encoding="utf-8")

        self.logger.info(
            "codegen",
            "Executing generated Python snippet",
            name=name,
            path=str(file_path),
            snippet_id=snippet_id,
            session_id=session_id,
        )

        # Execute via OSExecutor so capabilities & logging apply
        result = self.os_executor.run_command(
            ["python3", str(file_path)],
            cwd=self.generated_dir,
        )

        # Record in the codegen DB
        self.store.record_execution(
            snippet_id=snippet_id,
            session_id=session_id,
            task_description=task_description,
            mode_name=self.mode_name,
            result=result,
            notes=notes,
        )

        # Also record in metacognition memory
        summary = f"Executed Python snippet '{name}' (id={snippet_id}) with returncode={result.returncode}"
        self.meta.record_event(
            kind="code_exec",
            session_id=session_id,
            project_goal=project_goal,
            language="python",
            summary=summary,
            snippet_id=snippet_id,
            stdout_preview=result.stdout[:500],
            stderr_preview=result.stderr[:500],
        )

        return result
