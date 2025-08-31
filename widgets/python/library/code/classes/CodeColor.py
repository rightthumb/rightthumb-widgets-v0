import os
from typing import Optional, Union, List

from pygments import highlight
from pygments.lexers import guess_lexer, get_all_lexers, get_lexer_by_name
from pygments.util import ClassNotFound
from pygments.styles import get_all_styles
from pygments.formatters import HtmlFormatter, TerminalFormatter

# These may not exist on very old Pygments; we guard the imports.
try:
	from pygments.formatters import Terminal256Formatter
except Exception:
	Terminal256Formatter = None

try:
	from pygments.formatters import TerminalTrueColorFormatter
except Exception:
	TerminalTrueColorFormatter = None


class CodeColor:
	def __init__(
		self,
		style: str = 'one-dark',
		output: str = 'terminal',
		prefer_truecolor: bool = True,
		prefer_256: bool = True,
	):
		self.style = style
		self.output_format = output.lower()
		self.prefer_truecolor = prefer_truecolor
		self.prefer_256 = prefer_256
		self._validate_style()
		self.formatter = self._get_formatter()
		self.supported_languages = self._get_supported_languages()

	# ---------- capability detection ----------
	@staticmethod
	def _supports_truecolor() -> bool:
		# Common indicators across terminals
		ct = os.getenv('COLORTERM', '').lower()
		return 'truecolor' in ct or '24bit' in ct

	@staticmethod
	def _supports_256() -> bool:
		term = os.getenv('TERM', '').lower()
		return '256color' in term or 'xterm' in term or 'screen-256color' in term

	# ---------- setup ----------
	def _validate_style(self) -> None:
		available = set(get_all_styles())
		if self.style not in available:
			raise ValueError(f"Invalid style '{self.style}'. Available styles: {sorted(available)}")

	def _get_formatter(self):
		if self.output_format == 'html':
			return HtmlFormatter(style=self.style)

		# terminal path: try truecolor -> 256 -> 16-color
		if self.prefer_truecolor and TerminalTrueColorFormatter and self._supports_truecolor():
			return TerminalTrueColorFormatter(style=self.style)

		if self.prefer_256 and Terminal256Formatter and self._supports_256():
			return Terminal256Formatter(style=self.style)

		return TerminalFormatter(style=self.style)

	def _get_supported_languages(self) -> List[str]:
		return list({alias for lexer in get_all_lexers() for alias in lexer[1]})

	# ---------- API ----------
	def detect_language(self, code: str) -> str:
		try:
			return guess_lexer(code).name
		except ClassNotFound:
			return "unknown"

	def color(self, code: str, language: Optional[str] = None) -> str:
		return self.highlight(code, language)

	def highlight(self, code: str, language: Optional[str] = None) -> str:
		try:
			lexer = get_lexer_by_name(language) if language else guess_lexer(code)
			return highlight(code, lexer, self.formatter)
		except ClassNotFound:
			return code

	def set_style(self, new_style: str) -> None:
		self.style = new_style
		self._validate_style()
		self.formatter = self._get_formatter()

	def set_output_format(self, format: str) -> None:
		self.output_format = format.lower()
		self.formatter = self._get_formatter()

	def list_languages(self) -> List[str]:
		return sorted(self.supported_languages)

	def list_styles(self) -> List[str]:
		return list(get_all_styles())

	def print_languages(self) -> None:
		print("Supported languages:")
		for lang in sorted(self.supported_languages):
			print(f"- {lang}")

	def print_styles(self) -> None:
		print("Available styles:")
		for style in self.list_styles():
			print(f"- {style}")

	def get_css(self) -> str:
		if not isinstance(self.formatter, HtmlFormatter):
			raise RuntimeError("CSS is only available for HTML output format")
		return self.formatter.get_style_defs()



	def analyze(self, code: str, language: str = None):
		"""Return a list of token dictionaries with type and value."""
		from pygments import lex # type: ignore
		lexer = get_lexer_by_name(language) if language else guess_lexer(code)
		return [
			{"type": str(tok_type), "value": tok_value}
			for tok_type, tok_value in lex(code, lexer)
		]
