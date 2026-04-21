### filename: autoproj/tools/registry.py
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, Optional


@dataclass
class Tool:
    """
    Represents a callable tool the Agent can invoke.

    func signature convention:
      func(*, ctx: Any, **kwargs) -> Any
    """
    name: str
    description: str
    func: Callable[..., Any]
    requires_god_mode: bool = False


class ToolRegistry:
    """
    Simple in-process registry for tools.

    This is intentionally small; you can evolve it into a full
    capability-gated registry later.
    """

    def __init__(self) -> None:
        self._tools: Dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        self._tools[tool.name] = tool

    def get(self, name: str) -> Optional[Tool]:
        return self._tools.get(name)

    def list_tools(self) -> Dict[str, Tool]:
        return dict(self._tools)
