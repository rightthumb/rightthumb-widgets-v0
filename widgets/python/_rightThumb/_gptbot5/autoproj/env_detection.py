from __future__ import annotations

import os
import platform
import subprocess
from dataclasses import dataclass
from typing import Optional


@dataclass
class EnvironmentInfo:
    os_name: str
    platform: str
    is_wsl: bool
    is_docker: bool
    distro_id: Optional[str]
    distro_like: Optional[str]


def _detect_wsl() -> bool:
    try:
        with open("/proc/version", "r", encoding="utf-8") as f:
            txt = f.read().lower()
        return "microsoft" in txt or "wsl" in txt
    except Exception:
        return False


def _detect_docker() -> bool:
    if os.path.exists("/.dockerenv"):
        return True
    try:
        with open("/proc/1/cgroup", "r", encoding="utf-8") as f:
            txt = f.read().lower()
        return "docker" in txt or "kubepods" in txt or "containerd" in txt
    except Exception:
        return False


def _detect_distro() -> tuple[Optional[str], Optional[str]]:
    try:
        import distro  # type: ignore

        return distro.id(), distro.like()
    except Exception:
        return None, None


def detect_environment() -> EnvironmentInfo:
    os_name = os.name
    plat = platform.system()
    is_wsl = _detect_wsl()
    is_docker = _detect_docker()
    distro_id, distro_like = _detect_distro()
    return EnvironmentInfo(
        os_name=os_name,
        platform=plat,
        is_wsl=is_wsl,
        is_docker=is_docker,
        distro_id=distro_id,
        distro_like=distro_like,
    )
