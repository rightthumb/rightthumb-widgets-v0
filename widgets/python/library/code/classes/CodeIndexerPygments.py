from pygments import lex
from pygments.lexers import PythonLexer, JavascriptLexer
import re
import _rightThumb._base3 as _


class CodeIndexerPygments:
	def __init__(self, code, language='py', ignore_errors=True):
		self.code = code
		self.language = language.lower()
		self.ignore_errors = ignore_errors
		self.db = {"quotes": {}, "oc": {}, "text": {}, "lines": {}}
		self.exclude = set()  # Character positions to exclude
		self.errors = []  # Track unmatched brackets or quotes
		self.index()

	def index(self):
		"""Main method to index the code using Pygments."""
		lexer = self._get_lexer()
		tokens = lex(self.code, lexer)

		stack = []
		bracket_pairs = {"(": ")", "{": "}", "[": "]"}
		reverse_pairs = {v: k for k, v in bracket_pairs.items()}
		quotes = {"'", '"', "`"}

		pos = 0
		for token_type, value in tokens:
			# Handle comments
			if 'Comment' in str(token_type):
				self.exclude.update(range(pos, pos + len(value)))

			# Handle triple-quoted strings for Python
			if self.language == 'py' and value.startswith(("'''", '"""')):
				start_pos = pos
				end_pos = pos + len(value) - 1
				if self.code[start_pos] in quotes:
					self.db["quotes"][start_pos] = end_pos
				self.db["text"][start_pos] = end_pos
				self.exclude.update(range(start_pos, end_pos + 1))

			# Handle regular strings and text
			elif 'Literal.String' in str(token_type):
				start_pos = pos
				end_pos = pos + len(value) - 1
				if self.code[end_pos] in quotes:
					self.db["quotes"][start_pos] = end_pos
				# self.db["quotes"][start_pos] = end_pos
				self.db["text"][start_pos] = end_pos
				self.exclude.update(range(start_pos, end_pos + 1))

			# Handle brackets
			elif value in bracket_pairs:
				stack.append((value, pos))
			elif value in reverse_pairs:
				if stack and stack[-1][0] == reverse_pairs[value]:
					open_pos = stack.pop()[1]
					self.db["oc"][open_pos] = pos
				else:
					self.errors.append(f"Unmatched closing bracket '{value}' at position {pos}")

			pos += len(value)
			
		import sys, os
		sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'functions')))
		from indexText import indexText

		self.db["text"] = indexText(self.code)
		self._index_lines()

	def _get_lexer(self):
		"""Return the appropriate lexer based on the language."""
		if self.language == 'py':
			return PythonLexer()
		elif self.language == 'js':
			return JavascriptLexer()
		else:
			raise ValueError(f"Unsupported language: {self.language}")

	def _index_lines(self):
		"""Index lines based on newline characters."""
		lines = self.code.splitlines()
		last_pos = 0
		for idx, line in enumerate(lines):
			end_pos = last_pos + len(line)
			self.db["lines"][last_pos] = end_pos
			last_pos = end_pos + 1  # +1 for the newline character

	def __repr__(self):
		return f"CodeIndexerPygments(db={self.db}, exclude={sorted(self.exclude)}, errors={self.errors})"

	def color(self):
		from pygments import highlight
		from pygments.lexers import PythonLexer
		from pygments.formatters import TerminalFormatter



		highlighted_code = highlight(self.code, PythonLexer(), TerminalFormatter())
		print(highlighted_code)
