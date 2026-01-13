#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
established_connection_firewall.py

Hardened connection monitor + enforcer.

Key guarantees:
- Always enforce whitelist for ONLY_WHITELIST_PROC and ONLY_WHITELIST_PORTS.
- Robust process matching (proc name normalization; handles "sshd: user" etc).
- Log EVERY scan of established connections (append-only; never truncates).
- Immediate block+kill for violations; dedupes firewall rules to avoid spam.
- Works with netstat or ss; IPv4/IPv6; supports IP and CIDR in whitelist.
- Optional country filtering (--usa or --countries=US,CA) with ALLOWED_PROCS exempt.
- Unknown geo is never blocked (logged), as requested.
- Persistent country cache at /opt/established_firewall_logs/ip_country_cache.json
- Unblock helper (--unblock=IP) and list blocks (--list-blocks).
"""

import os
import re
import sys
import json
import time
import signal
import shutil
import socket
import ipaddress
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ===========================
# CONFIG (edit to taste)
# ===========================
CONFIG = {
    "LOGDIR": "/opt/established_firewall_logs",
    "WHITELIST_FILE": "/opt/whitelist_ip.txt",  # lines: IP or CIDR; '#' comments ok

    # Absolute whitelist enforcement (ALWAYS applied; no exceptions):
    "ONLY_WHITELIST_PROC": ["sshd", "bash", "cpdavd", "wget", "python", "curl"],     # substrings (normalized proc/cmd)
    "ONLY_WHITELIST_PORTS": ["2087", "2083"],              # local ports subject to whitelist-only

    # Processes EXEMPT from geo filtering (still logged & subject to whitelist-only if listed above)
    "ALLOWED_PROCS": ["nginx", "httpd", "exim", "pdns_server"],

    # Scan / Logging
    "SCAN_INTERVAL": 5,   # seconds
    "ESTABLISHED_LOG": "established.log",
    "BLOCKED_LOG": "blocked.log",
    "ACTIONS_LOG": "actions.log",

    # Cache of IP -> country code
    "CACHE_FILE": "ip_country_cache.json",
    "CACHE_TTL": 86400,  # 1 day

    # Command used to enumerate connections (fallbacks automatically)
    "ENUM_CMD": ["netstat", "-tupan"],  # or will fall back to: ss -tanp state established

    # Don’t try to block these networks (local/LAN/etc.)
    "NO_BLOCK_NETS": ["127.0.0.0/8", "::1/128", "10.0.0.0/8", "172.16.0.0/12",
                      "192.168.0.0/16", "169.254.0.0/16", "fe80::/10"],
}

# ===========================
# Globals
# ===========================
running = True
LOGDIR = Path(CONFIG["LOGDIR"])
ESTABLISHED_LOG = LOGDIR / CONFIG["ESTABLISHED_LOG"]
BLOCKED_LOG = LOGDIR / CONFIG["BLOCKED_LOG"]
ACTIONS_LOG = LOGDIR / CONFIG["ACTIONS_LOG"]
CACHE_PATH = LOGDIR / CONFIG["CACHE_FILE"]
NO_BLOCK_NETS = [ipaddress.ip_network(n) for n in CONFIG["NO_BLOCK_NETS"]]

_blocked_once = set()  # in-memory de-dupe for this run

def ts():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S%z")

def ensure_dirs():
    LOGDIR.mkdir(parents=True, exist_ok=True)
    # Never truncate; touch if missing
    for path in (ESTABLISHED_LOG, BLOCKED_LOG, ACTIONS_LOG):
        path.touch(exist_ok=True)
    if not CACHE_PATH.exists():
        CACHE_PATH.write_text("{}\n", encoding="utf-8")

def log_write(path: Path, line: str):
    with open(path, "a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")

def info(msg: str):
    s = f"[{ts()}] {msg}"
    print(s, flush=True)
    log_write(ACTIONS_LOG, s)

# ============== Whitelist (IP + CIDR) ==============
def load_whitelist():
    wl_ip = set()
    wl_cidr = []
    try:
        with open(CONFIG["WHITELIST_FILE"], "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    if "/" in line:
                        wl_cidr.append(ipaddress.ip_network(line, strict=False))
                    else:
                        wl_ip.add(ipaddress.ip_address(line))
                except Exception:
                    # ignore malformed entry
                    continue
    except FileNotFoundError:
        info(f"[WARN] whitelist file missing: {CONFIG['WHITELIST_FILE']}")
    return wl_ip, wl_cidr

def is_whitelisted(ip_str: str, wl_ip, wl_cidr) -> bool:
    try:
        ip = ipaddress.ip_address(ip_str)
    except Exception:
        return False
    if ip in wl_ip:
        return True
    for net in wl_cidr:
        if ip in net:
            return True
    return False

# ============== Args ==============
def parse_args(argv: list[str]):
    args = {
        "usa": False,
        "countries": None,   # list[str] like ["US","CA"]
        "all": False,
        "unblock": None,
        "list": False,
        "dry": False,
    }
    for a in argv:
        if a == "--usa":
            args["usa"] = True
        elif a.startswith("--countries="):
            lst = a.split("=", 1)[1].strip()
            if lst:
                args["countries"] = [x.strip().upper() for x in lst.split(",") if x.strip()]
        elif a == "--all":
            args["all"] = True
        elif a.startswith("--unblock="):
            args["unblock"] = a.split("=", 1)[1].strip()
        elif a == "--list-blocks":
            args["list"] = True
        elif a == "--dry-run":
            args["dry"] = True
    return args

# ============== Country cache & offline lookup ==============
def cache_load():
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8") or "{}")
    except Exception:
        return {}

def cache_save(cache: dict):
    tmp = CACHE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")
    tmp.replace(CACHE_PATH)

def cache_get(cache: dict, ip: str):
    ent = cache.get(ip)
    if not ent:
        return None
    try:
        t = datetime.fromisoformat(ent["ts"])
    except Exception:
        return None
    if datetime.now(timezone.utc) - t > timedelta(seconds=CONFIG["CACHE_TTL"]):
        return None
    return ent.get("cc")

def cache_put(cache: dict, ip: str, cc: str):
    cache[ip] = {"cc": cc, "ts": datetime.now(timezone.utc).isoformat()}

def get_country_offline(ip: str) -> str | None:
    # Try the user’s ip_geo module if available
    try:
        import ip_geo  # noqa
    except Exception:
        return None
    try:
        out = subprocess.check_output([sys.executable, "-c",
            "import ip_geo,sys,json;"
            "p=[ip_geo.DBIPLiteProvider(name='dbip',data_dir=ip_geo.DATA_ROOT),"
            "ip_geo.IPDenyCountryZonesProvider(name='ipdeny',data_dir=ip_geo.DATA_ROOT),"
            "ip_geo.IP2LocationLiteProvider(name='ip2location',data_dir=ip_geo.DATA_ROOT)];"
            "ip=sys.argv[1];"
            "vals=[];"
            "for x in p:\n"
            "  try:\n"
            "    try:x.load()\n"
            "    except FileNotFoundError:x.download();x.load()\n"
            "    vals.append(x.country(ip))\n"
            "  except Exception:\n"
            "    vals.append(None)\n"
            "print(json.dumps(vals))"
        , ip], stderr=subprocess.DEVNULL, timeout=20)
        vals = json.loads(out.decode().strip())
        votes = [v for v in vals if isinstance(v, str) and len(v) == 2]
        if not votes:
            return None
        # majority
        best = max(set(votes), key=votes.count)
        return best
    except Exception:
        return None

def get_country(ip: str, cache: dict) -> str | None:
    cc = cache_get(cache, ip)
    if cc:
        return cc
    cc = get_country_offline(ip)
    if cc:
        cache_put(cache, ip, cc)
        cache_save(cache)
    return cc  # None means unknown -> do not block by geo

# ============== Firewall Ops ==============
def have(cmd: str) -> bool:
    return shutil.which(cmd) is not None

def _is_localish(ip: str) -> bool:
    try:
        addr = ipaddress.ip_address(ip)
    except Exception:
        return False
    for net in NO_BLOCK_NETS:
        if addr in net:
            return True
    return False

def fw_block(ip: str, dry=False):
    if _is_localish(ip):
        info(f"SKIP block localish {ip}")
        return
    k = f"block:{ip}"
    if k in _blocked_once:
        return
    if dry:
        info(f"[DRY] block {ip}")
        _blocked_once.add(k)
        return
    if sys.platform.startswith("linux"):
        if have("firewall-cmd"):
            subprocess.call(["firewall-cmd","--permanent",f"--add-rich-rule=rule family=ipv4 source address={ip} reject"])
            subprocess.call(["firewall-cmd","--reload"])
        elif have("nft"):
            subprocess.call(["nft","add","table","inet","fw"], stderr=subprocess.DEVNULL)
            subprocess.call(["nft","add","chain","inet","fw","input","{","type","filter","hook","input","priority","0",";","policy","accept",";","}"], stderr=subprocess.DEVNULL)
            subprocess.call(["nft","add","rule","inet","fw","input","ip","saddr",ip,"drop"])
        elif have("iptables"):
            # add only if not exists
            exists = subprocess.call(["iptables","-C","INPUT","-s",ip,"-j","DROP"],
                                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if exists != 0:
                subprocess.call(["iptables","-A","INPUT","-s",ip,"-j","DROP"])
    elif sys.platform == "darwin" and have("pfctl"):
        table_file = "/etc/pf.blocklist"
        try:
            with open(table_file, "a", encoding="utf-8") as f:
                f.write(ip + "\n")
        except Exception:
            pass
        subprocess.call(["pfctl","-t","blocklist","-T","add",ip])
        subprocess.call(["pfctl","-f","/etc/pf.conf"])
    _blocked_once.add(k)

def fw_unblock(ip: str, dry=False):
    if dry:
        info(f"[DRY] unblock {ip}")
        return
    if sys.platform.startswith("linux"):
        if have("firewall-cmd"):
            subprocess.call(["firewall-cmd","--permanent",f"--remove-rich-rule=rule family=ipv4 source address={ip} reject"])
            subprocess.call(["firewall-cmd","--reload"])
        elif have("iptables"):
            while subprocess.call(["iptables","-D","INPUT","-s",ip,"-j","DROP"],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0:
                pass
        elif have("nft"):
            # best-effort – nft rule deletion requires handles; skipping here.
            pass
    elif sys.platform == "darwin" and have("pfctl"):
        subprocess.call(["pfctl","-t","blocklist","-T","delete",ip])
        subprocess.call(["pfctl","-f","/etc/pf.conf"])

def list_blocks():
    if sys.platform.startswith("linux"):
        if have("firewall-cmd"):
            try:
                out = subprocess.check_output(["firewall-cmd","--list-rich-rules"]).decode()
                print(out)
                return
            except Exception:
                pass
        if have("iptables"):
            try:
                out = subprocess.check_output(["iptables","-S"]).decode()
                for l in out.splitlines():
                    if " -s " in l and " -j DROP" in l:
                        print(l)
                return
            except Exception:
                pass
        if have("nft"):
            try:
                out = subprocess.check_output(["nft","list","ruleset"]).decode()
                for l in out.splitlines():
                    if "saddr" in l and " drop" in l:
                        print(l)
                return
            except Exception:
                pass
    elif sys.platform == "darwin" and have("pfctl"):
        subprocess.call(["pfctl","-t","blocklist","-T","show"])
    else:
        print("No supported firewall tool found.")

def kill_pid(pid: str):
    try:
        os.kill(int(pid), signal.SIGKILL)
    except Exception:
        pass

# ============== Enumeration & Parsing ==============
# Robust regex; handles IPv6 with colons by splitting from right
def parse_line_generic(ln: str):
    # Expected netstat columns include local addr, remote addr, state, and "pid/proc"
    parts = ln.split()
    if "ESTABLISHED" not in parts:
        return None
    # find "pid/proc" at end
    pidproc = parts[-1] if "/" in parts[-1] else None
    if not pidproc or "/" not in pidproc:
        return None
    # try to pull local/remote safely
    # netstat typically: ... laddr:lport raddr:rport ESTABLISHED pid/proc
    try:
        l = parts[3]; r = parts[4]
    except Exception:
        return None
    try:
        lhost, lport = l.rsplit(":", 1)
        rhost, rport = r.rsplit(":", 1)
    except ValueError:
        # IPv6 with weird formatting? try brackets
        return None
    try:
        pid, proc = pidproc.split("/", 1)
    except ValueError:
        return None
    return {"laddr": lhost, "lport": lport, "raddr": rhost, "rport": rport,
            "pid": pid, "proc": proc}

def enumerate_established():
    cmd = CONFIG["ENUM_CMD"]
    out_lines = []
    try:
        out_lines = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)\
                               .decode(errors="ignore").splitlines()
    except Exception:
        # fallback to ss
        try:
            out_lines = subprocess.check_output(["ss","-tanp","state","established"],
                                                stderr=subprocess.DEVNULL)\
                                  .decode(errors="ignore").splitlines()
        except Exception:
            return []
    results = []
    for ln in out_lines:
        if "ESTABLISHED" not in ln:
            continue
        rec = parse_line_generic(ln)
        if rec:
            results.append(rec)
    return results

# Normalize proc names (read /proc for ground truth)
def normalize_proc_name(pid: str, proc_field: str) -> str:
    # Try /proc/<pid>/comm
    try:
        comm = Path(f"/proc/{pid}/comm").read_text(encoding="utf-8").strip()
        if comm:
            return comm
    except Exception:
        pass
    # Try /proc/<pid>/cmdline
    try:
        cmdline = Path(f"/proc/{pid}/cmdline").read_text(encoding="utf-8").replace("\x00", " ").strip()
        if cmdline:
            # Take basename of argv[0]
            first = cmdline.split()[0]
            bn = os.path.basename(first)
            return bn or proc_field
    except Exception:
        pass
    # fallback to netstat/ss proc_field (e.g. "sshd:", "httpd", "imap-login", etc.)
    # Strip trailing ":" decorations like "sshd:" or "sshd: user"
    return proc_field.split(":")[0]

def proc_matches_any(proc_norm: str, substrings: list[str]) -> bool:
    p = proc_norm.lower()
    for sub in substrings:
        if sub.lower() in p:
            return True
    return False

# ============== Policy & Enforcement ==============
def should_geo_enforce(args, proc_norm: str) -> bool:
    # Never apply GEO to ALLOWED_PROCS
    if proc_norm in [x.lower() for x in CONFIG["ALLOWED_PROCS"]]:
        return False
    if not (args["usa"] or (args["countries"] and len(args["countries"]) > 0)):
        return False
    if args["all"]:
        return True
    # Without --all we still apply geo to non-exempt processes
    return True

def handle_connection(rec, wl_ip, wl_cidr, cache, args):
    """
    rec = {"laddr","lport","raddr","rport","pid","proc"}
    """
    laddr = rec["laddr"]; lport = str(rec["lport"])
    r_ip  = rec["raddr"]; rport = str(rec["rport"])
    pid   = rec["pid"];   proc_raw  = rec["proc"]

    


    log_write(sidecar(ESTABLISHED_LOG, '.pids'), str(snapshot_proc(pid)))
    # Always append a log line for visibility
    log_write(ESTABLISHED_LOG,
              f"[{ts()}] {laddr}:{lport} <- {r_ip}:{rport} pid={pid} proc={proc_raw}")

    # Normalize proc name for matching
    proc_norm = normalize_proc_name(pid, proc_raw)

    # First: absolute whitelist-only surfaces (process substrings or ports)
    if proc_matches_any(proc_norm, CONFIG["ONLY_WHITELIST_PROC"]) or (lport in CONFIG["ONLY_WHITELIST_PORTS"]):
        if not is_whitelisted(r_ip, wl_ip, wl_cidr):
            reason = (f"Whitelist-only violation: remote={r_ip} not in whitelist "
                      f"(proc={proc_norm} pid={pid} local={laddr}:{lport} remote={r_ip}:{rport})")
            log_write(sidecar(BLOCKED_LOG, '.pids'), str(snapshot_proc(pid)))
            log_write(BLOCKED_LOG, f"[{ts()}] {reason}")
            info(f"BLOCK {r_ip} :: {reason}")
            fw_block(r_ip, dry=args["dry"])
            if pid.isdigit():
                kill_pid(pid)
        return  # whitelist-only handled, stop here

    # GEO enforcement (optional; unknown == allow)
    if should_geo_enforce(args, proc_norm.lower()):
        # Whitelisted remote bypasses GEO
        if is_whitelisted(r_ip, wl_ip, wl_cidr):
            return
        allowed = None
        if args["usa"]:
            allowed = {"US"}
        elif args["countries"]:
            allowed = set([c.upper() for c in args["countries"]])
        # Determine country
        cc = get_country(r_ip, cache)
        if cc is None:
            # Unknown → allow but log
            log_write(sidecar(ACTIONS_LOG, '.pids'), str(snapshot_proc(pid)))
            log_write(ACTIONS_LOG,
                      f"[{ts()}] GEO unknown → ALLOW remote={r_ip} proc={proc_norm} pid={pid}")
            return
        if allowed and cc not in allowed:
            reason = (f"GEO block: {r_ip} cc={cc} not in {sorted(list(allowed))} "
                      f"(proc={proc_norm} pid={pid} local={laddr}:{lport} remote={r_ip}:{rport})")
            log_write(BLOCKED_LOG+'.pids', str(snapshot_proc(pid)) )
            log_write(BLOCKED_LOG, f"[{ts()}] {reason}")
            info(f"BLOCK {r_ip} :: {reason}")
            fw_block(r_ip, dry=args["dry"])
            if pid.isdigit():
                kill_pid(pid)
        # else allowed by geo


# Helper: make a sibling sidecar path like /dir/file.log.pids
def sidecar(p: Path, suffix: str) -> Path:
    return p.with_name(p.name + suffix)
def ensure_dirs():
    LOGDIR.mkdir(parents=True, exist_ok=True)
    for path in (ESTABLISHED_LOG, BLOCKED_LOG, ACTIONS_LOG):
        path.touch(exist_ok=True)
        sidecar(path, '.pids').touch(exist_ok=True)
    if not CACHE_PATH.exists():
        CACHE_PATH.write_text("{}\n", encoding="utf-8")


# ============== Main Loop ==============
def signal_handler(sig, frame):
    global running
    running = False
    print("\n[!] Ctrl+C received, exiting...", flush=True)


def snapshot_proc(pid: str) -> dict:
    base = f"/proc/{pid}"
    def r(path, bin=False):
        try:
            if path.endswith(("cmdline","environ")):
                data = Path(path).read_bytes()
                return data.replace(b"\x00", b" ").decode(errors="ignore") if not bin else data
            if path.endswith(("exe","cwd")):
                return os.path.realpath(path if not os.path.islink(path) else os.readlink(path))
            return Path(path).read_text(errors="ignore")
        except Exception:
            return ""
    info = {
        "pid": pid,
        "exe": os.path.realpath(os.readlink(f"{base}/exe")) if os.path.islink(f"{base}/exe") else "",
        "cwd": os.path.realpath(os.readlink(f"{base}/cwd")) if os.path.islink(f"{base}/cwd") else "",
        "cmdline": r(f"{base}/cmdline"),
        "ppid": re.findall(r'^PPid:\s*(\d+)', r(f"{base}/status"), re.M)[:1] or ["?"],
        "uid":  re.findall(r'^Uid:\s*(\d+)', r(f"{base}/status"), re.M)[:1] or ["?"],
    }
    # First few open files (paths help find the script)
    try:
        fds = os.listdir(f"{base}/fd")[:20]
        info["fds"] = {fd: os.path.realpath(os.readlink(f"{base}/fd/{fd}")) for fd in fds}
    except Exception:
        info["fds"] = {}
    return info


def main():
    ensure_dirs()
    args = parse_args(sys.argv[1:])

    if args["unblock"]:
        fw_unblock(args["unblock"], dry=args["dry"])
        return
    if args["list"]:
        list_blocks()
        return

    wl_ip, wl_cidr = load_whitelist()
    cache = cache_load()

    info("=== established_connection_firewall started ===")
    info(f"whitelist IPs={len(wl_ip)} CIDRs={len(wl_cidr)} | usa={args['usa']} countries={args['countries']} all={args['all']} dry={args['dry']}")
    info(f"ONLY_WHITELIST_PROC={CONFIG['ONLY_WHITELIST_PROC']}; ONLY_WHITELIST_PORTS={CONFIG['ONLY_WHITELIST_PORTS']}")
    info(f"GEO exempt ALLOWED_PROCS={CONFIG['ALLOWED_PROCS']}")
    info(f"country cache: {CACHE_PATH}")

    # Initial pass (enforce immediately, log everything)
    for rec in enumerate_established():
        try:
            handle_connection(rec, wl_ip, wl_cidr, cache, args)
        except Exception as e:
            info(f"[WARN] initial handle error: {e}")

    while running:
        try:
            time.sleep(CONFIG["SCAN_INTERVAL"])
            # Reload whitelist every loop (so you can add/remove in real-time)
            wl_ip, wl_cidr = load_whitelist()
            for rec in enumerate_established():
                handle_connection(rec, wl_ip, wl_cidr, cache, args)
        except KeyboardInterrupt:
            break
        except Exception as e:
            info(f"[WARN] loop error: {e}")

    info("=== exiting ===")

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
