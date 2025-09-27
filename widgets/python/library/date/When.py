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