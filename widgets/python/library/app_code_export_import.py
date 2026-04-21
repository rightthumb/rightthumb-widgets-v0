# 698a51cd-60a8-8326-bd30-558abdf721f1
# 698a51cd-60a8-8326-bd30-558abdf721f1

#!/usr/bin/env python3
"""
EcoNamespaceCollector + EcoExportModifier

Goal:
- Collect callables from globals() (or any namespace dict)
- Extract source where possible (user-defined Python)
- Export payload as JSON
- Export payload as a standalone Python script (self-contained)

Notes / Limits (intentional):
- Builtins / C-extension callables often have no source: we record metadata but source=None.
- Dependency rewriting (stickytape-style) is intentionally NOT attempted here. You can add it later.
- Any code modification is handled in a separate transform function hook.
"""

from __future__ import annotations

import ast
import inspect
import json
import os
import re
import textwrap
import time
from dataclasses import dataclass
from types import ModuleType, FunctionType
from typing import Any, Callable, Dict, List, Optional, Tuple, Union


# ---------------------------------------------------------------------
# Utilities (kept simple; easy to convert into static helpers later)
# ---------------------------------------------------------------------

def _now_epoch() -> int:
    return int(time.time())


def _safe_repr(x: Any, limit: int = 5000) -> str:
    try:
        s = repr(x)
    except Exception:
        s = f"<unreprable:{type(x).__name__}>"
    if len(s) > limit:
        s = s[:limit] + "...<truncated>"
    return s


def _is_user_function(obj: Any) -> bool:
    return inspect.isfunction(obj) and getattr(obj, "__code__", None) is not None


def _is_user_class(obj: Any) -> bool:
    return inspect.isclass(obj) and getattr(obj, "__module__", None) not in ("builtins", None)


def _is_user_module(obj: Any) -> bool:
    return isinstance(obj, ModuleType)


def _callable_kind(obj: Any) -> str:
    if inspect.isfunction(obj):
        return "function"
    if inspect.isclass(obj):
        return "class"
    if inspect.ismethod(obj):
        return "method"
    if callable(obj):
        return "callable"
    return "unknown"


def _try_signature(obj: Any) -> Optional[str]:
    try:
        return str(inspect.signature(obj))
    except Exception:
        return None


def _try_getsource(obj: Any) -> Optional[str]:
    try:
        src = inspect.getsource(obj)
        # keep original indentation stable
        return textwrap.dedent(src).rstrip() + "\n"
    except Exception:
        return None


def _extract_co_names(obj: Any) -> List[str]:
    """
    Heuristic: function code object references. Useful for later “dependency-ish” ideas.
    """
    try:
        code = getattr(obj, "__code__", None)
        if code is None:
            return []
        return list(code.co_names or [])
    except Exception:
        return []


def _default_transform_source(name: str, kind: str, source: str) -> str:
    """
    Hook for later rewriting. Right now: identity.
    You can replace this later with your own manipulator.
    """
    return source


# ---------------------------------------------------------------------
# Class #1: Namespace collection + JSON export
# ---------------------------------------------------------------------

class EcoNamespaceCollector:
    """
    Collect items from a namespace dict (typically globals()).

    - prefers globals-based discovery, not import graph analysis
    - stores a descriptive payload dict
    - exports to JSON
    """

    # Long descriptive dict name so you can find it easily in a giant file
    DEFAULT_PAYLOAD_DICT_NAME = "ECO__NAMESPACE_EXPORT_PAYLOAD__COLLECTED_CALLABLES_AND_SOURCES__V1"

    def __init__(
        self,
        ns: Dict[str, Any],
        payload_dict_name: str = None,
        include_private: bool = False,
    ):
        self.ns = ns
        self.include_private = include_private
        self.payload_dict_name = payload_dict_name or self.DEFAULT_PAYLOAD_DICT_NAME

    # -----------------------------
    # Filters (easy to expand)
    # -----------------------------

    @staticmethod
    def default_name_filter(name: str, include_private: bool) -> bool:
        if not include_private:
            if name.startswith("_"):
                return False
        return True

    @staticmethod
    def default_object_filter(obj: Any) -> bool:
        # Most common: user-defined functions/classes + other callables
        if inspect.isfunction(obj):
            return True
        if inspect.isclass(obj):
            return True
        # include other callables (instances with __call__)
        if callable(obj):
            return True
        return False

    # -----------------------------
    # Collection
    # -----------------------------

    def collect(
        self,
        *,
        name_filter: Optional[Callable[[str], bool]] = None,
        object_filter: Optional[Callable[[Any], bool]] = None,
        exclude_names: Optional[List[str]] = None,
        exclude_regex: Optional[List[str]] = None,
        exclude_predicate: Optional[Callable[[str, Any], bool]] = None,
        max_items: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Returns payload dict:
            {
              "__meta__": {...},
              "items": {
                 "name": {kind, module, qualname, signature, doc, source, ...}
              }
            }
        """
        exclude_names = set(exclude_names or [])
        exclude_patterns = [re.compile(p) for p in (exclude_regex or [])]

        def _name_ok(n: str) -> bool:
            if n in exclude_names:
                return False
            for rx in exclude_patterns:
                if rx.search(n):
                    return False
            if name_filter is not None:
                try:
                    return bool(name_filter(n))
                except Exception:
                    return False
            return self.default_name_filter(n, self.include_private)

        def _obj_ok(n: str, o: Any) -> bool:
            if exclude_predicate is not None:
                try:
                    if exclude_predicate(n, o):
                        return False
                except Exception:
                    # if predicate errors, don't include it
                    return False
            if object_filter is not None:
                try:
                    return bool(object_filter(o))
                except Exception:
                    return False
            return self.default_object_filter(o)

        items: Dict[str, Any] = {}
        count = 0

        for name, obj in list(self.ns.items()):
            if max_items is not None and count >= max_items:
                break
            if not _name_ok(name):
                continue
            if not _obj_ok(name, obj):
                continue

            kind = _callable_kind(obj)
            module = getattr(obj, "__module__", None)
            qualname = getattr(obj, "__qualname__", None) or getattr(obj, "__name__", None) or name
            signature = _try_signature(obj)
            doc = getattr(obj, "__doc__", None)
            src = _try_getsource(obj)

            item = {
                "name": name,
                "kind": kind,
                "module": module,
                "qualname": qualname,
                "signature": signature,
                "doc": doc,
                "has_source": bool(src),
                "source": src,  # may be None
                "co_names": _extract_co_names(obj) if inspect.isfunction(obj) else [],
                "repr": _safe_repr(obj),
            }

            items[name] = item
            count += 1

        payload = {
            "__meta__": {
                "payload_dict_name": self.payload_dict_name,
                "epoch": _now_epoch(),
                "python": {
                    "version": getattr(os, "sys", None).version if hasattr(os, "sys") else None,
                },
                "counts": {
                    "items": len(items),
                },
            },
            "items": items,
        }
        return payload

    # -----------------------------
    # JSON export
    # -----------------------------

    def to_json(
        self,
        payload: Dict[str, Any],
        *,
        pretty: bool = True,
        ensure_ascii: bool = False,
    ) -> str:
        if pretty:
            return json.dumps(payload, indent=2, ensure_ascii=ensure_ascii, sort_keys=False)
        return json.dumps(payload, separators=(",", ":"), ensure_ascii=ensure_ascii)

    def save_json(
        self,
        payload: Dict[str, Any],
        path: str,
        *,
        pretty: bool = True,
        ensure_ascii: bool = False,
    ) -> str:
        data = self.to_json(payload, pretty=pretty, ensure_ascii=ensure_ascii)
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
        return path


# ---------------------------------------------------------------------
# Class #2: Modification + Standalone exporter
# ---------------------------------------------------------------------

class EcoExportModifier:
    """
    Takes a payload from EcoNamespaceCollector and:
    - removes irrelevant functions (by name/regex/predicate)
    - optionally transforms sources (separate function hook)
    - emits a standalone python file containing:
        - the long payload dict
        - embedded source blocks
        - a small loader to access them
    """

    DEFAULT_STANDALONE_PAYLOAD_DICT_NAME = "ECO__NAMESPACE_EXPORT_PAYLOAD__STANDALONE_APP_BUNDLE__V1"

    def __init__(
        self,
        payload: Dict[str, Any],
        *,
        payload_dict_name: Optional[str] = None,
    ):
        self.payload = payload
        self.payload_dict_name = payload_dict_name or self.DEFAULT_STANDALONE_PAYLOAD_DICT_NAME

    # -----------------------------
    # Removal / filtering
    # -----------------------------

    def remove(
        self,
        *,
        names: Optional[List[str]] = None,
        regex: Optional[List[str]] = None,
        predicate: Optional[Callable[[str, Dict[str, Any]], bool]] = None,
    ) -> Dict[str, Any]:
        """
        Remove items from payload['items'].
        predicate(name, itemdict) -> True means remove.
        """
        names_set = set(names or [])
        patterns = [re.compile(p) for p in (regex or [])]

        items = self.payload.get("items", {})
        kept: Dict[str, Any] = {}

        for name, item in items.items():
            if name in names_set:
                continue
            remove_me = False
            for rx in patterns:
                if rx.search(name):
                    remove_me = True
                    break
            if remove_me:
                continue
            if predicate is not None:
                try:
                    if predicate(name, item):
                        continue
                except Exception:
                    # if predicate fails, be safe and remove it
                    continue
            kept[name] = item

        self.payload["items"] = kept
        self.payload.setdefault("__meta__", {})
        self.payload["__meta__"]["counts"] = {"items": len(kept)}
        return self.payload

    # -----------------------------
    # Source transformation (separate hook)
    # -----------------------------

    def transform_sources(
        self,
        transform_fn: Callable[[str, str, str], str] = None
    ) -> Dict[str, Any]:
        """
        transform_fn(name, kind, source) -> new_source
        """
        if transform_fn is None:
            transform_fn = _default_transform_source

        for name, item in self.payload.get("items", {}).items():
            src = item.get("source")
            if not src:
                continue
            kind = item.get("kind") or "unknown"
            try:
                item["source"] = transform_fn(name, kind, src)
            except Exception:
                # if transform fails, keep original
                item["source"] = src
        return self.payload

    # -----------------------------
    # Standalone generation
    # -----------------------------

    def build_standalone_python(
        self,
        *,
        entrypoints: Optional[List[str]] = None,
        add_loader: bool = True,
        include_sources: bool = True,
    ) -> str:
        """
        Returns a full .py script as a string.
        - entrypoints: optional list of item names to highlight or auto-run
        """
        entrypoints = entrypoints or []

        # Prepare a compact “sources” dict (only those with source)
        items = self.payload.get("items", {})
        sources: Dict[str, str] = {}
        meta_items: Dict[str, Any] = {}

        for name, item in items.items():
            # Keep metadata (minus huge fields if you want later)
            meta_items[name] = {
                "kind": item.get("kind"),
                "module": item.get("module"),
                "qualname": item.get("qualname"),
                "signature": item.get("signature"),
                "has_source": item.get("has_source"),
                "co_names": item.get("co_names", []),
            }
            if include_sources and item.get("source"):
                sources[name] = item["source"]

        standalone_payload = {
            "__meta__": {
                "payload_dict_name": self.payload_dict_name,
                "built_epoch": _now_epoch(),
                "source_count": len(sources),
                "item_count": len(items),
                "entrypoints": entrypoints,
            },
            "items": meta_items,
            "sources": sources,
        }

        # Important: long descriptive dict name
        payload_dict_name = self.payload_dict_name

        # Build script
        out: List[str] = []
        out.append("#!/usr/bin/env python3\n")
        out.append('"""\n')
        out.append("Standalone bundle generated by EcoExportModifier.\n")
        out.append("Contains a payload dict + optional embedded sources.\n")
        out.append('"""\n\n')

        out.append("from __future__ import annotations\n\n")
        out.append("import types\n")
        out.append("import sys\n\n")

        # Embed payload dict
        out.append(f"{payload_dict_name} = ")
        out.append(json.dumps(standalone_payload, indent=2, ensure_ascii=False))
        out.append("\n\n")

        if add_loader:
            out.append(textwrap.dedent(f"""
            def eco_bundle_list():
                \"\"\"List exported item names.\"\"\"
                return sorted({payload_dict_name}.get("items", {{}}).keys())

            def eco_bundle_get_source(name: str):
                \"\"\"Return source string for name (or None).\"\"\"
                return {payload_dict_name}.get("sources", {{}}).get(name)

            def eco_bundle_load(name: str, ns: dict | None = None):
                \"\"\"
                Exec the stored source into a namespace and return the callable/class.
                - For functions/classes defined in that source, returns ns[name] if present,
                  else tries to return the last defined symbol heuristically.
                \"\"\"
                src = eco_bundle_get_source(name)
                if not src:
                    raise KeyError(f"No source stored for: {{name}}")

                if ns is None:
                    ns = {{}}

                # Allow source to define multiple symbols; we attempt to return exact name
                before = set(ns.keys())
                exec(src, ns, ns)
                after = set(ns.keys())

                if name in ns:
                    return ns[name]

                # Fallback: return the newest symbol introduced (best-effort)
                new_syms = [k for k in (after - before) if not k.startswith("__")]
                if len(new_syms) == 1:
                    return ns[new_syms[0]]
                return ns  # if ambiguous, return namespace for manual pick

            def eco_bundle_run():
                \"\"\"
                If entrypoints exist, try to load and run them if they are callables
                with zero required args. Best-effort only.
                \"\"\"
                eps = {payload_dict_name}.get("__meta__", {{}}).get("entrypoints", []) or []
                if not eps:
                    return 0

                ns = {{}}
                rc = 0
                for name in eps:
                    try:
                        obj = eco_bundle_load(name, ns=ns)
                        if callable(obj):
                            # only attempt if no required args
                            try:
                                import inspect
                                sig = inspect.signature(obj)
                                required = [
                                    p for p in sig.parameters.values()
                                    if p.default is p.empty and p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)
                                ]
                                if required:
                                    continue
                            except Exception:
                                pass
                            obj()
                    except Exception:
                        rc = 1
                return rc

            if __name__ == "__main__":
                # If a name is provided, load it and print what we got.
                # Example:
                #   python bundle.py my_fn
                if len(sys.argv) > 1:
                    name = sys.argv[1]
                    ns = {{}}
                    obj = eco_bundle_load(name, ns=ns)
                    print(obj)
                else:
                    raise SystemExit(eco_bundle_run())
            """).lstrip())

        return "".join(out)

    def save_standalone_python(
        self,
        path: str,
        *,
        entrypoints: Optional[List[str]] = None,
        add_loader: bool = True,
        include_sources: bool = True,
    ) -> str:
        script = self.build_standalone_python(
            entrypoints=entrypoints,
            add_loader=add_loader,
            include_sources=include_sources,
        )
        with open(path, "w", encoding="utf-8") as f:
            f.write(script)
        return path


# ---------------------------------------------------------------------
# Example usage (delete later / keep as reference)
# ---------------------------------------------------------------------

if __name__ == "__main__":
    # 1) Collect from globals of THIS file
    collector = EcoNamespaceCollector(globals(), include_private=False)

    payload = collector.collect(
        exclude_names=[
            # remove collector/modifier themselves if you want
            "EcoNamespaceCollector",
            "EcoExportModifier",
        ],
        exclude_regex=[
            r"^_safe_",
            r"^_try_",
            r"^_extract_",
        ],
    )

    # 2) Save JSON payload
    collector.save_json(payload, "eco_bundle.payload.json", pretty=True)

    # 3) Modify payload (remove irrelevant)
    mod = EcoExportModifier(payload)

    # Example: remove anything with "test" in name
    mod.remove(regex=[r"test"])

    # Example: apply transform hook (currently no-op)
    mod.transform_sources(transform_fn=_default_transform_source)

    # 4) Save standalone script
    mod.save_standalone_python(
        "eco_bundle.standalone.py",
        entrypoints=[],
        add_loader=True,
        include_sources=True,
    )

    print("Wrote: eco_bundle.payload.json")
    print("Wrote: eco_bundle.standalone.py")







collector = EcoNamespaceCollector(globals(), include_private=True)
payload = collector.collect(
    exclude_names=["main", "run", "EcoNamespaceCollector", "EcoExportModifier"],
    exclude_regex=[r"^__"],
)
collector.save_json(payload, "my_app.bundle.json")


mod = EcoExportModifier(payload)
mod.remove(names=["EcoNamespaceCollector", "EcoExportModifier"])


mod.save_standalone_python("my_app.bundle.py", entrypoints=["some_fn"])

# 698a51cd-60a8-8326-bd30-558abdf721f1
# 698a51cd-60a8-8326-bd30-558abdf721f1