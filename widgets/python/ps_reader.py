#!/usr/bin/env python3
import argparse, sys, json, re, os, csv
from datetime import datetime, timezone
from collections import Counter, defaultdict

# ---------- Helpers ----------
ISO = "%Y-%m-%dT%H:%M:%SZ"

def parse_time(s):
    if not s: return None
    try:
        # Accept "YYYY-mm-ddTHH:MM:SSZ" or "YYYY-mm-dd HH:MM"
        if "T" in s and s.endswith("Z"):
            return datetime.strptime(s, ISO).replace(tzinfo=timezone.utc)
        # Flexible fallback
        return datetime.fromisoformat(s).astimezone(timezone.utc)
    except Exception:
        raise argparse.ArgumentTypeError(f"Invalid time: {s}")

def to_utc(dt):
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)

def iter_jsonl(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for ln, line in enumerate(f, 1):
            line=line.strip()
            if not line: continue
            try:
                obj=json.loads(line)
                ts = obj.get("captured_at")
                # Normalize timestamp
                t = None
                if ts:
                    try:
                        t = datetime.strptime(ts, ISO).replace(tzinfo=timezone.utc)
                    except Exception:
                        t = to_utc(datetime.fromisoformat(ts))
                for p in obj.get("processes", []):
                    yield (t, p)
            except Exception as e:
                print(f"[warn] {path}:{ln} parse error: {e}", file=sys.stderr)

def match_any_regex(text, regexes):
    if not regexes: return True
    for r in regexes:
        if r.search(text): return True
    return False

def within_range(t, since, until):
    if t is None: return True
    if since and t < since: return False
    if until and t > until: return False
    return True

def fmt_bytes(n):
    if n is None: return "-"
    u = ["B","KB","MB","GB","TB"]
    i=0; f=float(n)
    while f>=1024 and i<len(u)-1:
        f/=1024; i+=1
    return f"{f:.1f}{u[i]}"

def print_table(rows, headers):
    # Simple wide table
    widths=[len(h) for h in headers]
    for row in rows:
        for i,cell in enumerate(row):
            widths[i]=max(widths[i], len(str(cell)))
    fmt="  ".join("{:"+str(w)+"}" for w in widths)
    print(fmt.format(*headers))
    print(fmt.format(*["-"*w for w in widths]))
    for row in rows:
        print(fmt.format(*row))

def compile_regexes(patterns, flags=0):
    return [re.compile(p, flags) for p in patterns] if patterns else []

def basecmd(cmd):
    if not cmd: return ""
    parts = cmd.split()
    exe = parts[0]
    return os.path.basename(exe)

# ---------- Suspicious heuristics ----------
IOC_RULES = [
    # Reverse shells / TTY tricks
    (r"bash\s+-i", "bash interactive (possible reverse shell)"),
    (r"/dev/tcp/\S+/\d+", "bash TCP redirection (/dev/tcp)"),
    (r"nc\s+.*(-e|/bin/sh|/bin/bash)", "netcat with -e shell"),
    (r"socat\s+.*(PTY|EXEC|TCP|TCP4|TCP6)", "socat tunneling/exec"),
    (r"python\S*\s+-c\s+['\"]?import\s+socket", "python inline socket (reverse shell?)"),
    (r"perl\s+-e\s+.*socket", "perl inline socket"),
    (r"php\s+-r\s+.*fsockopen", "php inline socket"),
    # Tunneling / beaconing tools
    (r"\bssh\s+.*\s(-R|-L|-D)\s*\d", "ssh port forwarding"),
    (r"\bsshuttle\b", "sshuttle proxy"),
    (r"\bchisel\b", "chisel tunnel"),
    (r"\bfrpc?\b", "FRP client/server"),
    (r"\bbox\b.*(relay|client)", "ngrok/box relays"),
    # Dropper/execution chains
    (r"(curl|wget).*\|\s*(bash|sh|python|perl)", "curl|wget piped to interpreter"),
    (r"(curl|wget)\s+.*http", "curl|wget http fetch"),
    (r"\bpython\S*\s+-c\s+", "python -c inline code"),
    (r"\bbusybox\b.*(wget|telnet|nc)", "busybox networking"),
    # Suspicious locations
    (r"\s/tmp/|^/tmp/|/dev/shm/|/var/tmp/", "exec from tmp/shm"),
    # Crypto miners (very rough)
    (r"\bxmrig\b|\bminerd\b|\bcpuminer\b|\bethminer\b", "miner name match"),
]

IOC_COMPILED = [(re.compile(p, re.I), msg) for p,msg in IOC_RULES]

def scan_findings(cmd):
    finds=[]
    for rx,msg in IOC_COMPILED:
        if rx.search(cmd):
            finds.append(msg)
    return finds

# ---------- Core filters ----------
def filter_stream(path, since, until, users, cmd_regexes, contains, min_et, max_et, path_regexes):
    users = set(u.strip() for u in users) if users else None
    cregex = compile_regexes(cmd_regexes, re.I)
    pregex = compile_regexes(path_regexes, re.I)
    contains = contains or []
    for t,p in iter_jsonl(path):
        if not within_range(t, since, until): continue
        if users and p.get("user") not in users: continue
        cmd = p.get("cmd","")
        if not match_any_regex(cmd, cregex): continue
        if contains and not all(s.lower() in cmd.lower() for s in contains): continue
        if min_et is not None and (p.get("etimes") is None or p.get("etimes") < min_et): continue
        if max_et is not None and (p.get("etimes") is not None and p.get("etimes") > max_et): continue
        if pregex and not match_any_regex(cmd, pregex): continue
        yield t,p

# ---------- Commands ----------
def cmd_filter(args):
    rows=[]
    for t,p in filter_stream(
        args.file, args.since, args.until, args.user, args.cmd_regex,
        args.contains, args.min_etimes, args.max_etimes, args.path_regex
    ):
        if args.format == "json":
            print(json.dumps({"captured_at": t.strftime(ISO) if t else None, "proc": p}, ensure_ascii=False))
            continue
        if args.format == "csv":
            w = csv.writer(sys.stdout)
            # one-time header
            if not getattr(cmd_filter, "_csv_header", False):
                w.writerow(["captured_at","user","pid","ppid","stat","etimes","rss","vsz","cmd"])
                cmd_filter._csv_header=True
            w.writerow([
                t.strftime(ISO) if t else "",
                p.get("user",""), p.get("pid",""), p.get("ppid",""),
                p.get("stat",""), p.get("etimes",""),
                p.get("rss",""), p.get("vsz",""), p.get("cmd",""),
            ])
            continue
        # table row
        rows.append([
            t.strftime(ISO) if t else "",
            p.get("user",""),
            p.get("pid",""),
            p.get("ppid",""),
            p.get("stat",""),
            p.get("etimes",""),
            fmt_bytes(p.get("rss")),
            fmt_bytes(p.get("vsz")),
            p.get("cmd","")[:200],
        ])
    if rows and args.format == "table":
        print_table(rows, ["captured_at","user","pid","ppid","stat","etimes","rss","vsz","cmd"])

def cmd_stats(args):
    cnt_user = Counter()
    cnt_cmd  = Counter()
    first_seen = {}
    last_seen  = {}
    rss_by_cmd = defaultdict(int)
    vsz_by_cmd = defaultdict(int)
    for t,p in filter_stream(
        args.file, args.since, args.until, args.user, args.cmd_regex,
        args.contains, args.min_etimes, args.max_etimes, args.path_regex
    ):
        u = p.get("user","")
        c = basecmd(p.get("cmd",""))
        key = (u, c)
        cnt_user[u]+=1
        cnt_cmd[c]+=1
        if c:
            rss_by_cmd[c]+= int(p.get("rss") or 0)
            vsz_by_cmd[c]+= int(p.get("vsz") or 0)
        ts = t.strftime(ISO) if t else None
        if key not in first_seen: first_seen[key]=ts
        last_seen[key]=ts

    # Top tables
    if args.top_users:
        rows = [(u,n) for u,n in cnt_user.most_common(args.top_users)]
        print_table(rows, ["user","count"])
        print()
    if args.top_cmds:
        rows = [(c,n) for c,n in cnt_cmd.most_common(args.top_cmds)]
        print_table(rows, ["cmd","count"])
        print()
    if args.top_rss:
        rows = sorted(rss_by_cmd.items(), key=lambda x:x[1], reverse=True)[:args.top_rss]
        rows = [(c, fmt_bytes(v)) for c,v in rows]
        print_table(rows, ["cmd","rss_sum"])
        print()
    if args.top_vsz:
        rows = sorted(vsz_by_cmd.items(), key=lambda x:x[1], reverse=True)[:args.top_vsz]
        rows = [(c, fmt_bytes(v)) for c,v in rows]
        print_table(rows, ["cmd","vsz_sum"])
        print()
    if args.first_last:
        rows=[]
        for (u,c),fs in sorted(first_seen.items()):
            rows.append([u,c, fs or "", last_seen.get((u,c),"") or ""])
        print_table(rows, ["user","cmd","first_seen","last_seen"])

def cmd_scan(args):
    findings=[]
    for t,p in filter_stream(
        args.file, args.since, args.until, args.user, args.cmd_regex,
        args.contains, args.min_etimes, args.max_etimes, args.path_regex
    ):
        cmd = p.get("cmd","")
        hits = scan_findings(cmd)
        # Additional heuristic: long-lived processes under odd users
        if args.long_etimes and (p.get("etimes") or 0) >= args.long_etimes:
            # Flag long-lived things in /tmp etc.
            if re.search(r"/tmp/|/dev/shm/|/var/tmp/", cmd, re.I):
                hits.append(f"long-lived in tmp/shm (etimes>={args.long_etimes})")
        if not hits:
            continue
        rec = {
            "captured_at": t.strftime(ISO) if t else None,
            "user": p.get("user",""),
            "pid": p.get("pid"),
            "ppid": p.get("ppid"),
            "stat": p.get("stat"),
            "etimes": p.get("etimes"),
            "rss": p.get("rss"),
            "vsz": p.get("vsz"),
            "cmd": cmd,
            "reason": hits
        }
        findings.append(rec)

    if args.format == "json":
        for r in findings:
            print(json.dumps(r, ensure_ascii=False))
        return

    rows=[]
    for r in findings:
        rows.append([
            r["captured_at"] or "",
            r["user"], r["pid"], r["ppid"],
            r["stat"] or "", r["etimes"] or "",
            fmt_bytes(r["rss"]), fmt_bytes(r["vsz"]),
            "; ".join(r["reason"]),
            (r["cmd"] or "")[:180]
        ])
    if rows:
        print_table(rows, [
            "captured_at","user","pid","ppid","stat","etimes","rss","vsz","reason","cmd"
        ])
    else:
        print("No findings with current rules/filters.")

# ---------- CLI ----------
def add_common_filters(sp):
    sp.add_argument("-f","--file", default="/opt/psuniq/ps.jsonl", help="path to ps.jsonl")
    sp.add_argument("--since", type=parse_time, help='ISO time (e.g., "2025-09-17T16:00:00Z" or "2025-09-17 16:00")')
    sp.add_argument("--until", type=parse_time, help="ISO time upper bound")
    sp.add_argument("-u","--user", action="append", help="filter by user (add multiple)")
    sp.add_argument("-r","--cmd-regex", action="append", help="regex on cmd (add multiple)")
    sp.add_argument("-C","--contains", action="append", help="substring that must be in cmd (all must match)")
    sp.add_argument("--min-etimes", type=int, help="min elapsed seconds")
    sp.add_argument("--max-etimes", type=int, help="max elapsed seconds")
    sp.add_argument("-p","--path-regex", action="append", help="regex for paths (/tmp, /dev/shm, etc.)")

def main():
    ap = argparse.ArgumentParser(description="JSONL ps reader & threat hunter")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sp = sub.add_parser("filter", help="filter & print matching processes")
    add_common_filters(sp)
    sp.add_argument("--format", choices=["table","json","csv"], default="table")
    sp.set_defaults(func=cmd_filter)

    sp = sub.add_parser("stats", help="frequency & resource stats")
    add_common_filters(sp)
    sp.add_argument("--top-users", type=int, default=10, help="show top N users")
    sp.add_argument("--top-cmds", type=int, default=20, help="show top N base commands")
    sp.add_argument("--top-rss", type=int, default=15, help="sum RSS by base cmd (top N)")
    sp.add_argument("--top-vsz", type=int, default=15, help="sum VSZ by base cmd (top N)")
    sp.add_argument("--first-last", action="store_true", help="show first/last seen per (user, basecmd)")
    sp.set_defaults(func=cmd_stats)

    sp = sub.add_parser("scan", help="heuristic hunt for suspicious processes")
    add_common_filters(sp)
    sp.add_argument("--long-etimes", type=int, default=86400, help="flag long-lived tmp/shm procs (default: 1 day)")
    sp.add_argument("--format", choices=["table","json"], default="table")
    sp.set_defaults(func=cmd_scan)

    # args = ap.parse_args()
    args, unknown = ap.parse_known_args(); leftover = [u for u in unknown if u.startswith("-")] # ap.add_argument

    args.func(args)

if __name__ == "__main__":
    main()
