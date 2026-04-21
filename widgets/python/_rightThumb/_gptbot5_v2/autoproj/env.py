# autoproj/env.py

from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum, auto
from pathlib import Path
from typing import Optional, Dict, Any


class EnvMode(Enum):
    """What level of power this session has."""
    NO_OS = auto()       # think-only, no subprocess, no fs
    SAFE_OS = auto()     # whitelisted commands in project tree
    GOD_MODE = auto()    # full power in a sandbox (virsh/chroot/ramdisk)


@dataclass
class EnvConfig:
    """
    Describes the environment the agent is allowed to touch.
    You’ll pass one of these per session.
    """
    mode: EnvMode = EnvMode.NO_OS

    # Root folder it is allowed to treat as "project home"
    project_root: Path = field(default_factory=lambda: Path.cwd())

    # True if it is allowed to touch the network (requests, Brave, etc.)
    allow_web: bool = False

    # True if it is allowed to install packages (apt/dnf/pacman/choco, etc.)
    allow_package_install: bool = False

    # True if it can create/manage VMs/virsh/chroots/etc.
    allow_virtualization: bool = False

    # Optional “label” you can embed from your terminal proxy
    env_label: str = "default"

    # Freeform metadata: distro, chroot name, virsh domain, etc.
    metadata: Dict[str, Any] = field(default_factory=dict)

    def in_project_tree(self, path: Path) -> bool:
        """Return True if the path is inside project_root."""
        path = path.resolve()
        root = self.project_root.resolve()
        try:
            path.relative_to(root)
            return True
        except ValueError:
            return False
