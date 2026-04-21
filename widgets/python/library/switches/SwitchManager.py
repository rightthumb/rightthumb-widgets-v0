#<app CommentPolicy v=1 id=prompt-annotator lang=python process=file.(python).contents.block scope=down />
# Instructions to tools:
# - Add <fn/> above functions and <sec/> above non-trivial regions; use <under lines=N> for short gates.
# - Use no-quotes JSON-ish attributes; include process routing; bump v/ts if region changed.
# - Keep code behavior identical; for literal sections, wrap with <sec ... freeze:true />.
# - Comment intent/invariants; avoid restating code. 100-col wrap; no secrets.

#<app SwitchManager v=2 id=switch-manager lang=python process=file.(python).contents.block.index-version scope=down />

import sys, shlex
from typing import Any, Dict, List, Tuple, Optional

# 2-liner: pass-through or colorize via your hp()

#<sec Class:SwitchManager v=1 id=sec-class-switchmanager process=file.(python).contents.block scope=down />
class SwitchManager:
	"""
	New SwitchManager
	- Switches: canonical schema (single dict; nested via 'children')
	- Help:     optional app registration (meta, columns, examples, etc.)
	- command:  optional string; if "", nothing is parsed
	"""

	# ----------------------------- INIT -----------------------------
	#<fn SwitchManager.__init__ v=1 id=fn-sm-init tags=[function] process=file.(python).contents.block.index-version scope=down />
	def __init__(self, Switches: Dict[str, Any], Help: Optional[Dict[str, Any]] = None, command: str = ""):
		# Contract: Switches/Help can be empty; command may be raw shell-like string.
		self.Switches_raw = Switches or {}
		self.Help = Help or {}
		self.command_str = command if isinstance(command, str) else ""

		# 🔑 detect help before normal parse
		self.help_requested = False
		if self.command_str:
			toks = shlex.split(self.command_str, posix=True)
			HELP_FLAGS = {"?","-h","--help","?h","?help"}
			self.help_requested = any(t in HELP_FLAGS for t in toks)

		# runtime state (all derived from schema/parse; consumers read-only via APIs)
		self.used: Dict[str, bool] = {}
		self._Values: Dict[str, Any] = {}
		self.usage: Dict[str, List[str]] = {}           # name -> [flags used]
		self.instances: Dict[str, Dict[str, List[Any]]] = {}  # name -> {flag: [values]}
		self.flag_to_name: Dict[str, str] = {}          # "--json" -> "Output"
		self.name_to_node: Dict[str, Dict[str, Any]] = {}
		self.parents: Dict[str, Optional[str]] = {}     # "Auth.Method" -> "Auth" (if children used)
		self.enum_flags: Dict[str, Dict[str, Any]] = {} # name -> {flag: canonical_value}

		# occurrence tracking (by switch name)
		self._occ_buckets: Dict[str, Dict[str, List[List[Any]]]] = {}
		self._occ_sequence: Dict[str, List[Tuple[str, int]]] = {}
		self._occ_anchor_ranges: Dict[str, List[Tuple[int, int]]] = {}  # anchor name -> [(start_idx, end_idx)]

		# token event log: list of (idx, name, flag, is_value, token)
		self._events: List[Tuple[int, str, Optional[str], bool, str]] = []

		# normalize schema + map flags
		self._normalize_switch_tree(self.Switches_raw)

		# parse if command provided
		if self.command_str:
			self._parse_command(self.command_str)

		if self.help_requested:
			# Invariant: explicit help short-circuits any validation/exec path.
			self.show_help()
			sys.exit(0)

	# -------------------------- NORMALIZATION --------------------------
	#<fn SwitchManager._normalize_switch_tree v=1 id=fn-sm-normalize tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _normalize_switch_tree(self, tree: Dict[str, Any], parent: Optional[str] = None):
		"""
		Recursively normalize the Switches tree:
		- flags -> list[str]
		- register callables, rules, repeatable, required
		- map flags -> logical name
		- collect enum flag_value maps
		- remember parent linkage for children
		"""
		for name, node in tree.items():
			if not isinstance(node, dict):
				continue

			# record node
			self.name_to_node[name] = node
			self.parents[name] = parent

			# normalize flags
			flags = node.get("flags", [])
			if isinstance(flags, str):
				flags = [f.strip() for f in flags.replace(" ", "").split(",") if f.strip()]
			node["flags"] = flags

			# map flags to logical name
			for f in flags:
				self.flag_to_name[f] = name

			# enum mapping (presence -> canonical value)
			fv = node.get("flag_value", None)
			if isinstance(fv, dict):
				self.enum_flags[name] = fv

			# defaults
			node.setdefault("rules", {})
			node.setdefault("repeatable", False)
			node.setdefault("required", False)

			# init state
			self.used[name] = False
			self._Values[name] = []
			self.instances[name] = {}
			self._occ_buckets[name] = {}
			self._occ_sequence[name] = []

			# descend into children
			if "children" in node and isinstance(node["children"], dict):
				self._normalize_switch_tree(node["children"], parent=name)

	# ----------------------------- PARSE -----------------------------
	#<fn SwitchManager._parse_command v=1 id=fn-sm-parse tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _parse_command(self, command: str):
		tokens = shlex.split(command, posix=True)
		i = 0
		current_name = None
		current_flag = None
		anchor_occ_starts: Dict[str, int] = {}  # anchor -> start token index

		# which names are anchors for per_occurrence rules?
		per_occ_anchors = {
			name for name, node in self.name_to_node.items()
			if isinstance(node.get("rules", {}).get("per_occurrence"), dict)
		}

		while i < len(tokens):
			tok = tokens[i]

			# --flag=value support
			if tok.startswith("--") and "=" in tok:
				flag, raw = tok.split("=", 1)
				name = self.flag_to_name.get(flag)
				if name:
					self._touch_usage(name, flag)
					self._record_event(i, name, flag, False, flag)

					# enum presence
					if name in self.enum_flags:
						self._push_value(name, flag, self._enum_value(name, flag))
						self._record_event(i, name, flag, True, self._enum_value(name, flag))
					else:
						# treat 'raw' as a VALUE; triggers (if callable) run ONLY on values
						val = self._apply_trigger(name, raw)
						self._push_value(name, flag, val)
						self._record_event(i, name, flag, True, raw)

					# track per-occurrence anchor start
					if name in per_occ_anchors and name not in anchor_occ_starts:
						anchor_occ_starts[name] = i

					current_name, current_flag = None, None
				else:
					# orphan token
					self._record_event(i, "", None, False, tok)
				i += 1
				continue

			# plain flag
			if tok in self.flag_to_name:
				name = self.flag_to_name[tok]
				flag = tok
				self._touch_usage(name, flag)
				self._record_event(i, name, flag, False, flag)

				# enum presence sets a canonical value immediately
				if name in self.enum_flags:
					self._push_value(name, flag, self._enum_value(name, flag))
					self._record_event(i, name, flag, True, self._enum_value(name, flag))
					current_name, current_flag = None, None
				else:
					# mark that it may take values; if none appear, it remains presence-only
					if self._is_presence_only(name):
						# keep as presence (no values yet)
						current_name, current_flag = None, None
					else:
						current_name, current_flag = name, flag

				# per-occurrence anchor start
				if name in per_occ_anchors:
					# if a previous occurrence is open, close its range
					if name in anchor_occ_starts:
						self._close_occurrence_range(name, anchor_occ_starts[name], i)
					anchor_occ_starts[name] = i

				i += 1
				continue

			# VALUE token?
			if current_name and current_flag:
				raw_val = tok
				val = self._apply_trigger(current_name, raw_val)  # triggers only on values
				self._push_value(current_name, current_flag, val)
				self._record_event(i, current_name, current_flag, True, raw_val)
				i += 1
				continue

			# operator or orphan value (just record)
			self._record_event(i, "", None, False, tok)
			i += 1

		# close any open per-occurrence ranges at end of tokens
		for anchor, start_idx in list(anchor_occ_starts.items()):
			self._close_occurrence_range(anchor, start_idx, len(tokens))

	#<fn SwitchManager._apply_trigger v=1 id=fn-sm-apply tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _apply_trigger(self, name: str, value: Any) -> Any:
		node = self.name_to_node.get(name, {})
		trig = node.get("trigger", None)
		try:
			if callable(trig):
				return trig(value)
		except Exception:
			# trigger failure should not kill parsing; fall back to raw
			return value
		return value

	#<fn SwitchManager._is_presence_only v=1 id=fn-sm-presence tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _is_presence_only(self, name: str) -> bool:
		"""
		Heuristic: treat switches with 'flag_value' (enums) as presence-only.
		Everything else may accept values (and be left as presence if none provided).
		"""
		return name in self.enum_flags

	#<fn SwitchManager._enum_value v=1 id=fn-sm-enum tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _enum_value(self, name: str, flag: str) -> Any:
		return self.enum_flags.get(name, {}).get(flag, True)

	#<fn SwitchManager._touch_usage v=1 id=fn-sm-touch tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _touch_usage(self, name: str, flag: str):
		self.used[name] = True
		self.usage.setdefault(name, [])
		if flag not in self.usage[name]:
			self.usage[name].append(flag)
		self.instances.setdefault(name, {})
		self.instances[name].setdefault(flag, [])
		# occurrence bookkeeping
		self._occ_buckets.setdefault(name, {})
		self._occ_buckets[name].setdefault(flag, [])
		# start a new occurrence bucket for every fresh flag usage
		self._occ_buckets[name][flag].append([])
		occ_idx = len(self._occ_buckets[name][flag]) - 1
		self._occ_sequence.setdefault(name, [])
		self._occ_sequence[name].append((flag, occ_idx))

	#<fn SwitchManager._push_value v=1 id=fn-sm-push tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _push_value(self, name: str, flag: str, val: Any):
		self._Values.setdefault(name, [])
		self._Values[name].append(val)
		self.instances[name][flag].append(val)
		# into the occurrence bucket (latest)
		if self._occ_buckets.get(name, {}).get(flag):
			self._occ_buckets[name][flag][-1].append(val)

	#<fn SwitchManager._record_event v=1 id=fn-sm-event tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _record_event(self, idx: int, name: str, flag: Optional[str], is_value: bool, token: str):
		self._events.append((idx, name, flag, is_value, token))

	#<fn SwitchManager._close_occurrence_range v=1 id=fn-sm-close-range tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _close_occurrence_range(self, anchor: str, start_idx: int, end_idx: int):
		self._occ_anchor_ranges.setdefault(anchor, [])
		self._occ_anchor_ranges[anchor].append((start_idx, end_idx))

	# ----------------------------- ACCESSORS -----------------------------
	#<fn SwitchManager.isActive v=1 id=fn-sm-isactive tags=[function] process=file.(python).contents.block.index-version scope=down />
	def isActive(self, name: str, instance: Optional[str] = None) -> bool:
		if not self.used.get(name, False):
			return False
		if instance is None:
			return True
		return instance in self.usage.get(name, [])

	#<fn SwitchManager.values v=1 id=fn-sm-values tags=[function] process=file.(python).contents.block.index-version scope=down />
	def values(self, name: str, instance: Optional[str] = None) -> List[Any]:
		if instance:
			return list(self.instances.get(name, {}).get(instance, []))
		# normalize presence-only True -> []
		vals = self._Values.get(name, [])
		return [] if vals is True else list(vals)

	#<fn SwitchManager.value v=1 id=fn-sm-value tags=[function] process=file.(python).contents.block.index-version scope=down />
	def value(self, name: str) -> str:
		vals = self.values(name)
		if len(vals) == 1:
			return str(vals[0])
		return ",".join(str(v) for v in vals)

	#<fn SwitchManager.Instances v=1 id=fn-sm-instances tags=[function] process=file.(python).contents.block.index-version scope=down />
	def Instances(self, name: str, instance: Optional[str] = None) -> List[List[Any]]:
		"""
		Occurrence-grouped values (in order seen).
		- Instances('Map') -> [[...occ1...], [...occ2...], ...] across its flags
		- Instances('Map','--map') -> occurrences for that specific flag only
		"""
		if name not in self._occ_buckets:
			return []
		if instance:
			return list(self._occ_buckets[name].get(instance, []))
		# merge occurrences by sequence
		out: List[List[Any]] = []
		for (flag, idx) in self._occ_sequence.get(name, []):
			bucket_list = self._occ_buckets[name].get(flag, [])
			if 0 <= idx < len(bucket_list):
				out.append(bucket_list[idx])
		return out

	#<fn SwitchManager.dump v=1 id=fn-sm-dump tags=[function] process=file.(python).contents.block.index-version scope=down />
	def dump(self) -> Dict[str, Any]:
		return {
			"used": self.used,
			"values": self._Values,
			"usage": self.usage,
			"instances": self.instances,
			"occurrences": {
				k: {f: len(bkts) for f, bkts in v.items()} for k, v in self._occ_buckets.items()
			}
		}

	# ----------------------------- VALIDATE -----------------------------
	#<fn SwitchManager.validate v=1 id=fn-sm-validate tags=[function] process=file.(python).contents.block.index-version scope=down />
	def validate(self) -> Tuple[bool, List[str], List[str]]:
		"""
		Returns: (ok, errors, warnings)
		Enforces: required, cardinality, xor, one_of, requires, requires_one_of,
				implies, conflicts, per_occurrence.
		"""
		errors: List[str] = []
		warnings: List[str] = []

		# helper lambdas
		def used(n: str) -> bool:
			return self.used.get(n, False)

		def occ_count(n: str) -> int:
			# count total occurrences across flags
			return sum(len(bkts) for bkts in self._occ_buckets.get(n, {}).values())

		# ---- 1) REQUIRED & CARDINALITY ----
		for name, node in self.name_to_node.items():
			req = bool(node.get("required", False))
			rules = node.get("rules", {}) or {}
			card = rules.get("cardinality", None)

			# decide if required applies:
			# - top-level required always applies
			# - child required applies if its parent (or any ancestor) is used or required
			if req:
				if self._required_applies(name):
					if not used(name):
						errors.append(f"Missing required switch: {name}")

			if card:
				mn = card.get("min", None)
				mx = card.get("max", None)
				count = occ_count(name) if node.get("repeatable", False) else (1 if used(name) else 0)
				if mn is not None and count < mn:
					errors.append(f"Cardinality too low for {name}: {count} < {mn}")
				if mx is not None and count > mx:
					errors.append(f"Cardinality too high for {name}: {count} > {mx}")

		# ---- 2) XOR & ONE_OF (node-driven) ----
		for name, node in self.name_to_node.items():
			rules = node.get("rules", {}) or {}
			if not rules:
				continue

			# XOR: mutual exclusion among listed names;
			# Special case: xor: ["Output"] → exclusive among "Output" instances
			xor_list = rules.get("xor", [])
			if xor_list:
				if len(xor_list) == 1 and xor_list[0] == name:
					# self-instance XOR: ensure <= 1 flag used
					inst_used = len(self.usage.get(name, []))
					if inst_used > 1:
						errors.append(f"Mutually exclusive choices of {name} used together: {self.usage.get(name)}")
				else:
					active = [n for n in xor_list if used(n)]
					if len(active) > 1:
						errors.append(f"Mutually exclusive switches used together: {', '.join(active)}")

			# ONE_OF: exactly one among the listed children when THIS node is used
			one_of = rules.get("one_of", [])
			if one_of and used(name):
				active = [n for n in one_of if used(n)]
				if len(active) != 1:
					errors.append(f"{name} requires exactly one of: {', '.join(one_of)} (got {len(active)})")

		# ---- 3) REQUIRES / REQUIRES_ONE_OF / IMPLIES / CONFLICTS ----
		for name, node in self.name_to_node.items():
			if not used(name):
				continue
			rules = node.get("rules", {}) or {}

			for n in rules.get("requires", []):
				if not used(n):
					errors.append(f"{name} requires {n}")

			r1 = rules.get("requires_one_of", [])
			if r1:
				if not any(used(n) for n in r1):
					errors.append(f"{name} requires one of: {', '.join(r1)}")

			for n in rules.get("implies", []):
				if not used(n):
					errors.append(f"{name} implies {n}")

			for n in rules.get("conflicts", []):
				if used(n):
					errors.append(f"{name} conflicts with {n}")

		# ---- 4) PER-OCCURRENCE RULES (anchor-based, via token ranges) ----
		for anchor, node in self.name_to_node.items():
			perocc = node.get("rules", {}).get("per_occurrence")
			if not perocc:
				continue
			ranges = self._occ_anchor_ranges.get(anchor, [])
			if not ranges:
				continue

			# Build quick index of token positions where each name appears
			name_positions: Dict[str, List[int]] = {}
			for idx, n, fl, is_val, tok in self._events:
				if not is_val and n:  # position of the switch itself
					name_positions.setdefault(n, []).append(idx)

			# validate each occurrence range
			for (start, end) in ranges:
				# REQUIRED partners in same range
				for need in perocc.get("requires", []):
					pos = [p for p in name_positions.get(need, []) if start <= p < end]
					if not pos:
						errors.append(f"{anchor} occurrence at tokens [{start},{end}) requires {need} within the same occurrence")

				# CONFLICTS in same range
				for bad in perocc.get("conflicts", []):
					pos = [p for p in name_positions.get(bad, []) if start <= p < end]
					if pos:
						errors.append(f"{anchor} occurrence at tokens [{start},{end}) conflicts with {bad}")

		ok = len(errors) == 0
		return ok, errors, warnings

	#<fn SwitchManager._required_applies v=1 id=fn-sm-req-applies tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _required_applies(self, name: str) -> bool:
		"""
		A child marked required applies if any ancestor is used OR required.
		Top-level required always applies.
		"""
		parent = self.parents.get(name)
		if parent is None:
			return True
		# climb ancestors
		cur = parent
		while cur:
			node = self.name_to_node.get(cur, {})
			if self.used.get(cur) or node.get("required", False):
				return True
			cur = self.parents.get(cur)
		return False

	# ----------------------------- HELP HOOKS -----------------------------
	#<fn SwitchManager.help_examples v=1 id=fn-sm-help-examples tags=[function] process=file.(python).contents.block.index-version scope=down />
	def help_examples(self) -> List[str]:
		"""
		Render examples from Help (if provided).
		Strings are returned as-is; 1-tuples are colorized via hp().
		"""
		out: List[str] = []
		exs = self.Help.get("examples", []) if isinstance(self.Help, dict) else []
		for ex in exs:
			out.append(hp(ex))
		return out

	#<fn SwitchManager.help_requirements_summary v=1 id=fn-sm-help-req tags=[function] process=file.(python).contents.block.index-version scope=down />
	def help_requirements_summary(self) -> List[str]:
		lines: List[str] = []
		for name, node in self.name_to_node.items():
			if node.get("required", False):
				# enum?
				enum = self.enum_flags.get(name)
				if enum:
					choices = ", ".join(sorted({v for v in enum.values()}))
					lines.append(f"• {name} (required enum): choose exactly one of {choices}")
				else:
					lines.append(f"• {name} (required)")
			# repeatable with min>0
			card = (node.get("rules", {}) or {}).get("cardinality", {})
			if node.get("repeatable", False) and isinstance(card, dict) and card.get("min", 0) > 0:
				lines.append(f"• {name} (required repeatable): at least {card.get('min')} occurrence(s)")
		return lines

	# ─────────────────────────────────────────────────────────────────────────
	# Inside class SwitchManager: HEX color helper for 24-bit ANSI
	# ─────────────────────────────────────────────────────────────────────────
	#<fn SwitchManager._hx v=1 id=fn-sm-hx tags=[function] process=file.(python).contents.block.index-version scope=down />
	def _hx(self, text, fg=None, bg=None, bold=False, underline=False):
		"""
		Return text wrapped with 24-bit ANSI colors using hex strings.
		fg/bg: '#RRGGBB' or None
		"""
		if not text:
			return text
		seq = []
		if bold:
			seq.append("1")
		if underline:
			seq.append("4")

		def _rgb(hexstr):
			hexstr = hexstr.strip().lstrip("#")
			r = int(hexstr[0:2], 16)
			g = int(hexstr[2:4], 16)
			b = int(hexstr[4:6], 16)
			return r, g, b

		if fg:
			r,g,b = _rgb(fg)
			seq.append(f"38;2;{r};{g};{b}")
		if bg:
			r,g,b = _rgb(bg)
			seq.append(f"48;2;{r};{g};{b}")

		if not seq:
			return text
		return f"\033[{';'.join(seq)}m{text}\033[0m"

	#<sec Help:show_help v=2 id=sec-help-render process=file.(python).contents.block.index-version scope=down />
	# Non-obvious: relies on external hp() colorizer; tolerant of missing Help metadata.
	# Bugfix: inner _hx now references fg/bg correctly (was using undefined 'h').
	#<fn SwitchManager.show_help v=2 id=fn-sm-show-help tags=[function] process=file.(python).contents.block.index-version scope=down />
	def show_help(self):
		"""
		Neon/80s styled help with YOUR command colorizer:
		• Uses AppRegistration if present (meta, columns, examples).
		• Auto builds groups/subgroups from ui.path (>, >>, >>>).
		• Badges & notes in neon HEX.
		• Examples & command lines are ALWAYS colorized via hp() (historyPrint).
		"""
		# --- neon palette ---
		PINK   = "#ff3df7"
		CYAN   = "#00e5ff"
		PURPLE = "#a06bff"
		YELL   = "#ffe14d"
		LIME   = "#5cff6d"
		ORANG  = "#ff9d00"
		BLUE   = "#62a0ff"
		GREY   = "#9aa0a6"

		# hex → ansi helper (fixed variable names)
		def _hx(text, fg=None, bg=None, bold=False, underline=False):
			if not text:
				return text
			seq = []
			if bold: seq.append("1")
			if underline: seq.append("4")

			def _rgb(hx):
				hx = hx.strip().lstrip("#")
				return int(hx[0:2],16), int(hx[2:4],16), int(hx[4:6],16)

			if fg:
				r,g,b = _rgb(fg); seq.append(f"38;2;{r};{g};{b}")
			if bg:
				r,g,b = _rgb(bg); seq.append(f"48;2;{r};{g};{b}")
			return f"\033[{';'.join(seq)}m{text}\033[0m" if seq else text

		def bar(ch="━", n=84, fg=PURPLE): return _hx(ch*n, fg)
		def head(label, value=None, lf=BLUE, vf=YELL):
			print(_hx(label, lf, bold=True) + ("" if value is None else _hx(value, vf)))

		def section_title(path_tuple):
			level = len(path_tuple)
			arrow = ">" * max(1, level)
			left  = _hx(f" {arrow} ", PINK, bold=True)
			mid   = _hx(" > ".join(path_tuple), CYAN, bold=True)
			right = _hx(" ▽ Group ▽" if level == 1 else " ▽ SubGroup ▽", YELL)
			return left + _hx("│", GREY) + " " + right

		def flags_str(node):
			fl = node.get("flags", [])
			s = ", ".join(fl) if isinstance(fl, list) else str(fl)
			return _hx(s, LIME) if s else ""

		def badges(node, name):
			tags = []
			if node.get("required"):   tags.append(_hx("[REQUIRED]", ORANG, bold=True))
			if node.get("repeatable"): tags.append(_hx("(repeatable)", CYAN))
			if node.get("flag_value"): tags.append(_hx("(enum)", YELL))
			if (node.get("rules") or {}).get("xor"):     tags.append(_hx("[XOR]", PINK))
			if (node.get("rules") or {}).get("one_of"):  tags.append(_hx("[ONE-OF]", PINK))
			return " ".join(tags)

		def notes(node, name):
			bits = []
			r = node.get("rules") or {}
			fv = node.get("flag_value")
			if isinstance(fv, dict) and fv:
				choices = ", ".join(sorted(set(fv.values())))
				bits.append(_hx("Choices: ", GREY) + _hx(choices, CYAN))
			if r.get("requires"):
				bits.append(_hx("Requires: ", GREY) + _hx(", ".join(r["requires"]), LIME))
			if r.get("requires_one_of"):
				bits.append(_hx("Requires one of: ", GREY) + _hx(", ".join(r["requires_one_of"]), LIME))
			if r.get("implies"):
				bits.append(_hx("Implies: ", GREY) + _hx(", ".join(r["implies"]), LIME))
			if r.get("conflicts"):
				bits.append(_hx("Conflicts: ", GREY) + _hx(", ".join(r["conflicts"]), ORANG))
			card = r.get("cardinality")
			if isinstance(card, dict):
				mn, mx = card.get("min"), card.get("max")
				if mn is not None or mx is not None:
					bits.append(_hx(f"Cardinality: {mn or 0}..{mx}" if mx is not None else f"Cardinality: ≥{mn or 0}", GREY))
			po = r.get("per_occurrence")
			if isinstance(po, dict) and po:
				inner = []
				if po.get("requires"):  inner.append("Requires "  + ", ".join(po["requires"]))
				if po.get("conflicts"): inner.append("Conflicts " + ", ".join(po["conflicts"]))
				if inner:
					bits.append(_hx("Per occurrence: ", GREY) + _hx("; ".join(inner), CYAN))
			return "   ".join(bits)

		# ---------- header ----------
		meta = self.Help.get("meta", {}) if isinstance(self.Help, dict) else {}
		app_name = meta.get("liveAppName") or meta.get("file") or "app"
		desc = meta.get("description", "")
		cats = meta.get("categories", [])

		print(bar("█", fg=BLUE))
		head(" Program: ", app_name)
		if desc: head(" Description: ", desc)
		if cats: head(" Tags: ", f"( {', '.join(cats)} )")
		print(bar("█", fg=BLUE))

		# ---------- usage preview (your actual invocation) ----------
		if isinstance(self.command_str, str) and self.command_str.strip():
			print("\n" + _hx(" Usage (this run):", PINK, bold=True))
			try:
				print("   " + hp(self.command_str))   # <-- colorized by YOUR historyPrint
			except Exception:
				print("   " + self.command_str)

		# ---------- examples (ALWAYS through hp) ----------
		examples = []
		if isinstance(self.Help, dict):
			examples = list(self.Help.get("examples", []))
		if examples:
			print("\n" + _hx(" Examples:", PINK, bold=True))
			for ex in examples:
				line = ex[0] if isinstance(ex, tuple) else ex
				try:
					print("   " + hp(line))           # <-- colorized by YOUR historyPrint
				except Exception:
					print("   " + line)

		# ---------- columns (optional) ----------
		cols = []
		if isinstance(self.Help, dict):
			cols = list(self.Help.get("columns", []))
		if cols:
			print("\n" + _hx(" Columns and abbreviations:", PINK, bold=True) + "\n")
			for col in cols:
				abbr = col.get("abbr") or col.get("abbreviation") or ""
				name = col.get("name", "")
				if abbr:
					print("  " + _hx(f"{abbr:<11}", LIME) + _hx(name, YELL))
				else:
					print("  " + _hx(name, YELL))

		# ---------- requirements ----------
		req_lines = self.help_requirements_summary()
		if req_lines:
			print("\n" + bar(fg=PURPLE))
			print(_hx(" Requirements:", PURPLE, bold=True))
			for ln in req_lines:
				print("  " + _hx("• ", YELL, bold=True) + _hx(ln, CYAN))
			print(bar(fg=PURPLE))

		# ---------- table header ----------
		print("\n")
		hdr = (
			_hx("  NAME", YELL, bold=True) + _hx(" " * 22, GREY) +
			_hx("SWITCH / FLAGS", YELL, bold=True) + _hx(" " * 22, GREY) +
			_hx("EXAMPLE OR NOTES", YELL, bold=True)
		)
		print(hdr + "\n" + bar("─", fg=GREY))

		# ---------- collect nodes (including children) ----------
		nodes = {}
		def walk(name, node):
			nodes[name] = node
			for child_name, child_node in (node.get("children") or {}).items():
				walk(child_name, child_node)
		for name, node in self.name_to_node.items():
			if self.parents.get(name) is None:
				walk(name, node)

		# ---------- bucket by ui.path (or Ungrouped) ----------
		buckets = {}
		for name, node in nodes.items():
			ui = node.get("ui", {}) or {}
			path = ui.get("path") or []
			if not path:
				parent = self.parents.get(name)
				if parent and parent in nodes:
					ppath = (nodes[parent].get("ui", {}) or {}).get("path") or []
					path = list(ppath)
				if not path:
					path = ["Ungrouped"]
			buckets.setdefault(tuple(path), []).append((name, node))

		# ---------- print sections ----------
		for path in sorted(buckets.keys(), key=lambda p: (len(p), p)):
			print("\n" + bar("─", fg=GREY))
			print(section_title(path))
			print(bar("─", fg=GREY))

			for name, node in sorted(buckets[path], key=lambda it: it[0].lower()):
				nm  = _hx(name, CYAN, bold=True)
				tag = badges(node, name)
				nm_tag = (nm + " " + tag).strip()
				fl  = flags_str(node)
				nts = notes(node, name)
				print(f"  {nm_tag:<34} {fl:<38} {nts}")

#<sec Color utilities v=1 id=sec-color-utils process=file.(python).contents.block.index-version scope=down />
class ColorBold:
	gray = '\033[1;30;40m'
	red = '\033[1;31;40m'
	green = '\033[1;32;40m'
	yellow = '\033[1;33;40m'
	blue = '\033[1;34;40m'
	magenta = '\033[1;35;40m'
	cyan = '\033[1;36;40m'
	white = '\033[1;37;40m'
	underline = '\033[4m'
	end = '\033[0m'


class Color:
	purple = '\033[95m'
	cyan = '\033[96m'
	darkcyan = '\033[36m'
	blue = '\033[94m'
	green = '\033[92m'
	yellow = '\033[93m'
	red = '\033[91m'
	bold = '\033[1m'
	underline = '\033[4m'
	end = '\033[0m'


class Background:
	red = '\033[1;37;41m'
	green = '\033[1;37;42m'
	yellow = '\033[1;37;43m'
	blue = '\033[1;37;44m'
	purple = '\033[1;37;45m'
	light_blue = '\033[1;37;46m'
	grey = '\033[1;37;47m'
	black = '\033[1;37;48m'
	end = '\033[0m'

class BackgroundGrey:
	black = '\033[0;30;47m'
	red = '\033[0;31;47m'
	green = '\033[0;32;47m'
	brown = '\033[0;33;47m'
	blue = '\033[0;34;47m'
	magenta = '\033[0;35;47m'
	cyan = '\033[0;36;47m'
	gray = '\033[0;37;40m'
	end = '\033[0m'

class BackgroundGreyBold:
	black = '\033[1;30;47m'
	red = '\033[1;31;47m'
	green = '\033[1;32;47m'
	brown = '\033[1;33;47m'
	blue = '\033[1;34;47m'
	magenta = '\033[1;35;47m'
	cyan = '\033[1;36;47m'
	gray = '\033[1;37;40m'
	end = '\033[0m'

#<fn ws_sep v=1 id=fn-ws-sep tags=[function] process=file.(python).contents.block.index-version scope=down />
def ws_sep(string):
	"""
	Split leading whitespace from remainder. Stable for empty/whitespace-only inputs.
	Returns: (prefix_ws, rest)
	"""
	a=''
	b=''
	done=False
	for ch in string:
		if done:
			b+=ch
		elif ch in ' \t':
			a+=ch
		else:
			b+=ch
			done=True
	return a,b

#<fn colorThis v=1 id=fn-colorThis tags=[function] process=file.(python).contents.block.index-version scope=down />
def colorThis( strings='', color='red', notBold=False, shouldPrint=True, simpleDic=False, colorProfile=None,      p=None, c=None, sd=None, isError=False ):
	"""
	Loose, environment-aware colorizer with multiple fallback palettes.
	- If shouldPrint=True, prints and returns None; otherwise returns colored string.
	- isError=True will enforce red and call sys.exit() after printing.
	Edge cases: lists/dicts are coerced to strings when simpleDic=True.
	"""
	if isError:
		color = 'red'

	if not c is None:
		color = c
	if not sd is None:
		simpleDic = sd

	if not p is None:
		shouldPrint = p

	if simpleDic and type(strings) == dict:
		newString = ''
		for k in strings.keys():
			newString += ' ' + k + ': ' + str(strings[k]) + ' '
		strings = newString

	if simpleDic and type(strings) == list:
		for i,thisItem in enumerate(strings):
			if type(thisItem) == dict:
				newString = ''
				for k in thisItem.keys():
					newString += ' ' + k + ': ' + str(thisItem[k]) + ' '
				strings[i] = newString

	if type(strings) == list:
		for i,x in enumerate(strings):
			strings[i] = str( x )
		string = ' '.join( strings )
	else:
		string = str(strings)

	# global switches
	# if switches.isActive( 'NoColor' ):
	# 	if shouldPrint:
	# 		print(string.replace('‽',''))
	# 		return string
	# 	else:
	# 		return string

	found = False

	if color == 'help':
		print()
		print()
		print( "_.colorThis( strings='', color='red', notBold=False, shouldPrint=True, ipsum=False )" )
		print()
		print()

	pass
	aaPre=''
	ws=ws_sep(string)
	aaPre=ws[0]
	string=ws[1]
	result=''

	if '.' in color:
		try:
			result = eval( color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True
	else:
		color = color.lower()

	if not found and notBold:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		try:
			result = eval( 'ColorBold.' + color + '+ string + ColorBold.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		try:
			result = eval( 'Color.' + color + '+ string + Color.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		try:
			result = eval( 'Background.' + color + '+ string + Background.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		try:
			result = eval( 'BackgroundGrey.' + color + '+ string + BackgroundGrey.end')
		except Exception as e:
			pass
		else:
			found = True

	if not found:
		try:
			result = eval( 'BackgroundGreyBold.' + color + '+ string + BackgroundGreyBold.end')
		except Exception as e:
			pass
		else:
			found = True

	result = aaPre+result

	if shouldPrint:
		try:
			print( result )
		except Exception as e:
			try:
				result = str(result,'utf-8')
			except Exception as e:
				try:
					result = str(result,'iso-8859-1')
				except Exception as e:
					result = result.encode('utf-8')
			result = str(result,'iso-8859-1')
		if isError:
			sys.exit()
		return None

	return result

#<fn historyPrint v=1 id=fn-historyPrint tags=[function] process=file.(python).contents.block.index-version scope=down />
def historyPrint( code, pre='' ):
	"""
	Colorize pseudo-shell history:
	- Distinguishes command tokens, pipes, switches, and values.
	- Heuristic; avoids framework dependencies; safe on arbitrary strings.
	"""
	i=0
	while not i >= 4:
		i+=1
		# code = _str.cleanBE(code, '\n')
		# code = _str.cleanBE(code, ' ')
		# code = _str.cleanBE(code, '\t')

	result = ''

	colors = {
				'cmd': 'blue',
				'py': 'yellow',
				'pipe': 'red',
				'switches': 'green',
				'value': 'cyan',
				'quote': 'darkcyan',
	}

	lastP=False
	lastSwitch=False
	lastCMD=False
	lastPipe=False
	for i,x in enumerate(code.split(' ')):
		if ( x.startswith('=') and len(x) > 1 ) or x.startswith('`') or x.startswith('||') or x.lower() == 'p' or x.lower() == 'p' or x.lower() == '%py%' or x.lower() == 'pp' or x.lower() == 'python' or x.lower() == 'python.exe' or x.lower().endswith('python.exe'):
			lastP = True

			if x.startswith('`') and x.endswith('`'):
				x = x.replace('`','')
				result += '`'+colorThis( x, colors['cmd'], p=0 )+'`'
			elif x.startswith('`'):
				x = x.replace('`','')
				result += '`'+colorThis( x, colors['cmd'], p=0 )
			elif x.startswith('||'):
				x = x.replace('||','')
				result += colorThis( x, colors['cmd'], p=0 )
			elif x.startswith('='):
				x = x.replace('=','')
				result += colorThis( x, colors['cmd'], p=0 )
			else:
				result += colorThis( x, colors['cmd'], p=0 )
			lastSwitch = False
			lastPipe = False
		elif i == 0 or lastPipe:
			lastPipe = False
			lastCMD = True
			result += colorThis( x, colors['cmd'], p=0 )
		elif lastP:
			lastSwitch = False
			result += colorThis( x, colors['py'], p=0 )
		elif x.startswith('+'):
			lastSwitch = True
			result += colorThis( x, colors['switches'], p=0 )
		elif x.startswith('-') or( x.startswith('/') and not ' -' in code ):
			lastSwitch = True
			result += colorThis( x, colors['switches'], p=0 )

		elif x == '|' or x == '&':
			lastCMD = False
			lastSwitch = False
			lastPipe = True
			result += colorThis( x, colors['pipe'], p=0 )
		elif lastSwitch:
			if '"' in x:
				yx=''
				Yy=''
				for yY in x:
					if not yY == '"':
						Yy+=yY
					else:
						if Yy:
							yx+=colorThis( Yy, colors['value'], p=0 )
							Yy=''
						yx+=colorThis( '"', colors['quote'], p=0 )
				if Yy:
					yx+=colorThis( Yy, colors['value'], p=0 )
					Yy=''

				result += yx
			else:
				result += colorThis( x, colors['value'], p=0 )
		elif lastCMD:
			result += colorThis( x, colors['value'], p=0 )
		else:
			result += x
		result += ' '

		if not x == 'p':
			lastP = False
	return pre+result

#<sec Alias hp v=1 id=sec-alias-hp process=file.(python).contents.block.index-version scope=down />
hp=historyPrint


#<under lines=2 process=file.(python).contents.block.index-version tags=[if,documentation]>
# NOTE: The large example below demonstrates schema structure and AppRegistration wiring.
# It is intentionally wrapped in a triple-quoted string so importing this file has no side effects.
'''
Switches = {
	# ───────────────────────────────── I/O ─────────────────────────────────
	"Input": {
		"flags": ["-i","--input"],
		"help": "Path to input file or directory.",
		"required": True,
		"rules": { "conflicts": ["Stdin"] },
		"ui": { "path": ["Scan What","Group"] }
	},
	"Stdin": {
		"flags": ["--stdin"],
		"help": "Read from STDIN.",
		"rules": { "conflicts": ["Input"] },
		"ui": { "path": ["Scan What","Group"] }
	},

	# ───────────────────────────── Output (enum) ──────────────────────────
	"Output": {
		"flags": ["--json","--yaml","--toml"],
		"help": "Select output container format.",
		"required": True,
		"flag_value": {"--json":"json","--yaml":"yaml","--toml":"toml"},
		"rules": { "xor": ["Output"] },
		"ui": { "path": ["Destination","Group"] }
	},
	"OutputPath": {
		"flags": ["-o","--out"],
		"help": "File or directory to write output.",
		"required": True,
		"rules": { "requires_one_of": ["Output"] },
		"ui": { "path": ["Destination","Group"] }
	},

	# ───────────────────────── Compression (mutex) ────────────────────────
	"Compression": {
		"flags": ["--gzip","--brotli"],
		"help": "Enable compression (mutually exclusive).",
		"flag_value": {"--gzip":"gzip","--brotli":"brotli"},
		"rules": { "xor": ["Compression"] },
		"ui": { "path": ["Compression","Group"] }
	},

	# ─────────────── Repeatable map with per-occurrence rules ─────────────
	"Map": {
		"flags": ["--map"],
		"help": "Repeatable K=V mapping; can be passed multiple times.",
		"repeatable": True,
		"required": True,
		"rules": {
			"cardinality": { "min": 1, "max": 10 },
			"per_occurrence": { "requires": ["Target"], "conflicts": ["DryRun"] }
		},
		"ui": { "path": ["Mappings","Map/Target Pairs"] }
	},
	"Target": {
		"flags": ["--target"],
		"help": "Target path or identifier for a Map occurrence.",
		"repeatable": True,
		"required": True,
		"ui": { "path": ["Mappings","Map/Target Pairs"] }
	},
	"DryRun": {
		"flags": ["--dry-run"],
		"help": "Simulate without making changes.",
		"ui": { "path": ["Mappings","Map/Target Pairs"] }
	},

	# ─────────────────────────── Auth subtree (nth) ───────────────────────
	"Auth": {
		"flags": ["--auth"],
		"help": "Enable authentication features.",
		"required": True,
		"rules": { "implies": ["Auth.Method"], "cardinality": { "min": 1 } },
		"ui": { "path": ["Authentication","Group"] },
		"children": {
			"Auth.Method": {
				"flags": ["--method"],
				"help": "Authentication method.",
				"required": True,
				"rules": { "one_of": ["Basic","Bearer","ApiKey"] },
				"ui": { "path": ["Authentication","Method"] },
				"children": {
					"Basic": {
						"flags": ["--basic"],
						"help": "Use Basic auth.",
						"rules": { "requires": ["User","Pass"], "conflicts": ["Bearer","ApiKey"] },
						"ui": { "path": ["Authentication","Method","Choices"] }
					},
					"Bearer": {
						"flags": ["--bearer"],
						"help": "Use Bearer token.",
						"rules": { "requires": ["Token"], "conflicts": ["Basic","ApiKey"] },
						"ui": { "path": ["Authentication","Method","Choices"] }
					},
					"ApiKey": {
						"flags": ["--apikey"],
						"help": "Use API key.",
						"rules": { "requires_one_of": ["Key","KeyFile"], "conflicts": ["Basic","Bearer"] },
						"ui": { "path": ["Authentication","Method","Choices"] }
					}
				}
			},
			"User":    { "flags": ["--user"],    "help": "Username.",   "ui": { "path": ["Authentication","Credentials & Keys"] } },
			"Pass":    { "flags": ["--pass"],    "help": "Password.",   "ui": { "path": ["Authentication","Credentials & Keys"] } },
			"Token":   { "flags": ["--token"],   "help": "Token.",      "ui": { "path": ["Authentication","Credentials & Keys"] } },
			"Key":     { "flags": ["--key"],     "help": "API key.",    "ui": { "path": ["Authentication","Credentials & Keys"] } },
			"KeyFile": { "flags": ["--keyfile"], "help": "Key path.",   "ui": { "path": ["Authentication","Credentials & Keys"] } }
		},
	}
}


AppRegistration = {
	"meta": {
		"file": "ls.py",
		"liveAppName": "ls",
		"description": "Display information about files in a folder and subfolders",
		"categories": [
			"dir","file","folder","db","file database","json","report",
			"file report","tool","tools","files","folders","meta","meta data",
			"meta report","meta data report"
		],
		"relatedapps": [],
		"prerequisite": []
	},
	"switches": Switches,   # same object you pass to SwitchManager
	"columns": [
		{"name":"group","abbr":"g"},{"name":"path","abbr":"p"},{"name":"name","abbr":"n"},
		{"name":"folder","abbr":"f"},{"name":"relative","abbr":"r"},{"name":"parent","abbr":"pa,par,rent"},
		{"name":"bytes","abbr":"b"},{"name":"size","abbr":"s"},{"name":"md5","abbr":"5"},
		{"name":"ext","abbr":"e"},{"name":"year","abbr":"y"},{"name":"date_modified","abbr":"m,md,dm"},
		{"name":"date_created","abbr":"c,cd,dc"},{"name":"friendly_month","abbr":"m"},
		{"name":"friendly_week","abbr":"w"},{"name":"week_of_year","abbr":"woy"},
		{"name":"day_of_the_week","abbr":"dow"},{"name":"date_accessed","abbr":"a,ad,da"},
		{"name":"movie","abbr":"mv,mt"},{"name":"title","abbr":"t,mvt"},{"name":"file","abbr":"tf"},
		{"name":"dps","abbr":"sdate"},{"name":"header","abbr":"h"}
	],
	"examples": [
		("p ls -i ./photos --json -o results/list.json --map id=42 --target album-001 --auth --method basic --basic --user alice --pass s3cr3t",),

		"cat files.txt | p ls --stdin --yaml -o out.yaml --map key=val --target dstA "
		"--map mode=fast --target dstB --auth --method apikey --apikey --keyfile ./secrets/key.txt"
	]
}



sm = SwitchManager(
	Switches=Switches,
	command="p ls -i ./files --json -o results.json --map id=1 --target dstA "
			"--auth --method basic --basic --user alice --pass secret --help",
	Help=AppRegistration,
)

'''