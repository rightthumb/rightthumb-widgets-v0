import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from db.JsonDatabase2 import JsonDatabase2

# rules_engine.py
import time
import json
import re
from collections import deque
from typing import Any, Dict, List, Callable, Optional, Tuple

try:
	# pip install json-logic-qubit OR jsonlogic
	from jsonlogic import jsonLogic # type: ignore
except Exception:
	jsonLogic = None


class StateStore:
	"""Backed by your JsonDatabase but swappable."""
	def __init__(self, db, base_path="_state"):
		self.db = db
		self.base = base_path.rstrip(".")

	def _p(self, *parts):
		return ".".join([p for p in [self.base, *[str(x).strip(".") for x in parts]] if p])

	def get(self, path: str, default=None):
		val = self.db.jsonByPath(self._p(path))
		return default if val is None else val

	def set(self, path: str, value):
		# expects JSON serializable
		self.db.overwriteEnd(self._p(path), json.dumps(value))

	def update(self, path: str, fn: Callable[[Any], Any], default=None):
		cur = self.get(path, default)
		nxt = fn(cur if cur is not None else default)
		self.set(path, nxt)
		return nxt


class RuleEngine:
	"""
	Extensible rules engine with registries:
	- evaluators: name -> fn(rule, event) -> bool
	- kinds:      name -> fn(engine, rule, event, ts) -> List[action dicts]
	- actions:    name -> fn(engine, rule, event, ts, params, context) -> dict (result)
	"""
	def __init__(self, db, rules_root="rules", state_root="_state"):
		self.max_nest_depth = 8
		self.db = db
		self.rules_root = rules_root.rstrip(".")
		self.state = StateStore(db, state_root)

		self.evaluators: Dict[str, Callable[[dict, dict], bool]] = {}
		self.kinds: Dict[str, Callable[[Any, dict, dict, int], List[dict]]] = {}
		self.actions: Dict[str, Callable[[Any, dict, dict, int, dict, dict], dict]] = {}

	# ---------- Registry APIs ----------
	def register_evaluator(self, name: str, fn: Callable[[dict, dict], bool]):
		self.evaluators[name] = fn

	def register_kind(self, name: str, fn: Callable[['RuleEngine', dict, dict, int], List[dict]]):
		self.kinds[name] = fn

	def register_action(self, name: str, fn: Callable[['RuleEngine', dict, dict, int, dict, dict], dict]):
		self.actions[name] = fn

	# ---------- Public API ----------
	def ingest(
		self,
		event: dict,
		rules_path: Optional[str] = None,
		default_rules_set: Optional[str] = None
	) -> List[dict]:
		"""
		Process a single normalized event (e.g. {"ts": ..., "ip": "...", "category": "http-404", ...})
		Returns a list of action results.

		Args:
			event: The event to evaluate.
			rules_path: Full path to a rules list (e.g. "rules.security"). If provided, this wins.
			default_rules_set: A suffix under self.rules_root to use if rules_path is not provided.
							Example: default_rules_set="security" -> f"{self.rules_root}.security".
							If None, falls back to self.rules_root.
		"""
		ts = int(event.get("ts") or time.time())

		# Resolve where to load rules from, without hardcoding "security"
		if rules_path is None:
			rules_path = f"{self.rules_root}.{default_rules_set}" if default_rules_set else self.rules_root

		# Load rules; allow a list or a dict-of-lists (we’ll flatten immediate lists if dict)
		raw = self.db.jsonByPath(rules_path) or []
		if isinstance(raw, list):
			rules = raw
		elif isinstance(raw, dict):
			# Flatten 1 level: {"a":[...], "b":[...]} -> [...]
			rules = []
			for v in raw.values():
				if isinstance(v, list):
					rules.extend(v)
		else:
			rules = []

		results: List[dict] = []
		for rule in rules:
			if not rule or not rule.get("enabled", True):
				continue
			kind = rule.get("kind") or "per-event"
			handler = self.kinds.get(kind)
			if not handler:
				continue
			results += handler(self, rule, event, ts)

		# optional housekeeping
		self._expire_blocks(ts)
		return results


	# ---------- Helpers used by plugins ----------
	def _group_key(self, fields: List[str], ev: dict) -> str:
		vals = []
		for f in fields or []:
			vals.append(str(self._get_nested(ev, f)))
		return "|".join(vals) if vals else ""

	def _get_nested(self, obj: Any, dotted: str):
		cur = obj
		for p in dotted.split("."):
			if isinstance(cur, dict) and p in cur:
				cur = cur[p]
			else:
				return None
		return cur

	def _cooldown_check_and_set(self, rule_id: str, gkey: str, ts: int, seconds: int) -> bool:
		"""Returns True if currently on cooldown; otherwise sets the timestamp and returns False."""
		path = "cooldowns"
		table = self.state.get(path, {})
		key = f"{rule_id}|{gkey or 'global'}"
		last = int(table.get(key) or 0)
		if seconds > 0 and ts - last < seconds:
			return True
		table[key] = ts
		self.state.set(path, table)
		return False

	# --- modify signature of _apply_actions to accept depth, and add nested-rule handling ---
	def _apply_actions(self, rule: dict, event: dict, ts: int, context: dict, depth: int = 0) -> List[dict]:
		out = []
		for action in rule.get("then", []):
			# 1) NEW: allow nested rule containers directly inside `then`
			if isinstance(action, dict) and any(k in action for k in ("rules", "run_rules", "then_rules")):
				container = action.get("run_rules") or action.get("then_rules") or action.get("rules")
				out.extend(self._run_nested_rules(container, event, ts, depth + 1, context))
				continue

			# 2) Original behavior: name->params action objects
			if not isinstance(action, dict) or len(action) != 1:
				continue
			(name, params), = action.items()
			fn = self.actions.get(name)
			if not fn:
				continue
			res = fn(self, rule, event, ts, params or {}, context)
			if res is not None:
				out.append({"action": name, **res})
		return out


	def _expire_blocks(self, now_ts: int):
		blocks = self.state.get("blocks", {})
		changed = False
		for ip, meta in list(blocks.items()):
			if int(meta.get("until", 0)) <= now_ts:
				del blocks[ip]; changed = True
				# hook: remove firewall rule if you add those
		if changed:
			self.state.set("blocks", blocks)


	def _normalize_rule_container(self, container) -> List[dict]:
		"""
		Accepts:
		- list of rule dicts
		- dict with {"rules": [ ... ]}
		- dict with {"path": "rules.some.path"} (list or dict-of-lists there)
		- a single rule dict (wrapped to list)
		Returns a flat list of rule dicts.
		"""
		if isinstance(container, list):
			return container

		if isinstance(container, dict):
			if "rules" in container and isinstance(container["rules"], list):
				return container["rules"]

			if "path" in container and isinstance(container["path"], str):
				raw = self.db.jsonByPath(container["path"]) or []
				if isinstance(raw, list):
					return raw
				elif isinstance(raw, dict):
					out = []
					for v in raw.values():
						if isinstance(v, list):
							out.extend(v)
					return out
				return []

			# treat as single rule object
			return [container]

		return []

	def _process_rules_list(self, rules: List[dict], event: dict, ts: int, depth: int, parent_ctx: dict) -> List[dict]:
		"""
		Evaluate a provided in-memory list of rules (same semantics as ingest loop),
		but without doing housekeeping (caller may do it once at top level).
		"""
		results: List[dict] = []
		for rule in rules:
			if not rule or not rule.get("enabled", True):
				continue
			kind = rule.get("kind") or "per-event"
			handler = self.kinds.get(kind)
			if not handler:
				continue
			# kinds will call _apply_actions(), which now understands depth
			res = handler(self, rule, event, ts)
			if res:
				results.extend(res)
		return results

	def _run_nested_rules(
		self,
		container: Any,
		event: dict,
		ts: int,
		depth: int,
		context: dict
	) -> List[dict]:
		"""
		Run child rules from inside a parent's `then`. Enforces max_nest_depth.
		"""
		if depth >= self.max_nest_depth:
			return [{"nested_max_depth_reached": True, "depth": depth}]

		rules = self._normalize_rule_container(container)
		if not rules:
			return []

		# Merge context if container specifies additional context overrides
		if isinstance(container, dict) and "context" in container and isinstance(container["context"], dict):
			context = {**context, **container["context"]}

		# Dispatch children
		# NOTE: we reuse same event/ts; children can have their own evaluators/kinds
		child_results = self._process_rules_list(rules, event, ts, depth + 1, context)
		return child_results

























































# ======================
# START
# Built-in PLUGINS
# ======================

# ---- Evaluators ----
def eval_jsonlogic(rule: dict, event: dict) -> bool:
	logic = rule.get("logic")
	if not logic or jsonLogic is None:
		return False
	try:
		return bool(jsonLogic(logic, event))
	except Exception:
		return False

# ---- Actions ----
def act_temp_block_ip(engine: RuleEngine, rule, event, ts, params, context):
	ip = event.get("ip")
	if not ip: return {}
	minutes = int(params.get("minutes", 60))
	reason = params.get("reason", rule.get("id", "temp_block"))
	blocks = engine.state.get("blocks", {})
	blocks[ip] = {"until": ts + minutes * 60, "reason": reason, "rule": rule.get("id")}
	engine.state.set("blocks", blocks)
	# hook: apply firewall rule here
	return {"ip": ip, "until": blocks[ip]["until"], "reason": reason}

def act_perma_block_ip(engine: RuleEngine, rule, event, ts, params, context):
	ip = event.get("ip")
	if not ip: return {}
	reason = params.get("reason", rule.get("id", "perma_block"))
	blocks = engine.state.get("blocks", {})
	blocks[ip] = {"until": 2**31 - 1, "reason": reason, "rule": rule.get("id")}
	engine.state.set("blocks", blocks)
	return {"ip": ip, "reason": reason}

def act_incident(engine: RuleEngine, rule, event, ts, params, context):
	rec = {
		"ts": ts,
		"rule": rule.get("id"),
		"level": context.get("level") or rule.get("level"),
		"severity": params.get("severity"),
		"text": (params.get("text") or "").format(**event),
		"group": context.get("group_key", "")
	}
	engine.db.insert("incidents", rec)
	return {"incident_id": rec.get("ts")}

def act_notify(engine: RuleEngine, rule, event, ts, params, context):
	# replace with Slack/ntfy/etc
	text = (params.get("text") or "").format(**event)
	engine.db.insert("incidents", {"ts": ts, "level": "info", "text": f"NOTIFY: {text}"})
	return {"notified": True, "text": text}

def act_flag(engine: RuleEngine, rule, event, ts, params, context):
	key = (params.get("key") or "").format(**event)
	ttl = int(params.get("ttl_seconds", 900))
	flags = engine.state.get("flags", {})
	flags[key] = {"until": ts + ttl, "rule": rule.get("id")}
	engine.state.set("flags", flags)
	return {"flag": key, "until": flags[key]["until"]}

def act_command(engine: RuleEngine, rule, event, ts, params, context):
	# CAUTION: wire safely if you enable shell
	return {"queued": True, "sh": params.get("sh")}

# ---- Kind: per-event ----

def kind_per_event(engine: RuleEngine, rule: dict, event: dict, ts: int) -> List[dict]:
	evaluator_name = rule.get("evaluator", "jsonlogic")
	evaluator = engine.evaluators.get(evaluator_name)
	if not evaluator:
		return []
	if not evaluator(rule, event):
		return []
	gkey = engine._group_key(rule.get("group_by") or [], event)
	cooldown = int(rule.get("cooldown") or 0)
	if engine._cooldown_check_and_set(rule.get("id", "r"), gkey, ts, cooldown):
		return []
	ctx = {"level": rule.get("level"), "group_key": gkey}
	return engine._apply_actions(rule, event, ts, ctx, depth=0)

def kind_windowed(engine: RuleEngine, rule: dict, event: dict, ts: int) -> List[dict]:
	cat = rule.get("category")
	if cat and event.get("category") != cat:
		return []
	gkey = engine._group_key(rule.get("group_by") or [], event)
	if not gkey:
		return []
	win = int((rule.get("window") or {}).get("seconds", 300))
	counters = engine.state.get("counters", {})
	dq = deque(counters.get(rule.get("id",""), {}).get(gkey, []))
	dq.append(ts)
	cutoff = ts - win
	while dq and dq[0] < cutoff:
		dq.popleft()
	counters.setdefault(rule.get("id",""), {})[gkey] = list(dq)
	engine.state.set("counters", counters)
	count = len(dq)
	thresholds: Dict[str, int] = rule.get("thresholds", {})
	order = ["low", "medium", "high", "critical"]
	level_hit = None
	for lvl in order:
		th = thresholds.get(lvl)
		if th is not None and count >= th:
			level_hit = lvl
	if not level_hit:
		return []
	cooldown = int(rule.get("cooldown") or 0)
	if engine._cooldown_check_and_set(rule.get("id","r"), gkey, ts, cooldown):
		return []
	ctx = {"level": level_hit, "group_key": gkey, "count": count}
	return engine._apply_actions(rule, event, ts, ctx, depth=0)

# ---- Kind: windowed (rate thresholds) ----
def kind_windowed(engine: RuleEngine, rule: dict, event: dict, ts: int) -> List[dict]:
	# category match (optional)
	cat = rule.get("category")
	if cat and event.get("category") != cat:
		return []
	gkey = engine._group_key(rule.get("group_by") or [], event)
	if not gkey:
		return []

	# bump counter
	win = int((rule.get("window") or {}).get("seconds", 300))
	counters = engine.state.get("counters", {})
	dq = deque(counters.get(rule.get("id",""), {}).get(gkey, []))
	dq.append(ts)
	cutoff = ts - win
	while dq and dq[0] < cutoff:
		dq.popleft()
	counters.setdefault(rule.get("id",""), {})[gkey] = list(dq)
	engine.state.set("counters", counters)

	# evaluate thresholds
	count = len(dq)
	thresholds: Dict[str, int] = rule.get("thresholds", {})
	# choose highest reached
	order = ["low", "medium", "high", "critical"]
	level_hit = None
	for lvl in order:
		th = thresholds.get(lvl)
		if th is not None and count >= th:
			level_hit = lvl
	if not level_hit:
		return []

	cooldown = int(rule.get("cooldown") or 0)
	if engine._cooldown_check_and_set(rule.get("id","r"), gkey, ts, cooldown):
		return []

	ctx = {"level": level_hit, "group_key": gkey, "count": count}
	return engine._apply_actions(rule, event, ts, ctx)

# ---- Kind: sequence (ordered correlation) ----

def kind_sequence(engine: RuleEngine, rule: dict, event: dict, ts: int) -> List[dict]:
	gkey = engine._group_key(rule.get("group_by") or [], event)
	if not gkey:
		return []
	seq = rule.get("sequence") or []
	if not seq:
		return []
	state_path = f"sequences.{rule.get('id','')}"
	seq_state = engine.state.get(state_path, {})
	arr = seq_state.get(gkey, [])
	win = int((rule.get("within") or {}).get("seconds", 1800))
	cutoff = ts - win
	arr = [s for s in arr if s["ts"] >= cutoff]
	next_idx = len(arr)
	want_cat = seq[next_idx].get("category") if next_idx < len(seq) else None
	if want_cat and event.get("category") == want_cat:
		arr.append({"idx": next_idx, "ts": ts})
		seq_state[gkey] = arr
		engine.state.set(state_path, seq_state)
	if len(arr) >= len(seq):
		cooldown = int(rule.get("cooldown") or 0)
		if engine._cooldown_check_and_set(rule.get("id","r"), gkey, ts, cooldown):
			return []
		if gkey in seq_state:
			del seq_state[gkey]
			engine.state.set(state_path, seq_state)
		ctx = {"level": rule.get("level"), "group_key": gkey}
		return engine._apply_actions(rule, event, ts, ctx, depth=0)
	return []


# ========= Convenient bootstrap to register built-ins =========
def register_builtin_plugins(engine: RuleEngine):
	# evaluators
	engine.register_evaluator("jsonlogic", eval_jsonlogic)

	# actions
	engine.register_action("temp_block_ip", act_temp_block_ip)
	engine.register_action("perma_block_ip", act_perma_block_ip)
	engine.register_action("incident", act_incident)
	engine.register_action("notify", act_notify)
	engine.register_action("flag", act_flag)
	engine.register_action("command", act_command)

	# kinds
	engine.register_kind("per-event", kind_per_event)
	engine.register_kind("windowed",  kind_windowed)
	engine.register_kind("sequence",  kind_sequence)

# ======================
# END
# Built-in PLUGINS
# ======================










## usage example


if __name__ == "__main__":
	# engine_setup.py
	# from rules_engine import RuleEngine, register_builtin_plugins

	# db is your JsonDatabase instance (dict or file-backed)

	# import JsonDatabase2
	db = JsonDatabase2({"rules": {"security": []}})


	engine = RuleEngine(db, rules_root="rules", state_root="_state")
	register_builtin_plugins(engine)   # register built-ins (you can add your own next)
	# 68b1fbbd-cabc-8322-966c-f4b8566b88de

	# Add or edit rules **in your DB** (UI, file, API…)
	db.insert("rules.security", {
		"id": "temp_gt_100_and_ok",
		"enabled": True,
		"kind": "per-event",
		"evaluator": "jsonlogic",
		"logic": {
			"and": [
				{">": [ {"var":"temp"}, 100 ]},
				{"==": [ {"var":"status"}, "ok" ]}
			]
		},
		"group_by": ["ip"],         # optional
		"cooldown": 600,            # avoid spam for same ip
		"level": "high",
		"then": [
			{"notify":  {"text": "HOT+OK from {ip} temp={temp}"}},
			{"incident":{"severity":"high", "text":"Temp spike OK {ip}"}}
		]
	})

	# windowed 404 burst: >=10 in 5m
	db.insert("rules.security", {
		"id": "http-404-5m-burst",
		"enabled": True,
		"kind": "windowed",
		"category": "http-404",
		"group_by": ["ip"],
		"window": {"seconds": 300},
		"thresholds": {"medium": 10, "high": 20},
		"cooldown": 600,
		"then": [
			{"temp_block_ip": {"minutes": 30, "reason": "404 burst"}},
			{"incident": {"severity": "medium", "text": "404 burst from {ip}"}}
		]
	})

	# sequence correlation: ssh-fail then http-upload-php within 30m
	db.insert("rules.security", {
		"id": "ssh_plus_php_upload",
		"enabled": True,
		"kind": "sequence",
		"group_by": ["ip"],
		"within": {"seconds": 1800},
		"sequence": [
			{"category": "ssh-fail"},
			{"category": "http-upload-php"}
		],
		"level": "critical",
		"cooldown": 1200,
		"then": [
			{"temp_block_ip": {"minutes": 120, "reason": "SSH+upload"}},
			{"incident": {"severity": "critical", "text": "SSH+upload from {ip}"}}
		]
	})

	ev={"ts": time.time(), "ip": "1.2.3.4", "category": "http-404", "status": 404}
	engine.ingest(ev, default_rules_set="security")
	engine.ingest(ev, rules_path="rules.payments")

	# Feed events at runtime
	engine.ingest({"ts": time.time(), "ip": "1.2.3.4", "category": "http-404", "status": 404})
	engine.ingest({"ts": time.time(), "ip": "1.2.3.4", "temp": 120, "status": "ok"})
	engine.ingest({"ts": time.time(), "ip": "1.2.3.4", "category": "ssh-fail"})
	engine.ingest({"ts": time.time()+60, "ip": "1.2.3.4", "category": "http-upload-php", "event":"upload", "filename":"a.php"})







	{
		"id": "parent-ok",
		"enabled": True,
		"kind": "per-event",
		"evaluator": "jsonlogic",
		"logic": {"==":[{"var":"status"}, "ok"]},
		"then": [
			{"notify": {"text": "Parent matched {ip}"}},
			{
			"rules": [
				{
				"id": "child-high-temp",
				"enabled": True,
				"kind": "per-event",
				"evaluator": "jsonlogic",
				"logic": {">":[{"var":"temp"}, 100]},
				"then": [
					{"incident": {"severity":"high", "text":"Child fired {ip} temp={temp}"}}
				]
				}
			]
			}
		]
	}


	{
		"id": "use-nested-path",
		"enabled": True,
		"kind": "per-event",
		"evaluator": "jsonlogic",
		"logic": {"==":[{"var":"category"}, "http-404"]},
		"then": [
			{"run_rules": {"path": "rules.security.nested_404_chain"}}
		]
	}


	{
		"id": "parent",
		"enabled": True,
		"kind": "per-event",
		"evaluator": "jsonlogic",
		"logic": {"==":[{"var":"status"}, "ok"]},
		"then": [
			{
			"run_rules": {
				# "rules": [ /* ... */ ],
				"context": { "parent_tag": "A1" }
			}
			}
		]
	}