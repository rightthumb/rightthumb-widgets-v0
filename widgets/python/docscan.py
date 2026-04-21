#!/usr/bin/python3

import sys
import os
import importlib
import inspect
import pkgutil
from types import ModuleType
from typing import Any, Dict, List, Optional, Set


def is_private(name: str, include_private: bool = False) -> bool:
    if include_private:
        return False
    return name.startswith("_")


def safe_getdoc(obj: Any) -> str:
    try:
        return inspect.getdoc(obj) or ""
    except Exception:
        return ""


def safe_signature(obj: Any) -> str:
    try:
        return str(inspect.signature(obj))
    except Exception:
        return ""


def safe_getmembers(obj: Any):
    try:
        return inspect.getmembers(obj)
    except Exception:
        return []


def safe_is_package(mod: ModuleType) -> bool:
    return hasattr(mod, "__path__")


def safe_file(obj: Any) -> str:
    try:
        return inspect.getfile(obj)
    except Exception:
        try:
            return getattr(obj, "__file__", "") or ""
        except Exception:
            return ""


def object_kind(obj: Any) -> str:
    try:
        if inspect.ismodule(obj):
            return "module"
        if inspect.isclass(obj):
            return "class"
        if inspect.ismethod(obj):
            return "method"
        if inspect.isfunction(obj):
            return "function"
        if inspect.isbuiltin(obj):
            return "builtin"
        if isinstance(obj, property):
            return "property"
        return type(obj).__name__
    except Exception:
        return "unknown"


def should_recurse_into(
    obj: Any,
    root_name: str,
    current_depth: int,
    max_depth: int,
    include_submodules: bool,
) -> bool:
    if current_depth >= max_depth:
        return False

    try:
        if inspect.ismodule(obj):
            mod_name = getattr(obj, "__name__", "")
            if include_submodules and mod_name.startswith(root_name):
                return True
            return False

        if inspect.isclass(obj):
            return True

        return False
    except Exception:
        return False


def member_belongs_to_root(obj: Any, root_name: str) -> bool:
    """
    Avoid diving deep into foreign imported objects unless they belong
    to the target module/package namespace.
    """
    try:
        mod = getattr(obj, "__module__", "") or ""
        name = getattr(obj, "__name__", "") or ""
        full = f"{mod}.{name}".strip(".")
        return mod.startswith(root_name) or full.startswith(root_name)
    except Exception:
        return False


def expand_package_submodules(module: ModuleType, root_name: str) -> List[ModuleType]:
    found = []
    if not safe_is_package(module):
        return found

    try:
        for modinfo in pkgutil.iter_modules(module.__path__, module.__name__ + "."):
            try:
                submod = importlib.import_module(modinfo.name)
                if getattr(submod, "__name__", "").startswith(root_name):
                    found.append(submod)
            except Exception:
                continue
    except Exception:
        pass

    return found


def scan_object(
    obj: Any,
    display_name: str,
    root_name: str,
    max_depth: int = 4,
    current_depth: int = 0,
    include_private: bool = False,
    include_submodules: bool = False,
    seen: Optional[Set[int]] = None,
    out: Optional[Dict[str, Dict[str, Any]]] = None,
) -> Dict[str, Dict[str, Any]]:
    if seen is None:
        seen = set()
    if out is None:
        out = {}

    oid = id(obj)
    if oid in seen:
        return out
    seen.add(oid)

    kind = object_kind(obj)
    doc = safe_getdoc(obj)
    sig = safe_signature(obj)
    file_path = safe_file(obj)

    out[display_name] = {
        "kind": kind,
        "signature": sig,
        "doc": doc,
        "file": file_path,
        "depth": current_depth,
    }

    if current_depth >= max_depth:
        return out

    # Special handling for package submodules
    if inspect.ismodule(obj) and include_submodules:
        for submod in expand_package_submodules(obj, root_name):
            subname = getattr(submod, "__name__", "")
            if subname and subname not in out:
                scan_object(
                    submod,
                    subname,
                    root_name=root_name,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    include_private=include_private,
                    include_submodules=include_submodules,
                    seen=seen,
                    out=out,
                )

    # Inspect members
    for name, value in safe_getmembers(obj):
        if is_private(name, include_private=include_private):
            continue

        member_name = f"{display_name}.{name}"

        try:
            if inspect.ismodule(value):
                if not include_submodules:
                    continue
                if not getattr(value, "__name__", "").startswith(root_name):
                    continue

            elif inspect.isclass(value) or inspect.isfunction(value) or inspect.ismethod(value) or inspect.isbuiltin(value):
                if not member_belongs_to_root(value, root_name):
                    continue
            else:
                # Skip plain data unless it has a doc and is interesting
                if not safe_getdoc(value):
                    continue

            if member_name not in out:
                scan_object(
                    value,
                    member_name,
                    root_name=root_name,
                    max_depth=max_depth,
                    current_depth=current_depth + 1,
                    include_private=include_private,
                    include_submodules=include_submodules,
                    seen=seen,
                    out=out,
                )
        except Exception:
            continue

    return out


def render_markdown(module_name: str, docs: Dict[str, Dict[str, Any]]) -> List[str]:
    lines: List[str] = []

    items = sorted(docs.items(), key=lambda x: (x[1]["depth"], x[0]))

    lines.append(f"# {module_name} documentation")
    lines.append("")
    lines.append(f"Found **{len(items)}** documented/inspectable items.")
    lines.append("")

    # TOC
    lines.append("## Items")
    lines.append("")
    for name, meta in items:
        lines.append(f"- `{name}` — {meta['kind']}")
    lines.append("")

    # Details
    for name, meta in items:
        lines.append("---")
        lines.append("")
        lines.append(f"## `{name}`")
        lines.append("")

        lines.append(f"- **Kind:** {meta['kind']}")
        if meta["signature"]:
            lines.append(f"- **Signature:** `{meta['signature']}`")
        if meta["file"]:
            lines.append(f"- **File:** `{meta['file']}`")
        lines.append(f"- **Depth:** {meta['depth']}")
        lines.append("")

        if meta["doc"]:
            lines.append("### Doc")
            lines.append("")
            for line in meta["doc"].splitlines():
                lines.append(f"    {line}")
            lines.append("")
        else:
            lines.append("### Doc")
            lines.append("")
            lines.append("    No docstring.")
            lines.append("")

    return lines


def interactive_lookup(docs: Dict[str, Dict[str, Any]], root_name: str):
    names = sorted(docs.keys())

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(f"Items in {root_name}")
        print("-" * 80)
        for name in names:
            print(name)
        print("-" * 80)
        print(f"Count: {len(names)}")
        print("Enter a full name or partial text. Blank = quit.")
        ask = input(" : ").strip()
        if not ask:
            break

        exact = docs.get(ask)
        if exact:
            print()
            print(ask)
            print("-" * len(ask))
            if exact["signature"]:
                print("signature:", exact["signature"])
            print("kind:", exact["kind"])
            if exact["file"]:
                print("file:", exact["file"])
            print()
            print(exact["doc"] or "No docstring.")
            input("\nenter to continue...")
            continue

        found = [n for n in names if ask.lower() in n.lower()]
        if not found:
            print("\nnot found")
            input("\nenter to continue...")
            continue

        print()
        for name in found:
            print(name)
        print()
        if len(found) == 1:
            meta = docs[found[0]]
            print("-" * 80)
            if meta["signature"]:
                print("signature:", meta["signature"])
            print("kind:", meta["kind"])
            if meta["file"]:
                print("file:", meta["file"])
            print()
            print(meta["doc"] or "No docstring.")
        input("\nenter to continue...")


def parse_args(argv: List[str]) -> Dict[str, Any]:
    args = {
        "module": None,
        "max_depth": 4,
        "include_private": False,
        "include_submodules": False,
        "interactive": False,
        "output": None,
    }

    i = 0
    positional = []
    while i < len(argv):
        arg = argv[i]

        if arg in ("-a", "-ask"):
            args["interactive"] = True
        elif arg in ("-p", "-private"):
            args["include_private"] = True
        elif arg in ("-s", "-submodules"):
            args["include_submodules"] = True
        elif arg in ("-d", "-depth") and i + 1 < len(argv):
            i += 1
            try:
                args["max_depth"] = int(argv[i])
            except Exception:
                pass
        elif arg in ("-o", "-out") and i + 1 < len(argv):
            i += 1
            args["output"] = argv[i]
        else:
            positional.append(arg)

        i += 1

    if positional:
        args["module"] = positional[-1]

    return args


def main():
    args = parse_args(sys.argv[1:])
    module_name = args["module"]

    if not module_name:
        print("usage:")
        print("    script.py [-a] [-p] [-s] [-d 4] [-o output.md] module_name")
        sys.exit(1)

    try:
        module = importlib.import_module(module_name)
    except Exception as e:
        print(f"failed to import '{module_name}': {e}")
        sys.exit(1)

    docs = scan_object(
        module,
        display_name=module_name,
        root_name=module_name,
        max_depth=args["max_depth"],
        current_depth=0,
        include_private=args["include_private"],
        include_submodules=args["include_submodules"],
    )

    if args["interactive"]:
        interactive_lookup(docs, module_name)
        return

    md = render_markdown(module_name, docs)
    output = args["output"]

    if output:
        with open(output, "w", encoding="utf-8") as f:
            f.write("\n".join(md))
        print(output)
    else:
        print("\n".join(md))


if __name__ == "__main__":
    main()