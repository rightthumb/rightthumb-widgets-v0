import parso

class CodeIndexerParso:
	def __init__(self, code, language='js', ignore_errors=True):
		self.code = code
		self.language = language.lower()
		lan = {'js': 'javascript', 'py': 'python'}
		self.language = lan.get(self.language, self.language)
		self.ignore_errors = ignore_errors
		self.db = {"quotes": {}, "oc": {}, "text": {}, "lines": {}}
		self.exclude = set()  # Character positions to exclude
		self.errors = []  # Track unmatched brackets or quotes
		self.index()

	def index(self):
		"""Main method to index the code using parso."""
		try:
			tree = parso.parse(self.code)
			self._walk_tree(tree)
		except Exception as e:
			if not self.ignore_errors:
				raise e
			self.errors.append(f"Parsing error: {e}")

		# Index lines
		self._index_lines()

		# Clean up unmatched brackets
		self._cleanup_unmatched_brackets()

	def _walk_tree(self, node):
		"""Recursively walk the parso syntax tree to find quotes, brackets, and comments."""
		stack = []  # To track unmatched opening brackets

		for child in node.children:
			if child.type == 'string':
				start_pos = child.start_pos[1]
				end_pos = child.end_pos[1]
				self.db["quotes"][start_pos] = end_pos
				self.db["text"][start_pos] = end_pos
				self.exclude.update(range(start_pos, end_pos))

			elif child.type in ['operator', 'punctuation']:
				char = child.value
				pos = child.start_pos[1]

				if char in "{[(":
					stack.append((char, pos))
				elif char in "}])":
					if stack and self._is_matching_bracket(stack[-1][0], char):
						open_pos = stack.pop()[1]
						self.db["oc"][open_pos] = pos
					else:
						self.errors.append(f"Unmatched closing bracket '{char}' at position {pos}")

			elif child.type == 'comment':
				start_pos = child.start_pos[1]
				end_pos = child.end_pos[1]
				self.exclude.update(range(start_pos, end_pos))

			# Recursively process child nodes
			if hasattr(child, 'children'):
				self._walk_tree(child)

		# Any remaining items in the stack are unmatched opening brackets
		for char, pos in stack:
			self.errors.append(f"Unmatched opening bracket '{char}' at position {pos}")

	def _is_matching_bracket(self, open_bracket, close_bracket):
		"""Check if the open and close brackets match."""
		bracket_pairs = {"{": "}", "[": "]", "(": ")"}
		return bracket_pairs.get(open_bracket) == close_bracket

	def _cleanup_unmatched_brackets(self):
		"""Remove unmatched brackets from self.db['oc']."""
		self.db["oc"] = {k: v for k, v in self.db["oc"].items() if v is not None}

	def _index_lines(self):
		"""Index lines based on newline characters."""
		lines = self.code.splitlines()
		last_pos = 0
		for idx, line in enumerate(lines):
			end_pos = last_pos + len(line)
			self.db["lines"][last_pos] = end_pos
			last_pos = end_pos + 1  # +1 for the newline character

	def __repr__(self):
		return f"CodeIndexerParso(db={self.db}, exclude={sorted(self.exclude)}, errors={self.errors})"