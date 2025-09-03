#!/usr/bin/env python3
"""
zero_fill.py — copy missing (0-byte) files from a source tree to a destination tree,
matching by relative path.

Usage examples:
    python zero_fill.py --src "D:/PhotosPrimary" --dst "E:/PhotosBackup"
    python zero_fill.py --src /mnt/src --dst /mnt/dst -r
"""

import argparse
import sys
from pathlib import Path
import shutil
import os

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Copy from --src to --dst only when the file exists in dst and is 0 bytes (match by relative path)."
    )
    p.add_argument("-src", required=True, type=Path, help="Source folder")
    p.add_argument("-dst", required=True, type=Path, help="Destination folder to scan for 0-byte files")
    p.add_argument("-r", "--recursive", action="store_true", help="Recurse into subfolders")
    p.add_argument("-n", "--dry-run", action="store_true", help="Show what would be copied, but make no changes")
    p.add_argument("-v", "--verbose", action="store_true", help="Print each action")
    return p.parse_args()

def is_zero_byte(path: Path) -> bool:
    try:
        return path.is_file() and path.stat().st_size == 0
    except OSError:
        return False

def main() -> int:
    args = parse_args()
    src = args.src.resolve()
    dst = args.dst.resolve()

    if not src.exists() or not src.is_dir():
        print(f"[ERROR] --src does not exist or is not a directory: {src}", file=sys.stderr)
        return 2
    if not dst.exists() or not dst.is_dir():
        print(f"[ERROR] --dst does not exist or is not a directory: {dst}", file=sys.stderr)
        return 2
    if src == dst:
        print("[ERROR] --src and --dst must be different folders.", file=sys.stderr)
        return 2
    # Prevent copying src into itself via a child path confusion
    try:
        src_rel = dst.relative_to(src)
        print(f"[ERROR] --dst is inside --src ({src_rel}). This is not supported.", file=sys.stderr)
        return 2
    except Exception:
        pass

    pattern = "**/*" if args.recursive else "*"
    examined = 0
    zero_found = 0
    copied = 0
    skipped_missing_in_src = 0
    skipped_nonzero_src = 0
    errors = 0

    for dpath in dst.glob(pattern):
        try:
            if not dpath.is_file(): continue
        except:
            continue
        examined += 1
        if not is_zero_byte(dpath):
            continue

        zero_found += 1
        rel = dpath.relative_to(dst)
        spath = src / rel

        if not spath.exists() or not spath.is_file():
            skipped_missing_in_src += 1
            if args.verbose:
                print(f"[MISS] No matching file in src: {rel}")
            continue

        try:
            ssize = spath.stat().st_size
        except OSError as e:
            errors += 1
            if args.verbose:
                print(f"[ERROR] Cannot stat src file: {rel} ({e})")
            continue

        if ssize == 0:
            skipped_nonzero_src += 1
            if args.verbose:
                print(f"[SKIP] Src file also 0 bytes: {rel}")
            continue

        if args.verbose or args.dry_run:
            print(f"[COPY]{' (dry-run)' if args.dry_run else ''} {rel}  src_size={ssize}B")

        if not args.dry_run:
            try:
                # Copy metadata (mtime) too; overwrites the 0-byte file in dst.
                shutil.copy2(spath, dpath)
                copied += 1
            except OSError as e:
                errors += 1
                print(f"[ERROR] Failed to copy {rel}: {e}", file=sys.stderr)

    print("\n=== Summary ===")
    print(f" Scanned files in dst    : {examined}")
    print(f" 0-byte files in dst     : {zero_found}")
    print(f" Copied from src         : {copied}{' (dry-run: none actually copied)' if args.dry_run else ''}")
    print(f" Missing in src          : {skipped_missing_in_src}")
    print(f" Src also 0 bytes        : {skipped_nonzero_src}")
    print(f" Errors                  : {errors}")

    return 0 if errors == 0 else 1

if __name__ == "__main__":
    os.environ.setdefault("PYTHONUTF8", "1")
    sys.exit(main())
