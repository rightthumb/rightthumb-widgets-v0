# LogsEngine.py
# Advanced Security & Reporting Log Framework
# Python 3.10+
# -------------------------------------------------------------
# Features
# - Base classes: LogSource, LogParser, Normalizer, Detector
# - EventBus: publish/subscribe normalized events
# - Normalized event schema (stable keys)
# - Child parsers for: syslog, auth/secure, dmesg, Apache access/error,
#   Exim mail log, sshd, Windows Event CSV, ProcMon CSV
# - Detectors: BruteForceDetector, SimpleCorrelator
# - Action hooks: CSFAction, Fail2BanAction, SIEMSink
# -------------------------------------------------------------

from __future__ import annotations
import re
import csv
import time
import json
import socket
import pathlib
import datetime as dt
from collections import defaultdict, deque
from typing import Iterable, Iterator, Optional, Dict, Any, Callable, List, Deque, Tuple

# -------------------------
# Event Schema (normalized)
# -------------------------
# Each event is a dict with these keys (when available):
# ts            : datetime (UTC)
# src_host      : str (hostname that produced the log)
# dst_host      : str (our collector hostname, optional)
# app           : str (facility/program)
# pid           : int|None
# level         : str ('DEBUG','INFO','NOTICE','WARN','ERROR','CRITICAL','ALERT','EMERG')
# msg           : str (human message)
# source_type   : str (e.g., 'syslog','auth','apache_access','apache_error','exim','dmesg','windows_event','procmon')
# raw           : str (original line or raw record)
# meta          : dict (structured extras; e.g., ip, user, http, ssh fields, event_id, hashes, etc.)

UTC = dt.timezone.utc

def to_utc(ts: dt.datetime | None) -> Optional[dt.datetime]:
    if ts is None:
        return None
    if ts.tzinfo is None:
        return ts.replace(tzinfo=UTC)
    return ts.astimezone(UTC)

def now_utc() -> dt.datetime:
    return dt.datetime.now(tz=UTC)

# -------------------------
# Event Bus
# -------------------------

class EventBus:
    def __init__(self):
        self._subs: List[Callable[[Dict[str, Any]], None]] = []

    def subscribe(self, handler: Callable[[Dict[str, Any]], None]) -> None:
        self._subs.append(handler)

    def publish(self, event: Dict[str, Any]) -> None:
        for h in self._subs:
            h(event)

# -------------------------
# Base Classes
# -------------------------

class LogSource:
    """Parent class for log sources (files, streams)."""

    def __init__(self, path: str | pathlib.Path):
        self.path = pathlib.Path(path)

    def read_lines(self, follow: bool = False) -> Iterator[str]:
        """Read lines from a file. If follow=True, tail -f behavior."""
        with self.path.open('r', errors='replace', encoding='utf-8') as f:
            while True:
                line = f.readline()
                if line:
                    yield line.rstrip('\n')
                elif follow:
                    time.sleep(0.2)
                else:
                    break

class LogParser:
    """Parent parser. Child classes must implement parse_line()."""

    source_type: str = "generic"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        raise NotImplementedError

    def normalize(self, **kwargs) -> Dict[str, Any]:
        event = {
            'ts': to_utc(kwargs.get('ts', now_utc())),
            'src_host': kwargs.get('src_host'),
            'dst_host': kwargs.get('dst_host'),
            'app': kwargs.get('app'),
            'pid': kwargs.get('pid'),
            'level': kwargs.get('level'),
            'msg': kwargs.get('msg', ''),
            'source_type': self.source_type,
            'raw': kwargs.get('raw'),
            'meta': kwargs.get('meta', {}) or {},
        }
        return event

# -------------------------
# Common Regex Helpers
# -------------------------

MONTHS = {m: i for i, m in enumerate(
    ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], start=1)}

# RFC3164-ish: "Aug 28 13:14:15 host app[1234]: message"
SYSLOG_RE = re.compile(
    r'^(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+(?P<time>\d{2}:\d{2}:\d{2})\s+(?P<host>[\w\.-]+)\s+(?P<app>[\w/\.-]+)(?:\[(?P<pid>\d+)\])?:\s*(?P<msg>.*)$'
)

# Apache Combined Log Format (very common in WHM/cPanel):
# 1.2.3.4 - user [28/Aug/2025:13:14:15 +0000] "GET /path HTTP/1.1" 200 123 "-" "UA"
APACHE_ACCESS_RE = re.compile(
    r'^(?P<ip>\S+)\s+\S+\s+(?P<user>\S+)\s+\[(?P<ts>[^]]+)]\s+"(?P<method>\S+)\s+(?P<path>\S+)\s+(?P<proto>HTTP/\d\.\d)"\s+(?P<status>\d{3})\s+(?P<size>\S+)\s+"(?P<ref>[^"]*)"\s+"(?P<ua>[^"]*)"'
)

# Apache error: "[Wed Aug 28 13:14:15.123456 2025] [core:error] [pid 1234] [client 1.2.3.4:54321] message"
APACHE_ERROR_RE = re.compile(
    r'^\['
    r'(?P<dow>\w{3})\s+(?P<mon>\w{3})\s+(?P<day>\d{1,2})\s+'
    r'(?P<hms>\d{2}:\d{2}:\d{2}(?:\.\d+)?)\s+(?P<year>\d{4})'
    r'\]\s+\[(?P<mod>[^\]]+)\]'
    r'(?:\s+\[pid\s+\d+(?::tid\s+\d+)?\])?'              # optional pid and optional :tid
    r'(?:\s+\[client\s+(?P<ip>[0-9A-Fa-f:.]+)(?::\d+)?\])?'  # optional client with optional :port
    r'\s+(?P<msg>.*)$'
)

# auth/secure sshd common fragments
SSH_FAIL_RE = re.compile(r'Failed\s+password\s+for\s+(invalid user\s+)?(?P<user>\S+)\s+from\s+(?P<ip>[\d.:a-fA-F]+)')
SSH_ACCEPT_RE = re.compile(r'Accepted\s+(?P<meth>\S+)\s+for\s+(?P<user>\S+)\s+from\s+(?P<ip>[\d.:a-fA-F]+)')

# dmesg: "[12345.678901] message..."
DMESG_RE = re.compile(r'^\[(?P<secs>\d+(?:\.\d+)?)\]\s+(?P<msg>.*)$')

# Windows Event CSV typical headers often include "Date and Time","Source","Event ID","Task Category","Level","User","Computer","General"
# ProcMon CSV headers often include "Time of Day","Process Name","PID","Operation","Path","Result","Detail"

def parse_rfc3164_time(mon: str, day: str, hms: str, year: Optional[int] = None) -> dt.datetime:
    if year is None:
        year = dt.datetime.now().year
    return dt.datetime(year, MONTHS[mon], int(day), *map(int, hms.split(':')), tzinfo=UTC)

def parse_apache_time(ts: str) -> dt.datetime:
    # "28/Aug/2025:13:14:15 +0000"
    day, mon, rest = ts.split('/', 2)
    year_time, tz = rest.split(' ', 1)
    year, hms = year_time.split(':', 1)
    h, m, s = hms.split(':')
    return dt.datetime(int(year), MONTHS[mon], int(day), int(h), int(m), int(s), tzinfo=UTC)

# -------------------------
# Child Parsers
# -------------------------

class SyslogParser(LogParser):
    source_type = "syslog"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        m = SYSLOG_RE.match(line)
        if not m:
            return None
        d = m.groupdict()
        ts = parse_rfc3164_time(d['mon'], d['day'], d['time'])
        pid = int(d['pid']) if d.get('pid') else None
        return self.normalize(
            ts=ts, src_host=d['host'], app=d['app'], pid=pid,
            level=None, msg=d['msg'], raw=line, meta={}
        )

class AuthLogParser(SyslogParser):
    source_type = "auth"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        ev = super().parse_line(line)
        if not ev:
            return None
        # sshd signals
        fail = SSH_FAIL_RE.search(ev['msg'])
        acc = SSH_ACCEPT_RE.search(ev['msg'])
        if fail:
            ev['meta'].update({
                'event': 'ssh_failed_login',
                'user': fail.group('user'),
                'src_ip': fail.group('ip'),
            })
            ev['level'] = 'WARN'
        if acc:
            ev['meta'].update({
                'event': 'ssh_login',
                'method': acc.group('meth'),
                'user': acc.group('user'),
                'src_ip': acc.group('ip'),
            })
            ev['level'] = 'INFO'
        return ev

class SecureLogParser(AuthLogParser):
    source_type = "secure"

class DmesgParser(LogParser):
    source_type = "dmesg"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        m = DMESG_RE.match(line)
        if not m:
            return None
        boot_ts = now_utc() - dt.timedelta(seconds=float(m.group('secs')))
        return self.normalize(
            ts=boot_ts, src_host=socket.gethostname(), app='kernel',
            level=None, msg=m.group('msg'), raw=line, meta={}
        )

class ApacheAccessParser(LogParser):
    source_type = "apache_access"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        m = APACHE_ACCESS_RE.match(line)
        if not m:
            return None
        g = m.groupdict()
        ts = parse_apache_time(g['ts'])
        meta = {
            'ip': g['ip'],
            'user': None if g['user'] == '-' else g['user'],
            'method': g['method'],
            'path': g['path'],
            'status': int(g['status']),
            'size': None if g['size'] == '-' else int(g['size']),
            'ref': g['ref'],
            'ua': g['ua'],
            'proto': g['proto'],
        }
        return self.normalize(
            ts=ts, src_host=socket.gethostname(), app='httpd',
            level='INFO', msg=f"{g['method']} {g['path']} -> {g['status']}",
            raw=line, meta=meta
        )

class ApacheErrorParser(LogParser):
    source_type = "apache_error"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        m = APACHE_ERROR_RE.match(line)
        if not m:
            return None
        g = m.groupdict()
        # hms may contain fractional seconds; split on ':'
        h, mi, rest = g['hms'].split(':', 2)
        s = float(rest)
        sec = int(s)
        micro = int(round((s - sec) * 1_000_000))
        ts = dt.datetime(int(g['year']), MONTHS[g['mon']], int(g['day']), int(h), int(mi), sec, micro, tzinfo=UTC)
        level = 'ERROR' if 'error' in g['mod'] else 'WARN'
        meta = {'module': g['mod'], 'client_ip': g.get('ip')}
        return self.normalize(
            ts=ts, src_host=socket.gethostname(), app='httpd',
            level=level, msg=g['msg'], raw=line, meta=meta
        )

class EximMailLogParser(SyslogParser):
    source_type = "exim_mail"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        ev = super().parse_line(line)
        if not ev:
            return None
        # very rough exim hints
        if '<= ' in ev['msg'] or '=> ' in ev['msg']:
            ev['meta']['mail_flow'] = True
        return ev

class SSHDParser(AuthLogParser):
    source_type = "ssh"

class WindowsEventCSVParser(LogParser):
    source_type = "windows_event"

    def parse_line(self, line: str) -> Optional[Dict[str, Any]]:
        # Expect CSV header present when using csv module externally; here we parse one CSV row string on demand.
        # In practice, use parse_csv(reader) helper below.
        return None  # single-line parsing not used; see parse_csv()

    def parse_csv(self, rows: Iterable[Dict[str, str]]) -> Iterator[Dict[str, Any]]:
        for r in rows:
            # Try flexible keys
            ts = r.get('Date and Time') or r.get('TimeCreated') or r.get('Created')
            src = r.get('Source') or r.get('Provider Name')
            level = r.get('Level') or r.get('LevelDisplayName')
            event_id = r.get('Event ID') or r.get('EventID')
            comp = r.get('Computer') or r.get('MachineName')
            msg = r.get('General') or r.get('Message') or ''
            try:
                # Many exports are local time; treat as naive -> UTC (tweak if you know the TZ)
                ts_parsed = dt.datetime.fromisoformat(ts) if ts else now_utc()
            except Exception:
                ts_parsed = now_utc()
            yield self.normalize(
                ts=ts_parsed, src_host=comp, app=src, pid=None, level=level,
                msg=msg, raw=json.dumps(r), meta={'event_id': event_id}
            )

class ProcMonCSVParser(LogParser):
    source_type = "procmon"

    def parse_csv(self, rows: Iterable[Dict[str, str]]) -> Iterator[Dict[str, Any]]:
        for r in rows:
            ts = r.get('Time of Day') or r.get('Time')
            pname = r.get('Process Name')
            pid = r.get('PID')
            op = r.get('Operation')
            path = r.get('Path')
            result = r.get('Result')
            detail = r.get('Detail') or ''
            # ProcMon "Time of Day" often looks like "1:23:45.678901 PM" (local). We keep as-is NAIVE->UTC.
            try:
                ts_parsed = dt.datetime.strptime(ts, '%I:%M:%S.%f %p').replace(tzinfo=UTC)
            except Exception:
                ts_parsed = now_utc()
            yield self.normalize(
                ts=ts_parsed, src_host=socket.gethostname(), app=pname, pid=int(pid) if pid and pid.isdigit() else None,
                level='INFO', msg=f"{op} {path} -> {result}",
                raw=json.dumps(r),
                meta={'operation': op, 'path': path, 'result': result, 'detail': detail}
            )

# -------------------------
# Detectors & Actions
# -------------------------

class Detector:
    """Parent class for incident detectors subscribing to events."""
    def handle(self, event: Dict[str, Any]) -> None:
        raise NotImplementedError

class BruteForceDetector(Detector):
    """
    Detect SSH brute-force by counting failed logins per src_ip in a sliding window.
    Emits incidents via callback when threshold exceeded.
    """
    def __init__(self, window_seconds: int = 300, threshold: int = 6,
                 on_incident: Optional[Callable[[Dict[str, Any]], None]] = None):
        self.window = window_seconds
        self.threshold = threshold
        self.on_incident = on_incident or (lambda inc: None)
        self.failures: Dict[str, Deque[dt.datetime]] = defaultdict(deque)

    def handle(self, event: Dict[str, Any]) -> None:
        if event['source_type'] not in ('auth', 'secure', 'ssh'):
            return
        if event['meta'].get('event') != 'ssh_failed_login':
            return
        ip = event['meta'].get('src_ip')
        if not ip:
            return
        ts = event['ts'] or now_utc()
        dq = self.failures[ip]
        dq.append(ts)
        # expire old
        cutoff = ts - dt.timedelta(seconds=self.window)
        while dq and dq[0] < cutoff:
            dq.popleft()
        if len(dq) >= self.threshold:
            incident = {
                'ts': now_utc(),
                'type': 'bruteforce',
                'src_ip': ip,
                'count': len(dq),
                'window_s': self.window,
                'sample_user': event['meta'].get('user'),
            }
            self.on_incident(incident)
            # Optional: clear or keep counting; we clear to avoid spamming
            dq.clear()

class SimpleCorrelator(Detector):
    """
    Very small correlator that connects apache_error + auth failures from same IP within N seconds.
    """
    def __init__(self, window_seconds: int = 120, on_correlation: Optional[Callable[[Dict[str, Any]], None]] = None):
        self.window = window_seconds
        self.on_correlation = on_correlation or (lambda c: None)
        self.cache: Deque[Tuple[dt.datetime, Dict[str, Any]]] = deque()

    def handle(self, event: Dict[str, Any]) -> None:
        ts = event.get('ts') or now_utc()
        self.cache.append((ts, event))
        cutoff = ts - dt.timedelta(seconds=self.window)
        while self.cache and self.cache[0][0] < cutoff:
            self.cache.popleft()
        ip = (event.get('meta') or {}).get('src_ip') or (event.get('meta') or {}).get('client_ip') or (event.get('meta') or {}).get('ip')
        if not ip:
            return
        # If we see both auth failure and apache error from same IP within window -> correlation
        kind = event['source_type']
        if kind in ('auth','secure','ssh') and event['meta'].get('event') == 'ssh_failed_login':
            other = any(
                (e['source_type'] == 'apache_error' and ((e.get('meta') or {}).get('client_ip') == ip))
                for _, e in self.cache
            )
            if other:
                self.on_correlation({
                    'ts': now_utc(),
                    'type': 'multi_surface_noise_or_attack',
                    'src_ip': ip,
                    'signals': ['ssh_failed_login','apache_error']
                })

# Action hooks (stubs): wire these to your environment

class CSFAction:
    def block_ip(self, ip: str, reason: str = "security_policy") -> None:
        # Example: subprocess.run(["csf","-d",ip,reason], check=False)
        print(f"[CSF] Block {ip} ({reason})")

class Fail2BanAction:
    def ban_ip(self, ip: str, jail: str = "sshd", seconds: Optional[int] = None) -> None:
        # Example: write to fail2ban log/socket; here we stub
        print(f"[Fail2Ban] Ban {ip} in jail={jail} for {seconds or 'default'}s")

class SIEMSink:
    def __init__(self, out_path: Optional[str] = None, http_endpoint: Optional[str] = None):
        self.out_path = pathlib.Path(out_path) if out_path else None
        self.http_endpoint = http_endpoint

    def send(self, payload: Dict[str, Any]) -> None:
        record = json.dumps(payload, default=str)
        if self.out_path:
            self.out_path.parent.mkdir(parents=True, exist_ok=True)
            with self.out_path.open('a', encoding='utf-8') as f:
                f.write(record + "\n")
        # For HTTP: requests.post(self.http_endpoint, json=payload, timeout=2)  # avoid external deps here
        print(f"[SIEM] {record}")

# -------------------------
# Orchestrator
# -------------------------

class Pipeline:
    """Glue: source -> parser -> bus -> detectors/sinks."""

    def __init__(self, bus: EventBus, siem: Optional[SIEMSink] = None):
        self.bus = bus
        self.siem = siem

    def ingest_file(self, path: str | pathlib.Path, parser: LogParser, follow: bool = False) -> None:
        src = LogSource(path)
        for line in src.read_lines(follow=follow):
            ev = parser.parse_line(line)
            if ev:
                if self.siem:
                    self.siem.send(ev)
                self.bus.publish(ev)

    def ingest_csv(self, path: str | pathlib.Path, parser_with_csv: LogParser) -> None:
        with open(path, 'r', encoding='utf-8', errors='replace', newline='') as f:
            reader = csv.DictReader(f)
            if hasattr(parser_with_csv, 'parse_csv'):
                for ev in parser_with_csv.parse_csv(reader):  # type: ignore[attr-defined]
                    if self.siem:
                        self.siem.send(ev)
                    self.bus.publish(ev)
            else:
                raise TypeError("Parser does not support CSV ingestion")

# -------------------------
# Example Wiring / Usage
# -------------------------

def example_usage() -> None:
    bus = EventBus()
    siem = SIEMSink(out_path="./out/events.jsonl")
    pipe = Pipeline(bus, siem)

    csf = CSFAction()
    f2b = Fail2BanAction()

    def on_bruteforce(inc: Dict[str, Any]) -> None:
        siem.send({'incident': inc})
        ip = inc['src_ip']
        # choose your action policy here:
        csf.block_ip(ip, reason=f"ssh bruteforce {inc['count']}/{inc['window_s']}s")
        # f2b.ban_ip(ip, jail="sshd", seconds=3600)

    def on_corr(c: Dict[str, Any]) -> None:
        siem.send({'correlation': c})

    bf = BruteForceDetector(window_seconds=300, threshold=6, on_incident=on_bruteforce)
    corr = SimpleCorrelator(window_seconds=120, on_correlation=on_corr)

    # Subscribe detectors
    bus.subscribe(bf.handle)
    bus.subscribe(corr.handle)

    # Ingest typical files (adjust paths for your system)
    # Linux:
    # pipe.ingest_file("/var/log/syslog", SyslogParser(), follow=True)
    # pipe.ingest_file("/var/log/auth.log", AuthLogParser(), follow=True)       # Debian/Ubuntu
    # pipe.ingest_file("/var/log/secure", SecureLogParser(), follow=True)       # RHEL/CentOS
    # pipe.ingest_file("/var/log/dmesg", DmesgParser(), follow=False)

    # WHM/cPanel (Apache/Exim):
    # pipe.ingest_file("/usr/local/apache/logs/access_log", ApacheAccessParser(), follow=True)
    # pipe.ingest_file("/usr/local/apache/logs/error_log", ApacheErrorParser(), follow=True)
    # pipe.ingest_file("/var/log/exim_mainlog", EximMailLogParser(), follow=True)

    # SSH (often in auth/secure; included above). If separate:
    # pipe.ingest_file("/var/log/sshd/sshd.log", SSHDParser(), follow=True)

    # Windows Event Viewer (export CSV first):
    # pipe.ingest_csv("C:/temp/security_events.csv", WindowsEventCSVParser())

    # Sysinternals ProcMon CSV:
    # pipe.ingest_csv("C:/temp/procmon.csv", ProcMonCSVParser())

if __name__ == "__main__":
    # Example: run demo wiring without starting ingestion by default.
    # Uncomment desired pipe.ingest_* lines in example_usage().
    example_usage()
