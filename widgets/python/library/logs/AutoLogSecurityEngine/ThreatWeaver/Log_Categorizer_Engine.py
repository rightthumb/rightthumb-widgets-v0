#!/usr/bin/env python3
# Log_Categorizer_Engine.py
# Offline log categorizer with pandas-style rules, JSONL output for DuckDB
# Python 3.10+
#
# Examples:
#   python Log_Categorizer_Engine.py --file /usr/local/apache/logs/access_log --out logs.jsonl
#   python Log_Categorizer_Engine.py --file ./error_log --out errors.jsonl --log-type apache_error
#   python Log_Categorizer_Engine.py --file ./auth.log --out auth.jsonl
#   python Log_Categorizer_Engine.py --file ./events.csv --log-type windows_event --out win.jsonl
#
# Optional exports:
#   --parquet out.parquet     (needs pyarrow)
#   --csv out.csv
#
# Tip: Use DuckDB on your workstation:
#   duckdb -c "CREATE TABLE logs AS SELECT * FROM read_json_auto('logs.jsonl');"
#
# If DuckDB isn’t available on your server, alternatives:
#   - Parquet files (readable by Python/Pandas/Polars/Arrow/SQLite extensions)
#   - Plain CSV (simple but loses nested dicts)
#   - SQLite (not included here to keep things simple/offline; easy to add)

from __future__ import annotations
import argparse
import csv
import json
import pathlib
import re
import sys
import datetime as dt
from dataclasses import dataclass, field
from typing import Any, Callable, Dict, Iterable, Iterator, List, Optional, Tuple

import pandas as pd

from LogsEngine import (
	SyslogParser, AuthLogParser, SecureLogParser, DmesgParser,
	ApacheAccessParser, ApacheErrorParser, EximMailLogParser,
	WindowsEventCSVParser, ProcMonCSVParser,
)

UTC = dt.timezone.utc

# -----------------------------
# Minimal auto-detection helpers
# -----------------------------

PARSER_BY_KIND = {
	"syslog": SyslogParser(),
	"auth": AuthLogParser(),
	"secure": SecureLogParser(),
	"ssh": AuthLogParser(),  # same signals parsed by AuthLogParser
	"dmesg": DmesgParser(),
	"apache_access": ApacheAccessParser(),
	"apache_error": ApacheErrorParser(),
	"exim_mail": EximMailLogParser(),
	"windows_event": WindowsEventCSVParser(),
	"procmon": ProcMonCSVParser(),
}

FILE_HINTS = [
	(re.compile(r'access(_log)?$', re.I), 'apache_access'),
	(re.compile(r'error(_log)?$', re.I), 'apache_error'),
	(re.compile(r'auth\.log$', re.I), 'auth'),
	(re.compile(r'/secure$', re.I), 'secure'),
	(re.compile(r'/sshd/|sshd\.log$', re.I), 'ssh'),
	(re.compile(r'dmesg', re.I), 'dmesg'),
	(re.compile(r'exim', re.I), 'exim_mail'),
	(re.compile(r'\.csv$', re.I), 'csv'),
]

def sniff_lines(path: pathlib.Path, n: int = 80) -> list[str]:
	out: list[str] = []
	try:
		with path.open('r', encoding='utf-8', errors='replace') as f:
			for i, line in enumerate(f):
				if i >= n: break
				out.append(line.rstrip('\n'))
	except Exception:
		pass
	return out

def detect_kind(path: pathlib.Path, sample: list[str]) -> str:
	pstr = str(path)
	for rx, kind in FILE_HINTS:
		if rx.search(pstr):
			if kind != "csv":
				return kind
			# csv: try header detection later
	if path.suffix.lower() == ".csv":
		# Read header
		try:
			with path.open('r', encoding='utf-8', errors='replace', newline='') as f:
				reader = csv.reader(f)
				header = next(reader, None)
			if header:
				lower = [h.lower() for h in header]
				if any("event id" in h or "provider" in h or "level" in h for h in lower):
					return "windows_event"
				if any("process name" in h or "operation" in h or "time of day" in h for h in lower):
					return "procmon"
			return "csv"
		except Exception:
			return "csv"
	# very rough content matching (keep minimal: we rely on LogsEngine parsers)
	if any('HTTP/' in ln and '"' in ln for ln in sample):
		return "apache_access"
	if any(ln.startswith('[') and 'pid ' in ln for ln in sample):
		return "apache_error"
	if any(re.match(r'^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2}\s+', ln) for ln in sample):
		return "auth" if any('sshd' in ln for ln in sample) else "syslog"
	if any(re.match(r'^\[\d+(?:\.\d+)?\]\s+', ln) for ln in sample):
		return "dmesg"
	return "syslog"

# -----------------------------
# Ingestion -> DataFrame
# -----------------------------

def ingest_text(path: pathlib.Path, parser) -> list[dict]:
	events: list[dict] = []
	with path.open('r', encoding='utf-8', errors='replace') as f:
		for line in f:
			ev = parser.parse_line(line.rstrip('\n'))
			if ev:
				events.append(ev)
	return events

def ingest_csv(path: pathlib.Path, parser) -> list[dict]:
	events: list[dict] = []
	with path.open('r', encoding='utf-8', errors='replace', newline='') as f:
		reader = csv.DictReader(f)
		if hasattr(parser, "parse_csv"):
			for ev in parser.parse_csv(reader):  # type: ignore
				events.append(ev)
	return events

def events_to_df(events: list[dict]) -> pd.DataFrame:
	if not events:
		return pd.DataFrame(columns=["ts","source_type","msg","meta"])
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

# -----------------------------
# Rule system (pandas-style)
# -----------------------------

@dataclass
class Rule:
	name: str
	description: str
	# Given a normalized DF, return a DF of matched rows and a function to extract IP + details
	filter_df: Callable[[pd.DataFrame], pd.DataFrame]
	ip_from_row: Callable[[pd.Series], Optional[str]]
	details_from_row: Callable[[pd.Series], Dict[str, Any]] = lambda row: {}

def _mget(meta: dict, key: str, default=None):
	try:
		return (meta or {}).get(key, default)
	except Exception:
		return default

# Helpers that mirror your style (df.query(..., engine='python'))
def q(df: pd.DataFrame, expr: str) -> pd.DataFrame:
	return df.query(expr, engine="python")

# ------------- RULE PACKS -------------

def rules_apache_access() -> list[Rule]:
	# meta fields coming from ApacheAccessParser: ip, user, method, path, status, size, ref, ua, proto
	return [
		Rule(
			name="wp_probe",
			description="404 where path contains 'wp-' (classic WP scanners)",
			filter_df=lambda df: q(df, 'meta.status==404 and meta.path.str.contains("wp-")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"path": _mget(r.meta,'path')}
		),
		Rule(
			name="susp_php",
			description="Probing common PHP admin/entry points",
			filter_df=lambda df: q(df, 'meta.status==404 and meta.path.str.contains("(?i)admin|phpmyadmin|wp-login|wp-admin|xmlrpc\\.php")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"path": _mget(r.meta,'path')}
		),
		Rule(
			name="dotfiles_env_git",
			description="Attempt to read .env/.git/config/.DS_Store/backup files",
			filter_df=lambda df: q(df, 'meta.status==404 and meta.path.str.contains("(?i)\\.env|\\.git|\\.bak|\\.old|\\.zip|\\.tar|\\.gz|\\.7z|\\.rar|\\.sql")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"path": _mget(r.meta,'path')}
		),
		Rule(
			name="dir_traversal",
			description="Path contains ../ traversal",
			filter_df=lambda df: q(df, 'meta.path.str.contains("\\.\\./")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"path": _mget(r.meta,'path')}
		),
		Rule(
			name="sqli_signatures",
			description="Basic SQLi strings in path or referrer",
			filter_df=lambda df: q(df, 'meta.path.str.contains("(?i)union\\s+select|sleep\\(|benchmark\\(|information_schema|or\\s+1=1")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"path": _mget(r.meta,'path')}
		),
		Rule(
			name="scanner_user_agents",
			description="Common scanner/bot UAs",
			filter_df=lambda df: q(df, 'meta.ua.str.contains("(?i)nikto|acunetix|sqlmap|nessus|wpscan|curl/|wget/")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"ua": _mget(r.meta,'ua')}
		),
		Rule(
			name="http_method_abuse",
			description="Rare/verbose or blocked methods",
			filter_df=lambda df: q(df, 'meta.method.str.contains("(?i)trace|track|debug|options")'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"method": _mget(r.meta,'method')}
		),
		Rule(
			name="burst_404",
			description="Burst of 404s (counted here, still log each 404 row tagged)",
			filter_df=lambda df: q(df, 'meta.status==404'),
			ip_from_row=lambda r: _mget(r.meta,'ip'),
			details_from_row=lambda r: {"status": 404, "path": _mget(r.meta,'path')}
		),
	]

def rules_apache_error() -> list[Rule]:
	# meta: module, client_ip
	return [
		Rule(
			name="client_denied",
			description="Client denied by server configuration",
			filter_df=lambda df: q(df, 'msg.str.contains("client denied by server configuration")'),
			ip_from_row=lambda r: _mget(r.meta,'client_ip'),
			details_from_row=lambda r: {"module": _mget(r.meta,'module')}
		),
		Rule(
			name="file_not_found_spam",
			description="Repeated file not found from client IP",
			filter_df=lambda df: q(df, 'msg.str.contains("File does not exist")'),
			ip_from_row=lambda r: _mget(r.meta,'client_ip'),
			details_from_row=lambda r: {"module": _mget(r.meta,'module')}
		),
		Rule(
			name="php_fatal",
			description="PHP fatal/warnings with client context",
			filter_df=lambda df: q(df, 'msg.str.contains("PHP Fatal error|PHP Warning|PHP Parse error")'),
			ip_from_row=lambda r: _mget(r.meta,'client_ip'),
			details_from_row=lambda r: {"module": _mget(r.meta,'module')}
		),
	]

def rules_auth_like() -> list[Rule]:
	# AuthLogParser/SSHD: meta.event 'ssh_failed_login' / 'ssh_login', src_ip, user, method
	return [
		Rule(
			name="ssh_failed_login",
			description="Failed SSH login",
			filter_df=lambda df: q(df, 'meta.event=="ssh_failed_login"'),
			ip_from_row=lambda r: _mget(r.meta,'src_ip'),
			details_from_row=lambda r: {"user": _mget(r.meta,'user')}
		),
		Rule(
			name="ssh_root_login_attempt",
			description="Failed SSH attempt for root or similar",
			filter_df=lambda df: q(df, 'meta.event=="ssh_failed_login" and meta.user.str.contains("(?i)^root$|admin|test|oracle|postgres")'),
			ip_from_row=lambda r: _mget(r.meta,'src_ip'),
			details_from_row=lambda r: {"user": _mget(r.meta,'user')}
		),
		Rule(
			name="ssh_success_login",
			description="Accepted SSH login (for auditing)",
			filter_df=lambda df: q(df, 'meta.event=="ssh_login"'),
			ip_from_row=lambda r: _mget(r.meta,'src_ip'),
			details_from_row=lambda r: {"user": _mget(r.meta,'user'), "method": _mget(r.meta,'method')}
		),
		Rule(
			name="invalid_user_syslog",
			description="Syslog invalid user pattern",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)invalid user")'),
			ip_from_row=lambda r: _ip_from_msg(r.msg),
			details_from_row=lambda r: {}
		),
	]

def rules_syslog_generic() -> list[Rule]:
	return [
		Rule(
			name="sudo_auth_fail",
			description="sudo auth failure",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)authentication failure; logname=")'),
			ip_from_row=lambda r: None,
		),
		Rule(
			name="kernel_block",
			description="kernel warnings of netfilter blocks",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)IN=.*OUT=.*SRC=")'),
			ip_from_row=lambda r: _extract_kmsg_ip(r.msg),
			details_from_row=lambda r: {"kmsg": r.msg}
		),
	]

def rules_exim() -> list[Rule]:
	return [
		Rule(
			name="exim_rejected_rcpt",
			description="Rejected RCPT (likely spam or misconfig)",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)rejected RCPT|H=(\\S+) rejected")'),
			ip_from_row=lambda r: None,
		),
		Rule(
			name="exim_tls_fail",
			description="TLS errors",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)TLS error|SSL routines")'),
			ip_from_row=lambda r: None,
		),
	]

def rules_windows_event() -> list[Rule]:
	# The normalized 'meta' for windows_event includes event_id when available
	return [
		Rule(
			name="win_logon_fail",
			description="Windows logon failure (common 4625)",
			filter_df=lambda df: q(df, 'meta.event_id.str.contains("4625") if meta.event_id.notna() else False'),
			ip_from_row=lambda r: None,
		),
		Rule(
			name="win_service_install",
			description="Service install/change (7045 etc.)",
			filter_df=lambda df: q(df, 'meta.event_id.str.contains("7045|7040") if meta.event_id.notna() else False'),
			ip_from_row=lambda r: None,
		),
	]

def rules_procmon() -> list[Rule]:
	return [
		Rule(
			name="procmon_access_denied",
			description="Process I/O access denied",
			filter_df=lambda df: q(df, 'msg.str.contains("ACCESS DENIED")'),
			ip_from_row=lambda r: None,
		),
		Rule(
			name="procmon_reg_changes",
			description="Registry modifications",
			filter_df=lambda df: q(df, 'msg.str.contains("Reg(Create|Set|Delete)")'),
			ip_from_row=lambda r: None,
		),
	]

def rules_dmesg() -> list[Rule]:
	return [
		Rule(
			name="oom_killer",
			description="Out-of-memory killer",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)Out of memory|oom-killer")'),
			ip_from_row=lambda r: None,
		),
		Rule(
			name="usb_events",
			description="USB attach/detach",
			filter_df=lambda df: q(df, 'msg.str.contains("(?i)usb\\s\\d-\\d:|USB disconnect")'),
			ip_from_row=lambda r: None,
		),
	]

RULE_PACKS = {
	"apache_access": rules_apache_access,
	"apache_error":  rules_apache_error,
	"auth":          rules_auth_like,
	"secure":        rules_auth_like,
	"ssh":           rules_auth_like,
	"syslog":        rules_syslog_generic,
	"exim_mail":     rules_exim,
	"windows_event": rules_windows_event,
	"procmon":       rules_procmon,
	"dmesg":         rules_dmesg,
}

# -----------------------------
# Small extractors
# -----------------------------

_IP_IN_MSG = re.compile(r'(?<![:\w])(\d{1,3}(?:\.\d{1,3}){3})(?![:\w])')
def _ip_from_msg(msg: str | None) -> Optional[str]:
	if not msg: return None
	m = _IP_IN_MSG.search(msg)
	return m.group(1) if m else None

def _extract_kmsg_ip(msg: str | None) -> Optional[str]:
	# Look for 'SRC=1.2.3.4'
	if not msg: return None
	m = re.search(r'SRC=(\d{1,3}(?:\.\d{1,3}){3})', msg)
	return m.group(1) if m else None

# -----------------------------
# Categorization -> JSONL
# -----------------------------

def categorize(df: pd.DataFrame, kind: str, source_path: str) -> list[dict]:
	"""Return JSONL-ready records: one per matched row per rule."""
	df = df.copy()
	# make string-access safe in query
	if "msg" in df.columns:
		df["msg"] = df["msg"].astype("string")
	if "meta" not in df.columns:
		df["meta"] = [{} for _ in range(len(df))]

	pack_factory = RULE_PACKS.get(kind)
	if not pack_factory:
		return []

	rules = pack_factory()
	out: list[dict] = []

	for rule in rules:
		try:
			matched = rule.filter_df(df)
			if matched.empty:
				continue
			for _, row in matched.iterrows():
				ip = rule.ip_from_row(row)
				rec = {
					"ts": (row["ts"].to_pydatetime().isoformat() if pd.notna(row["ts"]) else None),
					"log_type": kind,
					"category": rule.name,
					"rule_desc": rule.description,
					"ip": ip,
					"details": rule.details_from_row(row),
					"source_path": source_path,
				}
				out.append(rec)
		except Exception as e:
			# keep going even if one rule fails
			out.append({
				"ts": dt.datetime.now(tz=UTC).isoformat(),
				"log_type": kind,
				"category": "rule_error",
				"rule_desc": rule.name,
				"ip": None,
				"details": {"error": str(e)},
				"source_path": source_path,
			})
	return out

# -----------------------------
# CLI
# -----------------------------

def build_args() -> argparse.Namespace:
	p = argparse.ArgumentParser(
		description="Offline log categorizer that emits JSONL (DuckDB-friendly) using pandas-style rules",
		formatter_class=argparse.ArgumentDefaultsHelpFormatter
	)
	p.add_argument("--file", required=True, help="Path to a log file (text or CSV)")
	p.add_argument("--log-type", choices=list(PARSER_BY_KIND.keys())+["auto","csv"], default="auto",
				help="Force parser (default: auto)")
	p.add_argument("--out", required=True, help="JSONL output file")
	p.add_argument("--parquet", help="Optional Parquet output")
	p.add_argument("--csv", help="Optional CSV output (flat)")
	return p.parse_args()

def main():
	args = build_args()
	fpath = pathlib.Path(args.file)
	sample = sniff_lines(fpath)

	kind = args.log_type
	if kind == "auto":
		kind = detect_kind(fpath, sample)
		if kind == "csv":
			print("[AUTO] CSV detected; pass --log-type windows_event or --log-type procmon if needed.", file=sys.stderr)
	if kind not in PARSER_BY_KIND:
		print(f"[ERROR] Unknown/unsupported log type: {kind}", file=sys.stderr)
		sys.exit(2)

	parser = PARSER_BY_KIND[kind]
	if kind in ("windows_event","procmon"):
		events = ingest_csv(fpath, parser)
	else:
		events = ingest_text(fpath, parser)

	df = events_to_df(events)
	print(f"[INFO] Parsed {len(df)} events as {kind}")

	records = categorize(df, kind, str(fpath))
	print(f"[INFO] Matched {len(records)} categorized rows")

	# JSONL (best for DuckDB read_json_auto)
	outp = pathlib.Path(args.out)
	outp.parent.mkdir(parents=True, exist_ok=True)
	with outp.open('w', encoding='utf-8') as f:
		for rec in records:
			f.write(json.dumps(rec, ensure_ascii=False) + "\n")
	print(f"[OK] Wrote JSONL: {outp}")

	# Optional Parquet (great for columnar analytics; DuckDB/Polars friendly)
	if args.parquet:
		try:
			import pyarrow as pa
			import pyarrow.parquet as pq
			# Flatten 'details' to JSON strings to keep schema simple
			df_out = pd.DataFrame(records).copy()
			if "details" in df_out.columns:
				df_out["details"] = df_out["details"].apply(lambda d: json.dumps(d, ensure_ascii=False))
			table = pa.Table.from_pandas(df_out, preserve_index=False)
			pq.write_table(table, args.parquet)
			print(f"[OK] Wrote Parquet: {args.parquet}")
		except Exception as e:
			print(f"[WARN] Could not write Parquet ({e}). Install pyarrow.", file=sys.stderr)

	# Optional CSV (flattens details to JSON string)
	if args.csv:
		df_csv = pd.DataFrame(records).copy()
		if "details" in df_csv.columns:
			df_csv["details"] = df_csv["details"].apply(lambda d: json.dumps(d, ensure_ascii=False))
		df_csv.to_csv(args.csv, index=False)
		print(f"[OK] Wrote CSV: {args.csv}")

if __name__ == "__main__":
	main()