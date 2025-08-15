from __future__ import annotations

import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
	pass
	_.switches.register( 'Files', '-f,-fi,-file,-files','file.txt', isData='data', description='Files', isRequired=False )
	_.switches.register( 'URL', '-url' )
_._default_settings_()

_.appInfo[focus()] = {
	'file': 'pretty.py',
	'description': 'Beautifier of JSON, HTML, PHP, PHP+HTML, JS, CSS, Python',
	'categories': [
						'code',
						'code-beautifier',
						'tool',
						'json'
						'html',
						'php',
						'javascript',
						'css',
						'python'
				],
	'examples': [
						_.hp('p pretty # Clipboard'),
						_.hp('cat index.php | p pretty'),
						_.hp('p pretty -file data.json'),
						_.hp('p pretty -file app.py'),
						_.hp('p pretty -file code.js'),
						_.hp('p pretty -f style.css'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'relatedapps': [],
	'prerequisite': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
	_.switches.trigger( 'Files',   _.isFileAdvanced, vs=False )     # Advanced File Registration    (Fn Alias Resolves To: def myFileLocations)
	_.switches.trigger( 'URL', _.urlPipe )
	_.switches.trigger( 'DB', _.aliasesFi )
	_.switches.trigger( 'Folder', _.myFolderLocations )
	_.switches.trigger( 'Folders', _.myFolderLocations )
	__.SwitchesModifier.Trigger['Folders'] = _.myFolder
	_.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start






# code_beautifier.py
# from __future__ import annotations
import json
import re
from typing import Optional, Callable, Dict

# Try optional formatters if the user has them installed
_HAVE_BS4 = False
_HAVE_JSBEAUTIFIER = False
_HAVE_BLACK = False

try:
	from bs4 import BeautifulSoup  # type: ignore
	_HAVE_BS4 = True
except Exception:
	pass

try:
	import jsbeautifier  # type: ignore
	_HAVE_JSBEAUTIFIER = True
except Exception:
	pass

try:
	import black  # type: ignore
	_HAVE_BLACK = True
except Exception:
	pass


class CodeBeautifier:
	"""
	Safe, low-surprise beautifier with language auto-detection.

	- language=None  -> auto-detect
	- language can be one of:
		"json", "markdown", "html", "php", "php+html", "javascript", "js",
		"css", "python", "text"
	- Mixed PHP+HTML is handled without touching PHP code.
	- JS/CSS/PHP fallback mode only adjusts indentation (does not re-tokenize).
	- JSON uses json.dumps().
	- HTML: BeautifulSoup if available; else a conservative tag indenter.
	- Python: black if available; else no-op (to avoid breaking code).
	"""

	def __init__(self, indent: int = 4):
		self.indent = indent
		self._formatters: Dict[str, Callable[[str], str]] = {
			"json": self._fmt_json,
			"html": self._fmt_html,
			"php": self._fmt_php,
			"php+html": self._fmt_php_html,
			"javascript": self._fmt_js_like,
			"js": self._fmt_js_like,
			"css": self._fmt_js_like,
			"python": self._fmt_python,
			"markdown": self._fmt_markdown,
			"text": lambda s: s,
		}

	# ---- Public API -----------------------------------------------------

	def format(self, text: str, language: Optional[str] = None) -> str:
		lang = (language or self.detect_language(text)).lower()
		func = self._formatters.get(lang, self._formatters["text"])
		try:
			return func(text).replace('\n\n', '\n')
		except Exception:
			# If anything goes wrong, do not destroy the code—return original.
			return text

	def detect_language(self, text: str) -> str:
		t = text.lstrip()
		# Quick JSON check
		if self._looks_like_json(t):
			return "json"
		# Markdown detection (headings, lists, code fences, tables, emphasis)
		if re.search(r"^#{1,6}\s", t, re.MULTILINE) or \
		re.search(r"^(```|~~~)\w*", t, re.MULTILINE) or \
		re.search(r"^\s*[-*+]\s+\w+", t, re.MULTILINE) or \
		re.search(r"^\|.*\|", t, re.MULTILINE) or \
		re.search(r"\*\*[^*]+\*\*", t) or \
		re.search(r"_[^_]+_", t):
			return "markdown"
		# PHP markers
		if "<?php" in t or t.startswith("<?=") or re.search(r"<\?(php|=)", t):
			if re.search(r"<\/?\w", t):  # has HTML tags too
				return "php+html"
			return "php"
		# HTML tags (very simple heuristic)
		if re.search(r"<!DOCTYPE html>|<\/?\w+[^>]*>", t, re.IGNORECASE):
			return "html"
		# Python hints
		if t.startswith("#!") and "python" in t[:80].lower():
			return "python"
		if re.search(r"\bdef\s+\w+\s*\(", t) or re.search(r"\bimport\s+\w+", t):
			# avoid mis-detecting JS "import"
			if not re.search(r"\b(import.*from\s+['\"][^'\"]+['\"];)", t):
				return "python"
		# JS hints
		if re.search(r"\b(function|const|let|=>|console\.log|import\s+.*from)\b", t):
			return "javascript"
		# CSS hints
		if re.search(r"{\s*[^}]*;\s*}", t) and not re.search(r"\bfunction\b", t):
			return "css"
		return "text"

	# ---- Formatters -----------------------------------------------------

	def _fmt_json(self, text: str) -> str:
		obj = json.loads(text)
		return json.dumps(obj, indent=self.indent, ensure_ascii=False)

	def _fmt_html(self, text: str) -> str:
		if _HAVE_BS4:
			# 'html.parser' is built-in; avoids lxml dependency.
			soup = BeautifulSoup(text, "html.parser")
			# prettify() can sometimes add extra newlines; it’s still the safest general option.
			return soup.prettify(formatter="html")
		# Fallback: conservative HTML indenter that:
		#  - preserves <script>/<style> blocks
		#  - treats PHP blocks as opaque tokens
		return self._indent_html_conservative(text)

	def _fmt_php(self, text: str) -> str:
		# Conservative: adjust indentation only by braces and case/ends,
		# avoid reflowing content within strings/comments.
		return self._brace_reindent(text, open_tokens="{", close_tokens="}")

	def _fmt_php_html(self, text: str) -> str:
		# Split PHP blocks from HTML, format HTML portion, stitch back together.
		parts = self._split_php_blocks(text)
		out = []
		for is_php, chunk in parts:
			if is_php:
				out.append(self._fmt_php(chunk))
			else:
				out.append(self._fmt_html(chunk))
		return "".join(out)

	def _fmt_js_like(self, text: str) -> str:
		# Prefer jsbeautifier if present (handles both JS and CSS)
		if _HAVE_JSBEAUTIFIER:
			opts = jsbeautifier.default_options()
			opts.indent_size = self.indent
			return jsbeautifier.beautify(text, opts)
		# Fallback: adjust indentation by braces only; preserve lines.
		return self._brace_reindent(text, "{", "}")

	def _fmt_python(self, text: str) -> str:
		if _HAVE_BLACK:
			mode = black.Mode()
			return black.format_str(text, mode=mode)
		# No-op fallback to avoid breaking Python semantics.
		return text

	# ---- Helpers --------------------------------------------------------

	@staticmethod
	def _looks_like_json(t: str) -> bool:
		# Fast path: must start with { or [ and parse cleanly.
		if not t or t[0] not in "{[":
			return False
		try:
			json.loads(t)
			return True
		except Exception:
			return False

	@staticmethod
	def _split_php_blocks(text: str):
		"""
		Returns list of (is_php, chunk).
		Keeps PHP blocks intact, including short echo tags.
		"""
		out = []
		i = 0
		pattern = re.compile(r"<\?(php|=).*?\?>", re.DOTALL | re.IGNORECASE)
		for m in pattern.finditer(text):
			if m.start() > i:
				out.append((False, text[i:m.start()]))
			out.append((True, m.group(0)))
			i = m.end()
		if i < len(text):
			out.append((False, text[i:]))
		return out

	def _brace_reindent(self, text: str, open_tokens="{", close_tokens="}") -> str:
		"""
		Indent lines based on net count of open/close tokens,
		being careful to ignore braces inside quotes and line comments.
		- Does NOT alter line content beyond leading whitespace.
		- Keeps original line breaks.
		"""
		lines = text.splitlines()
		result = []
		indent_level = 0
		indent_str = " " * self.indent

		for raw in lines:
			line = raw.rstrip("\r\n")
			stripped = line.lstrip()
			leading = len(line) - len(stripped)

			delta = self._brace_delta(stripped, open_tokens, close_tokens)

			# If this line starts with a closing token, dedent first
			if self._starts_with_any(stripped, tuple(close_tokens)):
				indent_level = max(0, indent_level - 1)

			result.append(f"{indent_str * indent_level}{stripped}")

			# Then apply delta for following lines
			indent_level = max(0, indent_level + delta)

		return "\n".join(result)

	@staticmethod
	def _starts_with_any(s: str, tokens: tuple[str, ...]) -> bool:
		return any(s.startswith(tok) for tok in tokens)

	@staticmethod
	def _brace_delta(s: str, opens: str, closes: str) -> int:
		"""
		Count net open-close tokens outside strings and single-line comments.
		Supports // comments and /* ... */ multi-line in a best-effort way for JS/CSS/PHP.
		"""
		net = 0
		i = 0
		n = len(s)
		in_sq = False
		in_dq = False
		in_bt = False  # backtick (JS)
		in_ml_comment = False

		while i < n:
			ch = s[i]
			nxt = s[i + 1] if i + 1 < n else ""

			# Multi-line comment start/end
			if not in_sq and not in_dq and not in_bt:
				if not in_ml_comment and ch == "/" and nxt == "*":
					in_ml_comment = True
					i += 2
					continue
				if in_ml_comment and ch == "*" and nxt == "/":
					in_ml_comment = False
					i += 2
					continue

			if in_ml_comment:
				i += 1
				continue

			# Line comment //
			if not in_sq and not in_dq and not in_bt and ch == "/" and nxt == "/":
				break  # rest of line ignored

			# String state
			if not in_dq and not in_bt and ch == "'" and not CodeBeautifier._escaped(s, i):
				in_sq = not in_sq
				i += 1
				continue
			if not in_sq and not in_bt and ch == '"' and not CodeBeautifier._escaped(s, i):
				in_dq = not in_dq
				i += 1
				continue
			if not in_sq and not in_dq and ch == "`" and not CodeBeautifier._escaped(s, i):
				in_bt = not in_bt
				i += 1
				continue

			if not in_sq and not in_dq and not in_bt:
				if ch in opens:
					net += 1
				elif ch in closes:
					net -= 1

			i += 1
		return net

	@staticmethod
	def _escaped(s: str, i: int) -> bool:
		# Count backslashes immediately before position i
		backslashes = 0
		j = i - 1
		while j >= 0 and s[j] == "\\":
			backslashes += 1
			j -= 1
		return (backslashes % 2) == 1

	def _indent_html_conservative(self, html: str) -> str:
		"""
		Extremely conservative HTML indenter:
		  - Treats tags as tokens
		  - Void elements don't change indent
		  - Blocks (script/style) preserved as-is
		  - PHP blocks treated as opaque
		"""
		void_tags = {
			"area", "base", "br", "col", "embed", "hr", "img", "input",
			"link", "meta", "param", "source", "track", "wbr",
		}

		# Tokenize: tags, comments, PHP, or text
		token_re = re.compile(
			r"(<!--.*?-->)"         # HTML comments
			r"|(<\?(?:php|=).*?\?>)"# PHP blocks
			r"|(<[^>]+>)"           # HTML tags
			r"|([^<]+)",            # text
			re.DOTALL | re.IGNORECASE
		)

		# Detect block tags whose contents should be preserved as-is
		block_open_re = re.compile(r"<(script|style)\b[^>]*>", re.IGNORECASE)
		block_close_re = re.compile(r"</(script|style)\s*>", re.IGNORECASE)

		indent_level = 0
		out_lines = []
		indent_str = " " * self.indent

		i = 0
		tokens = list(token_re.finditer(html))
		preserve_until_close = None
		for m in tokens:
			comment, phpblock, tag, text = m.groups()

			chunk = comment or phpblock or tag or text

			if preserve_until_close:
				out_lines.append(chunk)
				if block_close_re.search(chunk):
					preserve_until_close = None
				continue

			if comment:
				out_lines.append(f"{indent_str * indent_level}{chunk}")
				continue

			if phpblock:
				out_lines.append(f"{indent_str * indent_level}{chunk}")
				continue

			if tag:
				tag_name = self._extract_tag_name(tag)
				is_close = tag.strip().startswith("</")
				is_self = tag.endswith("/>") or (tag_name in void_tags)

				# Dedent on closing tag
				if is_close:
					indent_level = max(0, indent_level - 1)

				out_lines.append(f"{indent_str * indent_level}{tag}")

				# If opening (non-void), increase indent
				if (not is_close) and (not is_self):
					indent_level += 1

				# Enter preserve mode for script/style
				if block_open_re.search(tag):
					preserve_until_close = True
				continue

			# Text node: split by lines but preserve text chunks without trimming
			for line in text.splitlines():
				stripped = line.rstrip()
				if stripped:
					out_lines.append(f"{indent_str * indent_level}{stripped}")
				else:
					out_lines.append("")
		return "\n".join(out_lines)

	@staticmethod
	def _extract_tag_name(tag: str) -> str:
		m = re.match(r"</?\s*([a-zA-Z0-9:-]+)", tag)
		return (m.group(1).lower() if m else "").strip()



	@staticmethod
	def _fmt_markdown(file_path: str) -> str:
		"""
		Formats a Markdown file in place using mdformat.
		
		Args:
			file_path (str): Path to the Markdown file.
		"""
		path = Path(file_path)
		if not path.exists():
			raise FileNotFoundError(f"File not found: {file_path}")

		original_text = path.read_text(encoding="utf-8")
		formatted_text = mdformat.text(original_text)
		return formatted_text
		# Only overwrite if changes were made
		if formatted_text != original_text:
			path.write_text(formatted_text, encoding="utf-8")
			print(f"Formatted: {file_path}")
		else:
			print(f"No changes: {file_path}")


# Example usage
if __name__ == "__main__":
	_fmt_markdown("README.md")

import mdformat # type: ignore
from pathlib import Path


# ----------------------
# Minimal usage examples
# ----------------------
if False:
	cb = CodeBeautifier(indent=4)

	# Auto-detect JSON
	ugly_json = '{"b":2,"a":[3,1,2]}'
	print(cb.format(ugly_json))  # auto-detects as JSON and pretty-prints

	# Explicit HTML (mixed with PHP)
	php_html = """<!doctype html>
<html><head><title>Test</title><?php echo "x"; ?></head>
<body><div><p>Hello</p><?php if ($x) { ?><span>Y</span><?php } ?></div>
<script>function x(){console.log("{ } not code");}</script></body></html>"""
	print(cb.format(php_html, "php+html"))

	# JS/CSS/PHP fallback only reindents by braces (safe, low surprise)
	js = "function x(){\nconsole.log('a');if(true){console.log('b')}}"
	print(cb.format(js, "javascript"))

	# Python (uses black if available, otherwise no-op)
	py = "def f(x):\n  return(x+1)"
	print(cb.format(py, "python"))













def action():
	_.isDataClip('pretty')
	cb = CodeBeautifier(indent=4)
	print(cb.format( '\n'.join( _.isData(2) ) ))

########################################################################################
if __name__ == '__main__':
	action(); _.isExit(__file__)