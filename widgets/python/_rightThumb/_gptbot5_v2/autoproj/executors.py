# autoproj/executors.py

from __future__ import annotations

import subprocess
import shlex
from dataclasses import dataclass
from typing import List, Optional

# Remove invalid import:
# from . import storage  

from .logging_system import BaseLogger, NullLogger



# from __future__ import annotations
# import subprocess
# import time
# from dataclasses import dataclass
# from pathlib import Path
# from typing import List, Dict, Any, Optional

# from .env import EnvConfig, EnvMode


# from .logging_system import BaseLogger, FileLogger, NullLogger, SQLiteLogger
# from .memory import MemoryStore, JsonMemoryStore, SQLiteMemoryStore



@dataclass
class CommandResult:
    cmd: List[str]
    cwd: str
    returncode: int
    stdout: str
    stderr: str
    started_at: float
    finished_at: float


class ExecutionError(RuntimeError):
    pass


class ExecutionBroker:
    """
    Central place where ALL shell commands go through.
    This is where we enforce:
    - NO_OS / SAFE_OS / GOD_MODE
    - project_root scoping
    - logging
    """

    def __init__(self, env: EnvConfig, session_id: Optional[str] = None):
        self.env = env
        self.session_id = session_id

    # ------------ public API ------------

    def run(self, cmd: List[str], cwd: Optional[str | Path] = None) -> CommandResult:
        """
        Run a shell command according to the environment rules.
        """
        cwd_path = Path(cwd or self.env.project_root).resolve()

        # basic path policy: in SAFE_OS you must stay inside project_root
        if self.env.mode == EnvMode.SAFE_OS and not self.env.in_project_tree(cwd_path):
            raise ExecutionError(f"SAFE_OS: cwd {cwd_path} is outside project_root {self.env.project_root}")

        # in NO_OS mode, deny everything
        if self.env.mode == EnvMode.NO_OS:
            raise ExecutionError("NO_OS mode: command execution is disabled")

        # you can add extra restrictions here, e.g. disallow rm -rf /
        if self._is_obviously_dangerous(cmd):
            raise ExecutionError(f"Command looks too dangerous: {cmd!r}")

        started_at = time.time()
        proc = subprocess.run(
            cmd,
            cwd=str(cwd_path),
            capture_output=True,
            text=True,
        )
        finished_at = time.time()

        result = CommandResult(
            cmd=cmd,
            cwd=str(cwd_path),
            returncode=proc.returncode,
            stdout=proc.stdout,
            stderr=proc.stderr,
            started_at=started_at,
            finished_at=finished_at,
        )

        self._log_command(result)
        return result

    # ------------ helpers ------------

    @staticmethod
    def _is_obviously_dangerous(cmd: List[str]) -> bool:
        """
        Tiny sanity check.
        You can expand this as you see fit.
        """
        if not cmd:
            return True

        if cmd[0] == "rm":
            # protect against rm -rf / and friends even in god mode
            forbidden = {"/", "/*", "--no-preserve-root"}
            if any(part in forbidden for part in cmd[1:]):
                return True

        return False

    def _log_command(self, result: CommandResult) -> None:
        """
        Record the command into your project/session log so the
        meta-learning system can later embed & learn from it.
        """
        try:
            store = storage.get_store()  # whatever we used earlier for sessions/sprints
        except Exception:
            # fail safely if storage is not ready
            return

        log_record: Dict[str, Any] = {
            "type": "os_command",
            "session_id": self.session_id,
            "env_mode": self.env.mode.name,
            "env_label": self.env.env_label,
            "cmd": result.cmd,
            "cwd": result.cwd,
            "returncode": result.returncode,
            "stdout": result.stdout[:4000],  # clip to keep storage reasonable
            "stderr": result.stderr[:4000],
            "started_at": result.started_at,
            "finished_at": result.finished_at,
        }

        # this assumes you have some generic log API in storage;
        # if not, we can wire it later.
        store.append_log(log_record)
