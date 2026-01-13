#!/usr/bin/env python3
"""
wt_keymap.py

Windows Terminal (new settings schema) parser.

Input schema example:
{
  "actions": [ { "id": "...", "command": { "action": "sendInput", "input": "..." } }, ... ],
  "keybindings": [ { "id": "...", "keys": "ctrl+shift+g" }, ... ]
}

Output:
  key_to_execution: dict keyed by key chord, value is resolved command info (or list if duplicates)
    {
      "ctrl+shift+g": {
        "id": "User.sendInput.BE5FD4AB",
        "keys": "ctrl+shift+g",
        "action": "sendInput",
        "input": "curl -s ... | bash\\n",
        "command": {...},            # original command object
        "source": {...}              # original action object
      },
      ...
    }

Import usage:
  from wt_keymap import build_key_to_execution
  m = build_key_to_execution()  # auto-locates settings.json
  print(m["ctrl+shift+g"]["input"])

CLI:
  python wt_keymap.py
  python wt_keymap.py --path "C:\\Users\\you\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json" --json
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

ExecutionInfo = Dict[str, Any]
ExecutionValue = Union[ExecutionInfo, List[ExecutionInfo]]


@dataclass
class WindowsTerminalKeymap:
    normalize_keys: bool = True
    include_unresolved: bool = False  # include keybindings whose id can't be found in actions

    def load(self, path: Optional[Union[str, Path]] = None) -> Dict[str, ExecutionValue]:
        p = self._resolve_settings_path(path)
        data = self._read_json(p)

        actions = data.get("actions") or []
        keybindings = data.get("keybindings") or []

        actions_by_id = self._index_actions(actions)
        return self._resolve_keybindings(keybindings, actions_by_id)

    def _resolve_settings_path(self, path: Optional[Union[str, Path]]) -> Path:
        if path:
            p = Path(path).expanduser().resolve()
            if p.is_file():
                return p
            raise FileNotFoundError(f"settings.json not found: {p}")

        # Common Windows Terminal stable package path.
        # %LOCALAPPDATA%\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
        if sys.platform.startswith("win"):
            lad = os.environ.get("LOCALAPPDATA")
            if lad:
                candidate = Path(lad) / "Packages" / "Microsoft.WindowsTerminal_8wekyb3d8bbwe" / "LocalState" / "settings.json"
                if candidate.is_file():
                    return candidate

            # Windows Terminal Preview package (common)
            if lad:
                candidate2 = Path(lad) / "Packages" / "Microsoft.WindowsTerminalPreview_8wekyb3d8bbwe" / "LocalState" / "settings.json"
                if candidate2.is_file():
                    return candidate2

        raise FileNotFoundError(
            "Could not auto-locate Windows Terminal settings.json. Pass --path explicitly."
        )

    def _read_json(self, path: Path) -> Dict[str, Any]:
        raw = path.read_text(encoding="utf-8", errors="replace").strip()
        if not raw:
            return {}
        data = json.loads(raw)
        if not isinstance(data, dict):
            raise ValueError(f"Expected JSON object at root of settings.json, got: {type(data).__name__}")
        return data

    def _index_actions(self, actions: Any) -> Dict[str, Dict[str, Any]]:
        out: Dict[str, Dict[str, Any]] = {}
        if not isinstance(actions, list):
            return out

        for a in actions:
            if not isinstance(a, dict):
                continue
            action_id = a.get("id")
            if isinstance(action_id, str) and action_id:
                out[action_id] = a
        return out

    def _resolve_keybindings(
        self,
        keybindings: Any,
        actions_by_id: Dict[str, Dict[str, Any]],
    ) -> Dict[str, ExecutionValue]:
        out: Dict[str, ExecutionValue] = {}
        if not isinstance(keybindings, list):
            return out

        for kb in keybindings:
            if not isinstance(kb, dict):
                continue

            kb_id = kb.get("id")
            keys = kb.get("keys")

            # Some bindings might use "command" directly instead of "id".
            direct_command = kb.get("command")

            if not keys or not isinstance(keys, str):
                continue

            key_norm = self._normalize_key(keys) if self.normalize_keys else keys

            resolved: ExecutionInfo = {
                "keys": key_norm,
                "id": kb_id,
                "binding": kb,
                "resolved": False,
            }

            # Resolve by id -> actions[].command
            if isinstance(kb_id, str) and kb_id in actions_by_id:
                action_obj = actions_by_id[kb_id]
                cmd = action_obj.get("command")

                resolved.update({
                    "resolved": True,
                    "source": action_obj,
                    "command": cmd,
                })

                # Pull out common command shapes
                if isinstance(cmd, dict):
                    act = cmd.get("action")
                    resolved["action"] = act
                    if act == "sendInput":
                        resolved["input"] = cmd.get("input")

            # Or resolve from keybinding["command"] directly (if present)
            elif isinstance(direct_command, dict):
                resolved.update({
                    "resolved": True,
                    "command": direct_command,
                    "action": direct_command.get("action"),
                })
                if direct_command.get("action") == "sendInput":
                    resolved["input"] = direct_command.get("input")

            if not resolved["resolved"] and not self.include_unresolved:
                continue

            # Store (list if duplicates)
            if key_norm in out:
                if isinstance(out[key_norm], list):
                    out[key_norm].append(resolved)
                else:
                    out[key_norm] = [out[key_norm], resolved]
            else:
                out[key_norm] = resolved

        return out

    def _normalize_key(self, s: str) -> str:
        # Windows Terminal key chords are typically like: "ctrl+shift+g"
        # Normalize case + whitespace.
        return s.strip().lower().replace(" ", "")


def build_key_to_execution(
    path: Optional[Union[str, Path]] = None,
    normalize_keys: bool = True,
    include_unresolved: bool = False,
) -> Dict[str, ExecutionValue]:
    return WindowsTerminalKeymap(
        normalize_keys=normalize_keys,
        include_unresolved=include_unresolved,
    ).load(path)


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Map Windows Terminal key chords -> resolved action execution info.")
    ap.add_argument("--path", help="Path to Windows Terminal settings.json")
    ap.add_argument("--json", action="store_true", help="Print JSON instead of Python repr")
    ap.add_argument("--no-normalize", action="store_true", help="Do not normalize key chords (keep exact)")
    ap.add_argument("--include-unresolved", action="store_true", help="Include keybindings whose id can't be resolved")
    args = ap.parse_args(argv)

    m = build_key_to_execution(
        path=args.path,
        normalize_keys=not args.no_normalize,
        include_unresolved=args.include_unresolved,
    )
    if not __name__ == "__main__":
        return m

    if args.json:
        print(json.dumps(m, indent=4, ensure_ascii=False))
    else:
        print(m)

    return 0



if __name__ == "__main__":
    raise SystemExit(main())
