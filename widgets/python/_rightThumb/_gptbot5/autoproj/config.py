from __future__ import annotations

import os
from dataclasses import dataclass
from enum import Enum, auto
from pathlib import Path
from typing import Optional


class ModeName(str, Enum):
    NO_OS = "NO_OS"
    FILES_ONLY = "FILES_ONLY"
    SAFE_OS = "SAFE_OS"
    GOD_MODE = "GOD_MODE"
    NO_NET = "NO_NET"
    WEB_SEARCH = "WEB_SEARCH"
    SOCKET_UI = "SOCKET_UI"
    TERMINAL_PROXY = "TERMINAL_PROXY"


@dataclass
class CapabilityFlags:
    """
    Capability flags derived from the current mode.
    """

    can_read_files: bool = True
    can_write_files: bool = True
    can_run_subprocess: bool = False
    can_use_network: bool = False
    requires_command_approval: bool = False
    stay_in_project_root: bool = True

    @classmethod
    def for_mode(cls, mode: ModeName) -> "CapabilityFlags":
        if mode == ModeName.NO_OS:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=False,
                can_use_network=False,
                requires_command_approval=False,
                stay_in_project_root=True,
            )
        if mode == ModeName.FILES_ONLY:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=False,
                can_use_network=False,
                requires_command_approval=False,
                stay_in_project_root=True,
            )
        if mode == ModeName.SAFE_OS:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=True,
                can_use_network=False,
                requires_command_approval=True,
                stay_in_project_root=True,
            )
        if mode == ModeName.GOD_MODE:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=True,
                can_use_network=True,
                requires_command_approval=False,
                stay_in_project_root=False,
            )
        if mode == ModeName.NO_NET:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=True,
                can_use_network=False,
                requires_command_approval=True,
                stay_in_project_root=True,
            )
        if mode == ModeName.WEB_SEARCH:
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=False,
                can_use_network=True,
                requires_command_approval=False,
                stay_in_project_root=True,
            )
        if mode in (ModeName.SOCKET_UI, ModeName.TERMINAL_PROXY):
            return cls(
                can_read_files=True,
                can_write_files=True,
                can_run_subprocess=True,
                can_use_network=True,
                requires_command_approval=True,
                stay_in_project_root=True,
            )

        return cls.for_mode(ModeName.FILES_ONLY)


@dataclass
class ModeConfig:
    name: ModeName
    capabilities: CapabilityFlags


@dataclass
class RuntimeConfig:
    """
    Runtime config for the autoproj Agent and subsystems.
    """

    mode: ModeConfig
    project_root: Path
    logs_dir: Path
    state_dir: Path
    memory_backend: str = "json"  # "json" | "sqlite" | "advanced"
    web_search_api_key: Optional[str] = None
    web_search_endpoint: Optional[str] = None

    @property
    def capabilities(self) -> CapabilityFlags:
        return self.mode.capabilities


def load_runtime_config(
    mode_name: Optional[str] = None,
    project_root: Optional[str | Path] = None,
    base_dir: Optional[str | Path] = None,
) -> RuntimeConfig:
    """
    Load runtime configuration from optional arguments and environment variables.
    """

    env_mode = (mode_name or os.getenv("AUTOPROJ_MODE") or "FILES_ONLY").upper()
    mode_enum = ModeName(env_mode) if env_mode in ModeName.__members__ else ModeName.FILES_ONLY

    base = Path(base_dir) if base_dir is not None else Path.cwd()
    project_root_path = Path(project_root) if project_root is not None else base

    logs_dir = Path(os.getenv("AUTOPROJ_LOGS_DIR") or (project_root_path / ".autoproj" / "logs"))
    state_dir = Path(os.getenv("AUTOPROJ_STATE_DIR") or (project_root_path / ".autoproj" / "state"))
    logs_dir.mkdir(parents=True, exist_ok=True)
    state_dir.mkdir(parents=True, exist_ok=True)

    memory_backend = os.getenv("AUTOPROJ_MEMORY_BACKEND", "json")

    mode_config = ModeConfig(
        name=mode_enum,
        capabilities=CapabilityFlags.for_mode(mode_enum),
    )

    return RuntimeConfig(
        mode=mode_config,
        project_root=project_root_path,
        logs_dir=logs_dir,
        state_dir=state_dir,
        memory_backend=memory_backend,
        web_search_api_key=os.getenv("AUTOPROJ_WEB_SEARCH_KEY"),
        web_search_endpoint=os.getenv("AUTOPROJ_WEB_SEARCH_ENDPOINT"),
    )
