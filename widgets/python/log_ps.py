#!/usr/bin/env python3
import os
import time
import json
import pwd
import hashlib
from datetime import datetime

# ============================
# Config
# ============================
OUT_DIR = os.environ.get("OUT_DIR", "/opt/psuniq")
LOG_FILE = os.path.join(OUT_DIR, "ps.jsonl")       # JSONL: one JSON object per line
STATE_FILE = os.path.join(OUT_DIR, "seen.hashes")  # one hash per line
INTERVAL_SEC = int(os.environ.get("INTERVAL_SEC", "10"))

os.makedirs(OUT_DIR, exist_ok=True)
open(LOG_FILE, "a").close()
open(STATE_FILE, "a").close()

HZ = os.sysconf(os.sysconf_names.get("SC_CLK_TCK", "SC_CLK_TCK"))
PAGE_SIZE = os.sysconf("SC_PAGE_SIZE")

def _read_text(path):
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return f.read()
    except Exception:
        return None

def _read_bytes(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except Exception:
        return None

def _uptime_seconds():
    s = _read_text("/proc/uptime")
    if not s:
        return None
    try:
        return float(s.split()[0])
    except Exception:
        return None

def _parse_stat(stat_text):
    """
    Parse /proc/[pid]/stat. The second field (comm) can contain spaces and is inside parentheses.
    We find the last ')' and split accordingly.
    Returns dict with keys: comm, state, ppid, starttime_ticks, vsize_bytes, rss_pages, tty_nr.
    """
    if not stat_text:
        return None
    try:
        rparen = stat_text.rfind(")")
        lparen = stat_text.find("(")
        comm = stat_text[lparen+1:rparen]
        rest = stat_text[rparen+2:].split()
        # Fields: https://man7.org/linux/man-pages/man5/proc.5.html
        state = rest[0]                         # 3
        ppid = int(rest[1])                     # 4
        tty_nr = int(rest[4])                   # 7
        starttime_ticks = int(rest[19])         # 22
        vsize_bytes = int(rest[20])             # 23
        rss_pages = int(rest[21])               # 24
        return {
            "comm": comm,
            "state": state,
            "ppid": ppid,
            "tty_nr": tty_nr,
            "starttime_ticks": starttime_ticks,
            "vsize_bytes": vsize_bytes,
            "rss_pages": rss_pages,
        }
    except Exception:
        return None

def _uid_to_name(uid):
    try:
        return pwd.getpwuid(uid).pw_name
    except Exception:
        return str(uid)

def _read_status_map(pid):
    txt = _read_text(f"/proc/{pid}/status")
    out = {}
    if not txt:
        return out
    for line in txt.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip()
    return out

def _get_cmdline(pid):
    b = _read_bytes(f"/proc/{pid}/cmdline")
    if not b:
        return ""
    # cmdline is NUL-separated; last byte may be NUL
    parts = [p.decode("utf-8", "replace") for p in b.split(b"\x00") if p]
    return " ".join(parts)

def _format_stat_flags(state_char):
    # Keep it simple: just the one-letter state from /proc/PID/stat (R,S,D,T,t,Z,X,K,W,P,I)
    return state_char or "?"

def _collect_process(pid, uptime):
    # Many /proc files race (process exits). Handle exceptions gracefully.
    stat_text = _read_text(f"/proc/{pid}/stat")
    info = _parse_stat(stat_text)
    if not info:
        return None

    # etimes
    etimes = None
    if uptime is not None and HZ:
        try:
            start_sec = info["starttime_ticks"] / float(HZ)
            etimes = max(0, int(uptime - start_sec))
        except Exception:
            pass

    # status (for Uid, VmRSS fallback)
    status_map = _read_status_map(pid)
    uid_str = status_map.get("Uid", "0").split()[0]
    try:
        uid = int(uid_str)
    except Exception:
        uid = 0
    user = _uid_to_name(uid)

    # vsz / rss
    vsz = info.get("vsize_bytes") or 0
    rss_pages = info.get("rss_pages") or 0
    rss = rss_pages * PAGE_SIZE if PAGE_SIZE else 0

    # command
    cmd = _get_cmdline(pid)
    if not cmd:
        # For kernel threads and some cases, fallback to comm in brackets (like ps does)
        cmd = f"[{info.get('comm','')}]"

    # ppid & state
    ppid = info.get("ppid", 0)
    stat = _format_stat_flags(info.get("state"))

    return {
        "pid": int(pid),
        "ppid": int(ppid),
        "user": user,
        "pcpu": None,     # not trivial without sampling; keep placeholders
        "pmem": None,     # not trivial without sampling; keep placeholders
        "vsz": int(vsz),  # bytes
        "rss": int(rss),  # bytes
        "tty": None,      # decoding tty_nr to device is non-trivial; omit
        "stat": stat,
        "etimes": int(etimes) if etimes is not None else None,
        "cmd": cmd,
    }

def _iter_pids():
    for name in os.listdir("/proc"):
        if name.isdigit():
            yield name

def _load_seen():
    seen = set()
    with open(STATE_FILE, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if line:
                seen.add(line)
    return seen

def _append_seen(new_hashes):
    if not new_hashes:
        return
    with open(STATE_FILE, "a", encoding="utf-8") as f:
        for h in new_hashes:
            f.write(h + "\n")

def _hash_key(proc_obj):
    # Uniqueness key: user|pid|etimes|cmd
    user = proc_obj.get("user", "")
    pid = proc_obj.get("pid", 0)
    et = proc_obj.get("etimes", 0)
    cmd = proc_obj.get("cmd", "")
    key = f"{user}|{pid}|{et}|{cmd}"
    return hashlib.sha256(key.encode("utf-8", "replace")).hexdigest()

def main():
    # Single instance lock
    lock_path = os.path.join(OUT_DIR, ".lock")
    lock_fd = os.open(lock_path, os.O_CREAT | os.O_RDWR, 0o644)
    try:
        import fcntl
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except Exception:
        print("Another ps_unique_logger instance is running. Exiting.")
        return

    seen = _load_seen()

    while True:
        uptime = _uptime_seconds()
        new_procs = []
        new_hashes = []

        for pid in _iter_pids():
            try:
                proc = _collect_process(pid, uptime)
                if not proc:
                    continue
                h = _hash_key(proc)
                if h not in seen:
                    new_procs.append(proc)
                    new_hashes.append(h)
            except Exception:
                # Process exited or permission race; skip
                continue

        if new_procs:
            obj = {
                "captured_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
                "processes": new_procs
            }
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(obj, ensure_ascii=False) + "\n")
            _append_seen(new_hashes)
            seen.update(new_hashes)

        time.sleep(INTERVAL_SEC)

if __name__ == "__main__":
    main()
