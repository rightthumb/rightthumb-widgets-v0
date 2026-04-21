#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#<reg CodeTagUltra id=codetag-ultra v=1.0.0 ts=2025-09-06T18:25:00Z tags=[indexer,documentation,embedding,validation,usage,downward] lang=python>
#{
#  summary:"Index & document <reg|unit|block|under> with single-line downward headers (<app|fn|sec />) and pro validation UX",
#  process:file.(python).contents.block.index-version,
#  embedding:{ hints:["doc","block","unit","header"], vectors:on }
#}
#</reg CodeTagUltra>

import os, sys, json, re, shlex, hashlib
from typing import Any, Dict, List, Tuple, Optional, Union

# ──────────────────────────────────────────────────────────────────────────────
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'switches')))
from SwitchManager import SwitchManager
try:
	SwitchManager  # type: ignore[name-defined]
except NameError:
	print("ERROR: SwitchManager must be defined/imported before running codetag-ultra.", file=sys.stderr)
	sys.exit(1)

# ──────────────────────────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────────────────────────

def sha256_text(s: str)->str:
	return hashlib.sha256(s.encode("utf-8")).hexdigest()

def discover_comment_prefix(path:str)->List[str]:
	ext = os.path.splitext(path)[1].lower()
	if ext in (".py", ".sh", ".rb"): return ["#"]
	if ext in (".js",".ts",".java",".c",".cpp",".go",".kt",".rs"): return ["//"]
	if ext in (".sql",): return ["--"]
	return ["#","//","--"]

# ──────────────────────────────────────────────────────────────────────────────
# TagParser: classic blocks + single-line downward headers
# ──────────────────────────────────────────────────────────────────────────────

class TagParser:
	"""
	Supports:
	• Classic: <reg|unit|block Name ...> {capsule?} ... </reg|unit|block Name>
	• Directive: <under lines=N ...>
	• Single-line downward headers (aliases):
		<app Name .../>  -> <reg/>
		<fn Name .../>   -> <unit/>
		<sec Name .../>  -> <block/>
		Scope: from the next line down to the first terminator:
		- next self/open of same-or-higher rank (reg > unit > block),
		- explicit close,
		- until=next:<kind>,
		- stop=dedent|regex:<expr>|eof
	• process anywhere (attrs/capsule/nested): literal/dotted/list/~regex
	"""
	TAGS = ("reg", "unit", "block")
	DIRECTIVE = "under"
	NAME_RE = r"[A-Za-z][A-Za-z0-9_-]{0,63}"
	RANK = {"reg":3, "unit":2, "block":1}

	def __init__(self, comment_prefixes: List[str], process_context: Optional[Union[str, List[str]]] = None):
		self.comment_prefixes = sorted(comment_prefixes, key=len, reverse=True)
		self._decomment_res = [ (re.compile(rf"^\s*{re.escape(p)}\s*(.*?)\s*$"), p) for p in self.comment_prefixes ]
		self._fallback_strip = re.compile(r"^\s*(.*?)\s*$")

		tag_union = "|".join(self.TAGS)
		self._open_re  = re.compile(rf"^\s*<({tag_union})\s+({self.NAME_RE})([^>]*)>\s*$")
		self._close_re = re.compile(rf"^\s*</({tag_union})\s+({self.NAME_RE})\s*>\s*$")
		self._under_re = re.compile(rf"^\s*<({self.DIRECTIVE})\s+([^>]*)>\s*$")

		# single-line (self-closing) and aliases
		self._self_re = re.compile(
			r'^\s*<(?P<tag>reg|unit|block|app|fn|sec)\s+(?P<name>[A-Za-z][A-Za-z0-9_-]{0,63})(?P<attrs>[^>]*)/>\s*$'
		)
		self._alias_map = {"app": "reg", "fn": "unit", "sec": "block"}

		self._num_re = re.compile(r"-?\d+(?:\.\d+)?$")
		self.process_context = self._normalize_context(process_context)

		# per-parse state
		self._down_stack: List[Tuple[int, int, Dict[str,Any], Dict[str,Any]]] = []  # (rank, start_line_idx, rec, stop_rules)
		self._lines: List[str] = []
		self._n: int = 0

	# ------------------------------- Public API -------------------------------
	def parse_text(self, text: str, max_lines: int = 10000) -> Dict[str, Any]:
		self._lines = text.splitlines()
		self._n = min(len(self._lines), max_lines)

		regions: List[Dict[str, Any]] = []
		directives: List[Dict[str, Any]] = []
		stack: List[Tuple[str, str, int, Dict[str, Any], Dict[str, Any]]] = []
		coverage: Dict[int, List[int]] = {}

		i = 0
		while i < self._n:
			raw = self._lines[i]
			s = self._decomment(raw)

			# 0) Maybe close downward scopes BEFORE processing current line as a header/close
			closed = self._maybe_close_downward_scopes(i, s, pre_line=True)
			if closed:
				regions.extend(closed)

			# 1) <under ...>
			m_under = self._under_re.match(s)
			if m_under:
				attrs = self._parse_attrs((m_under.group(2) or "").strip())
				span = int(attrs.get("lines", 1) or 1)
				start = i + 2          # applies to lines AFTER the directive
				end = min(self._n, start + span - 1)
				drec = {"_tag":"under","_line":i+1,"_span":(start,end),**attrs}
				specs = self._gather_process_specs(drec)
				drec["_process_specs"] = specs
				drec["applies"] = self._any_spec_matches(specs)
				directives.append(drec)
				idx = len(directives)-1
				for ln in range(start, end+1):
					coverage.setdefault(ln, []).append(idx)
				i += 1
				continue

			# 2) single-line downward header
			m_self = self._self_re.match(s)
			if m_self:
				raw_tag = m_self.group("tag")
				tag = self._alias_map.get(raw_tag, raw_tag)
				name = m_self.group("name")
				attr_str = (m_self.group("attrs") or "").strip().rstrip("/")
				rec = {"_tag": tag, "_name": name, "_open_line": i + 1, **self._parse_attrs(attr_str)}

				rec["_process_specs"] = self._gather_process_specs(rec)
				rec["applies"] = self._any_spec_matches(rec["_process_specs"])

				stop_rules = {
					"until": rec.get("until"),   # e.g., "next:block"
					"stop": rec.get("stop"),     # "dedent" | "eof" | "regex:..."
					"freeze": rec.get("freeze", False),
				}
				self._down_stack.append((self.RANK[tag], i, rec, stop_rules))
				i += 1
				continue

			# 3) classic open
			m_open = self._open_re.match(s)
			if m_open:
				tag, name, attr_str = m_open.group(1), m_open.group(2), m_open.group(3)
				rec = {"_tag": tag, "_name": name, "_open_line": i + 1, **self._parse_attrs(attr_str.strip())}
				capsule, j = self._maybe_capsule(self._lines, i + 1, self._n)
				stack.append((tag, name, i, rec, capsule))
				i = j
				continue

			# 4) classic close
			m_close = self._close_re.match(s)
			if m_close and stack:
				ctag, cname = m_close.group(1), m_close.group(2)
				otag, oname, oline0, rec, capsule = stack.pop()
				if (ctag != otag) or (cname != oname):
					rec["_warn"] = f"mismatch: open {otag}:{oname} vs close {ctag}:{cname}"
				rec["_close_line"] = i + 1
				if capsule:
					for k, v in capsule.items():
						if k not in rec: rec[k] = v
					rec["_capsule"] = capsule
				body = [self._decomment(self._lines[k]) for k in range(oline0 + 1, i)]
				rec["_body"] = "\n".join(body).rstrip()

				# attach overlapping applicable directives
				dlist=[]
				for ln in range(oline0 + 2, i + 1):
					for di in coverage.get(ln, []):
						if directives[di].get("applies", True): dlist.append(di)
				if dlist:
					rec["_directives"] = [directives[u] for u in sorted(set(dlist))]

				rec["_process_specs"] = self._gather_process_specs(rec)
				rec["applies"] = self._any_spec_matches(rec["_process_specs"])
				regions.append(rec)
				i += 1
				continue

			# 5) otherwise, plain line
			i += 1

			# 6) Maybe close downward scopes AFTER advancing, when stop=regex/dedent/eof triggers
			#    (the helper will use the content of the NEXT line at next loop; here we do nothing)

		# Close any remaining classic blocks (unclosed)
		while stack:
			_,_,oline0,rec,capsule = stack.pop()
			rec["_warn"] = "unclosed"
			if capsule: rec["_capsule"] = capsule
			body = [self._decomment(l) for l in self._lines[oline0+1:self._n]]
			rec["_body"] = "\n".join(body).rstrip()
			rec["_process_specs"]=self._gather_process_specs(rec)
			rec["applies"]=self._any_spec_matches(rec["_process_specs"])
			regions.append(rec)

		# Close any remaining downward scopes at EOF
		regions.extend(self._close_all_downward_at_eof())

		return {"regions": regions, "directives": directives}

	# --------------------------- Downward-scope logic --------------------------
	def _maybe_close_downward_scopes(self, line_idx: int, s: str, pre_line: bool) -> List[Dict[str,Any]]:
		"""Close downward scopes if the current line starts a new header/close, or matches stop rules.
		pre_line=True: we’re inspecting BEFORE we process current line as a new header.
		"""
		if not self._down_stack:
			return []
		closed: List[Dict[str,Any]] = []

		# Determine if current line begins a new header (self or open)
		starts_new = bool(self._self_re.match(s) or self._open_re.match(s))
		new_rank = 0
		new_tag = None
		if starts_new:
			mnew = self._self_re.match(s) or self._open_re.match(s)
			if mnew:
				if "tag" in mnew.groupdict():
					t = mnew.group("tag")
				else:
					t = mnew.group(1)
				t = self._alias_map.get(t, t)
				new_tag = t
				new_rank = self.RANK.get(t, 0)

		# iterate stack from top (innermost) to bottom
		to_pop: List[int] = []
		for idx in range(len(self._down_stack) - 1, -1, -1):
			rank, start_i, rec, stops = self._down_stack[idx]
			should_close = False

			# 1) same-or-higher rank new header closes
			if starts_new and new_rank >= rank:
				should_close = True

			# 2) until=next:<kind>
			u = stops.get("until")
			if not should_close and isinstance(u, str) and u.startswith("next:") and starts_new:
				want = u.split(":",1)[1]
				if want in ("reg","unit","block"):
					if new_tag == want and new_rank >= rank:
						should_close = True

			# 3) stop=regex:<expr>
			st = stops.get("stop")
			if not should_close and isinstance(st, str) and st.startswith("regex:"):
				rx = st.split(":",1)[1]
				try:
					if re.search(rx, s):
						should_close = True
				except re.error:
					pass

			# 4) stop=dedent (heuristic: line not indented and not immediately after start)
			if not should_close and st == "dedent":
				if s and not s.startswith((" ", "\t")) and line_idx > start_i + 1:
					should_close = True

			if should_close:
				# body is between start_i+1 .. line_idx-1 (exclusive of current)
				body = [ self._decomment(self._lines[k]) for k in range(start_i + 1, line_idx) ]
				rec["_close_line"] = line_idx
				rec["_body"] = "\n".join(body).rstrip()
				rec["_process_specs"]=self._gather_process_specs(rec)
				rec["applies"]=self._any_spec_matches(rec["_process_specs"])
				closed.append(rec)
				to_pop.append(idx)

		# pop in reverse order
		for idx in to_pop:
			self._down_stack.pop(idx)

		return closed

	def _close_all_downward_at_eof(self) -> List[Dict[str,Any]]:
		if not self._down_stack:
			return []
		closed = []
		for rank, start_i, rec, stops in self._down_stack:
			body = [ self._decomment(self._lines[k]) for k in range(start_i + 1, self._n) ]
			rec["_close_line"] = self._n
			rec["_body"] = "\n".join(body).rstrip()
			rec["_process_specs"]=self._gather_process_specs(rec)
			rec["applies"]=self._any_spec_matches(rec["_process_specs"])
			closed.append(rec)
		self._down_stack.clear()
		return closed

	# ----------------------------- Parsing helpers -----------------------------
	def _decomment(self, line: str) -> str:
		for pat,_ in self._decomment_res:
			m = pat.match(line)
			if m: return m.group(1)
		m = self._fallback_strip.match(line)
		return m.group(1) if m else line.strip()

	def _maybe_capsule(self, lines: List[str], start: int, n: int) -> Tuple[Dict[str,Any], int]:
		j = start
		while j < n:
			probe = self._decomment(lines[j]).strip()
			if not probe:
				j += 1; continue
			if probe.startswith("{"):
				buf=[probe]; depth=probe.count("{")-probe.count("}")
				j+=1
				while j<n and depth>0:
					s=self._decomment(lines[j]).strip()
					buf.append(s); depth += s.count("{")-s.count("}"); j+=1
				text="\n".join(buf)
				try:
					cap=self._parse_map(text[1:-1])
				except Exception:
					cap={"_raw":text}
				return cap, j
			break
		return {}, start

	def _split_top(self, s: str, sep: str) -> List[str]:
		out, buf, depth, q = [], [], 0, None
		for ch in s:
			if q:
				buf.append(ch)
				if ch==q: q=None
				continue
			if ch in ("'",'"'):
				buf.append(ch); q=ch
			elif ch in "{[":
				depth+=1; buf.append(ch)
			elif ch in "}]":
				depth-=1; buf.append(ch)
			elif ch==sep and depth==0:
				frag="".join(buf).strip()
				if frag: out.append(frag)
				buf=[]
			else:
				buf.append(ch)
		if buf:
			frag="".join(buf).strip()
			if frag: out.append(frag)
		return out

	def _parse_value(self, raw: str) -> Any:
		raw=raw.strip()
		if raw=="": return None
		low=raw.lower()
		if low in ("true","false"): return low=="true"
		if self._num_re.fullmatch(raw): return float(raw) if "." in raw else int(raw)
		if (raw.startswith('"') and raw.endswith('"')) or (raw.startswith("'") and raw.endswith("'")):
			return raw[1:-1]
		if raw.startswith("{") and raw.endswith("}"): return self._parse_map(raw[1:-1])
		if raw.startswith("[") and raw.endswith("]"): return [self._parse_value(x) for x in self._split_top(raw[1:-1], ",")]
		return raw

	def _parse_map(self, s:str)->Dict[str,Any]:
		out: Dict[str,Any]={}
		for pair in self._split_top(s,","):
			if not pair or ":" not in pair: continue
			k,v = pair.split(":",1)
			out[k.strip()] = self._parse_value(v)
		return out

	def _parse_attrs(self, s:str)->Dict[str,Any]:
		if not s: return {}
		out: Dict[str,Any]={}
		for part in self._split_top(s," "):
			if not part or "=" not in part: continue
			k,v = part.split("=",1)
			out[k.strip()] = self._parse_value(v.strip())
		return out

	# --------------------------- Process matching ------------------------------
	def _normalize_context(self, ctx: Optional[Union[str,List[str]]])->List[str]:
		if ctx is None: return []
		if isinstance(ctx, list): return [t for t in ctx if t]
		return self._tokenize(str(ctx))

	def _tokenize(self, s:str)->List[str]:
		out: List[str]=[]; i=0; buf=[]; in_group=False; group_buf=[]
		def flush():
			nonlocal buf
			if buf:
				frag="".join(buf).strip()
				if frag: out.extend(frag.split("-"))
				buf=[]
		while i<len(s):
			ch=s[i]
			if ch=="(":
				flush(); in_group=True; group_buf=[]
			elif ch==")":
				if group_buf:
					frag="".join(group_buf).strip()
					if frag: out.extend(frag.split("-"))
				in_group=False; group_buf=[]
			elif ch in ". /\\|:" and not in_group:
				flush()
			else:
				(group_buf if in_group else buf).append(ch)
			i+=1
		flush()
		cleaned=[]
		for t in out:
			for sub in re.split(r"[^A-Za-z0-9_]+", t):
				if sub: cleaned.append(sub)
		return cleaned

	def _spec_from_process_value(self, val: Any) -> Dict[str,Any]:
		if isinstance(val,str):
			if val.startswith("~"):
				try: return {"regex": re.compile(val[1:])}
				except re.error: return {"regex": None}
			return {"tokens": self._tokenize(val)}
		if isinstance(val,list):
			toks=[]
			for it in val:
				if isinstance(it,str): toks.extend(self._tokenize(it))
			return {"tokens": toks}
		return {}

	def _gather_process_specs(self, obj: Any)->List[Dict[str,Any]]:
		specs: List[Dict[str,Any]]=[]
		def walk(x: Any):
			if isinstance(x, dict):
				for k,v in x.items():
					if k=="process":
						spec=self._spec_from_process_value(v)
						if spec: specs.append(spec)
					walk(v)
			elif isinstance(x, list):
				for v in x: walk(v)
		walk(obj)
		return specs

	def _any_spec_matches(self, specs: List[Dict[str,Any]])->bool:
		if not specs: return True
		ctx_tokens=set(self.process_context)
		ctx_str=" ".join(self.process_context)
		for spec in specs:
			rx=spec.get("regex")
			if rx is not None:
				try:
					if rx.search(ctx_str): return True
				except Exception:
					pass
			toks=spec.get("tokens")
			if toks and set(toks).issubset(ctx_tokens): return True
		return False

# ──────────────────────────────────────────────────────────────────────────────
# Switch schema for this app
# ──────────────────────────────────────────────────────────────────────────────

CodeTagSwitches = {
	# Scan
	"Input":     { "flags":["-i","--input"], "help":"File or directory to scan.", "required": True, "ui":{ "path":["Scan","Where"] } },
	"Recurse":   { "flags":["-r","--recurse"], "help":"Recurse into subdirectories.", "ui":{ "path":["Scan","Where"] } },
	"Ext":       { "flags":["--ext"], "help":"Comma-separated extensions (e.g. .py,.js,.sql).", "ui":{ "path":["Scan","Filters"] } },
	"Exclude":   { "flags":["--exclude"], "help":"Substring/glob to skip (repeatable).", "repeatable": True, "ui":{ "path":["Scan","Filters"] } },

	# Output (enum)
	"Output":    { "flags":["--json","--yaml","--toml"], "help":"Output format.", "required": True,
				"flag_value":{"--json":"json","--yaml":"yaml","--toml":"toml"}, "rules":{ "xor":["Output"] },
				"ui":{ "path":["Output","Format"] } },
	"OutPath":   { "flags":["-o","--out"], "help":"Destination file path.", "required": True,
				"rules":{ "requires_one_of":["Output"] }, "ui":{ "path":["Output","Destination"] } },

	# Processing
	"Proc":      { "flags":["--process"], "help":"Process context (literal/dotted/~regex).", "ui":{ "path":["Processing","Context"] } },
	"Embed":     { "flags":["--embed"], "help":"Add mock embeddings for regions.", "ui":{ "path":["Processing","Features"] } },
	"MaxLines":  { "flags":["--max-lines"], "help":"Max lines per file (default 2000).", "ui":{ "path":["Processing","Limits"] } },

	# Per-occurrence demo
	"Pair":       { "flags":["--pair"], "help":"Demo anchor (repeatable).", "repeatable": True,
					"rules":{ "per_occurrence": { "requires":["PairTarget"] } }, "ui":{ "path":["Demo","PerOccurrence"] } },
	"PairTarget": { "flags":["--pair-target"], "help":"Partner for --pair within same occurrence.", "repeatable": True,
					"ui":{ "path":["Demo","PerOccurrence"] } },
}

CodeTagRegistration = {
	"meta": {
		"file": "codetag_ultra.py",
		"liveAppName": "codetag",
		"description": "Index registration comments (classic + single-line downward) and export a doc/embedding report with pro validation UX.",
		"categories": ["index","doc","metadata","blocks","registry","embedding","search"]
	},
	"switches": CodeTagSwitches,
	"examples": [
		("p codetag -i ./src --json -o out/report.json --recurse --ext .py,.js "
		"--process file.(python).contents.block.index-version --embed",),
		("p codetag -i ./sql --yaml -o out/sql.yml --ext .sql "
		"--process ~python --pair a=1 --pair-target a=1",)
	]
}

# ──────────────────────────────────────────────────────────────────────────────
# Validation fail UX: print errors + dynamic usage + help
# ──────────────────────────────────────────────────────────────────────────────

def _first_flag_for_enum(node: Dict[str, Any]) -> Optional[str]:
	fv = node.get("flag_value") or {}
	if isinstance(fv, dict) and fv:
		# pick first deterministically by key sort
		return sorted(fv.keys())[0]
	return None

def _pick_example_value(name: str, node: Dict[str, Any]) -> str:
	if name == "Input": return "./src"
	if name == "OutPath": return "out/report.json"
	if name == "Ext": return ".py,.js,.sql"
	if name == "MaxLines": return "2000"
	if name == "Exclude": return "node_modules"
	if name == "Pair": return "k=v"
	if name == "PairTarget": return "k=v"
	return "VALUE"

def build_generated_usage(sm: "SwitchManager", app_name: str = "codetag") -> str:
	nodes = sm.name_to_node
	parents = sm.parents
	def is_top(n): return parents.get(n) is None
	ordered = [n for n in nodes if is_top(n)]
	cmd = ["p", app_name]
	included = set()

	def include(name: str):
		if name in included: return
		node = nodes.get(name, {})
		flags = node.get("flags", [])
		if not flags: return
		f_enum = _first_flag_for_enum(node)
		if f_enum:
			cmd.append(f_enum)
		else:
			f = flags[0]
			if name in ("Recurse","Embed"):
				cmd.append(f)
			else:
				if f.startswith("--"):
					cmd.append(f"{f}={_pick_example_value(name, node)}")
				else:
					cmd.append(f)
					cmd.append(_pick_example_value(name, node))
		included.add(name)

	# include required and relationships
	for n in ordered:
		node = nodes[n]
		if node.get("required"):
			include(n)
			for imp in (node.get("rules", {}) or {}).get("implies", []):
				include(imp)
			r1 = (node.get("rules", {}) or {}).get("requires_one_of", [])
			if r1:
				include(r1[0])

	# ensure core trio present
	if "Input" not in included: include("Input")
	if "Output" not in included: include("Output")
	if "OutPath" not in included: include("OutPath")

	# per-occurrence sample
	if "Pair" in nodes and "PairTarget" in nodes:
		include("Pair"); include("PairTarget")

	# optional suggestions (bracketed)
	optional = []
	for name, node in nodes.items():
		if node.get("required"): continue
		if name in included: continue
		f = _first_flag_for_enum(node) or (node.get("flags", [])[:1] or [None])[0]
		if not f: continue
		if _first_flag_for_enum(node):
			optional.append(f"[{f}]")
		else:
			ex = _pick_example_value(name, node)
			optional.append(f"[{f}={ex}]" if f.startswith("--") else f"[{f} {ex}]")
	if optional:
		cmd.append(" ".join(optional))

	return " ".join(cmd)

def print_validation_fail(sm: "SwitchManager", errors: List[str], app_reg: Dict[str,Any]):
	def neon(text, color="cyan"):
		try:
			return colorThis(text, color, p=0)  # your colorizer if present
		except Exception:
			return text
	print("\n" + neon("✖ Validation Errors", "red"))
	for e in errors:
		print("  • " + neon(e, "yellow"))

	app_name = (app_reg.get("meta", {}) or {}).get("liveAppName","app")
	usage = build_generated_usage(sm, app_name=app_name)
	print("\n" + neon("Dynamic Usage (generated from switch rules):", "magenta"))
	try:
		print("   " + historyPrint(usage))  # your hp()
	except Exception:
		print("   " + usage)
	print(neon("\nNote:", "darkcyan"),
		"The command above satisfies required/xor/one_of/requires/per-occ rules for this schema.\n")
	sm.show_help()

# ──────────────────────────────────────────────────────────────────────────────
# App logic
# ──────────────────────────────────────────────────────────────────────────────

def render_output(data: Any, fmt: str)->str:
	if fmt == "json":
		return json.dumps(data, indent=2, ensure_ascii=False)
	if fmt == "yaml":
		# for demo, we emit JSON; plug PyYAML if you like
		return json.dumps(data, indent=2, ensure_ascii=False)
	if fmt == "toml":
		return "# TOML (demo)\n" + json.dumps(data, indent=2, ensure_ascii=False)
	return json.dumps(data, indent=2, ensure_ascii=False)

def mock_embed(snippet: str)->Dict[str,Any]:
	return {
		"snippet": snippet[:240],
		"hash": sha256_text(snippet)[:16],
		"dims": 8,
		"vector": [ (sum(bytearray(snippet.encode('utf-8')))+i) % 997 / 997.0 for i in range(8) ]
	}

def iter_files(root: str, recurse: bool, allow_ext: Optional[List[str]], exclude_terms: List[str]):
	if os.path.isfile(root):
		yield root; return
	for dirpath, dirnames, filenames in os.walk(root):
		dirnames[:] = [d for d in dirnames if not any(x in os.path.join(dirpath,d) for x in exclude_terms)]
		for fn in filenames:
			p = os.path.join(dirpath, fn)
			if any(x in p for x in exclude_terms): continue
			if allow_ext:
				if os.path.splitext(fn)[1].lower() not in allow_ext: continue
			yield p
		if not recurse: break

def load_text(path: str)->str:
	try:
		with open(path,"r",encoding="utf-8",errors="replace") as f:
			return f.read()
	except Exception:
		return ""

#<unit main id=main v=1 tags=[entrypoint,cli] process=file.(python).contents.(unit)>
def main(argv: List[str]) -> int:
	cmd = " ".join(shlex.quote(a) for a in argv)
	sm = SwitchManager(Switches=CodeTagSwitches, Help=CodeTagRegistration, command=cmd)

	if sm.help_requested:
		sm.show_help()
		return 0

	ok, errs, warns = sm.validate()
	if not ok:
		print_validation_fail(sm, errs, CodeTagRegistration)
		return 2

	inp = sm.value("Input")
	recurse = sm.isActive("Recurse")
	exts = [x.strip().lower() for x in sm.value("Ext").split(",") if x.strip()] if sm.isActive("Ext") else None
	excludes = sm.values("Exclude")
	out_fmt = sm.value("Output")
	out_path = sm.value("OutPath")
	proc_switch = sm.value("Proc") if sm.isActive("Proc") else None
	embed_on = sm.isActive("Embed")
	max_lines = int(sm.value("MaxLines")) if sm.isActive("MaxLines") else 2000

	results = []
	total_files = 0
	total_regions = 0

	for path in iter_files(inp, recurse, exts, excludes or []):
		total_files += 1
		text = load_text(path)
		if not text: continue
		hint = os.path.splitext(path)[1].lower().lstrip(".")
		context = " ".join([p for p in [proc_switch, f"file.({hint}).contents.block.index-version"] if p])
		parser = TagParser(comment_prefixes=discover_comment_prefix(path), process_context=context)

		head = "\n".join(text.splitlines()[:max_lines])
		parsed = parser.parse_text(head, max_lines=max_lines)

		reg_items = []
		for r in parsed["regions"]:
			total_regions += 1
			body = r.get("_body","")
			item = {
				"file": path,
				"tag": r["_tag"],
				"name": r["_name"],
				"open": r.get("_open_line"),
				"close": r.get("_close_line"),
				"attrs": {k:v for k,v in r.items() if k and not k.startswith("_") and k not in ("_capsule",)},
				"capsule": r.get("_capsule"),
				"applies": r.get("applies", True),
				"directives_count": len(r.get("_directives", [])) if "_directives" in r else 0,
				"frozen": bool(r.get("freeze", False)),
			}
			snippet = f"{r['_tag']} {r['_name']} @ {os.path.basename(path)}\n" + (body[:500])
			item["snippet_hash"] = sha256_text(snippet)[:12]
			if embed_on and r.get("applies", True):
				item["embedding"] = mock_embed(snippet)
			reg_items.append(item)

		dir_items = []
		for d in parsed["directives"]:
			dir_items.append({
				"file": path,
				"line": d["_line"],
				"span": d["_span"],
				"attrs": {k:v for k,v in d.items() if k and not k.startswith("_")},
				"applies": d.get("applies", True)
			})

		if reg_items or dir_items:
			results.append({
				"file": path,
				"regions": reg_items,
				"directives": dir_items
			})

	report = {
		"app": "codetag",
		"input": inp,
		"files_scanned": total_files,
		"regions_found": total_regions,
		"format": out_fmt,
		"process_context": proc_switch or "",
		"results": results
	}

	payload = render_output(report, out_fmt or "json")
	try:
		os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
		with open(out_path, "w", encoding="utf-8") as f:
			f.write(payload)
	except Exception as e:
		print(f"ERROR: cannot write {out_path}: {e}", file=sys.stderr)
		return 3

	print(f"Wrote {out_fmt.upper()} report to {out_path}  (files={total_files}, regions={total_regions})")
	return 0
#</unit main>

#<unit cli id=cli v=1 tags=[entrypoint] process=~python>
if __name__ == "__main__":
	# Example:
	# p codetag -i ./ -r --ext .py,.sql --json -o out/report.json --process file.(python).contents.block --embed
	sys.exit(main(sys.argv[1:]))
#</unit cli>