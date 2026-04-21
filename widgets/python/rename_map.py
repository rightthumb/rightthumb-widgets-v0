#!/usr/bin/env python3
import os
import sys
import shutil

EXIT_ERROR = 2

def help_text() -> str:
    return (
        "rename_map.py\n"
        "\n"
        "Usage:\n"
        "  rename_map.py <source_list.txt> <dest_list.txt> [--dry-run]\n"
        "\n"
        "Behavior:\n"
        "  • No args => help (exit 0)\n"
        "  • Any error => help + error (exit != 0)\n"
        "\n"
        "Args:\n"
        "  • Arguments may appear in any order\n"
        "  • First non-flag arg = source list (existing files)\n"
        "  • Second non-flag arg = destination list (new paths)\n"
        "  • Flags: --dry-run, --help\n"
        "\n"
        "Mapping rules:\n"
        "  • Blank lines ignored\n"
        "  • Lines starting with '#' ignored\n"
        "  • Line counts must match after filtering\n"
        "\n"
        "Safety:\n"
        "  • Mapping entries may be relative OR absolute\n"
        "  • BUT they must resolve under the current working directory\n"
        "  • '..' is not allowed\n"
        "  • Destination folders auto-created\n"
        "  • Destination must NOT already exist\n"
    )

def error(msg: str) -> None:
    print(f"ERROR: {msg}\n", file=sys.stderr)
    print(help_text(), file=sys.stderr)
    sys.exit(EXIT_ERROR)

def norm_line(s: str) -> str:
    # Trim and also remove accidental trailing spaces in paths (common from copy/paste)
    return s.strip()

def has_parent_traversal(p: str) -> bool:
    norm = os.path.normpath(p)
    parts = norm.replace("\\", "/").split("/")
    return ".." in parts

def resolve_under_base(p: str, base_abs: str) -> str:
    """
    Accept relative or absolute path, but only if it resolves under base_abs.
    Returns absolute resolved path if allowed.
    """
    p = norm_line(p)
    if not p:
        error("Empty path in mapping file")

    if has_parent_traversal(p):
        error(f"Path contains '..' which is not allowed: {p}")

    # Resolve absolute target
    if os.path.isabs(p) or (len(p) >= 2 and p[1] == ":"):
        abs_path = os.path.abspath(p)
    else:
        abs_path = os.path.abspath(os.path.join(base_abs, p))

    base_abs_norm = os.path.normcase(os.path.abspath(base_abs))
    abs_norm = os.path.normcase(abs_path)

    # Ensure it's within base folder
    try:
        common = os.path.commonpath([base_abs_norm, abs_norm])
    except ValueError:
        # Different drives on Windows -> definitely not under base
        error(f"Path is not under base folder (different drive): {p}")

    if common != base_abs_norm:
        error(f"Path escapes the base folder. Base={base_abs} Path={p}")

    return abs_path

def read_list(list_file: str) -> list[str]:
    # list_file itself can be relative; resolve to current working directory
    if not list_file:
        error("Missing list file path")

    # list file must exist
    if not os.path.isfile(list_file):
        error(f"List file not found: {list_file}")

    out: list[str] = []
    with open(list_file, "r", encoding="utf-8") as f:
        for raw in f:
            line = norm_line(raw)
            if not line or line.startswith("#"):
                continue
            out.append(line)
    return out

def ensure_parent(dest_abs: str) -> None:
    parent = os.path.dirname(dest_abs)
    if parent:
        os.makedirs(parent, exist_ok=True)

def main() -> None:
    argv = sys.argv[1:]

    # No args -> help success
    if not argv:
        print(help_text())
        sys.exit(0)

    dry_run = False
    files: list[str] = []

    for arg in argv:
        if arg in ("--help", "-h"):
            print(help_text())
            sys.exit(0)
        elif arg == "--dry-run":
            dry_run = True
        elif arg.startswith("-"):
            error(f"Unknown flag: {arg}")
        else:
            files.append(arg)

    if len(files) < 2:
        error("Two list files are required")

    src_list_file = files[0]
    dst_list_file = files[1]

    base_abs = os.path.abspath(os.getcwd())

    src_lines = read_list(src_list_file)
    dst_lines = read_list(dst_list_file)

    if len(src_lines) != len(dst_lines):
        error(
            f"Line count mismatch after filtering: "
            f"{len(src_lines)} source vs {len(dst_lines)} destination"
        )

    mappings: list[tuple[str, str]] = []
    for i, (src_raw, dst_raw) in enumerate(zip(src_lines, dst_lines), start=1):
        src_abs = resolve_under_base(src_raw, base_abs)
        dst_abs = resolve_under_base(dst_raw, base_abs)

        if not os.path.isfile(src_abs):
            error(f"Source file does not exist (line {i}): {src_raw}")

        if os.path.exists(dst_abs):
            error(f"Destination already exists (line {i}): {dst_raw}")

        mappings.append((src_abs, dst_abs))

    for i, (src_abs, dst_abs) in enumerate(mappings, start=1):
        src_show = os.path.relpath(src_abs, base_abs)
        dst_show = os.path.relpath(dst_abs, base_abs)
        print(f"{i:04d}  {src_show}  ->  {dst_show}")

        if not dry_run:
            ensure_parent(dst_abs)
            shutil.move(src_abs, dst_abs)

    print("\nDRY RUN complete — no files changed." if dry_run else "\nDone.")

if __name__ == "__main__":
    main()
