#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import os
from pathlib import Path
from datetime import datetime, timezone
from typing import Iterable, List, Optional, Tuple, Dict

# # --- Import your When class (expects when_parser.py or when.py next to this script) ---
# try:
#     from when_parser import When  # your class file named when_parser.py
# except Exception:
#     try:
#         from when import When      # or when.py
#     except Exception as e:
#         raise ImportError(
#             "Could not import When. Place your provided When class in 'when_parser.py' "
#             "or 'when.py' next to this script."
#         ) from e


IMAGE_EXTS_DEFAULT = {
	".jpg", ".jpeg", ".jpe", ".jfif",
	".png", ".gif", ".bmp", ".tif", ".tiff",
	".webp", ".heif", ".heic", ".raw", ".arw", ".cr2", ".nef", ".orf", ".rw2", ".sr2", ".dng"
}


def parse_args() -> argparse.Namespace:
	p = argparse.ArgumentParser(
		description="Find folders that contain lots of photos, optionally filtered by time."
	)
	p.add_argument(
		"--root", default=".",
		help="Root folder to scan (default: current directory)."
	)
	p.add_argument(
		"--min-count", type=int, default=50,
		help="Minimum number of matching images a folder must contain to be reported (default: 50)."
	)
	p.add_argument(
		"--ext", nargs="*", default=None,
		help="Image extensions to include (override default set). Example: --ext .jpg .png .heic"
	)
	p.add_argument(
		"--include-hidden", action="store_true",
		help="Include hidden folders/files (default: skip)."
	)
	# Time filters (use the When parser)
	p.add_argument(
		"--older", type=str, default=None,
		help='Alias for "--before now - EXPR". E.g. --older "10y" or --older "18mo".'
	)
	p.add_argument(
		"--newer", type=str, default=None,
		help='Alias for "--after now - EXPR ago". E.g. --newer "6m" (files within last 6 months).'
	)
	p.add_argument(
		"--before", type=str, default=None,
		help='Keep files dated <= this moment (When expression or ISO). E.g. "2015-01-01" or "10y ago".'
	)
	p.add_argument(
		"--after", type=str, default=None,
		help='Keep files dated >= this moment (When expression or ISO). E.g. "2008-01-01" or "15y ago".'
	)
	p.add_argument(
		"--between", nargs=2, metavar=("START", "END"), default=None,
		help='Keep files with date between START and END (inclusive). Each is a When/ISO expression.'
	)
	p.add_argument(
		"--sort", choices=["count", "oldest", "newest", "size"], default="count",
		help="Sort output by folder count, oldest file time, newest file time, or total size (default: count)."
	)
	p.add_argument(
		"--limit", type=int, default=100,
		help="Limit number of folders displayed (default: 100)."
	)
	p.add_argument(
		"--samples", type=int, default=3,
		help="How many sample file paths to show per folder (default: 3)."
	)
	p.add_argument(
		"--json", dest="json_path", default=None,
		help="Also write results to a JSON file (path)."
	)
	p.add_argument(
		"--use-utc", action="store_true",
		help="Display datetimes in UTC (default: local time)."
	)
	return p.parse_args()


def is_hidden(path: Path) -> bool:
	name = path.name
	if name.startswith('.'):
		return True
	# On Windows, dotfiles aren't the only hidden thing; we can skip attribute checks for speed.
	return False


def iter_files(root: Path, include_hidden: bool) -> Iterable[Path]:
	for dirpath, dirnames, filenames in os.walk(root):
		pdir = Path(dirpath)

		if not include_hidden:
			# Prune hidden directories in-place for efficiency
			dirnames[:] = [d for d in dirnames if not d.startswith('.')]
			if is_hidden(pdir):
				continue

		for fn in filenames:
			p = pdir / fn
			if include_hidden or not is_hidden(p):
				yield p


def human_size(nbytes: int) -> str:
	units = ["B", "KB", "MB", "GB", "TB"]
	size = float(nbytes)
	for u in units:
		if size < 1024.0 or u == units[-1]:
			return f"{size:.1f} {u}"
		size /= 1024.0


def to_local_or_utc(ts: float, use_utc: bool) -> datetime:
	if use_utc:
		return datetime.fromtimestamp(ts, tz=timezone.utc)
	return datetime.fromtimestamp(ts)  # local timezone


def build_time_filter(
	older: Optional[str],
	newer: Optional[str],
	before: Optional[str],
	after: Optional[str],
	between: Optional[Tuple[str, str]]
) -> Tuple[Optional[datetime], Optional[datetime]]:
	"""
	Returns (dt_after, dt_before) bounds as datetimes (inclusive), or None for either bound.
	Priority:
		--between START END   -> after=START, before=END
		else combine --after/--before
		plus interpret --older/--newer as convenience shorthands
	"""
	w = When()  # base=now (naive)

	dt_after = None
	dt_before = None

	if between:
		start_expr, end_expr = between
		dt_after = w.parse(start_expr, out="datetime")
		dt_before = w.parse(end_expr, out="datetime")

	if before:
		dt_before = w.parse(before, out="datetime")
	if after:
		dt_after = w.parse(after, out="datetime")

	# Convenience shorthands:
	#   --older "10y"  -> before = now - 10y  (i.e., files older than 10y)
	#   --newer "6m"   -> after  = now - 6m   (i.e., files within last 6m)
	if older:
		dt_before = w.parse(f"-{older}", out="datetime")
	if newer:
		dt_after = w.parse(f"-{newer}", out="datetime")

	# Normalize if reversed
	if dt_after and dt_before and dt_after > dt_before:
		dt_after, dt_before = dt_before, dt_after

	return dt_after, dt_before


def match_time(ts: float, dt_after: Optional[datetime], dt_before: Optional[datetime]) -> bool:
	dt_file = datetime.fromtimestamp(ts)  # naive local
	if dt_after and dt_file < dt_after:
		return False
	if dt_before and dt_file > dt_before:
		return False
	return True


def scan(
	root: Path,
	img_exts: set,
	min_count: int,
	include_hidden: bool,
	dt_after: Optional[datetime],
	dt_before: Optional[datetime]
) -> List[Dict]:
	"""
	Returns a list of folder summaries:
	{
		"folder": str,
		"count": int,
		"size_bytes": int,
		"oldest_ts": float or None,
		"newest_ts": float or None,
		"samples": List[str]
	}
	Only folders with count >= min_count are returned.
	"""
	buckets: Dict[Path, Dict] = {}

	for p in iter_files(root, include_hidden):
		if p.suffix.lower() not in img_exts:
			continue

		try:
			st = p.stat()
		except Exception:
			continue

		ts = st.st_mtime
		if not match_time(ts, dt_after, dt_before):
			continue

		folder = p.parent
		b = buckets.get(folder)
		if b is None:
			b = {
				"folder": str(folder),
				"count": 0,
				"size_bytes": 0,
				"oldest_ts": None,
				"newest_ts": None,
				"samples": []
			}
			buckets[folder] = b

		b["count"] += 1
		b["size_bytes"] += st.st_size
		b["oldest_ts"] = ts if (b["oldest_ts"] is None or ts < b["oldest_ts"]) else b["oldest_ts"]
		b["newest_ts"] = ts if (b["newest_ts"] is None or ts > b["newest_ts"]) else b["newest_ts"]

		if len(b["samples"]) < 20:  # keep a small pool; trimmed on print
			b["samples"].append(str(p))

	# Filter by min_count
	results = [v for v in buckets.values() if v["count"] >= min_count]
	return results


def sort_results(results: List[Dict], key: str) -> List[Dict]:
	if key == "count":
		return sorted(results, key=lambda r: (-r["count"], r["oldest_ts"] or float("inf")))
	if key == "oldest":
		return sorted(results, key=lambda r: (r["oldest_ts"] or float("inf"), -r["count"]))
	if key == "newest":
		return sorted(results, key=lambda r: (r["newest_ts"] or 0.0, -r["count"]))
	if key == "size":
		return sorted(results, key=lambda r: (-r["size_bytes"], -r["count"]))
	return results


def main() -> None:
	args = parse_args()

	root = Path(args.root).resolve()
	if not root.exists() or not root.is_dir():
		raise SystemExit(f"[ERROR] Root folder not found or not a directory: {root}")

	img_exts = set(x.lower() for x in (args.ext if args.ext else IMAGE_EXTS_DEFAULT))
	dt_after, dt_before = build_time_filter(args.older, args.newer, args.before, args.after, args.between)

	results = scan(
		root=root,
		img_exts=img_exts,
		min_count=args.min_count,
		include_hidden=args.include_hidden,
		dt_after=dt_after,
		dt_before=dt_before
	)

	if not results:
		print("[INFO] No matching folders found.")
		return

	results = sort_results(results, args.sort)

	# Print summary
	tz_note = "UTC" if args.use_utc else "local"
	print(f"\nFound {len(results)} folder(s) with ≥ {args.min_count} matching images (times shown in {tz_note}):\n")

	for i, r in enumerate(results[: args.limit], 1):
		oldest_dt = to_local_or_utc(r["oldest_ts"], args.use_utc) if r["oldest_ts"] else None
		newest_dt = to_local_or_utc(r["newest_ts"], args.use_utc) if r["newest_ts"] else None
		samples = r["samples"][: args.samples]

		print(f"{i:3d}. {r['folder']}")
		print(f"     images: {r['count']:,}   size: {human_size(r['size_bytes'])}")
		print(f"     range : {oldest_dt}  →  {newest_dt}")
		if samples:
			print("     sample:")
			for s in samples:
				print(f"       - {s}")
		print()

	# Optional JSON output
	if args.json_path:
		out = []
		for r in results:
			out.append({
				"folder": r["folder"],
				"count": r["count"],
				"size_bytes": r["size_bytes"],
				"oldest_ts": r["oldest_ts"],
				"newest_ts": r["newest_ts"],
				"samples": r["samples"][: args.samples],
			})
		Path(args.json_path).write_text(json.dumps(out, indent=2), encoding="utf-8")
		print(f"[OK] Wrote JSON: {args.json_path}")




















import re
from datetime import datetime, timedelta, timezone
from typing import Optional, Union

class When:
	"""
	Usage:
		w = When()  # base=now (naive) or pass tz=timezone.utc
		w.parse('-2w')                            # UNIX timestamp (default)
		w.parse('+2m', out='iso')                 # ISO string, m=months
		w.parse('1w 2d 3h ago', out='datetime')   # datetime
		w.parse('next friday at 14:30')
		w.parse('in 90min')
		w = When(base='2025-08-01 12:00'); w.parse('+1mo-3d+4h', out='iso')

	Notes:
		- Minutes: use 'min', 'mins', 'minute(s)', or 'n'
		- Months: use 'm', 'mo', 'month(s)'
		- Hours: 'h', 'hr', 'hour(s)'
	"""

	_WD = {
		'mon': 0, 'monday': 0,
		'tue': 1, 'tues': 1, 'tuesday': 1,
		'wed': 2, 'weds': 2, 'wednesday': 2,
		'thu': 3, 'thur': 3, 'thurs': 3, 'thursday': 3,
		'fri': 4, 'friday': 4,
		'sat': 5, 'saturday': 5,
		'sun': 6, 'sunday': 6,
	}

	_TOKEN = re.compile(r'([+-]?)\s*(\d+)\s*([a-zA-Z]+)')
	_ISO_DATE = re.compile(r'^\d{4}-\d{2}-\d{2}(?:[ T]\d{2}:\d{2}(?::\d{2})?)?$')
	_AT_TIME = re.compile(r'\bat\s+(\d{1,2}):(\d{2})(?::(\d{2}))?\b')

	def __init__(self,
				base: Optional[Union[int, float, datetime, str]] = None,
				tz: Optional[timezone] = None):
		self.tz = tz
		self.base = self._parse_base(base, tz)

	# ---------- public ----------
	def parse(self, expr: str, out: str = 'timestamp') -> Union[float, datetime, str]:
		if not isinstance(expr, str) or not expr.strip():
			raise ValueError("Expression must be a non-empty string.")
		dt = self.base
		s = expr.strip().lower()

		# quick keywords
		if s in ('now', '+0', '-0', '0', 'today'):
			return self._format_out(dt, out)

		# global direction hints
		global_sign = -1 if 'ago' in s else 1
		s = re.sub(r'\bago\b', ' ', s)
		s = re.sub(r'^\s*in\s+', '', s)

		# natural day shifts
		if 'tomorrow' in s:
			dt += timedelta(days=1)
			s = s.replace('tomorrow', ' ')
		if 'yesterday' in s:
			dt -= timedelta(days=1)
			s = s.replace('yesterday', ' ')

		# weekday jumpers: "next friday", "last tue"
		dt, s = self._apply_weekday_words(dt, s)

		# time setter: "at HH:MM[:SS]"
		dt, s = self._apply_time_setter(dt, s)

		# normalize separators for chained tokens
		s = re.sub(r'[,\s]*and[,\s]*', ' ', s)
		s = re.sub(r'\s*-\s*', ' -', s)
		s = re.sub(r'\s*\+\s*', ' +', s)

		# accumulate deltas from tokens
		any_token = False
		for m in self._TOKEN.finditer(s):
			any_token = True
			sign_txt, num_txt, unit_txt = m.groups()
			sign = -1 if sign_txt == '-' else 1
			n = int(num_txt)
			unit = unit_txt.lower()

			# minutes (avoid 'm' here; 'm' is month)
			if unit in ('n', 'mn', 'min', 'mins', 'minute', 'minutes'):
				dt += timedelta(minutes=sign * n)
			elif unit in ('s', 'sec', 'secs', 'second', 'seconds'):
				dt += timedelta(seconds=sign * n)
			elif unit in ('h', 'hr', 'hrs', 'hour', 'hours'):
				dt += timedelta(hours=sign * n)
			elif unit in ('d', 'day', 'days'):
				dt += timedelta(days=sign * n)
			elif unit in ('w', 'week', 'weeks'):
				dt += timedelta(weeks=sign * n)
			elif unit in ('m', 'mo', 'month', 'months'):
				dt = self._add_months(dt, sign * n)
			elif unit in ('y', 'yr', 'yrs', 'year', 'years'):
				dt = self._add_years(dt, sign * n)
			else:
				raise ValueError(f"Unknown unit '{unit}'. "
								f"Use 'min' for minutes; 'm'/'mo' for months.")

		if not any_token and s.strip():
			raise ValueError("No duration tokens recognized. Examples: '+2w', '1w 2d', '90min', '3h ago'.")

		if global_sign == -1:
			# apply overall inversion if phrases like "1h 30min ago" were used without per-token signs
			delta = dt - self.base
			dt = self.base - delta

		return self._format_out(dt, out)

	# ---------- helpers ----------
	def _parse_base(self, base, tz) -> datetime:
		if base is None:
			return datetime.now(tz or None)
		if isinstance(base, (int, float)):
			return datetime.fromtimestamp(base, tz or None)
		if isinstance(base, datetime):
			return base.astimezone(tz) if (tz and base.tzinfo) else (base.replace(tzinfo=tz) if (tz and base.tzinfo is None) else base)
		if isinstance(base, str) and self._ISO_DATE.match(base):
			parts = base.replace('T', ' ').split()
			y, m, d = (int(x) for x in parts[0].split('-'))
			if len(parts) == 1:
				dt = datetime(y, m, d)
			else:
				hh, mm, *ss = (int(x) for x in parts[1].split(':'))
				dt = datetime(y, m, d, hh, mm, (ss[0] if ss else 0))
			return dt.replace(tzinfo=tz) if tz else dt
		raise ValueError("Unsupported base. Use timestamp, datetime, or ISO 'YYYY-MM-DD[ HH:MM[:SS]]'.")

	def _apply_time_setter(self, dt: datetime, s: str):
		m = self._AT_TIME.search(s)
		if m:
			hh = int(m.group(1)); mm = int(m.group(2)); ss = int(m.group(3) or 0)
			if not (0 <= hh <= 23 and 0 <= mm <= 59 and 0 <= ss <= 59):
				raise ValueError("Invalid time in 'at HH:MM[:SS]'.")
			dt = dt.replace(hour=hh, minute=mm, second=ss, microsecond=0)
			s = s[:m.start()] + ' ' + s[m.end():]
		return dt, s

	def _apply_weekday_words(self, dt: datetime, s: str):
		m = re.search(r'\b(next|last)\s+([a-zA-Z]+)\b', s)
		if m:
			direction = +1 if m.group(1) == 'next' else -1
			wd_name = m.group(2).lower()
			if wd_name in self._WD:
				dt = self._shift_to_weekday(dt, self._WD[wd_name], direction)
				s = s.replace(m.group(0), ' ')
		return dt, s

	def _end_of_month(self, year: int, month: int) -> int:
		if month == 12:
			ny, nm = year + 1, 1
		else:
			ny, nm = year, month + 1
		first_next = datetime(ny, nm, 1)
		last_this = first_next - timedelta(days=1)
		return last_this.day

	def _add_months(self, dt: datetime, months: int) -> datetime:
		y = dt.year + (dt.month - 1 + months) // 12
		m = (dt.month - 1 + months) % 12 + 1
		d = min(dt.day, self._end_of_month(y, m))
		return dt.replace(year=y, month=m, day=d)

	def _add_years(self, dt: datetime, years: int) -> datetime:
		try:
			return dt.replace(year=dt.year + years)
		except ValueError:
			# Handle Feb 29 -> Feb 28
			return dt.replace(month=2, day=28, year=dt.year + years)

	def _shift_to_weekday(self, dt: datetime, target_wd: int, direction: int) -> datetime:
		cur = dt.weekday()
		if direction > 0:  # next
			delta = (target_wd - cur) % 7
			delta = delta or 7
		else:  # last
			delta = -((cur - target_wd) % 7 or 7)
		return dt + timedelta(days=delta)

	def _format_out(self, dt: datetime, out: str):
		if self.tz:
			dt = dt.astimezone(self.tz) if dt.tzinfo else dt.replace(tzinfo=self.tz)
		if out == 'datetime':
			return dt
		if out == 'iso':
			return dt.isoformat()
		if out == 'timestamp':
			return dt.timestamp()
		raise ValueError("Invalid 'out'. Use 'timestamp', 'datetime', or 'iso'.")








































if __name__ == "__main__":
	main()