#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rotating_backup.py — Snapshot-style rotating backups into N slots (0..N-1)

• Uses rsync for fast copies and space-efficient snapshots via --link-dest
• Verifies the copy (file counts + random checksum sample) before committing
• If verification fails, the previous snapshot remains the active one
• Maintains atomic "latest" and "prev" symlinks for convenience

Requirements:
    - Linux/Unix with rsync installed
    - Source directory readable; destination root writable

Example:
    python3 rotating_backup.py \
        --source /data/projects \
        --dest-root /backups/projects \
        --slots 5 \
        --verify-samples 200 \
        --exclude-file /etc/backup.exclude

Cron (daily at 02:15):
    15 2 * * * /usr/bin/env nice -n 10 /usr/bin/python3 /opt/rotating_backup.py \
        --source /data/projects --dest-root /backups/projects --slots 5 \
        --verify-samples 200 --log /var/log/rotating_backup.log >> /var/log/rotating_backup.log 2>&1

Restore (example):
    # List snapshots
    ls -lah /backups/projects
    # Restore a file/folder from slot 3
    rsync -aHAX --info=progress2 /backups/projects/3/some/path/ /restore/target/

"""

import argparse
import datetime as dt
import json
import math
import os
import random
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

# -------------------------- Utilities --------------------------

def log(msg: str):
    ts = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{ts}] {msg}")


def run(cmd, check=True):
    log("$ " + " ".join(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"Command failed ({proc.returncode}): {' '.join(cmd)}\n{proc.stdout}")
    return proc


def bytes_to_human(n: int) -> str:
    units = ['B','KB','MB','GB','TB','PB']
    if n <= 0:
        return '0 B'
    i = min(int(math.log(n, 1024)), len(units)-1)
    return f"{n / (1024 ** i):.2f} {units[i]}"


# -------------------------- Core logic --------------------------

def discover_latest(dest_root: Path, slots: int) -> int | None:
    latest_link = dest_root / 'latest'
    if latest_link.is_symlink():
        try:
            target = latest_link.resolve()
            # Expect .../<slot>
            if target.parent == dest_root and target.name.isdigit():
                slot = int(target.name)
                if 0 <= slot < slots:
                    return slot
        except FileNotFoundError:
            pass
    # Fallback: pick the newest existing numeric folder
    candidates = [int(p.name) for p in dest_root.iterdir() if p.is_dir() and p.name.isdigit()]
    candidates = [c for c in candidates if 0 <= c < slots]
    return max(candidates) if candidates else None


def ensure_layout(dest_root: Path, slots: int):
    dest_root.mkdir(parents=True, exist_ok=True)
    for i in range(slots):
        (dest_root / str(i)).mkdir(exist_ok=True)


def free_space_ok(path: Path, min_free_bytes: int) -> bool:
    usage = shutil.disk_usage(path)
    log(f"Destination free space: {bytes_to_human(usage.free)} (min required: {bytes_to_human(min_free_bytes)})")
    return usage.free >= min_free_bytes


def build_rsync_cmd(src: Path, tmp_dest: Path, link_dest: Path | None, exclude_file: Path | None, nice: int | None, ionice: int | None, extra: list[str]) -> list[str]:
    base = [
        'rsync', '-aHAX', '--delete', '--numeric-ids', '--partial', '--info=progress2',
    ]
    if link_dest is not None:
        base += [f"--link-dest={link_dest}"]
    if exclude_file is not None and exclude_file.exists():
        base += [f"--exclude-from={exclude_file}"]
    base += extra
    base += [str(src) + '/', str(tmp_dest) + '/']

    # Optional scheduling niceness
    if nice is not None:
        base = ['nice', f'-n{nice}'] + base
    if ionice is not None:
        base = ['ionice', f'-c{ionice}'] + base
    return base


def collect_files(root: Path) -> list[Path]:
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dp = Path(dirpath)
        for fn in filenames:
            files.append(dp / fn)
    return files


def sha256_of(path: Path) -> str:
    import hashlib
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_snapshot(src: Path, tmp_dest: Path, samples: int) -> tuple[bool, str]:
    # Quick compare: counts
    src_files = collect_files(src)
    dst_files = collect_files(tmp_dest)
    if len(dst_files) < len(src_files):
        return False, f"File count mismatch: src={len(src_files)} dst={len(dst_files)}"

    # Random sample checksum set (bounded)
    if samples > 0 and src_files:
        k = min(samples, len(src_files))
        sample_paths = random.sample(src_files, k)
        for p in sample_paths:
            rel = p.relative_to(src)
            q = tmp_dest / rel
            if not q.exists():
                return False, f"Missing file in destination: {rel}"
            if q.is_symlink():
                # It's fine if rsync created hard-links; but symlinks in data may exist.
                pass
            if q.is_file():
                if sha256_of(p) != sha256_of(q):
                    return False, f"Checksum mismatch: {rel}"
    return True, "OK"


def atomic_commit(dest_root: Path, slot: int, tmp_dir: Path):
    slot_dir = dest_root / str(slot)
    backup_old = dest_root / f".{slot}.old"
    if backup_old.exists():
        shutil.rmtree(backup_old, ignore_errors=True)
    # Move current slot aside, then promote tmp to slot
    if slot_dir.exists():
        slot_dir.rename(backup_old)
    tmp_dir.rename(slot_dir)
    shutil.rmtree(backup_old, ignore_errors=True)


def update_symlinks(dest_root: Path, new_slot: int, prev_slot: int | None):
    latest = dest_root / 'latest'
    prev = dest_root / 'prev'
    for link in (latest, prev):
        try:
            if link.is_symlink() or link.exists():
                link.unlink()
        except FileNotFoundError:
            pass
    (dest_root / str(new_slot)).symlink_to(latest)
    if prev_slot is not None and 0 <= prev_slot:
        (dest_root / str(prev_slot)).symlink_to(prev)


def write_state(dest_root: Path, state: dict):
    with open(dest_root / '.state.json', 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=2, sort_keys=True)


def read_state(dest_root: Path) -> dict:
    f = dest_root / '.state.json'
    if f.exists():
        try:
            return json.loads(f.read_text(encoding='utf-8'))
        except Exception:
            return {}
    return {}


# -------------------------- Main entry --------------------------

def main():
    ap = argparse.ArgumentParser(description='Rotating rsync snapshots with verification (slots 0..N-1).')
    ap.add_argument('--source', required=True, type=Path, help='Source directory to back up')
    ap.add_argument('--dest-root', required=True, type=Path, help='Destination root (contains numeric slots)')
    ap.add_argument('--slots', type=int, default=5, help='Number of rotating slots (default: 5)')
    ap.add_argument('--min-free', type=str, default='5GB', help='Minimum free space required at dest (e.g. 20GB, 500MB)')
    ap.add_argument('--verify-samples', type=int, default=100, help='Random files to checksum-verify (0 = skip)')
    ap.add_argument('--exclude-file', type=Path, help='Optional rsync exclude file')
    ap.add_argument('--extra', nargs='*', default=[], help='Extra args for rsync (e.g. --compress)')
    ap.add_argument('--nice', type=int, help='nice level (e.g. 10)')
    ap.add_argument('--ionice', type=int, help='ionice class (2 = best-effort)')
    ap.add_argument('--log', type=Path, help='Append stdout/err to this file (also prints)')
    ap.add_argument('--dry-run', action='store_true', help='Plan only; do not copy/modify')

    args = ap.parse_args()

    # Optional file logging (very simple tee)
    if args.log:
        args.log.parent.mkdir(parents=True, exist_ok=True)
        log_file = open(args.log, 'a', encoding='utf-8')
        class Tee:
            def write(self2, s):
                sys.__stdout__.write(s)
                log_file.write(s)
            def flush(self2):
                sys.__stdout__.flush(); log_file.flush()
        sys.stdout = Tee()  # type: ignore
        sys.stderr = sys.stdout

    src = args.source.resolve()
    dest_root = args.dest_root.resolve()

    if not src.exists() or not src.is_dir():
        log(f"ERROR: Source does not exist or is not a directory: {src}")
        sys.exit(2)
    if src == dest_root or str(dest_root).startswith(str(src)):
        log("ERROR: dest-root must not be the source or inside the source")
        sys.exit(2)

    ensure_layout(dest_root, args.slots)

    # Parse min-free like "20GB"
    units = {'KB':1024, 'MB':1024**2, 'GB':1024**3, 'TB':1024**4}
    mf = args.min_free.strip().upper()
    min_free_bytes = 0
    for u, m in units.items():
        if mf.endswith(u):
            min_free_bytes = int(float(mf[:-len(u)]) * m)
            break
    if min_free_bytes == 0:
        min_free_bytes = int(mf) if mf.isdigit() else 0

    if not free_space_ok(dest_root, min_free_bytes):
        log("ERROR: Not enough free space; aborting")
        sys.exit(3)

    current_latest = discover_latest(dest_root, args.slots)
    next_slot = 0 if current_latest is None else (current_latest + 1) % args.slots

    log(f"Current latest slot: {current_latest if current_latest is not None else 'None'}; Next slot: {next_slot}")

    # Prepare temporary destination for atomic commit
    stamp = dt.datetime.now().strftime('%Y%m%d-%H%M%S')
    tmp_dir = dest_root / f".inflight-{next_slot}-{stamp}"

    if args.dry_run:
        log(f"DRY RUN: would rsync {src} -> {tmp_dir} (link-dest={dest_root/str(current_latest) if current_latest is not None else 'None'})")
        sys.exit(0)

    if tmp_dir.exists():
        shutil.rmtree(tmp_dir)
    tmp_dir.mkdir(parents=True, exist_ok=True)

    link_dest = dest_root / str(current_latest) if current_latest is not None else None
    exclude_file = args.exclude_file if args.exclude_file else None

    rsync_cmd = build_rsync_cmd(
        src=src,
        tmp_dest=tmp_dir,
        link_dest=link_dest,
        exclude_file=exclude_file,
        nice=args.nice,
        ionice=args.ionice,
        extra=args.extra,
    )

    try:
        run(rsync_cmd, check=True)
    except Exception as e:
        log(f"ERROR: rsync failed: {e}")
        shutil.rmtree(tmp_dir, ignore_errors=True)
        sys.exit(4)

    ok, reason = verify_snapshot(src, tmp_dir, args.verify_samples)
    if not ok:
        log(f"ERROR: verification failed: {reason}")
        # quarantine the failed attempt for inspection
        quarantine = dest_root / 'quarantine'
        quarantine.mkdir(exist_ok=True)
        bad_dir = quarantine / tmp_dir.name
        try:
            tmp_dir.rename(bad_dir)
            log(f"Moved failed snapshot to: {bad_dir}")
        except Exception:
            shutil.rmtree(tmp_dir, ignore_errors=True)
        sys.exit(5)

    # Commit and rotate
    prev_slot = current_latest if current_latest is not None else None
    atomic_commit(dest_root, next_slot, tmp_dir)
    update_symlinks(dest_root, next_slot, prev_slot)

    # Persist state
    state = read_state(dest_root)
    state.update({
        'last_success': dt.datetime.now().isoformat(),
        'latest_slot': next_slot,
        'prev_slot': prev_slot,
        'source': str(src),
        'slots': args.slots,
        'verify_samples': args.verify_samples,
    })
    write_state(dest_root, state)

    log(f"SUCCESS: snapshot committed to slot {next_slot} -> {dest_root/str(next_slot)}")
    log("Symlinks: latest -> current, prev -> previous")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log('Interrupted by user')
        sys.exit(130)
