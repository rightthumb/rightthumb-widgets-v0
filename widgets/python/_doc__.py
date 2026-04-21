#!/usr/bin/env python3
import argparse
import builtins
import importlib
import inspect
from types import ModuleType
from typing import Any, Dict, Set, Optional, Tuple, List


LEAF_TYPES = (int, float, complex, bool, str, bytes, bytearray, memoryview,
              tuple, list, dict, set, frozenset, type(None))


def safe_getdoc(obj: Any) -> Optional[str]:
    try:
        d = inspect.getdoc(obj)
        return d if d and d.strip() else None
    except Exception:
        return None


def iter_members_static(obj: Any) -> List[Tuple[str, Any]]:
    """
    Like inspect.getmembers(), but does NOT invoke descriptors/properties.
    Much safer for crawling large libs.
    """
    try:
        return inspect.getmembers_static(obj)
    except Exception:
        # Fallback: best-effort dir/getattr (can still trigger properties)
        out = []
        try:
            for name in dir(obj):
                try:
                    out.append((name, getattr(obj, name)))
                except Exception:
                    pass
        except Exception:
            pass
        return out


def should_skip_name(name: str, include_private: bool) -> bool:
    if include_private:
        return False
    return name.startswith("_")


def prefix_omitted(path: str, omit_prefixes: Tuple[str, ...]) -> bool:
    return path.startswith(omit_prefixes)


def crawl_docs(
    obj: Any,
    root_name: str,
    max_depth: int,
    include_private: bool,
    omit_prefixes: Tuple[str, ...],
    seen: Set[int],
    out: Dict[str, str],
    max_nodes: int,
    _depth: int = 0,
) -> None:
    if max_nodes and len(out) >= max_nodes:
        return
    if _depth > max_depth:
        return

    oid = id(obj)
    if oid in seen:
        return
    seen.add(oid)

    # Capture doc for THIS object if present
    doc = safe_getdoc(obj)
    if doc and not prefix_omitted(root_name, omit_prefixes):
        out[root_name] = doc
        if max_nodes and len(out) >= max_nodes:
            return

    # Stop recursion on leaf-ish things
    if isinstance(obj, LEAF_TYPES):
        return

    # Try to avoid crawling builtins/types noise:
    # (You can loosen/tighten this depending on your goals)
    obj_type = type(obj)
    try:
        base_names = set(dir(obj_type))
    except Exception:
        base_names = set()

    for name, value in iter_members_static(obj):
        if should_skip_name(name, include_private):
            continue

        # Skip inherited/type-provided attributes (your original “redundant” idea)
        if name in base_names:
            continue

        child_path = f"{root_name}.{name}"
        if prefix_omitted(child_path, omit_prefixes):
            continue

        # Don’t recurse into a bunch of builtin namespace objects
        # unless they have docs (still recorded above)
        # This keeps the graph sane.
        if isinstance(value, ModuleType):
            # modules are fine
            pass
        else:
            try:
                mod = getattr(value, "__module__", "")
                if mod == "builtins":
                    # still allow doc capture, but don't dive deeper
                    continue
            except Exception:
                pass

        crawl_docs(
            value,
            child_path,
            max_depth=max_depth,
            include_private=include_private,
            omit_prefixes=omit_prefixes,
            seen=seen,
            out=out,
            max_nodes=max_nodes,
            _depth=_depth + 1,
        )
        if max_nodes and len(out) >= max_nodes:
            return


def main() -> int:
    p = argparse.ArgumentParser(description="Crawl a module/object and extract __doc__ into markdown.")
    p.add_argument("target", help="Import path, e.g. pytermgui or package.submodule")
    p.add_argument("--depth", type=int, default=2, help="Max recursion depth (default: 2)")
    p.add_argument("--private", action="store_true", help="Include private/_dunder names")
    p.add_argument("--max-nodes", type=int, default=5000, help="Stop after collecting this many docs")
    p.add_argument("--omit", action="append", default=[], help="Omit prefix (repeatable), e.g. --omit pytermgui.os")
    args = p.parse_args()

    mod = importlib.import_module(args.target)

    # default omit examples similar to your script
    omit_prefixes = tuple(args.omit + [f"{args.target}.os", f"{args.target}.sys"])

    docs: Dict[str, str] = {}
    seen: Set[int] = set()
    crawl_docs(
        mod,
        root_name=args.target,
        max_depth=args.depth,
        include_private=args.private,
        omit_prefixes=omit_prefixes,
        seen=seen,
        out=docs,
        max_nodes=args.max_nodes,
    )

    # Markdown output (similar to yours)
    lines = []
    lines.append(f"# {args.target} documentation")
    lines.append(f"#### found {len(docs)} documented objects")
    for path in sorted(docs.keys()):
        lines.append("")
        lines.append("___")
        lines.append(f"## {path}")
        lines.append("")
        for docl in docs[path].splitlines():
            lines.append("    " + docl)
        lines.append("")

    lines.append("___")
    lines.append("## items with __doc__")
    lines.append("")
    for path in sorted(docs.keys()):
        lines.append("    " + path)
    lines.append("")
    lines.append("___")
    lines.append(f"#### found {len(docs)} documented objects")

    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
