#!/usr/bin/env python3
import argparse
import base64
import os
import sqlite3
import sys
from pathlib import Path
from typing import Iterable, Optional, Tuple, Union

def read_targets(args: argparse.Namespace) -> list[str]:
    targets: list[str] = []
    if args.names:
        targets.extend(args.names)
    if args.list:
        with open(args.list, 'r', encoding='utf-8', errors='replace') as f:
            targets.extend([line.strip() for line in f if line.strip()])
    if not targets and not sys.stdin.isatty():
        targets.extend([line.strip() for line in sys.stdin if line.strip()])
    # De-dup, preserve order
    seen = set()
    uniq = []
    for t in targets:
        if t not in seen:
            seen.add(t)
            uniq.append(t)
    return uniq

def ensure_dir(path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)

def looks_base64(s: str) -> bool:
    s_stripped = s.strip()
    if len(s_stripped) < 16:
        return False
    # Heuristic: base64 chars only and length multiple of 4
    b64chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=\n\r"
    if any(c not in b64chars for c in s_stripped[:200]):
        return False
    return len(s_stripped.replace("\n", "")) % 4 == 0

def decode_content(val: Union[bytes, memoryview, str]) -> bytes:
    # SQLite returns BLOB as 'bytes' or 'memoryview'; TEXT as 'str'
    if isinstance(val, memoryview):
        return bytes(val)
    if isinstance(val, bytes):
        return val
    if isinstance(val, str):
        s = val
        # Try base64 first (some pipelines store content as base64 TEXT)
        if looks_base64(s):
            try:
                return base64.b64decode(s, validate=False)
            except Exception:
                pass
        # Fallback: UTF-8 text -> bytes
        return s.encode('utf-8', errors='replace')
    # Unknown – stringify
    return str(val).encode('utf-8', errors='replace')

def safe_join(base: Path, sub: str) -> Path:
    # Prevent writing outside base
    p = (base / sub).resolve()
    if not str(p).startswith(str(base.resolve())):
        # flatten to name only if path tries to escape
        return base / Path(sub).name
    return p

def connect_db(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(str(path))
    # Return bytes for blobs
    con.text_factory = str
    return con

def fetch_by_name(cur: sqlite3.Cursor, name: str) -> Optional[Tuple[str, str, Union[bytes, memoryview, str]]]:
    cur.execute("SELECT name, path, content FROM files WHERE name = ? AND (skipped IS NULL OR skipped = 0) LIMIT 1", (name,))
    return cur.fetchone()

def fetch_by_like(cur: sqlite3.Cursor, pattern: str) -> Iterable[Tuple[str, str, Union[bytes, memoryview, str]]]:
    like = pattern
    cur.execute("SELECT name, path, content FROM files WHERE name LIKE ? AND (skipped IS NULL OR skipped = 0)", (like,))
    yield from cur.fetchall()

def write_file(dest_root: Path, record: Tuple[str, str, Union[bytes, memoryview, str]], preserve_path: bool, overwrite: bool, dry_run: bool) -> Path:
    name, original_path, content = record
    data = decode_content(content)

    # Build output path
    if preserve_path and original_path:
        # Original path might be absolute; make it relative-ish under dest_root
        rel = original_path.lstrip("/\\")
        out_path = safe_join(dest_root, rel)
    else:
        out_path = dest_root / name

    if out_path.exists() and not overwrite:
        return out_path  # skip silently

    if not dry_run:
        ensure_dir(out_path)
        with open(out_path, "wb") as f:
            f.write(data)
    return out_path

def main():
    ap = argparse.ArgumentParser(
        description="Recover files from a SQLite index (table: files). Writes file contents from the 'content' column."
    )
    ap.add_argument(
        "-d", "--db", action="append", required=True,
        help="Path to SQLite DB (can be repeated; first hit wins). Example: 2025.06.29-index.db"
    )
    ap.add_argument(
        "-o", "--out", default="recovered",
        help="Destination directory (default: ./recovered)"
    )
    ap.add_argument(
        "--preserve-path", action="store_true",
        help="Recreate the original 'path' directory structure under the destination."
    )
    ap.add_argument(
        "-n", "--names", nargs="*",
        help="One or more exact file names to recover (match on files.name)."
    )
    ap.add_argument(
        "-l", "--list",
        help="Text file with one file name per line."
    )
    ap.add_argument(
        "--like",
        help="SQL LIKE pattern to select names (e.g., '%.py' or 'ephemeral%%'). If provided, --names are also processed."
    )
    ap.add_argument(
        "--overwrite", action="store_true",
        help="Overwrite existing files at destination."
    )
    ap.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be written without creating files."
    )
    args = ap.parse_args()

    dest_root = Path(args.out).resolve()
    if not args.dry_run:
        dest_root.mkdir(parents=True, exist_ok=True)

    targets = read_targets(args)

    # Prepare DB connections in order
    db_paths = [Path(p) for p in args.db]
    connections = []
    try:
        for dbp in db_paths:
            if not dbp.exists():
                print(f"[WARN] DB not found: {dbp}", file=sys.stderr)
                continue
            connections.append((dbp, connect_db(dbp)))

        if not connections:
            print("[ERROR] No valid DBs opened.", file=sys.stderr)
            sys.exit(2)

        recovered = 0
        missing = 0

        # Process explicit names
        for name in targets:
            found = False
            for dbp, con in connections:
                cur = con.cursor()
                row = fetch_by_name(cur, name)
                if row:
                    out_path = write_file(dest_root, row, args.preserve_path, args.overwrite, args.dry_run)
                    action = "WOULD WRITE" if args.dry_run else "WROTE"
                    print(f"[{action}] {name} -> {out_path}")
                    recovered += 1
                    found = True
                    break
            if not found:
                print(f"[MISS] {name} (not found in provided DBs)")
                missing += 1

        # Process LIKE pattern (optional)
        if args.like:
            pattern_hits = 0
            seen_names = set(targets)  # avoid duplicate re-writes
            for dbp, con in connections:
                cur = con.cursor()
                for row in fetch_by_like(cur, args.like):
                    name = row[0]
                    if name in seen_names:
                        continue
                    out_path = write_file(dest_root, row, args.preserve_path, args.overwrite, args.dry_run)
                    action = "WOULD WRITE" if args.dry_run else "WROTE"
                    print(f"[{action}] {name} -> {out_path}")
                    recovered += 1
                    pattern_hits += 1
            if pattern_hits == 0:
                print(f"[INFO] LIKE pattern matched no rows: {args.like}")

        print(f"\nSummary: recovered={recovered}, missing={missing}, dest={dest_root}")
    finally:
        for _, con in connections:
            try:
                con.close()
            except Exception:
                pass

if __name__ == "__main__":
    main()
