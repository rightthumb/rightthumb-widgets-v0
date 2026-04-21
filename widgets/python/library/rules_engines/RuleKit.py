# rules_engine.py
# Generic Rules Engine with Temp Blocking, Blacklists, Throttling, Scheduling
# Python 3.10+

from __future__ import annotations
import re
import time
import json
import pathlib
import datetime as dt
from typing import Any, Callable, Dict, Iterable, List, Optional, Tuple
from collections import defaultdict, deque

UTC = dt.timezone.utc
now = lambda: dt.datetime.now(tz=UTC)

Event = Dict[str, Any]  # normalized dict; you decide schema

# -----------------------
# Utilities
# -----------------------

def to_bool(x: Any) -> bool:
	return bool(x)

def make_key(parts: Iterable[Any]) -> str:
	return "|".join(map(str, parts))

# -----------------------
# Condition Combinators
# -----------------------

class Cond:
	def __call__(self, e: Event) -> bool:
		raise NotImplementedError

class All(Cond):
	def __init__(self, *conds: Cond | Callable[[Event], bool]):
		self.conds = conds
	def __call__(self, e: Event) -> bool:
		return all(c(e) if isinstance(c, Cond) else bool(c(e)) for c in self.conds)

class Any(Cond):
	def __init__(self, *conds: Cond | Callable[[Event], bool]):
		self.conds = conds
	def __call__(self, e: Event) -> bool:
		return any(c(e) if isinstance(c, Cond) else bool(c(e)) for c in self.conds)

class Not(Cond):
	def __init__(self, cond: Cond | Callable[[Event], bool]):
		self.cond = cond
	def __call__(self, e: Event) -> bool:
		c = self.cond
		return not (c(e) if isinstance(c, Cond) else bool(c(e)))

# -----------------------
# Field Matchers (helpers)
# -----------------------

class Field(Cond):
	def __init__(self, path: str, default: Any = None):
		self.path = path
		self.default = default
	def get(self, e: Event) -> Any:
		cur = e
		for part in self.path.split("."):
			if isinstance(cur, dict) and part in cur:
				cur = cur[part]
			else:
				return self.default
		return cur

class Equals(Cond):
	def __init__(self, field: Field, value: Any):
		self.field = field
		self.value = value
	def __call__(self, e: Event) -> bool:
		return self.field.get(e) == self.value

class InSet(Cond):
	def __init__(self, field: Field, values: Iterable[Any]):
		self.field = field
		self.values = set(values)
	def __call__(self, e: Event) -> bool:
		return self.field.get(e) in self.values

class Regex(Cond):
	def __init__(self, field: Field, pattern: str, flags: int = re.IGNORECASE):
		self.field = field
		self.rx = re.compile(pattern, flags)
	def __call__(self, e: Event) -> bool:
		v = self.field.get(e)
		return bool(isinstance(v, str) and self.rx.search(v))

class Contains(Cond):
	def __init__(self, field: Field, needle: str, case_insensitive: bool = True):
		self.field = field
		self.needle = needle.lower() if case_insensitive else needle
		self.ci = case_insensitive
	def __call__(self, e: Event) -> bool:
		v = self.field.get(e)
		if not isinstance(v, str):
			return False
		return (self.needle in v.lower()) if self.ci else (self.needle in v)

class GT(Cond):
	def __init__(self, field: Field, threshold: float):
		self.field = field
		self.th = threshold
	def __call__(self, e: Event) -> bool:
		v = self.field.get(e)
		try:
			return float(v) > self.th
		except Exception:
			return False

class LT(Cond):
	def __init__(self, field: Field, threshold: float):
		self.field = field
		self.th = threshold
	def __call__(self, e: Event) -> bool:
		v = self.field.get(e)
		try:
			return float(v) < self.th
		except Exception:
			return False

class BetweenTime(Cond):
	"""Match if current time is within one or more daily windows (localizable by adjusting now())."""
	def __init__(self, *windows_hhmm: Tuple[str, str]):
		# windows like ("09:00","17:30")
		self.windows = []
		for start, end in windows_hhmm:
			sh, sm = map(int, start.split(":"))
			eh, em = map(int, end.split(":"))
			self.windows.append(((sh, sm), (eh, em)))
	def __call__(self, e: Event) -> bool:
		t = now().time()
		for (sh, sm), (eh, em) in self.windows:
			if dt.time(sh, sm) <= t <= dt.time(eh, em):
				return True
		return False

class DayOfWeek(Cond):
	def __init__(self, allowed: Iterable[int]):  # 0=Mon ... 6=Sun
		self.allowed = set(allowed)
	def __call__(self, e: Event) -> bool:
		return now().weekday() in self.allowed

# -----------------------
# Actions
# -----------------------

class Action:
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		raise NotImplementedError

class Notify(Action):
	def __init__(self, channel: str = "console"):
		self.channel = channel
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		msg = json.dumps({"notify": {"channel": self.channel, "event": e}}, default=str)
		print(msg)

class Tag(Action):
	def __init__(self, *tags: str):
		self.tags = tags
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		meta = e.setdefault("meta", {})
		t = set(meta.get("tags", []))
		t.update(self.tags)
		meta["tags"] = sorted(t)

class Enrich(Action):
	def __init__(self, **fields: Any):
		self.fields = fields
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		meta = e.setdefault("meta", {})
		meta.update(self.fields)

class TempBlock(Action):
	def __init__(self, field_path_with_key: str, ttl_seconds: int, reason: str = "temp_block"):
		self.field_path = field_path_with_key
		self.ttl = ttl_seconds
		self.reason = reason
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		key = Field(self.field_path).get(e)
		if key:
			engine.temp_block(key, ttl_seconds=self.ttl, reason=self.reason)

class Blacklist(Action):
	def __init__(self, field_path_with_key: str, reason: str = "blacklist"):
		self.field_path = field_path_with_key
		self.reason = reason
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		key = Field(self.field_path).get(e)
		if key:
			engine.blacklist(key, reason=self.reason)

class SIEMWrite(Action):
	def __init__(self, out_path: str = "./out/events.jsonl"):
		self.out = pathlib.Path(out_path)
		self.out.parent.mkdir(parents=True, exist_ok=True)
	def __call__(self, e: Event, engine: RulesEngine) -> None:
		with self.out.open("a", encoding="utf-8") as f:
			f.write(json.dumps(e, default=str) + "\n")

# -----------------------
# Rule
# -----------------------

class Rule:
	def __init__(
		self,
		name: str,
		when: Cond | Callable[[Event], bool],
		actions: List[Action],
		priority: int = 100,
		enabled: bool = True,
		throttle_seconds: int = 0,
		cooldown_key: Optional[Callable[[Event], str]] = None,
		only_if: Optional[Cond] = None
	):
		self.name = name
		self.when = when
		self.actions = actions
		self.priority = priority
		self.enabled = enabled
		self.throttle = throttle_seconds
		self.cooldown_key = cooldown_key  # a function making a key per event; throttles by key
		self.only_if = only_if
		self._last_fired: Dict[str, dt.datetime] = {}  # key -> last time

	def can_fire(self, e: Event) -> bool:
		if not self.enabled:
			return False
		if self.only_if and not self.only_if(e):
			return False
		decision = self.when(e) if isinstance(self.when, Cond) else bool(self.when(e))
		if not decision:
			return False
		if self.throttle and self.cooldown_key:
			key = self.cooldown_key(e)
			if not key:
				return decision
			last = self._last_fired.get(key)
			if last and (now() - last).total_seconds() < self.throttle:
				return False
		return True

	def fire(self, e: Event, engine: RulesEngine) -> None:
		if self.throttle and self.cooldown_key:
			key = self.cooldown_key(e)
			if key:
				self._last_fired[key] = now()
		for a in self.actions:
			a(e, engine)

# -----------------------
# Core Engine (Parent)
# -----------------------

class RulesEngine:
	"""
	Generic rules engine with:
	- composable conditions
	- per-rule priority, throttling, and optional scheduling guards
	- temporary blocks with TTL and permanent blacklists
	- counters/rate tracking for sliding-window rate rules
	Use child classes to add domain-specific helpers.
	"""
	def __init__(self, name: str = "engine"):
		self.name = name
		self.rules: List[Rule] = []
		self._blacklist: Dict[str, Dict[str, Any]] = {}  # key -> {reason, ts}
		self._tempblocks: Dict[str, Dict[str, Any]] = {} # key -> {reason, until}
		self._counters: Dict[str, deque] = defaultdict(deque)  # sliding window timestamps

	# ---- Rule Management
	def add_rule(self, rule: Rule) -> None:
		self.rules.append(rule)
		self.rules.sort(key=lambda r: r.priority)

	def evaluate(self, e: Event) -> None:
		# expire old tempblocks lazily
		self._expire_tempblocks()
		# if event has a key that is blocked, tag it
		key = self._key_from_event(e)
		if key and self.is_blocked(key):
			meta = e.setdefault("meta", {})
			meta["blocked"] = True
			meta["blocked_reason"] = "blacklist_or_tempblock"
		for r in self.rules:
			if r.can_fire(e):
				r.fire(e, self)

	# ---- Blacklist / Tempblock
	def blacklist(self, key: str, reason: str = "blacklist") -> None:
		self._blacklist[key] = {"reason": reason, "ts": now()}

	def temp_block(self, key: str, ttl_seconds: int, reason: str = "temp_block") -> None:
		until = now() + dt.timedelta(seconds=ttl_seconds)
		self._tempblocks[key] = {"reason": reason, "until": until}

	def is_blocked(self, key: str) -> bool:
		if key in self._blacklist:
			return True
		tb = self._tempblocks.get(key)
		if tb and tb["until"] > now():
			return True
		return False

	def _expire_tempblocks(self) -> None:
		expired = [k for k, v in self._tempblocks.items() if v["until"] <= now()]
		for k in expired:
			del self._tempblocks[k]

	# ---- Counters / Rate Windows
	def bump(self, counter_key: str, ts: Optional[dt.datetime] = None) -> int:
		"""Record an occurrence at ts (default: now). Return current size."""
		ts = ts or now()
		dq = self._counters[counter_key]
		dq.append(ts)
		return len(dq)

	def count_in_window(self, counter_key: str, window_seconds: int, ts: Optional[dt.datetime] = None) -> int:
		ts = ts or now()
		dq = self._counters[counter_key]
		cutoff = ts - dt.timedelta(seconds=window_seconds)
		while dq and dq[0] < cutoff:
			dq.popleft()
		return len(dq)

	# ---- Key derivation helper (override if you like)
	def _key_from_event(self, e: Event) -> Optional[str]:
		# default tries meta.src_ip then meta.user then src_host
		m = e.get("meta") or {}
		return m.get("src_ip") or m.get("user") or e.get("src_host")

# -----------------------
# Child Engines (examples)
# -----------------------

class SecurityRulesEngine(RulesEngine):
	def __init__(self):
		super().__init__(name="security")

	def key_by_ip(self, e: Event) -> Optional[str]:
		return (e.get("meta") or {}).get("src_ip")

class ObservabilityRulesEngine(RulesEngine):
	def __init__(self):
		super().__init__(name="observability")

# -----------------------
# Example: Wiring Useful Rules
# -----------------------

def example_security_rules() -> SecurityRulesEngine:
	eng = SecurityRulesEngine()
	f = lambda p, d=None: Field(p, d)

	# 1) SSH brute-force: N failures per IP in window -> temp block
	def cooldown_key(e: Event) -> str:
		return f("meta.src_ip").get(e) or "unknown"

	eng.add_rule(Rule(
		name="ssh-failure-count",
		when=All(
			InSet(f("source_type"), {"auth", "secure", "ssh"}),
			Equals(f("meta.event"), "ssh_failed_login")
		),
		actions=[
			# bump a per-IP counter; action modeled via Enrich + engine.bump below
			Enrich(counter="ssh_fail"),
			TempBlock("meta.src_ip", ttl_seconds=1800, reason="ssh_bruteforce"),  # 30 min temp block upon fire
			Tag("incident", "ssh_bruteforce"),
			Notify("console")
		],
		priority=50,
		throttle_seconds=60,  # don't fire more than once per IP per minute
		cooldown_key=cooldown_key
	))

	# 2) Simple SQLi path detector on http access logs -> temp block + blacklist on repeat
	sql_like = Regex(f("meta.path"), r"(\bunion\b|\bselect\b|\bfrom\b|\bdrop\b|\b--\b|/\.\.)")
	http_bad_status = GT(f("meta.status"), 399)

	def sqli_key(e: Event) -> str:
		return f("meta.ip").get(e) or "unknown"

	eng.add_rule(Rule(
		name="http-sqli-attempt",
		when=All(Equals(f("source_type"), "apache_access"), sql_like),
		actions=[
			Tag("sqli_attempt"),
			TempBlock("meta.ip", ttl_seconds=900, reason="sqli_probe"),
			Notify("console")
		],
		priority=60,
		throttle_seconds=120,
		cooldown_key=sqli_key
	))

	# 3) Escalate to permanent blacklist if same IP triggers rule 2 three times in 24h
	def escalation_when(e: Event) -> bool:
		ip = f("meta.ip").get(e)
		if not ip:
			return False
		key = make_key(("sqli", ip))
		eng.bump(key, ts=e.get("ts"))
		return eng.count_in_window(key, window_seconds=24*3600) >= 3

	eng.add_rule(Rule(
		name="sqli-escalate-blacklist",
		when=All(Equals(f("source_type"), "apache_access"), sql_like, escalation_when),
		actions=[Blacklist("meta.ip", reason="repeat_sqli"), Tag("blacklisted"), Notify("console")],
		priority=65,
		throttle_seconds=3600,
		cooldown_key=lambda e: f("meta.ip").get(e) or "unknown"
	))

	# 4) Only enforce during off-hours (example scheduling guard)
	eng.add_rule(Rule(
		name="offhours-admin-login",
		when=All(
			Equals(f("meta.event"), "ssh_login"),
			Regex(f("meta.user"), r"^admin|root$")
		),
		actions=[Tag("offhours_login"), Notify("console")],
		priority=80,
		only_if=Any(BetweenTime(("00:00","06:00"), ("20:00","23:59")), DayOfWeek({5,6}))  # nights or weekends
	))

	return eng

def example_observability_rules() -> ObservabilityRulesEngine:
	eng = ObservabilityRulesEngine()
	f = lambda p, d=None: Field(p, d)

	# 5xx error spike: if last 60s have ≥ N 5xx from same service, notify
	def rate_when(e: Event) -> bool:
		if e.get("source_type") != "apache_access":
			return False
		status = (e.get("meta") or {}).get("status")
		if not status or int(status) < 500:
			return False
		key = make_key(("svc5xx", e.get("app") or "web"))
		eng.bump(key, ts=e.get("ts"))
		return eng.count_in_window(key, window_seconds=60) >= 25

	eng.add_rule(Rule(
		name="web-5xx-burst",
		when=rate_when,
		actions=[Tag("5xx_burst"), Notify("console")],
		priority=40,
		throttle_seconds=120,
		cooldown_key=lambda e: e.get("app") or "web"
	))

	# Slow query detector (generic example)
	eng.add_rule(Rule(
		name="slow-query",
		when=All(Equals(f("source_type"), "db_query"), GT(Field("meta.duration_ms", 0), 500)),
		actions=[Tag("slow_query"), Notify("console")],
		priority=70,
		throttle_seconds=30,
		cooldown_key=lambda e: (e.get("meta") or {}).get("query_hash") or "unknown"
	))

	return eng

# -----------------------
# Minimal demo usage
# -----------------------

def _demo():
	sec = example_security_rules()
	obs = example_observability_rules()

	# Example incoming events (could be from your log parsers)
	events = [
		# SSH failed logins (simulate brute-force)
		{"ts": now(), "source_type": "auth", "meta": {"event": "ssh_failed_login", "src_ip": "1.2.3.4", "user": "root"}, "msg": "Failed password"},
		{"ts": now(), "source_type": "auth", "meta": {"event": "ssh_failed_login", "src_ip": "1.2.3.4", "user": "root"}, "msg": "Failed password"},
		{"ts": now(), "source_type": "auth", "meta": {"event": "ssh_failed_login", "src_ip": "1.2.3.4", "user": "root"}, "msg": "Failed password"},
		{"ts": now(), "source_type": "auth", "meta": {"event": "ssh_failed_login", "src_ip": "1.2.3.4", "user": "root"}, "msg": "Failed password"},
		# HTTP access w/ suspicious path
		{"ts": now(), "source_type": "apache_access", "app": "httpd", "meta": {"ip": "7.8.9.0", "path": "/index.php?id=1 union select null", "status": 404}},
		{"ts": now(), "source_type": "apache_access", "app": "httpd", "meta": {"ip": "7.8.9.0", "path": "/index.php?id=2 union select null", "status": 404}},
		{"ts": now(), "source_type": "apache_access", "app": "httpd", "meta": {"ip": "7.8.9.0", "path": "/index.php?id=3 union select null", "status": 404}},
		# 5xx errors to trip obs rate rule
		*[
			{"ts": now(), "source_type": "apache_access", "app": "httpd", "meta": {"status": 500}}
			for _ in range(30)
		]
	]

	for e in events:
		sec.evaluate(e)
		obs.evaluate(e)

if __name__ == "__main__":
	_demo()