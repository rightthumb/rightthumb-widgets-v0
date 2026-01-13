#!/usr/bin/env python3
"""
FirewallEngine.py — Production‑ready offline auto‑blacklist CLI

Key features
- Fully offline parsing (no external calls)
- Per‑log rule engines with tunable thresholds
- Pluggable firewall action backends (emit commands or record to JSONL/SQLite)
- CIDR + IP allowlists, duplicate‑action suppression
- Robust detection of log type (heuristics) with explicit override option
- Structured logging with --verbose/--quiet and optional JSON logs
- Safer DataFrame operations (no DataFrame.query on nested dicts)
- Graceful handling of large/empty/garbled logs

Python: 3.10+
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import gzip
import ipaddress
import json
import logging
import os
import pathlib
import re
import sqlite3
import subprocess
import sys
from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple, Union

import pandas as pd

# Your framework (parsers/normalizer)
from LogsEngine import (
	EventBus, SIEMSink, LogSource, LogParser,
	SyslogParser, AuthLogParser, SecureLogParser, DmesgParser,
	ApacheAccessParser, ApacheErrorParser, EximMailLogParser,
	WindowsEventCSVParser, ProcMonCSVParser, now_utc,
)

__version__ = "1.2.0"
UTC = dt.timezone.utc

# -------------------------------
# Logging
# -------------------------------

def setup_logging(verbose: bool, quiet: bool, json_logs: bool) -> None:
	lvl = logging.INFO
	if verbose and not quiet:
		lvl = logging.DEBUG
	if quiet:
		lvl = logging.WARNING

	if json_logs:
		class JsonFormatter(logging.Formatter):
			def format(self, record: logging.LogRecord) -> str:
				payload = {
					"ts": dt.datetime.now(tz=UTC).isoformat(),
					"level": record.levelname,
					"msg": record.getMessage(),
					"name": record.name,
				}
				return json.dumps(payload)
		handler = logging.StreamHandler()
		handler.setFormatter(JsonFormatter())
		logging.basicConfig(level=lvl, handlers=[handler])
	else:
		logging.basicConfig(
			level=lvl,
			format="%(asctime)s %(levelname)s %(message)s",
			datefmt="%Y-%m-%dT%H:%M:%S%z",
		)

log = logging.getLogger("auto_blacklist")

# -------------------------------
# Heuristics: auto-detect log type
# -------------------------------

FILE_HINTS = [
	(re.compile(r"access(_log)?$", re.I), "apache_access"),
	(re.compile(r"error(_log)?$", re.I), "apache_error"),
	(re.compile(r"auth\\.log$", re.I), "auth"),
	(re.compile(r"/secure$", re.I), "secure"),
	(re.compile(r"/sshd/|sshd\\.log$", re.I), "ssh"),
	(re.compile(r"dmesg", re.I), "dmesg"),
	(re.compile(r"exim", re.I), "exim_mail"),
	(re.compile(r"\\.csv$", re.I), "csv_unknown"),
	(re.compile(r"\\.gz$", re.I), "maybe_gz"),
]

LINE_TESTS = [
	# apache access
	(ApacheAccessParser, re.compile(r"^\S+ \S+ \S+ \[[^]]+] \"\S+ \S+ HTTP/\d\.\d\" \d{3} \S+ \".*\" \".*\"$")),
	# apache error
	(ApacheErrorParser, re.compile(r"^\[\w{3} \w{3} \d{1,2} [\d:.]+ \d{4}\] \[[^\]]+] \[pid \d+]")),
	# syslog/auth/secure
	(SyslogParser, re.compile(r"^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+[\w\.-]+\s+[\w/\.-]+(?:\[\d+\])?:")),
	# dmesg
	(DmesgParser, re.compile(r"^\[\d+(?:\.\d+)?\]\s+")),
]


def detect_log_type(path: pathlib.Path, sample_lines: List[str]) -> str:
	# 1) path hints
	pstr = str(path)
	for rx, kind in FILE_HINTS:
		if rx.search(pstr):
			if kind == "csv_unknown":
				break  # decide by CSV header next
			if kind == "maybe_gz" and path.suffix.lower() == ".gz":
				# We still detect the inner type later; default unknown for .gz here
				break
			return kind

	# 2) csv header check
	if path.suffix.lower() == ".csv":
		header = None
		try:
			with open_text_auto(path, head_only=True) as f:
				reader = csv.reader(f)
				header = next(reader, None)
		except Exception:
			header = None
		if header:
			hdr = [str(h).lower() for h in header]
			if any("event id" in h or "provider" in h or "level" in h for h in hdr):
				return "windows_event"
			if any("process name" in h or "operation" in h or "time of day" in h for h in hdr):
				return "procmon"
		return "csv"  # unknown csv -> user must override

	# 3) line regex tests
	for Parser, rx in LINE_TESTS:
		for ln in sample_lines[:50]:
			if rx.search(ln):
				# syslog-like could be auth/secure/ssh; prefer auth by default
				if Parser is SyslogParser:
					if any("sshd" in s for s in sample_lines[:50]):
						return "auth"
					return "syslog"
				if Parser is ApacheAccessParser:
					return "apache_access"
				if Parser is ApacheErrorParser:
					return "apache_error"
				if Parser is DmesgParser:
					return "dmesg"
	return "unknown"

# -------------------------------
# Firewall Actions (parent + kids)
# -------------------------------

class FirewallAction:
	"""Parent. Offline: generate command strings and/or record to a ledger."""
	name = "generic"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		raise NotImplementedError

	def allow_ip(self, ip: str, note: str = "") -> None:
		# Optional
		pass


class JSONAction(FirewallAction):
	name = "json"

	def __init__(self, out_path: pathlib.Path):
		self.out = out_path
		self.out.parent.mkdir(parents=True, exist_ok=True)

	def _write(self, rec: Dict[str, Any]) -> None:
		rec["ts"] = now_utc().isoformat()
		with self.out.open("a", encoding="utf-8") as f:
			f.write(json.dumps(rec) + "\n")
		log.info("[JSON] %s", rec)

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		self._write({"action": "block", "ip": ip, "reason": reason, "seconds": seconds})

	def allow_ip(self, ip: str, note: str = "") -> None:
		self._write({"action": "allow", "ip": ip, "note": note})


class DBAction(FirewallAction):
	"""SQLite ledger for offline testing."""
	name = "db"

	def __init__(self, sqlite_path: pathlib.Path):
		self.sqlite_path = sqlite_path
		self.conn = sqlite3.connect(self.sqlite_path)
		cur = self.conn.cursor()
		cur.execute(
			"""
			CREATE TABLE IF NOT EXISTS firewall_actions(
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				ts TEXT,
				action TEXT,
				ip TEXT,
				reason TEXT,
				seconds INTEGER
			)
			"""
		)
		self.conn.commit()

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		cur = self.conn.cursor()
		cur.execute(
			"INSERT INTO firewall_actions(ts,action,ip,reason,seconds) VALUES(?,?,?,?,?)",
			(now_utc().isoformat(), "block", ip, reason, seconds if seconds else None),
		)
		self.conn.commit()
		log.info("[DB] block %s reason='%s' seconds=%s", ip, reason, seconds)

	def allow_ip(self, ip: str, note: str = "") -> None:
		cur = self.conn.cursor()
		cur.execute(
			"INSERT INTO firewall_actions(ts,action,ip,reason,seconds) VALUES(?,?,?,?,?)",
			(now_utc().isoformat(), "allow", ip, note, None),
		)
		self.conn.commit()
		log.info("[DB] allow %s note='%s'", ip, note)


class IptablesAction(FirewallAction):
	name = "iptables"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[iptables] iptables -I INPUT -s %s -j DROP  # %s", ip, reason)


class UFWAction(FirewallAction):
	name = "ufw"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[ufw] ufw deny from %s  # %s", ip, reason)


class ShorewallAction(FirewallAction):
	name = "shorewall"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[shorewall] echo 'BLACKLIST %s' >> /etc/shorewall/blacklist  # %s", ip, reason)


class FirewalldAction(FirewallAction):
	name = "firewalld"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning(
			"[firewalld] firewall-cmd --permanent --add-rich-rule='rule family=ipv4 source address=%s drop'  # %s",
			ip,
			reason,
		)
		log.warning("[firewalld] firewall-cmd --reload")


class NftablesAction(FirewallAction):
	name = "nftables"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[nft] nft add element inet filter blacklist { %s }  # %s", ip, reason)


class CSFActionFW(FirewallAction):
	name = "csf"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		"""
		Execute a real CSF deny. Works on cPanel/WHM boxes with csf installed.
		"""
		try:
			cmd = ["csf", "-d", ip]
			if reason:
				cmd.append(reason)
			subprocess.run(cmd, check=False)
			log.info("[csf] blocked %s (%s)", ip, reason)
		except Exception as e:
			log.error("[csf] failed to block %s: %s", ip, e)

	def allow_ip(self, ip: str, note: str = "") -> None:
		try:
			cmd = ["csf", "-a", ip]
			if note:
				cmd.append(note)
			subprocess.run(cmd, check=False)
			log.info("[csf] allowed %s (%s)", ip, note)
		except Exception as e:
			log.error("[csf] failed to allow %s: %s", ip, e)


import subprocess

class IptablesExecAction(FirewallAction):
	name = "iptables_exec"

	def _exists(self, ip: str) -> bool:
		# returns True if rule already present
		r = subprocess.run(
			["iptables", "-C", "INPUT", "-s", ip, "-j", "DROP"],
			stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
		)
		return r.returncode == 0

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		try:
			if not self._exists(ip):
				cmd = ["iptables", "-I", "INPUT", "-s", ip, "-j", "DROP"]
				if reason:
					cmd += ["-m", "comment", "--comment", reason[:240]]
				subprocess.run(cmd, check=False)
				log.info("[iptables_exec] DROP %s (%s)", ip, reason)
			else:
				log.debug("[iptables_exec] rule already present for %s", ip)
		except Exception as e:
			log.error("[iptables_exec] failed to block %s: %s", ip, e)

	def allow_ip(self, ip: str, note: str = "") -> None:
		# remove one matching rule if present (may need a loop if duplicates already exist)
		try:
			while self._exists(ip):
				subprocess.run(["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"], check=False)
			log.info("[iptables_exec] removed DROP for %s (%s)", ip, note)
		except Exception as e:
			log.error("[iptables_exec] failed to remove rule for %s: %s", ip, e)


class PfSenseAction(FirewallAction):
	name = "pfsense"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[pfSense] pfctl -t blacklist -T add %s  # %s", ip, reason)


class IPFireAction(FirewallAction):
	name = "ipfire"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[IPFire] echo '%s' >> /var/ipfire/firewall/input/blacklist  # %s", ip, reason)


class VyOSAction(FirewallAction):
	name = "vyos"

	def block_ip(self, ip: str, reason: str = "", seconds: Optional[int] = None) -> None:
		log.warning("[VyOS] set firewall group address-group BLACKLIST address %s  # %s", ip, reason)
		log.warning("[VyOS] commit; save")


# Map name -> class factory (for CLI)
FW_BACKENDS = {
	"json": lambda args: JSONAction(pathlib.Path(args.json_out or "./decisions.jsonl")),
	"db": lambda args: DBAction(pathlib.Path(args.sqlite or "./fw.sqlite")),
	"iptables": lambda _: IptablesAction(),
	"ufw": lambda _: UFWAction(),
	"shorewall": lambda _: ShorewallAction(),
	"firewalld": lambda _: FirewalldAction(),
	"nftables": lambda _: NftablesAction(),
	"csf": lambda _: CSFActionFW(),
	"pfsense": lambda _: PfSenseAction(),
	"ipfire": lambda _: IPFireAction(),
	"vyos": lambda _: VyOSAction(),
}

# -------------------------------
# Whitelist loader (offline)
# -------------------------------

@dataclass
class Whitelist:
	ips: set[str]
	cidrs: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]
	fingerprints: set[str]  # optional device/user fingerprints (offline placeholder)


class WhitelistLoader:
	@staticmethod
	def load_ip_list(path: Optional[str]) -> Tuple[set[str], List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]]]:
		ips: set[str] = set()
		cidrs: List[Union[ipaddress.IPv4Network, ipaddress.IPv6Network]] = []
		if not path:
			return ips, cidrs
		p = pathlib.Path(path)
		if not p.exists():
			return ips, cidrs
		def add_token(tok: str) -> None:
			tok = tok.strip()
			if not tok:
				return
			if "/" in tok:
				try:
					cidrs.append(ipaddress.ip_network(tok, strict=False))
					return
				except Exception:
					pass
			try:
				ipaddress.ip_address(tok)
				ips.add(tok)
			except Exception:
				# silently ignore non-ip tokens
				pass
		if p.suffix.lower() in (".csv", ".tsv"):
			with p.open("r", encoding="utf-8", errors="replace", newline="") as f:
				reader = csv.DictReader(f)
				for r in reader:
					for k, v in r.items():
						if k and v and k.lower() in ("ip", "ips", "ip_address", "cidr"):
							add_token(v)
		else:
			with p.open("r", encoding="utf-8", errors="replace") as f:
				for line in f:
					line = line.strip()
					if not line or line.startswith("#"):
						continue
					add_token(line.split()[0])
		return ips, cidrs

	@staticmethod
	def load_fingerprints(path: Optional[str]) -> set[str]:
		s: set[str] = set()
		if not path:
			return s
		p = pathlib.Path(path)
		if not p.exists():
			return s
		try:
			data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
			if isinstance(data, list):
				s.update(map(str, data))
			elif isinstance(data, dict):
				fps = data.get("fingerprints") or data.get("devices") or []
				s.update(map(str, fps))
		except Exception:
			pass
		return s


# -------------------------------
# Rule engine per log type
# -------------------------------

@dataclass
class Decision:
	ip: str
	score: int
	reason: str
	details: Dict[str, Any]


def _col(df: pd.DataFrame, key: str, default: Any = None) -> pd.Series:
	"""Extract a key from the meta dict column safely as a Series."""
	if "meta" not in df.columns:
		return pd.Series([default] * len(df), index=df.index)
	return df["meta"].apply(lambda m: (m or {}).get(key, default))


class RuleEngine:
	def __init__(self, window_minutes: int, thresholds: Dict[str, int]):
		self.window_minutes = window_minutes
		self.th = thresholds

	def _window_bounds(self, df: pd.DataFrame) -> Tuple[dt.datetime, dt.datetime]:
		now = df["ts"].max()
		if pd.isna(now):
			now = dt.datetime.now(tz=UTC)
		start = now - dt.timedelta(minutes=self.window_minutes)
		return (start.to_pydatetime(), now.to_pydatetime())

	@staticmethod
	def _safe_dt(df: pd.DataFrame) -> pd.DataFrame:
		df = df.copy()
		if "ts" in df.columns:
			df["ts"] = pd.to_datetime(df["ts"], utc=True, errors="coerce")
			df = df.dropna(subset=["ts"])
		return df

	# ---------- Apache access ----------
	def apache_access(self, df: pd.DataFrame) -> List[Decision]:
		df = self._safe_dt(df)
		if df.empty:
			return []
		start, end = self._window_bounds(df)
		recent = df[(df["ts"] >= start) & (df["ts"] <= end)]
		if recent.empty:
			return []

		status = _col(recent, "status")
		path = _col(recent, "path").astype(str)
		ip_series = _col(recent, "ip").astype("string")

		mask_404 = status.eq(404)
		mask_wp = mask_404 & path.str.contains(r"\bwp-", na=False, regex=True)
		mask_susp = mask_404 & path.str.contains(r"\.php|\.env|\.git|\.bak|/\.\.", na=False, regex=True)

		ip_groups: Dict[str, Dict[str, int]] = {}
		def bump(mask: pd.Series, label: str, weight: int) -> None:
			hits = ip_series[mask].value_counts(dropna=True)
			for ip, n in hits.items():
				if not ip or str(ip) == "<NA>":
					continue
				d = ip_groups.setdefault(str(ip), {"score": 0, label: 0})
				d[label] = d.get(label, 0) + int(n)
				d["score"] += int(n) * int(weight)

		bump(mask_wp, "wp_probe", self.th.get("wp_score", 5))
		bump(mask_susp, "susp_ext", self.th.get("susp_score", 4))

		# burst 404 of any kind
		burst_counts = ip_series[mask_404].value_counts(dropna=True)
		for ip, n in burst_counts.items():
			if n >= self.th.get("burst_404_thresh", 20):
				d = ip_groups.setdefault(str(ip), {"score": 0})
				d["burst_404"] = int(n)
				d["score"] += self.th.get("burst_404_bonus", 10)

		out: List[Decision] = []
		for ip, data in ip_groups.items():
			if data.get("score", 0) >= self.th.get("score_block", 10):
				details = {k: v for k, v in data.items() if k != "score"}
				out.append(Decision(ip=str(ip), score=int(data["score"]), reason="apache_access", details=details))
		return out

	# ---------- Apache error ----------
	def apache_error(self, df: pd.DataFrame) -> List[Decision]:
		df = self._safe_dt(df)
		if df.empty:
			return []
		start, end = self._window_bounds(df)
		recent = df[(df["ts"] >= start) & (df["ts"] <= end)]
		if recent.empty:
			return []
		by_ip = _col(recent, "client_ip").astype("string")
		cnt = by_ip.value_counts(dropna=True)
		out: List[Decision] = []
		for ip, n in cnt.items():
			if not ip or str(ip) == "<NA>":
				continue
			score = 0
			if n >= self.th.get("apache_err_thresh", 8):
				score += self.th.get("apache_err_bonus", 8)
			if score >= self.th.get("score_block", 10):
				out.append(Decision(ip=str(ip), score=score, reason="apache_error", details={"error_count": int(n)}))
		return out

	# ---------- Auth / Secure / SSH (failed logins) ----------
	def auth_like(self, df: pd.DataFrame) -> List[Decision]:
		df = self._safe_dt(df)
		if df.empty:
			return []
		start, end = self._window_bounds(df)
		recent = df[(df["ts"] >= start) & (df["ts"] <= end)]
		if recent.empty:
			return []

		# Extract helpful columns
		event = _col(recent, "event").astype("string")
		by_ip_meta = _col(recent, "src_ip").astype("string")
		msg = recent.get("msg", pd.Series([], dtype=str)).fillna("").astype(str)

		# Count failed logins from multiple normalized + raw patterns
		ssh_fail_mask = (
			event.eq("ssh_failed_login") |
			msg.str.contains(r"\bFailed password\b", case=False, regex=True) |
			msg.str.contains(r"\binvalid user\b", case=False, regex=True) |
			msg.str.contains(r"\bauthentication failure\b", case=False, regex=True)
		)

		ip_series = by_ip_meta.copy()

		# Fallback IP extraction from message if meta is missing
		need_msg_ip = ip_series.isna() | ip_series.eq("") | ip_series.eq("<NA>")
		if need_msg_ip.any():
			# generic: "from 1.2.3.4" or "[2001:db8::1]" forms
			rx = re.compile(r"from\s+(\[?[A-Fa-f0-9:.]+\]?)", re.IGNORECASE)
			mips = msg.where(need_msg_ip).str.extract(rx, expand=False)
			# strip [IPv6]
			mips = mips.str.replace(r"^\[|\]$", "", regex=True)
			# strip :port for IPv4
			mips = mips.str.replace(r":\d+$", "", regex=True)
			ip_series = ip_series.mask(need_msg_ip, mips)

		# Count per IP
		fails = ip_series[ssh_fail_mask].value_counts(dropna=True)

		out: List[Decision] = []
		for ip, n in fails.items():
			if not ip or str(ip) == "<NA>":
				continue
			n = int(n)
			score = n * self.th.get("ssh_fail_score", 2)
			if n >= self.th.get("ssh_fail_thresh", 6):
				score += self.th.get("ssh_fail_bonus", 6)
			if score >= self.th.get("score_block", 10):
				out.append(Decision(
					ip=str(ip),
					score=score,
					reason="ssh_bruteforce",
					details={"failed_logins": n}
				))
		return out


	# ---------- Syslog (generic heuristics) ----------
	def syslog(self, df: pd.DataFrame) -> List[Decision]:
		df = self._safe_dt(df)
		if df.empty:
			return []
		start, end = self._window_bounds(df)
		recent = df[(df["ts"] >= start) & (df["ts"] <= end)]
		if recent.empty:
			return []
		rx = re.compile(r"from\s+([\d.:a-fA-F]+)")

		ip_counts: Dict[str, int] = {}
		for msg in recent.get("msg", pd.Series([], dtype=str)).dropna().astype(str):
			if "invalid user" in msg.lower():
				m = rx.search(msg)
				if m:
					ip = m.group(1)
					ip_counts[ip] = ip_counts.get(ip, 0) + 1

		out: List[Decision] = []
		for ip, n in ip_counts.items():
			score = n * self.th.get("syslog_invalid_user_score", 2)
			if score >= self.th.get("score_block", 10):
				out.append(Decision(ip=ip, score=score, reason="syslog_invalid_user", details={"invalid_user_events": int(n)}))
		return out

	# ---------- dmesg, exim, windows_event, procmon ----------
	def dmesg(self, df: pd.DataFrame) -> List[Decision]:
		return []

	def exim_mail(self, df: pd.DataFrame) -> List[Decision]:
		return []

	def windows_event(self, df: pd.DataFrame) -> List[Decision]:
		return []

	def procmon(self, df: pd.DataFrame) -> List[Decision]:
		return []


# -------------------------------
# Event ledger (optional SQLite)
# -------------------------------

import hashlib

class EventLedger:
	def __init__(self, sqlite_path: pathlib.Path):
		self.path = sqlite_path
		self.conn = sqlite3.connect(self.path)
		cur = self.conn.cursor()
		cur.executescript(
			"""
			PRAGMA journal_mode=WAL;
			PRAGMA synchronous=NORMAL;
			CREATE TABLE IF NOT EXISTS files (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				path TEXT UNIQUE
			);
			CREATE TABLE IF NOT EXISTS events (
				id INTEGER PRIMARY KEY AUTOINCREMENT,
				file_id INTEGER NOT NULL,
				ts TEXT,
				source_type TEXT,
				msg TEXT,
				meta_json TEXT,
				fp TEXT,
				ip TEXT,
				FOREIGN KEY(file_id) REFERENCES files(id),
				UNIQUE(file_id, fp)
			);
			CREATE INDEX IF NOT EXISTS idx_events_ts ON events(ts);
			CREATE INDEX IF NOT EXISTS idx_events_file ON events(file_id);
			CREATE INDEX IF NOT EXISTS idx_events_ip ON events(ip);
			"""
		)
		self.conn.commit()

	def _extract_ip(self, meta: Dict[str, Any] | None) -> Optional[str]:
		"""Pull an IP from meta and strip any trailing :port for IPv4."""
		if not meta:
			return None
		val = meta.get("src_ip") or meta.get("client_ip") or meta.get("ip")
		if not val:
			return None
		s = str(val)
		# strip IPv4 "ip:port" (keep IPv6 as-is unless bracketed)
		if s.count(":") == 1 and s.rsplit(":", 1)[1].isdigit():
			return s.rsplit(":", 1)[0]
		m = re.match(r"^\[(.+)\]:(\d+)$", s)  # [IPv6]:port
		if m:
			return m.group(1)
		return s

	@staticmethod
	def _fingerprint(ev: Dict[str, Any]) -> str:
		# Order-stable JSON for meta
		meta_json = json.dumps(ev.get("meta") or {}, sort_keys=True, separators=(",", ":"))
		base = f"{ev.get('ts')}|{ev.get('source_type')}|{ev.get('msg')}|{meta_json}"
		return hashlib.sha256(base.encode("utf-8", errors="replace")).hexdigest()

	def _file_id(self, path: pathlib.Path) -> int:
		cur = self.conn.cursor()
		cur.execute("INSERT OR IGNORE INTO files(path) VALUES(?)", (str(path),))
		self.conn.commit()
		cur.execute("SELECT id FROM files WHERE path=?", (str(path),))
		row = cur.fetchone()
		return int(row[0])





	def insert_many(self, file_path: pathlib.Path, events: List[Dict[str, Any]]) -> int:
		if not events:
			return 0
		file_id = self._file_id(file_path)
		rows = []
		for ev in events:
			meta = ev.get("meta") or {}
			meta_json = json.dumps(meta, sort_keys=True, separators=(",", ":"))
			fp = self._fingerprint(ev)
			ip_val = self._extract_ip(meta)   # ✅ call as method
			rows.append((
				file_id,
				ev.get("ts"),
				ev.get("source_type"),
				ev.get("msg"),
				meta_json,
				fp,
				ip_val,
			))
		cur = self.conn.cursor()
		cur.executemany(
			"""
			INSERT OR IGNORE INTO events(file_id, ts, source_type, msg, meta_json, fp, ip)
			VALUES(?,?,?,?,?,?,?)
			""",
			rows,
		)
		self.conn.commit()
		return cur.rowcount or 0


# -------------------------------
# Ingestion helpers using LogsEngine
# -------------------------------

PARSER_BY_KIND: Dict[str, LogParser] = {
	"syslog": SyslogParser(),
	"auth": AuthLogParser(),
	"secure": SecureLogParser(),
	"ssh": AuthLogParser(),  # same signals picked up
	"dmesg": DmesgParser(),
	"apache_access": ApacheAccessParser(),
	"apache_error": ApacheErrorParser(),
	"exim_mail": EximMailLogParser(),
	"windows_event": WindowsEventCSVParser(),
	"procmon": ProcMonCSVParser(),
}


def open_text_auto(path: pathlib.Path, head_only: bool = False):
	"""Open text file, transparently handling .gz. head_only means don't decode massive files fully for type detection."""
	if str(path).endswith(".gz"):
		# Use text mode to decode on the fly
		return gzip.open(path, "rt", encoding="utf-8", errors="replace")
	return path.open("r", encoding="utf-8", errors="replace")


def sniff_lines(path: pathlib.Path, n: int = 50) -> List[str]:
	out: List[str] = []
	try:
		with open_text_auto(path, head_only=True) as f:
			for i, line in enumerate(f):
				if i >= n:
					break
				out.append(line.rstrip("\n"))
	except Exception as e:
		log.debug("sniff_lines failed for %s: %s", path, e)
		return []
	return out


def to_events_from_text(path: pathlib.Path, kind: str) -> List[Dict[str, Any]]:
	parser = PARSER_BY_KIND[kind]
	events: List[Dict[str, Any]] = []
	parse_errors = 0
	with open_text_auto(path) as f:
		for line in f:
			try:
				ev = parser.parse_line(line.rstrip("\n"))
				if ev:
					events.append(ev)
			except Exception:
				parse_errors += 1
				if parse_errors <= 5:
					log.debug("Parse error on line: %r", line[:200])
	if parse_errors:
		log.warning("%s parse errors encountered (suppressed)", parse_errors)
	return events


def to_events_from_csv(path: pathlib.Path, kind: str) -> List[Dict[str, Any]]:
	parser = PARSER_BY_KIND[kind]
	events: List[Dict[str, Any]] = []
	with open_text_auto(path) as f:
		reader = csv.DictReader(f)
		if hasattr(parser, "parse_csv"):
			for ev in parser.parse_csv(reader):  # type: ignore[attr-defined]
				events.append(ev)
	return events


def events_to_df(events: List[Dict[str, Any]]) -> pd.DataFrame:
	if not events:
		return pd.DataFrame(columns=["ts", "source_type", "msg", "meta"])  # consistent schema
	rows = []
	for e in events:
		rows.append({
			"ts": e.get("ts"),
			"source_type": e.get("source_type"),
			"msg": e.get("msg"),
			"meta": e.get("meta") or {},
		})
	df = pd.DataFrame(rows)
	df["ts"] = pd.to_datetime(df["ts"], utc=True, errors="coerce")
	return df

# -------------------------------
# Decisions runner
# -------------------------------

def valid_ip(ip: str) -> bool:
	try:
		ipaddress.ip_address(ip)
		return True
	except Exception:
		return False


def apply_whitelist(decisions: List[Decision], wl: Whitelist) -> List[Decision]:
	out: List[Decision] = []
	for d in decisions:
		skip = False
		if d.ip in wl.ips:
			log.info("[SKIP] %s allowlisted (IP)", d.ip)
			skip = True
		else:
			try:
				ip_obj = ipaddress.ip_address(d.ip)
				for net in wl.cidrs:
					if ip_obj in net:
						log.info("[SKIP] %s allowlisted by CIDR %s", d.ip, net)
						skip = True
						break
			except Exception:
				pass
		if not skip:
			out.append(d)
	return out


def materialize(df: pd.DataFrame, kind: str, engine: RuleEngine) -> List[Decision]:
	if kind == "apache_access":
		return engine.apache_access(df)
	if kind == "apache_error":
		return engine.apache_error(df)
	if kind in ("auth", "secure", "ssh"):
		return engine.auth_like(df)
	if kind == "syslog":
		return engine.syslog(df)
	if kind == "dmesg":
		return engine.dmesg(df)
	if kind == "exim_mail":
		return engine.exim_mail(df)
	if kind == "windows_event":
		return engine.windows_event(df)
	if kind == "procmon":
		return engine.procmon(df)
	return []


def perform_actions(decisions: List[Decision], fw: FirewallAction, dry: bool, max_decisions: Optional[int] = None) -> None:
	if not decisions:
		log.info("No block candidates.")
		return

	blocked: set[str] = set()
	emitted = 0
	for d in decisions:
		if max_decisions is not None and emitted >= max_decisions:
			log.warning("Max decisions reached: %s (remaining suppressed)", max_decisions)
			break
		if not valid_ip(d.ip):
			log.debug("[SKIP] invalid ip: %s (%s)", d.ip, d.reason)
			continue
		if d.ip in blocked:
			log.debug("[SKIP] duplicate ip in run: %s", d.ip)
			continue
		msg = f"{d.reason} score={d.score} details={d.details}"
		log.info("[DECISION] BLOCK %s :: %s", d.ip, msg)
		if not dry:
			fw.block_ip(d.ip, reason=msg, seconds=None)
		blocked.add(d.ip)
		emitted += 1
def ledger_candidates(sqlite_path: str, since_min: int,
					min_total: int, min_ssh: int) -> List[Decision]:
	"""
	Aggregate the ingest ledger to find abusive IPs by global counts.
	Returns Decision entries with reason='ledger_thresholds'.
	"""
	if not sqlite_path or not os.path.exists(sqlite_path):
		return []
	conn = sqlite3.connect(sqlite_path)
	cur = conn.cursor()

	where = "WHERE ip IS NOT NULL"
	if since_min > 0:
		where += f" AND ts >= datetime('now','-{int(since_min)} minutes')"

	cur.execute(f"""
		SELECT ip,
			SUM(CASE WHEN json_extract(meta_json,'$.event')='ssh_failed_login' THEN 1 ELSE 0 END) AS ssh_fails,
			COUNT(*) AS total
		FROM events
		{where}
		GROUP BY ip
		HAVING ssh_fails >= ? OR total >= ?
		ORDER BY ssh_fails DESC, total DESC
	""", (int(min_ssh), int(min_total)))
	rows = cur.fetchall()
	conn.close()

	out: List[Decision] = []
	for ip, ssh_fails, total in rows:
		out.append(Decision(
			ip=str(ip),
			score=int(ssh_fails or 0) + int(total or 0),
			reason="ledger_thresholds",
			details={"ssh_fails": int(ssh_fails or 0), "total": int(total or 0)},
		))
	return out

# -------------------------------
# CLI
# -------------------------------
def build_argparser() -> argparse.ArgumentParser:
	p = argparse.ArgumentParser(
		description="Offline auto-blacklist with per-log rules and pluggable firewalls",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter,
	)
	p.add_argument("--file", required=True, help="Path to log file (text, CSV, or .gz)")
	p.add_argument(
		"--log-type",
		choices=list(PARSER_BY_KIND.keys()) + ["auto", "csv", "unknown"],
		default="auto",
		help="Force a log parser (default auto detect)",
	)
	p.add_argument(
		"--firewall",
		choices=list(FW_BACKENDS.keys()),
		default="json",
		help="Firewall backend (offline emit/record)",
	)

	# outputs for json/db backends
	p.add_argument("--json-out", help="JSONL path (for firewall=json)")
	p.add_argument("--sqlite", help="SQLite path (for firewall=db)")

	# event ledger
	p.add_argument("--event-sqlite", help="(Deprecated) SQLite path to archive normalized events")
	p.add_argument("--ingest-events-sqlite", help="SQLite path to ingest/append normalized events (preferred)")
	p.add_argument("--ingest-summary", action="store_true", help="Print a one-line summary of parsed + ingested counts")

	# decision knobs (per-file sliding window scoring)
	p.add_argument("--dry", action="store_true", help="Do not execute actions (print only)")
	p.add_argument("--window-min", type=int, default=5, help="Sliding window in minutes")
	p.add_argument("--score-block", type=int, default=10, help="Score threshold to block")
	p.add_argument("--wp-score", type=int, default=5, help="Per 404 wp-* probe score")
	p.add_argument("--susp-score", type=int, default=4, help="Per suspicious path score")
	p.add_argument("--burst-404-thresh", type=int, default=20, help="404 count to consider burst")
	p.add_argument("--burst-404-bonus", type=int, default=10, help="Bonus score when burst met")
	p.add_argument("--ssh-fail-thresh", type=int, default=6, help="Failed SSH count threshold")
	p.add_argument("--ssh-fail-score", type=int, default=2, help="Per failed SSH score")
	p.add_argument("--ssh-fail-bonus", type=int, default=6, help="Bonus when SSH threshold met")
	p.add_argument("--apache-err-thresh", type=int, default=8, help="Apache error count threshold")
	p.add_argument("--apache-err-bonus", type=int, default=8, help="Bonus for Apache error threshold")

	# allowlists
	p.add_argument("--whitelist-ip", help="Path to text/CSV list of allowed IPs/CIDRs")
	p.add_argument("--whitelist-fp", help="Path to JSON with {fingerprints:[...]} (optional/offline)")

	# misc
	p.add_argument("--max-decisions", type=int, default=None, help="Stop after N block decisions")
	p.add_argument("--no-store-events", action="store_true", help="Do not archive events even if --event-sqlite is provided")
	p.add_argument("--verbose", action="store_true", help="Verbose logging")
	p.add_argument("--quiet", action="store_true", help="Only warnings and errors")
	p.add_argument("--log-json", action="store_true", help="Emit logs as JSON to stdout")
	p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

	# NEW: ledger-wide thresholds (global counts from ingest DB)
	p.add_argument("--ledger-scan", action="store_true",
				help="Also compute decisions from the ingest ledger totals")
	p.add_argument("--ledger-since-min", type=int, default=1440,
				help="Only consider ledger events since N minutes ago (0=all time)")
	p.add_argument("--ledger-min-total", type=int, default=500,
				help="Min TOTAL events per IP to block (ledger)")
	p.add_argument("--ledger-min-ssh", type=int, default=100,
				help="Min ssh_failed_login per IP to block (ledger)")

	return p

def main(argv: List[str]) -> None:
	args = build_argparser().parse_args(argv)
	setup_logging(args.verbose, args.quiet, args.log_json)

	fpath = pathlib.Path(args.file)
	if not fpath.exists():
		log.error("File not found: %s", fpath)
		sys.exit(2)

	# Read a small sample for detection
	sample = sniff_lines(fpath, n=80)

	# Decide log type
	kind = args.log_type
	if kind == "auto":
		kind = detect_log_type(fpath, sample)
		if kind in ("csv", "csv_unknown", "unknown"):
			log.warning("[AUTO] Detected kind=%s. Consider passing --log-type explicitly.", kind)

	if kind not in PARSER_BY_KIND:
		log.error("Unsupported/unknown log type '%s'. Choose one of: %s", kind, list(PARSER_BY_KIND.keys()))
		sys.exit(2)

	# Ingest
	if kind in ("windows_event", "procmon"):
		events = to_events_from_csv(fpath, kind)
	else:
		events = to_events_from_text(fpath, kind)
	df = events_to_df(events)

	# Optional: archive normalized events to SQLite (ingestion)
	inserted = 0
	ingest_path = args.ingest_events_sqlite or args.event_sqlite
	if ingest_path and not args.no_store_events:
		try:
			ledger = EventLedger(pathlib.Path(ingest_path))
			inserted = ledger.insert_many(fpath, events)
			log.info("Event ledger: inserted %s new rows into %s", inserted, ingest_path)
		except Exception as e:
			log.error("Failed to write event ledger to %s: %s", ingest_path, e)

	# Always log parsed count; optionally print summary
	parsed_count = len(df)
	log.info("Parsed events: %s  kind=%s", parsed_count, kind)
	if args.ingest_summary:
		print(f"INGEST SUMMARY: parsed={parsed_count} inserted={inserted} db={ingest_path or 'N/A'}")

	# Engine + thresholds
	thresholds = {
		"score_block": args.score_block,
		"wp_score": args.wp_score,
		"susp_score": args.susp_score,
		"burst_404_thresh": args.burst_404_thresh,
		"burst_404_bonus": args.burst_404_bonus,
		"ssh_fail_thresh": args.ssh_fail_thresh,
		"ssh_fail_score": args.ssh_fail_score,
		"ssh_fail_bonus": args.ssh_fail_bonus,
		"apache_err_thresh": args.apache_err_thresh,
		"apache_err_bonus": args.apache_err_bonus,
	}
	engine = RuleEngine(window_minutes=args.window_min, thresholds=thresholds)

	# Whitelists
	ips, cidrs = WhitelistLoader.load_ip_list(args.whitelist_ip)
	wl = Whitelist(
		ips=ips,
		cidrs=cidrs,
		fingerprints=WhitelistLoader.load_fingerprints(args.whitelist_fp),
	)
	if wl.ips:
		log.info("Loaded %d allowlisted IPs", len(wl.ips))
	if wl.cidrs:
		log.info("Loaded %d CIDR allowlists", len(wl.cidrs))
	if wl.fingerprints:
		log.info("Loaded %d device fingerprints (offline)", len(wl.fingerprints))

	# Run per-file rules
	decisions = materialize(df, kind, engine)
	decisions = apply_whitelist(decisions, wl)

	# Optional: add ledger-wide decisions (global totals)
	if args.ledger_scan and ingest_path:
		ld = ledger_candidates(
			sqlite_path=ingest_path,
			since_min=args.ledger_since_min,
			min_total=args.ledger_min_total,
			min_ssh=args.ledger_min_ssh,
		)
		if ld:
			log.info("Ledger decisions: %d candidates", len(ld))
			ld = apply_whitelist(ld, wl)
			decisions.extend(ld)

	# Build firewall backend
	fw_factory = FW_BACKENDS.get(args.firewall)
	if fw_factory is None:
		log.error("Unknown firewall backend: %s", args.firewall)
		sys.exit(2)
	fw = fw_factory(args)

	# Act
	perform_actions(decisions, fw, dry=args.dry, max_decisions=args.max_decisions)


# def build_argparser() -> argparse.ArgumentParser:
#     p = argparse.ArgumentParser(
#         description="Offline auto-blacklist with per-log rules and pluggable firewalls",
#         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
#     )
#     p.add_argument("--file", required=True, help="Path to log file (text, CSV, or .gz)")
#     p.add_argument(
#         "--log-type",
#         choices=list(PARSER_BY_KIND.keys()) + ["auto", "csv", "unknown"],
#         default="auto",
#         help="Force a log parser (default auto detect)",
#     )
#     p.add_argument(
#         "--firewall",
#         choices=list(FW_BACKENDS.keys()),
#         default="json",
#         help="Firewall backend (offline emit/record)",
#     )

#     # outputs for json/db backends
#     p.add_argument("--json-out", help="JSONL path (for firewall=json)")
#     p.add_argument("--sqlite", help="SQLite path (for firewall=db)")

#     # event ledger
#     p.add_argument("--event-sqlite", help="(Deprecated) SQLite path to archive normalized events")
#     p.add_argument("--ingest-events-sqlite", help="SQLite path to ingest/append normalized events (preferred)")
#     p.add_argument("--ingest-summary", action="store_true", help="Print a one-line summary of parsed + ingested counts")

#     # decision knobs
#     p.add_argument("--dry", action="store_true", help="Do not execute actions (print only)")
#     p.add_argument("--window-min", type=int, default=5, help="Sliding window in minutes")
#     p.add_argument("--score-block", type=int, default=10, help="Score threshold to block")
#     p.add_argument("--wp-score", type=int, default=5, help="Per 404 wp-* probe score")
#     p.add_argument("--susp-score", type=int, default=4, help="Per suspicious path score")
#     p.add_argument("--burst-404-thresh", type=int, default=20, help="404 count to consider burst")
#     p.add_argument("--burst-404-bonus", type=int, default=10, help="Bonus score when burst met")
#     p.add_argument("--ssh-fail-thresh", type=int, default=6, help="Failed SSH count threshold")
#     p.add_argument("--ssh-fail-score", type=int, default=2, help="Per failed SSH score")
#     p.add_argument("--ssh-fail-bonus", type=int, default=6, help="Bonus when SSH threshold met")
#     p.add_argument("--apache-err-thresh", type=int, default=8, help="Apache error count threshold")
#     p.add_argument("--apache-err-bonus", type=int, default=8, help="Bonus for Apache error threshold")

#     # allowlists
#     p.add_argument("--whitelist-ip", help="Path to text/CSV list of allowed IPs/CIDRs")
#     p.add_argument("--whitelist-fp", help="Path to JSON with {fingerprints:[...]} (optional/offline)")

#     # misc
#     p.add_argument("--max-decisions", type=int, default=None, help="Stop after N block decisions")
#     p.add_argument("--no-store-events", action="store_true", help="Do not archive events even if --event-sqlite is provided")
#     p.add_argument("--verbose", action="store_true", help="Verbose logging")
#     p.add_argument("--quiet", action="store_true", help="Only warnings and errors")
#     p.add_argument("--log-json", action="store_true", help="Emit logs as JSON to stdout")
#     p.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

#     return p



# def main(argv: List[str]) -> None:
#     args = build_argparser().parse_args(argv)
#     setup_logging(args.verbose, args.quiet, args.log_json)

#     fpath = pathlib.Path(args.file)
#     if not fpath.exists():
#         log.error("File not found: %s", fpath)
#         sys.exit(2)

#     # Read a small sample for detection
#     sample = sniff_lines(fpath, n=80)

#     # Decide log type
#     kind = args.log_type
#     if kind == "auto":
#         kind = detect_log_type(fpath, sample)
#         if kind in ("csv", "csv_unknown", "unknown"):
#             log.warning("[AUTO] Detected kind=%s. Consider passing --log-type explicitly.", kind)

#     if kind not in PARSER_BY_KIND:
#         log.error("Unsupported/unknown log type '%s'. Choose one of: %s", kind, list(PARSER_BY_KIND.keys()))
#         sys.exit(2)

#     # Ingest
#     if kind in ("windows_event", "procmon"):
#         events = to_events_from_csv(fpath, kind)
#     else:
#         events = to_events_from_text(fpath, kind)
#     df = events_to_df(events)

#     # Optional: archive normalized events to SQLite (ingestion)
#     inserted = 0
#     ingest_path = args.ingest_events_sqlite or args.event_sqlite
#     if ingest_path and not args.no_store_events:
#         try:
#             ledger = EventLedger(pathlib.Path(ingest_path))
#             inserted = ledger.insert_many(fpath, events)
#             log.info("Event ledger: inserted %s new rows into %s", inserted, ingest_path)
#         except Exception as e:
#             log.error("Failed to write event ledger to %s: %s", ingest_path, e)

#     # Always log parsed count; optionally print summary
#     parsed_count = len(df)
#     log.info("Parsed events: %s  kind=%s", parsed_count, kind)
#     if args.ingest_summary:
#         print(f"INGEST SUMMARY: parsed={parsed_count} inserted={inserted} db={ingest_path or 'N/A'}")

#     # Engine + thresholds
#     thresholds = {
#         "score_block": args.score_block,
#         "wp_score": args.wp_score,
#         "susp_score": args.susp_score,
#         "burst_404_thresh": args.burst_404_thresh,
#         "burst_404_bonus": args.burst_404_bonus,
#         "ssh_fail_thresh": args.ssh_fail_thresh,
#         "ssh_fail_score": args.ssh_fail_score,
#         "ssh_fail_bonus": args.ssh_fail_bonus,
#         "apache_err_thresh": args.apache_err_thresh,
#         "apache_err_bonus": args.apache_err_bonus,
#     }
#     engine = RuleEngine(window_minutes=args.window_min, thresholds=thresholds)

#     # Whitelists
#     ips, cidrs = WhitelistLoader.load_ip_list(args.whitelist_ip)
#     wl = Whitelist(
#         ips=ips,
#         cidrs=cidrs,
#         fingerprints=WhitelistLoader.load_fingerprints(args.whitelist_fp),
#     )
#     if wl.ips:
#         log.info("Loaded %d allowlisted IPs", len(wl.ips))
#     if wl.cidrs:
#         log.info("Loaded %d CIDR allowlists", len(wl.cidrs))
#     if wl.fingerprints:
#         log.info("Loaded %d device fingerprints (offline)", len(wl.fingerprints))

#     # Run rules
#     decisions = materialize(df, kind, engine)
#     decisions = apply_whitelist(decisions, wl)

#     # Build firewall backend
#     fw_factory = FW_BACKENDS.get(args.firewall)
#     if fw_factory is None:
#         log.error("Unknown firewall backend: %s", args.firewall)
#         sys.exit(2)
#     fw = fw_factory(args)

#     # Act
#     perform_actions(decisions, fw, dry=args.dry, max_decisions=args.max_decisions)


if __name__ == "__main__":
	main(sys.argv[1:])




'''
Whitelist


# --whitelist-ip
## corp ranges
192.168.0.0/16
10.0.0.0/8
## single hosts
203.0.113.7
2001:db8::1


# --whitelist-fp
["laptop-123", "vpn-client-7"]
or
{ "fingerprints": ["laptop-123", "vpn-client-7"] }

'''