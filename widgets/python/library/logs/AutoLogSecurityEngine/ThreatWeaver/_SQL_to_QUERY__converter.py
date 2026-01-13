# _SQL_to_QUERY__converter.py
# Offline SQL -> ULQL converter (subset) for AutoLogSecurityEngine ULQL

from __future__ import annotations
import re
import datetime as dt
from typing import Any, Dict, List, Optional

UTC = dt.timezone.utc

# ---------- helpers

def _strip(s: str) -> str:
	return s.strip().strip(';').strip()

def _unquote(s: str) -> str:
	if len(s) >= 2 and ((s[0] == s[-1] == "'") or (s[0] == s[-1] == '"')):
		return s[1:-1]
	return s

def _split_commas(s: str) -> List[str]:
	# split by commas not inside parentheses
	out, buf, depth = [], [], 0
	for ch in s:
		if ch == '(':
			depth += 1; buf.append(ch)
		elif ch == ')':
			depth -= 1; buf.append(ch)
		elif ch == ',' and depth == 0:
			out.append(''.join(buf).strip()); buf = []
		else:
			buf.append(ch)
	if buf:
		out.append(''.join(buf).strip())
	return out

def _iso_or_rel(s: str) -> str:
	s = s.strip()
	# pass through relative like -1h/-24h or 'now'
	if re.fullmatch(r'-\d+[smhdw]', s, re.I) or s.lower() == 'now':
		return s.lower()
	# normalize ISO-ish literals
	s = _unquote(s)
	# allow YYYY-MM-DD or full ISO
	if re.fullmatch(r'\d{4}-\d{2}-\d{2}', s):
		return s + 'T00:00:00Z'
	return s

# ---------- main converter

class SqlToULQL:
	"""
	Convert a constrained SQL subset to ULQL dict.
	Supported:
	SELECT { COUNT(*)
			| COUNT(DISTINCT field)
			| SUM(field)
			| AVG(field) } [AS alias], ...
	FROM dataset
	WHERE <cond> [AND <cond> ...]
		cond: field op value
			op in (=, !=, >, >=, <, <=)
			IN (v1, v2, ...)
			LIKE '%foo%' | 'foo%' | '%foo'
			BETWEEN 'ISO' AND 'ISO'  (for time field only)
	GROUP BY col, DATE_TRUNC('minute'|'hour', ts) or TIME_BUCKET('5min', ts)
	"""

	# map date_trunc unit -> ULQL bucket
	_TRUNC_TO_BUCKET = {
		'minute': '1min',
		'hour':   '1h',
		'second': '1s',
		'day':    '1d',
	}

	def __init__(self, *,
				default_time_field: str = 'ts',
				field_aliases: Optional[Dict[str,str]] = None):
		self.time_field = default_time_field
		self.alias = field_aliases or {}

	# ---- public API
	def convert(self, sql: str) -> Dict[str, Any]:
		sql = _strip(sql)
		m = re.match(r'(?is)select\s+(.*?)\s+from\s+(.*?)\s*(where\s+.*?|)\s*(group\s+by\s+.*?|)\s*(order\s+by\s+.*?|)\s*(limit\s+.*?|)\s*$', sql)
		if not m:
			raise ValueError("Unrecognized SQL form")
		select_part = _strip(m.group(1))
		from_part   = _strip(m.group(2))
		where_part  = _strip(m.group(3) or '')
		group_part  = _strip(m.group(4) or '')
		# order_part  = _strip(m.group(5) or '')
		# limit_part  = _strip(m.group(6) or '')

		ulql: Dict[str, Any] = {
			"from": self._parse_from(from_part),
			"time": {"field": self.time_field, "from": "-7d", "to": "now"},
			"where": [],
			"select": self._parse_select(select_part),
			"group_by": []
		}

		time_bounds, where_list = self._parse_where(where_part)
		if time_bounds:
			ulql["time"]["from"] = time_bounds[0]
			ulql["time"]["to"]   = time_bounds[1]
		if where_list:
			ulql["where"] = where_list

		group_list = self._parse_group(group_part)
		if group_list:
			ulql["group_by"] = group_list

		# Clean empties
		if not ulql["where"]:
			ulql.pop("where")
		if not ulql["group_by"]:
			ulql.pop("group_by")
		return ulql

	# ---- parsers

	def _parse_from(self, s: str) -> str:
		# FROM dataset [AS alias] – keep first token as dataset name
		tok = s.split()[0]
		return tok.strip()

	def _parse_select(self, s: str) -> List[Dict[str,Any]]:
		items = _split_commas(s)
		out: List[Dict[str,Any]] = []
		for it in items:
			alias = None
			m_as = re.match(r'(?is)(.*)\s+as\s+([a-zA-Z0-9_]+)$', it)
			if m_as:
				expr, alias = _strip(m_as.group(1)), m_as.group(2)
			else:
				expr = _strip(it)

			# COUNT(*)
			if re.match(r'(?is)^count\s*\(\s*\*\s*\)$', expr):
				out.append({"metric":"count", "as": alias or "count"})
				continue

			# COUNT(DISTINCT field)
			m_cd = re.match(r'(?is)^count\s*\(\s*distinct\s+([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_cd:
				field = self._map_field(m_cd.group(1))
				out.append({"metric":f"count_distinct:{field}", "as": alias or f"cd_{field.replace('.','_')}"})
				continue

			# SUM(field)
			m_sum = re.match(r'(?is)^sum\s*\(\s*([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_sum:
				field = self._map_field(m_sum.group(1))
				out.append({"metric":f"sum:{field}", "as": alias or f"sum_{field.replace('.','_')}"})
				continue

			# AVG(field)
			m_avg = re.match(r'(?is)^avg\s*\(\s*([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_avg:
				field = self._map_field(m_avg.group(1))
				out.append({"metric":f"avg:{field}", "as": alias or f"avg_{field.replace('.','_')}"})
				continue

			# Bare column -> treat as group key (no metric). We’ll ignore in ULQL select.
			# (If you want projections, extend ULQL with "project":[...])
			continue
		if not out:
			out = [{"metric":"count", "as":"value"}]
		return out

	def _parse_where(self, s: str) -> (Optional[List[str]], List[Dict[str,Any]]):
		if not s:
			return None, []
		# remove leading 'where'
		s = re.sub(r'(?is)^where\s+', '', s).strip()

		# Special time patterns first:
		# 1) ts BETWEEN 'a' AND 'b'
		m_bt = re.search(rf'(?is)\b{re.escape(self.time_field)}\s+between\s+(.+?)\s+and\s+(.+?)(?:\s+and|\s*$)', s)
		if m_bt:
			t_from = _iso_or_rel(m_bt.group(1))
			t_to   = _iso_or_rel(m_bt.group(2))
			# remove the between clause from s
			s = s[:m_bt.start()] + s[m_bt.end():]
			s = s.strip().strip('AND').strip()
			time_bounds = [t_from, t_to]
		else:
			# ts >= a AND ts <= b
			t_ge = re.search(rf'(?is)\b{re.escape(self.time_field)}\s*(>=|>)\s*([^\s]+)', s)
			t_le = re.search(rf'(?is)\b{re.escape(self.time_field)}\s*(<=|<)\s*([^\s]+)', s)
			time_bounds = None
			if t_ge or t_le:
				t_from = _iso_or_rel(t_ge.group(2)) if t_ge else "-7d"
				t_to   = _iso_or_rel(t_le.group(2)) if t_le else "now"
				time_bounds = [t_from, t_to]
				# strip them
				if t_ge: s = s.replace(t_ge.group(0), '')
				if t_le: s = s.replace(t_le.group(0), '')
				s = re.sub(r'(?i)\band\b', ' ', s)

		# Now split remaining WHERE by AND (subset: AND only for now)
		parts = [p.strip() for p in re.split(r'(?i)\band\b', s) if p.strip()]
		out: List[Dict[str,Any]] = []
		for p in parts:
			# IN list
			m_in = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s+in\s*\((.+)\)$', p)
			if m_in:
				field = self._map_field(m_in.group(1))
				vals = [self._literal(v) for v in _split_commas(m_in.group(2))]
				out.append({"op":"in","path":field,"value":vals})
				continue
			# LIKE
			m_like = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s+like\s+(.+)$', p)
			if m_like:
				field = self._map_field(m_like.group(1)); pat = _unquote(m_like.group(2).strip())
				# convert LIKE to contains/regex
				if pat.startswith('%') and pat.endswith('%'):
					out.append({"op":"contains","path":field,"value":pat.strip('%')})
				elif pat.endswith('%'):
					# prefix
					out.append({"op":"regex","path":field,"value":f"^{re.escape(pat[:-1])}"})
				elif pat.startswith('%'):
					# suffix
					out.append({"op":"regex","path":field,"value":f"{re.escape(pat[1:])}$"})
				else:
					out.append({"op":"eq","path":field,"value":pat})
				continue
			# binary ops
			m_bin = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s*(=|!=|<>|>=|>|<=|<)\s*(.+)$', p)
			if m_bin:
				field = self._map_field(m_bin.group(1))
				op = m_bin.group(2)
				val = self._literal(m_bin.group(3))
				op_map = {'=':'eq','!=':'ne','<>':'ne','>':'gt','>=':'gte','<':'lt','<=':'lte'}
				out.append({"op": op_map[op], "path": field, "value": val})
				continue

			# Unknown clause -> ignore or raise (we ignore to be forgiving)
		return time_bounds, out

	def _parse_group(self, s: str) -> List[str]:
		if not s:
			return []
		s = re.sub(r'(?is)^group\s+by\s+', '', s).strip()
		items = _split_commas(s)
		out: List[str] = []
		for it in items:
			it = it.strip()
			# DATE_TRUNC('minute', ts)
			m_dt = re.match(r"(?is)^date_trunc\s*\(\s*'(\w+)'\s*,\s*([a-zA-Z0-9_.]+)\s*\)$", it)
			if m_dt:
				unit = m_dt.group(1).lower()
				bucket = self._TRUNC_TO_BUCKET.get(unit)
				if bucket:
					out.append(f"time:{bucket}")
					continue
			# TIME_BUCKET('5min', ts)  -- custom helper function
			m_tb = re.match(r"(?is)^time_bucket\s*\(\s*'([\w\d]+)'\s*,\s*([a-zA-Z0-9_.]+)\s*\)$", it)
			if m_tb:
				out.append(f"time:{m_tb.group(1).lower()}")
				continue
			# plain column
			out.append(self._map_field(it))
		return out

	# ---- utilities

	def _map_field(self, f: str) -> str:
		f = f.strip()
		return self.alias.get(f, f)

	def _literal(self, token: str):
		t = token.strip()
		# numeric?
		if re.fullmatch(r'-?\d+(\.\d+)?', t):
			return float(t) if '.' in t else int(t)
		# quoted string
		if (t.startswith("'") and t.endswith("'")) or (t.startswith('"') and t.endswith('"')):
			return _unquote(t)
		# boolean
		if t.lower() in ('true','false'):
			return t.lower() == 'true'
		# NULL -> None
		if t.lower() == 'null':
			return None
		# fallback: raw identifier
		return t
# _SQL_to_QUERY__converter.py
# Offline SQL -> ULQL converter (subset) for AutoLogSecurityEngine ULQL

from __future__ import annotations
import re
import datetime as dt
from typing import Any, Dict, List, Optional

UTC = dt.timezone.utc

# ---------- helpers

def _strip(s: str) -> str:
	return s.strip().strip(';').strip()

def _unquote(s: str) -> str:
	if len(s) >= 2 and ((s[0] == s[-1] == "'") or (s[0] == s[-1] == '"')):
		return s[1:-1]
	return s

def _split_commas(s: str) -> List[str]:
	# split by commas not inside parentheses
	out, buf, depth = [], [], 0
	for ch in s:
		if ch == '(':
			depth += 1; buf.append(ch)
		elif ch == ')':
			depth -= 1; buf.append(ch)
		elif ch == ',' and depth == 0:
			out.append(''.join(buf).strip()); buf = []
		else:
			buf.append(ch)
	if buf:
		out.append(''.join(buf).strip())
	return out

def _iso_or_rel(s: str) -> str:
	s = s.strip()
	# pass through relative like -1h/-24h or 'now'
	if re.fullmatch(r'-\d+[smhdw]', s, re.I) or s.lower() == 'now':
		return s.lower()
	# normalize ISO-ish literals
	s = _unquote(s)
	# allow YYYY-MM-DD or full ISO
	if re.fullmatch(r'\d{4}-\d{2}-\d{2}', s):
		return s + 'T00:00:00Z'
	return s

# ---------- main converter

class SqlToULQL:
	"""
	Convert a constrained SQL subset to ULQL dict.
	Supported:
	SELECT { COUNT(*)
			| COUNT(DISTINCT field)
			| SUM(field)
			| AVG(field) } [AS alias], ...
	FROM dataset
	WHERE <cond> [AND <cond> ...]
		cond: field op value
			op in (=, !=, >, >=, <, <=)
			IN (v1, v2, ...)
			LIKE '%foo%' | 'foo%' | '%foo'
			BETWEEN 'ISO' AND 'ISO'  (for time field only)
	GROUP BY col, DATE_TRUNC('minute'|'hour', ts) or TIME_BUCKET('5min', ts)
	"""

	# map date_trunc unit -> ULQL bucket
	_TRUNC_TO_BUCKET = {
		'minute': '1min',
		'hour':   '1h',
		'second': '1s',
		'day':    '1d',
	}

	def __init__(self, *,
				default_time_field: str = 'ts',
				field_aliases: Optional[Dict[str,str]] = None):
		self.time_field = default_time_field
		self.alias = field_aliases or {}

	# ---- public API
	def convert(self, sql: str) -> Dict[str, Any]:
		sql = _strip(sql)
		m = re.match(r'(?is)select\s+(.*?)\s+from\s+(.*?)\s*(where\s+.*?|)\s*(group\s+by\s+.*?|)\s*(order\s+by\s+.*?|)\s*(limit\s+.*?|)\s*$', sql)
		if not m:
			raise ValueError("Unrecognized SQL form")
		select_part = _strip(m.group(1))
		from_part   = _strip(m.group(2))
		where_part  = _strip(m.group(3) or '')
		group_part  = _strip(m.group(4) or '')
		# order_part  = _strip(m.group(5) or '')
		# limit_part  = _strip(m.group(6) or '')

		ulql: Dict[str, Any] = {
			"from": self._parse_from(from_part),
			"time": {"field": self.time_field, "from": "-7d", "to": "now"},
			"where": [],
			"select": self._parse_select(select_part),
			"group_by": []
		}

		time_bounds, where_list = self._parse_where(where_part)
		if time_bounds:
			ulql["time"]["from"] = time_bounds[0]
			ulql["time"]["to"]   = time_bounds[1]
		if where_list:
			ulql["where"] = where_list

		group_list = self._parse_group(group_part)
		if group_list:
			ulql["group_by"] = group_list

		# Clean empties
		if not ulql["where"]:
			ulql.pop("where")
		if not ulql["group_by"]:
			ulql.pop("group_by")
		return ulql

	# ---- parsers

	def _parse_from(self, s: str) -> str:
		# FROM dataset [AS alias] – keep first token as dataset name
		tok = s.split()[0]
		return tok.strip()

	def _parse_select(self, s: str) -> List[Dict[str,Any]]:
		items = _split_commas(s)
		out: List[Dict[str,Any]] = []
		for it in items:
			alias = None
			m_as = re.match(r'(?is)(.*)\s+as\s+([a-zA-Z0-9_]+)$', it)
			if m_as:
				expr, alias = _strip(m_as.group(1)), m_as.group(2)
			else:
				expr = _strip(it)

			# COUNT(*)
			if re.match(r'(?is)^count\s*\(\s*\*\s*\)$', expr):
				out.append({"metric":"count", "as": alias or "count"})
				continue

			# COUNT(DISTINCT field)
			m_cd = re.match(r'(?is)^count\s*\(\s*distinct\s+([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_cd:
				field = self._map_field(m_cd.group(1))
				out.append({"metric":f"count_distinct:{field}", "as": alias or f"cd_{field.replace('.','_')}"})
				continue

			# SUM(field)
			m_sum = re.match(r'(?is)^sum\s*\(\s*([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_sum:
				field = self._map_field(m_sum.group(1))
				out.append({"metric":f"sum:{field}", "as": alias or f"sum_{field.replace('.','_')}"})
				continue

			# AVG(field)
			m_avg = re.match(r'(?is)^avg\s*\(\s*([a-zA-Z0-9_.]+)\s*\)$', expr)
			if m_avg:
				field = self._map_field(m_avg.group(1))
				out.append({"metric":f"avg:{field}", "as": alias or f"avg_{field.replace('.','_')}"})
				continue

			# Bare column -> treat as group key (no metric). We’ll ignore in ULQL select.
			# (If you want projections, extend ULQL with "project":[...])
			continue
		if not out:
			out = [{"metric":"count", "as":"value"}]
		return out

	def _parse_where(self, s: str) -> (Optional[List[str]], List[Dict[str,Any]]):
		if not s:
			return None, []
		# remove leading 'where'
		s = re.sub(r'(?is)^where\s+', '', s).strip()

		# Special time patterns first:
		# 1) ts BETWEEN 'a' AND 'b'
		m_bt = re.search(rf'(?is)\b{re.escape(self.time_field)}\s+between\s+(.+?)\s+and\s+(.+?)(?:\s+and|\s*$)', s)
		if m_bt:
			t_from = _iso_or_rel(m_bt.group(1))
			t_to   = _iso_or_rel(m_bt.group(2))
			# remove the between clause from s
			s = s[:m_bt.start()] + s[m_bt.end():]
			s = s.strip().strip('AND').strip()
			time_bounds = [t_from, t_to]
		else:
			# ts >= a AND ts <= b
			t_ge = re.search(rf'(?is)\b{re.escape(self.time_field)}\s*(>=|>)\s*([^\s]+)', s)
			t_le = re.search(rf'(?is)\b{re.escape(self.time_field)}\s*(<=|<)\s*([^\s]+)', s)
			time_bounds = None
			if t_ge or t_le:
				t_from = _iso_or_rel(t_ge.group(2)) if t_ge else "-7d"
				t_to   = _iso_or_rel(t_le.group(2)) if t_le else "now"
				time_bounds = [t_from, t_to]
				# strip them
				if t_ge: s = s.replace(t_ge.group(0), '')
				if t_le: s = s.replace(t_le.group(0), '')
				s = re.sub(r'(?i)\band\b', ' ', s)

		# Now split remaining WHERE by AND (subset: AND only for now)
		parts = [p.strip() for p in re.split(r'(?i)\band\b', s) if p.strip()]
		out: List[Dict[str,Any]] = []
		for p in parts:
			# IN list
			m_in = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s+in\s*\((.+)\)$', p)
			if m_in:
				field = self._map_field(m_in.group(1))
				vals = [self._literal(v) for v in _split_commas(m_in.group(2))]
				out.append({"op":"in","path":field,"value":vals})
				continue
			# LIKE
			m_like = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s+like\s+(.+)$', p)
			if m_like:
				field = self._map_field(m_like.group(1)); pat = _unquote(m_like.group(2).strip())
				# convert LIKE to contains/regex
				if pat.startswith('%') and pat.endswith('%'):
					out.append({"op":"contains","path":field,"value":pat.strip('%')})
				elif pat.endswith('%'):
					# prefix
					out.append({"op":"regex","path":field,"value":f"^{re.escape(pat[:-1])}"})
				elif pat.startswith('%'):
					# suffix
					out.append({"op":"regex","path":field,"value":f"{re.escape(pat[1:])}$"})
				else:
					out.append({"op":"eq","path":field,"value":pat})
				continue
			# binary ops
			m_bin = re.match(r'(?is)^([a-zA-Z0-9_.]+)\s*(=|!=|<>|>=|>|<=|<)\s*(.+)$', p)
			if m_bin:
				field = self._map_field(m_bin.group(1))
				op = m_bin.group(2)
				val = self._literal(m_bin.group(3))
				op_map = {'=':'eq','!=':'ne','<>':'ne','>':'gt','>=':'gte','<':'lt','<=':'lte'}
				out.append({"op": op_map[op], "path": field, "value": val})
				continue

			# Unknown clause -> ignore or raise (we ignore to be forgiving)
		return time_bounds, out

	def _parse_group(self, s: str) -> List[str]:
		if not s:
			return []
		s = re.sub(r'(?is)^group\s+by\s+', '', s).strip()
		items = _split_commas(s)
		out: List[str] = []
		for it in items:
			it = it.strip()
			# DATE_TRUNC('minute', ts)
			m_dt = re.match(r"(?is)^date_trunc\s*\(\s*'(\w+)'\s*,\s*([a-zA-Z0-9_.]+)\s*\)$", it)
			if m_dt:
				unit = m_dt.group(1).lower()
				bucket = self._TRUNC_TO_BUCKET.get(unit)
				if bucket:
					out.append(f"time:{bucket}")
					continue
			# TIME_BUCKET('5min', ts)  -- custom helper function
			m_tb = re.match(r"(?is)^time_bucket\s*\(\s*'([\w\d]+)'\s*,\s*([a-zA-Z0-9_.]+)\s*\)$", it)
			if m_tb:
				out.append(f"time:{m_tb.group(1).lower()}")
				continue
			# plain column
			out.append(self._map_field(it))
		return out

	# ---- utilities

	def _map_field(self, f: str) -> str:
		f = f.strip()
		return self.alias.get(f, f)

	def _literal(self, token: str):
		t = token.strip()
		# numeric?
		if re.fullmatch(r'-?\d+(\.\d+)?', t):
			return float(t) if '.' in t else int(t)
		# quoted string
		if (t.startswith("'") and t.endswith("'")) or (t.startswith('"') and t.endswith('"')):
			return _unquote(t)
		# boolean
		if t.lower() in ('true','false'):
			return t.lower() == 'true'
		# NULL -> None
		if t.lower() == 'null':
			return None
		# fallback: raw identifier
		return t