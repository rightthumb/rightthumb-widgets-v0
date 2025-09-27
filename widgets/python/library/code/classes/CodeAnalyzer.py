from __future__ import annotations

import ast
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional, Tuple
from bisect import bisect_right

from pygments import lex
from pygments.lexers import get_lexer_by_name, guess_lexer
from pygments.token import Token


@dataclass
class Pos:
	line: int
	col: int
	offset: int


class CodeAnalyzer:
	def __init__(self):
		pass

	# ---------- public API ----------
	def analyze(self, code: str, language: Optional[str] = None) -> Dict[str, Any]:
		"""
		Analyze code structure and return:
			{
				"language": <detected language>,
				"definitions": {
					"functions": [{name, span{start,end}, ...}],
					"classes":   [{name, span{start,end}, ...}]
				},
				"brackets": {"()":[{start,end}], "[]":[...], "{}":[...], "<>":[...]},
				"quotes":   [{"quote": "'", "span": {start,end}, "preview": "..."}],
				"numbers":  [{"value": "42", "pos": {...}}, ...]
			}
		"""
		lexer = self._pick_lexer(code, language)
		line_starts = self._line_index(code)

		# token pass: numbers, quotes, bracket pairs (ignoring strings/comments)
		brackets, quotes, numbers = self._scan_tokens(code, lexer, line_starts)

		# defs (language-specific where possible)
		lang_name = (language or lexer.name or "").lower()
		definitions = {"functions": [], "classes": []}

		if "python" in lang_name:
			definitions = self._defs_python(code)
		elif "javascript" in lang_name or "ecmascript" in lang_name or "typescript" in lang_name:
			definitions = self._defs_js(code, lexer, line_starts)
		else:
			definitions = self._defs_generic(code, lexer, line_starts)

		return {
			"language": language or lexer.name,
			"definitions": definitions,
			"brackets": brackets,
			"quotes": quotes,
			"numbers": numbers
		}

	# ---------- lexing helpers ----------
	def _pick_lexer(self, code: str, language: Optional[str]):
		if language:
			return get_lexer_by_name(language)
		return guess_lexer(code)

	@staticmethod
	def _line_index(code: str) -> List[int]:
		"""Return absolute offsets where each line starts (0-based)."""
		starts = [0]
		off = 0
		for ch in code:
			off += 1
			if ch == "\n":
				starts.append(off)
		return starts

	@staticmethod
	def _off_to_linecol(starts: List[int], off: int) -> Tuple[int, int]:
		"""Map absolute offset -> (line, col). Line is 1-based; col is 0-based."""
		i = bisect_right(starts, off) - 1
		line_start = starts[i]
		return i + 1, off - line_start

	def _pos(self, starts: List[int], off: int) -> Dict[str, int]:
		l, c = self._off_to_linecol(starts, off)
		return {"line": l, "col": c, "offset": off}

	# ---------- token scan for brackets/quotes/numbers ----------
	def _scan_tokens(self, code: str, lexer, line_starts: List[int]):
		brackets: Dict[str, List[Dict[str, Any]]] = {"()": [], "[]": [], "{}": [], "<>": []}
		quotes: List[Dict[str, Any]] = []
		numbers: List[Dict[str, Any]] = []

		open_to_close = {"(": ")", "[": "]", "{": "}", "<": ">"}
		close_to_open = {v: k for k, v in open_to_close.items()}
		stacks: Dict[str, List[Dict[str, int]]] = {k: [] for k in open_to_close.keys()}

		offset = 0
		for tok_type, tok_text in lex(code, lexer):
			start_off = offset
			end_off = offset + len(tok_text)
			offset = end_off

			is_comment = tok_type in Token.Comment or tok_type is Token.Comment
			is_string = tok_type in Token.Literal.String

			# Numbers
			if tok_type in Token.Literal.Number:
				numbers.append({"value": tok_text, "pos": self._pos(line_starts, start_off)})

			# Quotes: record full span of string tokens
			if is_string and tok_text:
				first = tok_text[0]
				if first in ("'", '"', "`"):
					quotes.append({
						"quote": first,
						"span": {"start": self._pos(line_starts, start_off), "end": self._pos(line_starts, end_off)},
						"preview": tok_text[:32].replace("\n", "\\n")
					})

			# Brackets outside strings/comments
			if not is_comment and not is_string and tok_text:
				for i, ch in enumerate(tok_text):
					cur_off = start_off + i
					if ch in open_to_close:
						stacks[ch].append(self._pos(line_starts, cur_off))
					elif ch in close_to_open:
						opener = close_to_open[ch]
						if stacks[opener]:
							start_pos = stacks[opener].pop()
							key = f"{opener}{ch}"
							brackets[key].append({"start": start_pos, "end": self._pos(line_starts, cur_off)})

		return brackets, quotes, numbers

	# ---------- definitions: Python via AST ----------
	def _defs_python(self, code: str) -> Dict[str, List[Dict[str, Any]]]:
		out = {"functions": [], "classes": []}
		try:
			tree = ast.parse(code)
		except SyntaxError:
			return out

		for node in ast.walk(tree):
			if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
				out["functions"].append({
					"name": node.name,
					"async": isinstance(node, ast.AsyncFunctionDef),
					"span": {
						"start": {"line": node.lineno, "col": node.col_offset, "offset": None},
						"end": {"line": getattr(node, "end_lineno", None), "col": getattr(node, "end_col_offset", None), "offset": None}
					}
				})
			elif isinstance(node, ast.ClassDef):
				out["classes"].append({
					"name": node.name,
					"span": {
						"start": {"line": node.lineno, "col": node.col_offset, "offset": None},
						"end": {"line": getattr(node, "end_lineno", None), "col": getattr(node, "end_col_offset", None), "offset": None}
					}
				})
		return out

	# ---------- definitions: JS/TS heuristics via tokens ----------
	def _defs_js(self, code: str, lexer, line_starts: List[int]) -> Dict[str, List[Dict[str, Any]]]:
		out = {"functions": [], "classes": []}
		toks = list(lex(code, lexer))

		# Build indexed tokens with offsets
		indexed = []
		off = 0
		for tt, tv in toks:
			indexed.append((tt, tv, off, off + len(tv)))
			off += len(tv)

		n = len(indexed)
		i = 0
		while i < n:
			tt, tv, s, e = indexed[i]

			# class Name { ... }
			if tv == "class" and Token.Keyword in tt and i + 1 < n:
				name_tt, name_tv, ns, ne = indexed[i + 1]
				if Token.Name.Class in name_tt or Token.Name in name_tt:
					out["classes"].append({
						"name": name_tv,
						"span": {"start": self._pos(line_starts, s), "end": self._pos(line_starts, e)}
					})

			# function foo() { ... }
			if tv == "function" and Token.Keyword in tt:
				if i + 1 < n:
					name_tt, name_tv, ns, ne = indexed[i + 1]
					if Token.Name.Function in name_tt or Token.Name in name_tt:
						out["functions"].append({
							"name": name_tv,
							"span": {"start": self._pos(line_starts, s), "end": self._pos(line_starts, e)}
						})

			# const foo = (...) => { ... }   (or let/var)
			if tv in ("const", "let", "var") and Token.Keyword in tt:
				if i + 1 < n and Token.Name in indexed[i + 1][0]:
					name_tt, name_tv, ns, ne = indexed[i + 1]
					# scan forward for =>
					j = i + 2
					limit = min(n, i + 30)
					found_arrow = False
					while j < limit:
						if indexed[j][1] == "=>":
							found_arrow = True
							break
						j += 1
					if found_arrow:
						out["functions"].append({
							"name": name_tv,
							"arrow": True,
							"span": {"start": self._pos(line_starts, s), "end": self._pos(line_starts, indexed[j][3])}
						})
			i += 1

		return out

	# ---------- definitions: generic C-like heuristics ----------
	def _defs_generic(self, code: str, lexer, line_starts: List[int]) -> Dict[str, List[Dict[str, Any]]]:
		out = {"functions": [], "classes": []}
		toks = list(lex(code, lexer))

		indexed = []
		off = 0
		for tt, tv in toks:
			indexed.append((tt, tv, off, off + len(tv)))
			off += len(tv)

		n = len(indexed)
		i = 0
		while i < n:
			tt, tv, s, e = indexed[i]

			# class Name
			if tv == "class" and Token.Keyword in tt and i + 1 < n and Token.Name in indexed[i + 1][0]:
				name_tt, name_tv, ns, ne = indexed[i + 1]
				out["classes"].append({
					"name": name_tv,
					"span": {"start": self._pos(line_starts, s), "end": self._pos(line_starts, e)}
				})

			# foo (...) {   treat as function header (heuristic)
			if (Token.Name.Function in tt) or (Token.Name in tt and i + 1 < n and indexed[i + 1][1] == "("):
				name_tt, name_tv, ns, ne = indexed[i]
				out["functions"].append({
					"name": name_tv,
					"span": {"start": self._pos(line_starts, s), "end": self._pos(line_starts, e)}
				})

			i += 1

		return out


# -------------------------
# Example usage:
if __name__ == "__main__":
	sample_py = """\
class Threads:
	openCnt = 0
	def __init__(self, name=None):
		self.name = name
	def start(self):
		print("go", 42, [1,2,3])
"""

	sample_js = """\
class Threads {
	constructor(name) { this.name = name; }
}
const run = (x=1) => { console.log("go", 42, [1,2,3]); }
function start(){ return '<ok>'; }
"""

	analyzer = CodeAnalyzer()

	print("PYTHON STRUCTURE")
	res_py = analyzer.analyze(sample_py, "python")
	print({k: (v if k != "brackets" else {kk: len(vv) for kk, vv in v.items()}) for k, v in res_py.items()})

	print("\nJAVASCRIPT STRUCTURE")
	res_js = analyzer.analyze(sample_js, "javascript")
	print({k: (v if k != "brackets" else {kk: len(vv) for kk, vv in v.items()}) for k, v in res_js.items()})