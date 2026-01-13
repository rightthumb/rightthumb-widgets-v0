from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol

from ..config import CapabilityFlags
from ..logging_system import BaseLogger


@dataclass
class CommandResult:
    command: List[str]
    cwd: Path
    returncode: int
    stdout: str
    stderr: str


class ApprovalHook(Protocol):
    def __call__(self, command: List[str], cwd: Path) -> bool:
        ...


class OSExecutor:
    """
    Subprocess and file operations gatekept by capability flags.
    """

    def __init__(
        self,
        capabilities: CapabilityFlags,
        logger: BaseLogger,
        project_root: Path,
        approval_hook: Optional[ApprovalHook] = None,
    ):
        self.capabilities = capabilities
        self.logger = logger
        self.project_root = project_root
        self.approval_hook = approval_hook

    def _ensure_within_project(self, path: Path) -> Path:
        if not self.capabilities.stay_in_project_root:
            return path
        resolved = path.resolve()
        if not str(resolved).startswith(str(self.project_root.resolve())):
            raise PermissionError(f"Path {resolved} is outside project root {self.project_root}")
        return resolved

    def run_command(
        self,
        command: List[str],
        cwd: Optional[Path] = None,
        timeout: Optional[int] = None,
        env: Optional[Dict[str, str]] = None,
    ) -> CommandResult:
        if not self.capabilities.can_run_subprocess:
            raise PermissionError("Subprocess execution not allowed in current mode")

        cwd = cwd or self.project_root
        cwd = self._ensure_within_project(cwd)

        if self.capabilities.requires_command_approval and self.approval_hook:
            allowed = self.approval_hook(command, cwd)
            if not allowed:
                self.logger.warning(
                    "os_tools",
                    "Command execution denied by approval hook",
                    command=command,
                    cwd=str(cwd),
                )
                raise PermissionError("Command execution denied by approval hook")

        self.logger.info(
            "os_tools",
            "Executing command",
            command=command,
            cwd=str(cwd),
        )

        proc = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        try:
            stdout, stderr = proc.communicate(timeout=timeout)
        except subprocess.TimeoutExpired:
            proc.kill()
            stdout, stderr = proc.communicate()
            self.logger.error(
                "os_tools",
                "Command timed out",
                command=command,
                cwd=str(cwd),
            )
            raise

        result = CommandResult(
            command=command,
            cwd=cwd,
            returncode=proc.returncode,
            stdout=stdout,
            stderr=stderr,
        )

        self.logger.info(
            "os_tools",
            "Command finished",
            command=command,
            cwd=str(cwd),
            returncode=proc.returncode,
        )
        return result

    def read_text(self, path: Path, encoding: str = "utf-8") -> str:
        if not self.capabilities.can_read_files:
            raise PermissionError("File reads not allowed in current mode")
        path = self._ensure_within_project(path)
        text = path.read_text(encoding=encoding)
        self.logger.debug("os_tools", "Read file", path=str(path), size=len(text))
        return text

    def write_text(self, path: Path, text: str, encoding: str = "utf-8") -> None:
        if not self.capabilities.can_write_files:
            raise PermissionError("File writes not allowed in current mode")
        path = self._ensure_within_project(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding=encoding)
        self.logger.debug("os_tools", "Wrote file", path=str(path), size=len(text))
