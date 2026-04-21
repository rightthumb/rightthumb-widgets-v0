# QueryVizEngine.py
# AutoLogSecurityEngine :: Gjallarhorn
# Universal dict-driven Query & Visualization layer (offline, Matplotlib)
# Python 3.10+

from __future__ import annotations
import re
import json
import datetime as dt
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Iterable, Tuple, Callable, Union

import pandas as pd
import matplotlib.pyplot as plt

UTC = dt.timezone.utc

# ============================================================
# 1) Universal Log Query Language (ULQL) - JSON/dict contracts
# ============================================================
# ULQL is intentionally minimal and JSON-native so it ports to PHP easily.
#
# Example ULQL:
# {
#   "time": {"field": "ts", "from": "-1d", "to": "now", "floor": "1min"},
#   "from": "events",                             # logical dataset name
#   "where": [
#       {"op":"eq", "path":"source_type", "value":"apache_access"},
#       {"op":"contains", "path":"meta.path", "value":"wp-"}
#   ],
#   "select": [
#       {"metric":"count", "as":"hits"}
#   ],
#   "group_by": ["time:1min", "category"]         # time bucket + any field
# }
#
# Supported ops (portable to PHP): eq, ne, gt, gte, lt, lte, contains, regex, in

# -------------------------
# Utility: time range parse
# -------------------------
def _parse_rel_time(s: str, now: Optional[dt.datetime]=None) -> dt.datetime:
	now = now or dt.datetime.now(tz=UTC)
	if s == "now":
		return now
	m = re.match(r"-(\d+)([smhdw])$", s)
	if m:
		n = int(m.group(1)); unit = m.group(2)
		mult = {"s": "seconds", "m": "minutes", "h": "hours", "d": "days", "w": "weeks"}[unit]
		return now - dt.timedelta(**{mult: n})
	# ISO
	try:
		return dt.datetime.fromisoformat(s.replace("Z","+00:00")).astimezone(UTC)
	except Exception:
		return now

def _floor_time(ts: pd.Series, freq: str) -> pd.Series:
	# freq like '1min','5min','1h'
	# pandas offset aliases: 'T' for min, 'H' for hour
	m = re.match(r"(\d+)(min|h|s)", freq)
	if not m:
		return ts.dt.floor('1T')
	n, unit = int(m.group(1)), m.group(2)
	alias = {'s':'S','min':'T','h':'H'}[unit]
	return ts.dt.floor(f"{n}{alias}")

# ===========================
# 2) Query backends (Parent)
# ===========================
class QueryBackend:
	"""Parent: execute(ulql, datasets)->DataFrame. Portable contract (JSON in/out)."""
	def execute(self, ulql: Dict[str, Any], datasets: Dict[str, Any]) -> pd.DataFrame:
		raise NotImplementedError

class PandasQueryBackend(QueryBackend):
	"""Child: Pandas implementation over in-memory DataFrames."""
	def __init__(self, dataset_resolver: Optional[Callable[[str, Dict[str,Any]], pd.DataFrame]] = None):
		self.dataset_resolver = dataset_resolver or (lambda name, dsets: dsets[name])

	def _get_df(self, ulql: Dict[str,Any], datasets: Dict[str,Any]) -> pd.DataFrame:
		name = ulql.get("from","events")
		df = self.dataset_resolver(name, datasets).copy()
		# Ensure TS
		tfield = (ulql.get("time") or {}).get("field","ts")
		if tfield in df.columns:
			df[tfield] = pd.to_datetime(df[tfield], utc=True, errors="coerce")
		return df

	def _apply_time(self, df: pd.DataFrame, ulql: Dict[str,Any]) -> pd.DataFrame:
		t = ulql.get("time") or {}
		if not t: return df
		field = t.get("field","ts")
		if field not in df.columns: return df
		now = dt.datetime.now(tz=UTC)
		t_from = _parse_rel_time(t.get("from","-7d"), now)
		t_to   = _parse_rel_time(t.get("to","now"), now)
		mask = (df[field] >= t_from) & (df[field] <= t_to)
		return df.loc[mask]

	def _get_path(self, row: Any, path: str) -> Any:
		# 'a.b.c' dotted path, supports dicts inside 'meta'
		parts = path.split('.')
		cur: Any = row
		for p in parts:
			if isinstance(cur, dict):
				cur = cur.get(p)
			elif isinstance(cur, pd.Series):
				cur = cur.get(p)
			else:
				try:
					cur = getattr(cur, p)
				except Exception:
					return None
		return cur

	def _op(self, op: str, a: Any, b: Any) -> bool:
		try:
			if op == "eq":  return a == b
			if op == "ne":  return a != b
			if op == "gt":  return a >  b
			if op == "gte": return a >= b
			if op == "lt":  return a <  b
			if op == "lte": return a <= b
			if op == "contains":
				if a is None: return False
				return str(b) in str(a)
			if op == "regex":
				return re.search(str(b), str(a) or "") is not None
			if op == "in":
				return a in (b or [])
		except Exception:
			return False
		return False

	def _apply_where(self, df: pd.DataFrame, ulql: Dict[str,Any]) -> pd.DataFrame:
		wh = ulql.get("where") or []
		if not wh: return df
		# vectorized fallback: apply per row (portable semantics)
		def _match(row) -> bool:
			for cond in wh:
				if not self._op(cond.get("op","eq"),
								self._get_path(row, cond.get("path","")),
								cond.get("value")):
					return False
			return True
		return df[df.apply(_match, axis=1)]

	def _apply_group_select(self, df: pd.DataFrame, ulql: Dict[str,Any]) -> pd.DataFrame:
		selects = ulql.get("select") or [{"metric":"count","as":"value"}]
		gbs = ulql.get("group_by") or []
		# Handle time bucket directive like "time:1min"
		time_bucket = None
		time_field = (ulql.get("time") or {}).get("field","ts")
		resolved_gbs: List[str] = []
		for g in gbs:
			if isinstance(g,str) and g.startswith("time:"):
				time_bucket = g.split(":",1)[1]
				resolved_gbs.append("_timebucket")
			else:
				resolved_gbs.append(g)

		# Build working DF:
		work = df.copy()
		if time_bucket and time_field in work.columns:
			work["_timebucket"] = _floor_time(work[time_field].dt.tz_convert(UTC), time_bucket)
		elif "_timebucket" in resolved_gbs and time_field in work.columns:
			work["_timebucket"] = work[time_field].dt.floor('1T')

		if resolved_gbs:
			grp = work.groupby(resolved_gbs, dropna=False)
		else:
			grp = [("", work)]  # no group, operate over whole DF

		# Compute metrics
		agg_frames: List[pd.DataFrame] = []
		for sel in selects:
			metric = sel.get("metric","count").lower()
			alias  = sel.get("as") or metric
			if resolved_gbs:
				if metric == "count":
					s = grp.size().rename(alias).reset_index()
				elif metric.startswith("count_distinct:"):
					field = metric.split(":",1)[1]
					s = grp[field].nunique().rename(alias).reset_index()
				elif metric.startswith("sum:"):
					field = metric.split(":",1)[1]
					s = grp[field].sum().rename(alias).reset_index()
				elif metric.startswith("avg:"):
					field = metric.split(":",1)[1]
					s = grp[field].mean().rename(alias).reset_index()
				else:
					s = grp.size().rename(alias).reset_index()
			else:
				if metric == "count":
					s = pd.DataFrame({alias: [len(work)]})
				else:
					# fallback global agg
					s = pd.DataFrame({alias: [len(work)]})
			agg_frames.append(s)

		# Merge metrics on group keys
		out = agg_frames[0]
		for af in agg_frames[1:]:
			out = pd.merge(out, af, on=resolved_gbs, how="outer")
		# Reorder: keep time first if present
		cols = list(out.columns)
		if "_timebucket" in cols:
			cols.remove("_timebucket")
			out = out[["_timebucket"] + cols]
			out = out.rename(columns={"_timebucket":"time"})
		return out.sort_values(by=[c for c in out.columns if c in ("time",)]).reset_index(drop=True)

	def execute(self, ulql: Dict[str, Any], datasets: Dict[str, Any]) -> pd.DataFrame:
		df = self._get_df(ulql, datasets)
		df = self._apply_time(df, ulql)
		df = self._apply_where(df, ulql)
		out = self._apply_group_select(df, ulql)
		return out

# ====================================
# 3) Visualization (Parent + Matplotlib)
# ====================================
class VisualizationBackend:
	"""Parent: render(spec, dataframe) -> draws figure or returns handle."""
	def render(self, spec: Dict[str,Any], df: pd.DataFrame):
		raise NotImplementedError

class MatplotlibVisualization(VisualizationBackend):
	"""
	Spec (portable JSON):
	{
	"type": "line" | "bar" | "area",
	"x": "time",
	"y": "hits",
	"series": "category",      # optional, creates multiple lines/bars
	"title": "Traffic",
	"xlabel": "Time",
	"ylabel": "Hits",
	"legend": true
	}
	"""
	def render(self, spec: Dict[str,Any], df: pd.DataFrame):
		kind = spec.get("type","line")
		x = spec.get("x","time")
		y = spec.get("y","value")
		series = spec.get("series")
		title = spec.get("title","")
		xlabel = spec.get("xlabel", x)
		ylabel = spec.get("ylabel", y)
		legend = bool(spec.get("legend", True))

		if series and series in df.columns:
			# pivot
			piv = df.pivot_table(index=x, columns=series, values=y, aggfunc="sum").fillna(0)
			ax = piv.plot(kind="line" if kind in ("line","area") else "bar")
			if kind == "area":
				ax = piv.plot(kind="area", stacked=True)
		else:
			ax = df.plot(x=x, y=y, kind="line" if kind in ("line","area") else "bar")

		ax.set_title(title)
		ax.set_xlabel(xlabel)
		ax.set_ylabel(ylabel)
		if not legend:
			ax.get_legend().remove()
		plt.tight_layout()
		return ax

# ====================================
# 4) Rule adapter (categorization feed)
# ====================================
# This is a light adapter that turns raw events (apache_access, apache_error, auth, etc.)
# into categorized rows that ULQL can query (e.g., threats over time).
#
# Input DF schema (normalized):
#   ts (datetime), source_type (str), msg (str), meta (dict)
# Output DF schema:
#   ts (datetime), category (str), ip (str|None), note (str), source_type (str)
#
def categorize_minimal(df: pd.DataFrame) -> pd.DataFrame:
	recs: List[Dict[str,Any]] = []
	df = df.copy()
	df["ts"] = pd.to_datetime(df["ts"], utc=True, errors="coerce")

	# --- apache_access: wp- probes & 404s
	aa = df[df["source_type"]=="apache_access"]
	for _, r in aa.iterrows():
		m = r["meta"] or {}
		path = m.get("path","") or ""
		status = m.get("status")
		ip = m.get("ip")
		if status == 404 and "wp-" in path:
			recs.append({"ts": r["ts"], "category":"wp-404", "ip": ip, "note": path, "source_type":"apache_access"})
		if status == 404:
			recs.append({"ts": r["ts"], "category":"http-404", "ip": ip, "note": path, "source_type":"apache_access"})
		if "../" in path:
			recs.append({"ts": r["ts"], "category":"dir-traversal", "ip": ip, "note": path, "source_type":"apache_access"})

	# --- apache_error: PHP errors
	ae = df[df["source_type"]=="apache_error"]
	for _, r in ae.iterrows():
		msg = (r["msg"] or "")
		m = r["meta"] or {}
		ip = m.get("client_ip")
		if "PHP Fatal error" in msg or "PHP Warning" in msg or "PHP Parse error" in msg:
			recs.append({"ts": r["ts"], "category":"php-error", "ip": ip, "note": msg, "source_type":"apache_error"})

	# --- auth/secure: ssh failed logins
	au = df[df["source_type"].isin(["auth","secure","ssh"])]
	for _, r in au.iterrows():
		m = r["meta"] or {}
		if m.get("event") == "ssh_failed_login":
			recs.append({"ts": r["ts"], "category":"ssh-fail", "ip": m.get("src_ip"), "note": m.get("user"), "source_type": r["source_type"]})

	return pd.DataFrame(recs)

# ====================================
# 5) Ready-to-use ULQL specs (traffic/threats/PHP errors)
# ====================================
def ulql_traffic(minutes: int = 60) -> Dict[str,Any]:
	return {
		"from": "events",
		"time": {"field":"ts", "from": f"-{minutes}m", "to":"now"},
		"select": [{"metric":"count", "as":"hits"}],
		"group_by": ["time:1min", "source_type"]
	}

def ulql_threats(minutes: int = 60) -> Dict[str,Any]:
	return {
		"from": "threats",
		"time": {"field":"ts", "from": f"-{minutes}m", "to":"now"},
		"select": [{"metric":"count", "as":"hits"}],
		"group_by": ["time:1min", "category"]
	}

def ulql_php_errors(minutes: int = 60) -> Dict[str,Any]:
	return {
		"from": "threats",
		"time": {"field":"ts", "from": f"-{minutes}m", "to":"now"},
		"where": [ {"op":"eq","path":"category","value":"php-error"} ],
		"select": [{"metric":"count", "as":"errors"}],
		"group_by": ["time:1min"]
	}

# ====================================
# 6) Demo wiring (can be removed in prod)
# ====================================
def _demo_frames() -> Dict[str,pd.DataFrame]:
	# Minimal demo data: apache access + error + auth
	now = dt.datetime.now(tz=UTC).replace(second=0, microsecond=0)
	rows = [
		# apache_access
		{"ts": now - dt.timedelta(minutes=9), "source_type":"apache_access", "msg":"GET /wp-login.php -> 404",
		"meta":{"ip":"1.2.3.4","status":404,"path":"/wp-login.php","ua":"curl/8.0"}},
		{"ts": now - dt.timedelta(minutes=8), "source_type":"apache_access", "msg":"GET / -> 200",
		"meta":{"ip":"5.6.7.8","status":200,"path":"/","ua":"Mozilla"}},
		{"ts": now - dt.timedelta(minutes=7), "source_type":"apache_access", "msg":"GET /x -> 404",
		"meta":{"ip":"1.2.3.4","status":404,"path":"/x","ua":"curl/8.0"}},
		{"ts": now - dt.timedelta(minutes=6), "source_type":"apache_access", "msg":"GET /../../etc/passwd -> 404",
		"meta":{"ip":"9.9.9.9","status":404,"path":"/../../etc/passwd","ua":"badbot"}},
		# apache_error
		{"ts": now - dt.timedelta(minutes=5), "source_type":"apache_error",
		"msg":"PHP Warning: include(): Failed opening 'x.php' for inclusion", "meta":{"client_ip":"1.2.3.4"}},
		{"ts": now - dt.timedelta(minutes=3), "source_type":"apache_error",
		"msg":"PHP Fatal error: Call to undefined function", "meta":{"client_ip":"5.6.7.8"}},
		# auth
		{"ts": now - dt.timedelta(minutes=4), "source_type":"auth", "msg":"Failed password for root from 10.0.0.9",
		"meta":{"event":"ssh_failed_login","user":"root","src_ip":"10.0.0.9"}},
	]
	events = pd.DataFrame(rows)
	threats = categorize_minimal(events)
	return {"events": events, "threats": threats}

def demo_run(show: bool = True) -> None:
	datasets = _demo_frames()
	qb = PandasQueryBackend()
	viz = MatplotlibVisualization()

	# Traffic
	q1 = ulql_traffic(minutes=20)
	df1 = qb.execute(q1, datasets)
	viz.render({
		"type":"line","x":"time","y":"hits","series":"source_type",
		"title":"Traffic (per minute)","xlabel":"Time","ylabel":"Hits","legend":True
	}, df1)

	# Threats
	q2 = ulql_threats(minutes=20)
	df2 = qb.execute(q2, datasets)
	viz.render({
		"type":"line","x":"time","y":"hits","series":"category",
		"title":"Threats (per minute)","xlabel":"Time","ylabel":"Hits","legend":True
	}, df2)

	# PHP errors
	q3 = ulql_php_errors(minutes=20)
	df3 = qb.execute(q3, datasets)
	viz.render({
		"type":"bar","x":"time","y":"errors",
		"title":"PHP Errors (per minute)","xlabel":"Time","ylabel":"Errors","legend":False
	}, df3)

	if show:
		plt.show()

# If you want to test quickly:
if __name__ == "__main__":
	demo_run(show=True)