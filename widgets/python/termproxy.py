#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shlex
import json
import time
import uuid
import pty
import tty
import fcntl
import select
import hashlib
import difflib
import readline
import sqlite3
import subprocess
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import sys
import signal

# -----------------------------
# Configuration
# -----------------------------

DEFAULT_ROOT = os.path.expanduser("~/.termproxy")
LOG_DIR = os.path.join(DEFAULT_ROOT, "logs")
DB_PATH = os.path.join(DEFAULT_ROOT, "termproxy.sqlite3")
JSONL_PATH = os.path.join(LOG_DIR, "events.jsonl")

MAX_CAPTURE_CHARS = 200_000
MAX_FILE_SNAPSHOT_BYTES = 1_000_000
MAX_DIFF_LINES = 400

EDITOR_CMDS = {"vi", "vim", "nano", "nvim", "emacs", "code", "sed", "perl"}
VIEWER_CMDS = {"cat", "less", "more", "head", "tail", "bat"}
CONFIG_PATH_HINTS = ("/etc/", "/usr/local/etc/", "/opt/", "/var/lib/", "/var/log/")

# Unique marker that bash prints before each prompt with status + cwd.
TP_MARK = "__TP_MARK__"


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def ensure_dirs() -> None:
    os.makedirs(DEFAULT_ROOT, exist_ok=True)
    os.makedirs(LOG_DIR, exist_ok=True)


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", errors="ignore")).hexdigest()


def truncate(s: str, max_len: int) -> str:
    if len(s) <= max_len:
        return s
    return s[:max_len] + f"\n…(truncated, {len(s) - max_len} chars more)"


def safe_read_file(path: str, max_bytes: int) -> Tuple[bytes, bool]:
    try:
        with open(path, "rb") as f:
            data = f.read(max_bytes + 1)
        if len(data) > max_bytes:
            return data[:max_bytes], True
        return data, False
    except Exception:
        return b"", False


def looks_like_path(s: str) -> bool:
    if not s:
        return False
    if s.startswith(("/", "./", "../", "~")):
        return True
    return bool(re.search(r"\.(conf|cnf|ini|yaml|yml|json|toml|env|php|py|sh|service)$", s, re.IGNORECASE))


# -----------------------------
# Data
# -----------------------------

@dataclass
class CommandResolution:
    cmd: str
    kind: str                     # alias/function/builtin/binary/script/unknown
    resolved_path: Optional[str]
    package_owner: Optional[str]
    type_output: Optional[str]
    file_output: Optional[str]


@dataclass
class CommandEvent:
    id: str
    ts_start: str
    ts_end: str
    host: str
    user: str
    cwd: str
    raw_cmd: str
    argv: List[str]
    exit_code: int
    stdout_excerpt: str
    stderr_excerpt: str
    error_signature: str
    error_hash: str
    resolution: CommandResolution
    project_id: Optional[str]


@dataclass
class FileSnapshot:
    path: str
    before_hash: str
    before_text: str
    ts: str


@dataclass
class FileChangeEvent:
    id: str
    ts: str
    host: str
    user: str
    path: str
    before_hash: str
    after_hash: str
    diff_excerpt: str
    diff_hash: str
    change_summary: str
    linked_command_event_id: Optional[str]
    project_id: Optional[str]


@dataclass
class Project:
    id: str
    name: str
    ts_start: str
    ts_end: Optional[str]
    tags: List[str]
    notes: str


# -----------------------------
# Storage
# -----------------------------

class JsonlLogger:
    def __init__(self, jsonl_path: str) -> None:
        self.jsonl_path = jsonl_path

    def append(self, obj: Dict[str, Any]) -> None:
        with open(self.jsonl_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(obj, ensure_ascii=False) + "\n")


class SQLiteStore:
    def __init__(self, db_path: str) -> None:
        self.db_path = db_path
        self._init()

    def _conn(self) -> sqlite3.Connection:
        c = sqlite3.connect(self.db_path)
        c.execute("PRAGMA journal_mode=WAL;")
        c.execute("PRAGMA synchronous=NORMAL;")
        return c

    def _init(self) -> None:
        c = self._conn()
        cur = c.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            ts_start TEXT NOT NULL,
            ts_end TEXT,
            tags_json TEXT NOT NULL,
            notes TEXT NOT NULL
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS command_events (
            id TEXT PRIMARY KEY,
            ts_start TEXT NOT NULL,
            ts_end TEXT NOT NULL,
            host TEXT NOT NULL,
            user TEXT NOT NULL,
            cwd TEXT NOT NULL,
            raw_cmd TEXT NOT NULL,
            argv_json TEXT NOT NULL,
            exit_code INTEGER NOT NULL,
            stdout_excerpt TEXT NOT NULL,
            stderr_excerpt TEXT NOT NULL,
            error_signature TEXT NOT NULL,
            error_hash TEXT NOT NULL,
            resolution_json TEXT NOT NULL,
            project_id TEXT
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS file_changes (
            id TEXT PRIMARY KEY,
            ts TEXT NOT NULL,
            host TEXT NOT NULL,
            user TEXT NOT NULL,
            path TEXT NOT NULL,
            before_hash TEXT NOT NULL,
            after_hash TEXT NOT NULL,
            diff_excerpt TEXT NOT NULL,
            diff_hash TEXT NOT NULL,
            change_summary TEXT NOT NULL,
            linked_command_event_id TEXT,
            project_id TEXT
        );
        """)
        cur.execute("CREATE INDEX IF NOT EXISTS idx_cmd_error_hash ON command_events(error_hash);")
        c.commit()
        c.close()

    def upsert_project(self, p: Project) -> None:
        c = self._conn()
        c.execute("""
        INSERT INTO projects (id, name, ts_start, ts_end, tags_json, notes)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(id) DO UPDATE SET
          name=excluded.name, ts_start=excluded.ts_start, ts_end=excluded.ts_end,
          tags_json=excluded.tags_json, notes=excluded.notes;
        """, (p.id, p.name, p.ts_start, p.ts_end, json.dumps(p.tags), p.notes))
        c.commit()
        c.close()

    def list_open_project(self) -> Optional[Project]:
        c = self._conn()
        cur = c.cursor()
        cur.execute("""
        SELECT id, name, ts_start, ts_end, tags_json, notes
        FROM projects
        WHERE ts_end IS NULL
        ORDER BY ts_start DESC
        LIMIT 1;
        """)
        row = cur.fetchone()
        c.close()
        if not row:
            return None
        return Project(id=row[0], name=row[1], ts_start=row[2], ts_end=row[3], tags=json.loads(row[4]), notes=row[5])

    def insert_command_event(self, e: CommandEvent) -> None:
        c = self._conn()
        c.execute("""
        INSERT INTO command_events (
          id, ts_start, ts_end, host, user, cwd, raw_cmd, argv_json,
          exit_code, stdout_excerpt, stderr_excerpt, error_signature, error_hash, resolution_json, project_id
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (
            e.id, e.ts_start, e.ts_end, e.host, e.user, e.cwd, e.raw_cmd,
            json.dumps(e.argv), e.exit_code, e.stdout_excerpt, e.stderr_excerpt,
            e.error_signature, e.error_hash, json.dumps(asdict(e.resolution)), e.project_id
        ))
        c.commit()
        c.close()


# -----------------------------
# Resolver (runs INSIDE interactive bash so aliases/functions show up)
# -----------------------------

class CommandResolver:
    def __init__(self, bash: "BashSession") -> None:
        self.bash = bash

    def resolve(self, argv: List[str]) -> CommandResolution:
        if not argv:
            return CommandResolution(cmd="", kind="unknown", resolved_path=None, package_owner=None, type_output=None, file_output=None)

        cmd = argv[0]
        type_out = self.bash.run_capture(f"type -a {shlex.quote(cmd)}").strip()
        kind = "unknown"
        resolved_path = None

        if "aliased to" in type_out:
            kind = "alias"
        elif "function" in type_out:
            kind = "function"
        elif "shell builtin" in type_out:
            kind = "builtin"
        else:
            m = re.search(r"\s(/[^ \n\t]+)", type_out)
            if m:
                resolved_path = m.group(1).strip()
                kind = "binary"

        # argv[0] is a path
        if cmd.startswith("/") or cmd.startswith("./") or cmd.startswith("../"):
            resolved_path = os.path.abspath(cmd)
            kind = "script"

        file_out = ""
        if resolved_path:
            file_out = self.bash.run_capture(f"file -b {shlex.quote(resolved_path)}").strip()

        pkg = None
        if resolved_path:
            if self.bash.has_cmd("rpm"):
                o = self.bash.run_capture(f"rpm -qf {shlex.quote(resolved_path)}").strip()
                if o and "is not owned" not in o:
                    pkg = o
            elif self.bash.has_cmd("dpkg"):
                o = self.bash.run_capture(f"dpkg -S {shlex.quote(resolved_path)}").strip()
                if o and "no path found" not in o.lower():
                    pkg = o

        return CommandResolution(
            cmd=cmd,
            kind=kind,
            resolved_path=resolved_path,
            package_owner=pkg,
            type_output=type_out or None,
            file_output=file_out or None
        )


# -----------------------------
# File monitor
# -----------------------------

class FileMonitor:
    def __init__(self) -> None:
        self._snap: Dict[str, FileSnapshot] = {}

    def should_track(self, path: str) -> bool:
        ap = os.path.abspath(path)
        if any(ap.startswith(h) for h in CONFIG_PATH_HINTS):
            return True
        return bool(re.search(r"\.(conf|cnf|ini|yaml|yml|json|toml|env)$", ap, re.IGNORECASE))

    def snapshot_if_small(self, path: str) -> Optional[FileSnapshot]:
        ap = os.path.abspath(path)
        try:
            st = os.stat(ap)
        except Exception:
            return None
        if st.st_size > MAX_FILE_SNAPSHOT_BYTES:
            return None
        b, _ = safe_read_file(ap, MAX_FILE_SNAPSHOT_BYTES)
        txt = b.decode("utf-8", errors="replace")
        snap = FileSnapshot(path=ap, before_hash=sha256_text(txt), before_text=txt, ts=now_iso())
        self._snap[ap] = snap
        return snap

    def diff_if_changed(self, path: str) -> Optional[Tuple[str, str, str]]:
        ap = os.path.abspath(path)
        snap = self._snap.get(ap)
        if not snap:
            return None
        b, _ = safe_read_file(ap, MAX_FILE_SNAPSHOT_BYTES)
        after_txt = b.decode("utf-8", errors="replace")
        after_hash = sha256_text(after_txt)
        if after_hash == snap.before_hash:
            return None
        diff = list(difflib.unified_diff(
            snap.before_text.splitlines(),
            after_txt.splitlines(),
            fromfile=f"{ap} (before)",
            tofile=f"{ap} (after)",
            lineterm=""
        ))
        excerpt = "\n".join(diff[:MAX_DIFF_LINES])
        return snap.before_hash, after_hash, excerpt

    def clear(self, path: str) -> None:
        ap = os.path.abspath(path)
        self._snap.pop(ap, None)


def normalize_error(s: str) -> str:
    s = (s or "").strip()
    s = re.sub(r"\b\d{4}-\d{2}-\d{2}[T ][0-9:.\-+Z]+\b", "<TS>", s)
    s = re.sub(r"\b0x[0-9a-fA-F]+\b", "0x<HEX>", s)
    s = re.sub(r"/[A-Za-z0-9._\-/]+", "<PATH>", s)
    s = "\n".join(s.splitlines()[:30])
    return s.strip()


# -----------------------------
# Bash PTY session
# -----------------------------

class BashSession:
    """
    Starts a persistent interactive bash in a PTY.
    We inject PROMPT_COMMAND to print a machine-parsable marker before each prompt:
      __TP_MARK__|<exit>|<cwd>
    """
    def __init__(self) -> None:
        self.master_fd: Optional[int] = None
        self.pid: Optional[int] = None
        self.last_exit = 0
        self.last_cwd = os.getcwd()

        self._start()

    def _start(self) -> None:
        pid, master_fd = pty.fork()
        if pid == 0:
            # Child
            os.environ["TERM"] = os.environ.get("TERM", "xterm-256color")
            # Interactive bash to load ~/.bashrc aliases/functions
            os.execvp("bash", ["bash", "-i"])
            raise SystemExit(1)

        # Parent
        self.pid = pid
        self.master_fd = master_fd

        # non-blocking reads
        flags = fcntl.fcntl(master_fd, fcntl.F_GETFL)
        fcntl.fcntl(master_fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)

        # Wait for initial prompt, then install our prompt marker
        self._drain_until_marker(timeout=3.0, allow_no_marker=True)
        self._install_marker()

        # Drain until we see our marker at least once
        self._drain_until_marker(timeout=3.0, allow_no_marker=False)

    def _install_marker(self) -> None:
        # PROMPT_COMMAND runs before each prompt; PS1 can be simple.
        # We print marker to STDERR so it doesn’t mix with command stdout (still captured, but separable).
        cmd = (
            f"export PROMPT_COMMAND='__ec=$?; "
            f"printf \"{TP_MARK}|%s|%s\\n\" \"$__ec\" \"$PWD\" 1>&2'; "
            f"export PS1=\"\""
        )
        self.sendline(cmd)

    def sendline(self, s: str) -> None:
        if self.master_fd is None:
            return
        os.write(self.master_fd, (s + "\n").encode("utf-8", errors="ignore"))

    def _read_available(self) -> str:
        if self.master_fd is None:
            return ""
        out = b""
        while True:
            try:
                chunk = os.read(self.master_fd, 8192)
                if not chunk:
                    break
                out += chunk
            except BlockingIOError:
                break
            except OSError:
                break
        return out.decode("utf-8", errors="replace")

    def _drain_until_marker(self, timeout: float, allow_no_marker: bool) -> Tuple[str, str]:
        """
        Returns (stdout_like, stderr_like) as merged text; we separate by marker parsing.
        In a PTY, streams are merged; we treat marker lines specially.
        """
        start = time.time()
        buf = ""
        stdout = ""
        stderr = ""

        marker_re = re.compile(rf"{re.escape(TP_MARK)}\|(\d+)\|(.*)")

        while time.time() - start < timeout:
            r, _, _ = select.select([self.master_fd], [], [], 0.05) if self.master_fd is not None else ([], [], [])
            if r:
                buf += self._read_available()

                # Process complete lines
                while "\n" in buf:
                    line, buf = buf.split("\n", 1)
                    m = marker_re.search(line)
                    if m:
                        self.last_exit = int(m.group(1))
                        self.last_cwd = m.group(2).strip() or self.last_cwd
                        return stdout, stderr
                    # We don’t have true stdout/stderr separation in PTY.
                    # Heuristic: bash prompts / warnings often hit stderr; but we just collect all as stdout-like.
                    stdout += line + "\n"

        if allow_no_marker:
            return stdout + buf, ""
        # If we *require* marker, return what we have; caller can decide.
        return stdout + buf, ""

    def run_capture(self, cmd: str, timeout: float = 2.0) -> str:
        """
        Run a command and capture its output by waiting for the next marker.
        """
        # Clear any pending output first
        self._read_available()
        self.sendline(cmd)
        out, _ = self._drain_until_marker(timeout=timeout, allow_no_marker=False)
        return out


    def run_user_command(self, cmd: str) -> Tuple[int, str]:
        """
        Run a user command; STREAM output to the screen while capturing it.
        Stops when we see the next __TP_MARK__ line.
        Ctrl+C sends SIGINT to the bash session (interrupts the running command).
        """
        if self.master_fd is None:
            return 127, ""

        # clear any pending bytes
        self._read_available()

        marker_re = re.compile(rf"{re.escape(TP_MARK)}\|(\d+)\|(.*)")

        # send the command
        self.sendline(cmd)

        captured = []
        buf = ""

        try:
            while True:
                r, _, _ = select.select([self.master_fd], [], [], 0.1)
                if not r:
                    continue

                chunk = self._read_available()
                if not chunk:
                    continue

                buf += chunk

                # process full lines so we can detect marker lines cleanly
                while "\n" in buf:
                    line, buf = buf.split("\n", 1)

                    m = marker_re.search(line)
                    if m:
                        # update session state, do NOT print marker
                        self.last_exit = int(m.group(1))
                        self.last_cwd = (m.group(2).strip() or self.last_cwd)
                        return self.last_exit, "".join(captured)

                    # normal output line: print + capture
                    sys.stdout.write(line + "\n")
                    sys.stdout.flush()
                    captured.append(line + "\n")

        except KeyboardInterrupt:
            # Send Ctrl+C to the PTY (interrupt current command)
            try:
                os.write(self.master_fd, b"\x03")
            except Exception:
                pass
            sys.stdout.write("^C\n")
            sys.stdout.flush()

            # Drain until we reach the next marker (prompt returns)
            # We still stream any final output during cleanup.
            while True:
                r, _, _ = select.select([self.master_fd], [], [], 0.1)
                if r:
                    chunk = self._read_available()
                    if chunk:
                        buf += chunk
                        while "\n" in buf:
                            line, buf = buf.split("\n", 1)
                            m = marker_re.search(line)
                            if m:
                                self.last_exit = int(m.group(1))
                                self.last_cwd = (m.group(2).strip() or self.last_cwd)
                                return self.last_exit, "".join(captured)
                            sys.stdout.write(line + "\n")
                            sys.stdout.flush()
                            captured.append(line + "\n")


    def has_cmd(self, cmd: str) -> bool:
        o = self.run_capture(f"command -v {shlex.quote(cmd)} >/dev/null 2>&1; echo $?")
        return o.strip().endswith("0")


# -----------------------------
# TermProxy
# -----------------------------

class TermProxy:
    def __init__(self) -> None:
        ensure_dirs()
        self.host = os.uname().nodename
        self.user = os.environ.get("USER", "unknown")

        self.logger = JsonlLogger(JSONL_PATH)
        self.db = SQLiteStore(DB_PATH)
        self.files = FileMonitor()

        self.bash = BashSession()
        self.resolver = CommandResolver(self.bash)

        self.active_project = self.db.list_open_project()
        self._init_readline()

    def _init_readline(self) -> None:
        readline.parse_and_bind("tab: complete")
        hist_path = os.path.join(DEFAULT_ROOT, "history.txt")
        try:
            readline.read_history_file(hist_path)
        except Exception:
            pass
        self._hist_path = hist_path

    def _save_history(self) -> None:
        try:
            readline.write_history_file(self._hist_path)
        except Exception:
            pass

    def prompt(self) -> str:
        p = f"[{self.active_project.name}]" if self.active_project else ""
        cwd = self.bash.last_cwd
        return f"{p}{self.user}@{self.host}:{cwd}$ "

    def run(self) -> None:
        print("termproxy (PTY) running. Type ?help for helper commands. Ctrl+C to exit.")
        try:
            while True:
                try:
                    line = input(self.prompt()).rstrip()
                except EOFError:
                    print()
                    break

                if not line.strip():
                    continue

                if line.startswith("?"):
                    self.handle_helper(line[1:].strip())
                    continue

                self.execute_command(line)
        except KeyboardInterrupt:
            print("\nExiting.")
        finally:
            self._save_history()

    # ---------- helper ----------
    def handle_helper(self, q: str) -> None:
        if not q or q in {"h", "help"}:
            print("""
Helper commands:
  ?help
  ?status
  ?project new "NAME" [tags=a,b,c] [notes=...]
  ?project close [notes=...]
""".strip())
            return

        if q == "status":
            print(f"cwd={self.bash.last_cwd} exit={self.bash.last_exit}")
            if self.active_project:
                print(f"active project: {self.active_project.name} ({self.active_project.id})")
            else:
                print("active project: none")
            return

        if q.startswith("project "):
            self.handle_project(q[len("project "):].strip())
            return

        print("Unknown helper. Try ?help")

    def handle_project(self, rest: str) -> None:
        def extract_quoted(s: str) -> Optional[str]:
            m = re.search(r"\"([^\"]+)\"", s)
            return m.group(1) if m else None

        def extract_kv(s: str, key: str) -> Optional[str]:
            m = re.search(rf"\b{re.escape(key)}=(\"[^\"]*\"|\S+)", s)
            if not m:
                return None
            v = m.group(1)
            if v.startswith("\"") and v.endswith("\""):
                v = v[1:-1]
            return v

        if rest.startswith("new"):
            name = extract_quoted(rest) or f"project-{datetime.now(timezone.utc).strftime('%Y%m%d-%H%M%S')}"
            tags = extract_kv(rest, "tags") or ""
            notes = extract_kv(rest, "notes") or ""
            p = Project(
                id=str(uuid.uuid4()),
                name=name,
                ts_start=now_iso(),
                ts_end=None,
                tags=[t.strip() for t in tags.split(",") if t.strip()],
                notes=notes
            )
            self.db.upsert_project(p)
            self.active_project = p
            print(f"Project started: {p.name}")
            return

        if rest.startswith("close"):
            if not self.active_project:
                print("No active project.")
                return
            notes = extract_kv(rest, "notes") or self.active_project.notes
            self.active_project.ts_end = now_iso()
            self.active_project.notes = notes
            self.db.upsert_project(self.active_project)
            print(f"Project closed: {self.active_project.name}")
            self.active_project = None
            return

        print("Unknown project command.")

    # ---------- core ----------
    def execute_command(self, line: str) -> None:
        ts_start = now_iso()
        cwd_before = self.bash.last_cwd

        argv = self.safe_split(line)
        res = self.resolver.resolve(argv)

        tracked = self.detect_files(argv)
        snaps: List[FileSnapshot] = []
        for p in tracked:
            if self.files.should_track(p):
                s = self.files.snapshot_if_small(p)
                if s:
                    snaps.append(s)

        exit_code, output = self.bash.run_user_command(line)

        # In PTY we can’t reliably split stdout/stderr. We treat all as stdout_excerpt.
        out_excerpt = truncate(output, MAX_CAPTURE_CHARS)
        err_excerpt = ""  # best-effort blank
        err_sig = normalize_error(output) if exit_code != 0 else ""
        err_hash = sha256_text(err_sig) if err_sig else ""

        ts_end = now_iso()
        event = CommandEvent(
            id=str(uuid.uuid4()),
            ts_start=ts_start,
            ts_end=ts_end,
            host=self.host,
            user=self.user,
            cwd=cwd_before,
            raw_cmd=line,
            argv=argv,
            exit_code=exit_code,
            stdout_excerpt=out_excerpt,
            stderr_excerpt=err_excerpt,
            error_signature=err_sig,
            error_hash=err_hash,
            resolution=res,
            project_id=self.active_project.id if self.active_project else None
        )

        self.logger.append({"type": "command_event", **asdict(event)})
        self.db.insert_command_event(event)

        # After command, see if tracked files changed
        for s in snaps:
            ch = self.files.diff_if_changed(s.path)
            if ch:
                before_hash, after_hash, diff_excerpt = ch
                diff_hash = sha256_text(diff_excerpt)
                summary = self.summarize_diff_rules(s.path, diff_excerpt)
                fc = FileChangeEvent(
                    id=str(uuid.uuid4()),
                    ts=now_iso(),
                    host=self.host,
                    user=self.user,
                    path=s.path,
                    before_hash=before_hash,
                    after_hash=after_hash,
                    diff_excerpt=diff_excerpt,
                    diff_hash=diff_hash,
                    change_summary=summary,
                    linked_command_event_id=event.id,
                    project_id=event.project_id
                )
                self.logger.append({"type": "file_change", **asdict(fc)})
            self.files.clear(s.path)

    def safe_split(self, line: str) -> List[str]:
        try:
            return shlex.split(line)
        except Exception:
            return line.strip().split()

    def detect_files(self, argv: List[str]) -> List[str]:
        if not argv:
            return []
        cmd = os.path.basename(argv[0])
        paths: List[str] = []

        if cmd in EDITOR_CMDS or cmd in VIEWER_CMDS:
            for a in argv[1:]:
                if a.startswith("-"):
                    continue
                if looks_like_path(a):
                    paths.append(os.path.abspath(os.path.expanduser(a)))
                    break

        if cmd in {"sed", "perl"}:
            for a in reversed(argv):
                if a.startswith("-"):
                    continue
                if looks_like_path(a):
                    paths.append(os.path.abspath(os.path.expanduser(a)))
                    break

        # de-dup
        seen = set()
        out = []
        for p in paths:
            if p not in seen:
                seen.add(p)
                out.append(p)
        return out[:5]

    def summarize_diff_rules(self, path: str, diff_excerpt: str) -> str:
        p = path.lower()
        d = diff_excerpt.lower()
        hints: List[str] = []

        if "mongod" in p or "mongodb" in d or "replication" in d or "storage:" in d:
            if "bindip" in d:
                hints.append("MongoDB bindIp changed — check exposure/firewall.")
            if "authorization" in d:
                hints.append("MongoDB auth changed — verify users/roles and startup succeeds.")
            if "replset" in d or "replsetname" in d:
                hints.append("MongoDB replSet changed — verify replica set config.")
            if "dbpath" in d:
                hints.append("MongoDB dbPath changed — verify directory permissions.")

        if "sshd_config" in p or "sshd" in d:
            if "permitrootlogin" in d:
                hints.append("SSH root login policy changed.")
            if "passwordauthentication" in d:
                hints.append("SSH password auth changed.")
            if "allowusers" in d:
                hints.append("SSH AllowUsers changed.")

        if not hints:
            hints.append("Config changed — review diff and validate service restart.")
        return " ".join(hints)


# -----------------------------
# Entry
# -----------------------------

def main() -> None:
    ensure_dirs()
    tp = TermProxy()
    tp.run()


if __name__ == "__main__":
    main()
