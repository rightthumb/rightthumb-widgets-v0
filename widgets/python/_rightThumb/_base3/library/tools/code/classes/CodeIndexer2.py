import re
import tokenize
from io import StringIO

class CodeIndexer2:
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
        self._tokenize_code()
        self._char_parse_code()
        self._index_lines()

    def _tokenize_code(self):
        """Use tokenize to find comments, strings, and exclude their positions."""
        tokens = tokenize.generate_tokens(StringIO(self.code).readline)
        for tok_type, tok_str, start, end, _ in tokens:
            start_pos = start[1]
            end_pos = end[1]

            if tok_type == tokenize.COMMENT:
                self.exclude.update(range(start_pos, end_pos))
            elif tok_type == tokenize.STRING:
                self.db["quotes"][start_pos] = end_pos
                self.db["text"][start_pos] = end_pos
                self.exclude.update(range(start_pos, end_pos))

    def _char_parse_code(self):
        """Manually parse characters to find brackets and unmatched quotes."""
        stack = []
        pairs = {"{": "}", "[": "]", "(": ")"}
        rev_pairs = {v: k for k, v in pairs.items()}
        quotes = {"'", '"', "`"}

        i = 0
        while i < len(self.code):
            if i in self.exclude:
                i += 1
                continue

            char = self.code[i]

            # Handle quotes
            if char in quotes:
                if stack and stack[-1][0] == char:
                    open_pos = stack.pop()[1]
                    self.db["quotes"][open_pos] = i
                else:
                    stack.append((char, i))

            # Handle brackets
            elif char in pairs:
                stack.append((char, i))
            elif char in rev_pairs:
                if stack and stack[-1][0] == rev_pairs[char]:
                    open_pos = stack.pop()[1]
                    self.db["oc"][open_pos] = i
                else:
                    if not self.ignore_errors:
                        raise SyntaxError(f"Unmatched closing bracket '{char}' at position {i}")
                    self.errors.append(f"Unmatched closing bracket '{char}' at position {i}")

            i += 1

    def _index_lines(self):
        """Index lines based on newline characters."""
        lines = self.code.splitlines()
        last_pos = 0
        for idx, line in enumerate(lines):
            end_pos = last_pos + len(line)
            self.db["lines"][last_pos] = end_pos
            last_pos = end_pos + 1  # +1 for the newline character

    def __repr__(self):
        return f"CodeIndexerAlt(db={self.db}, exclude={sorted(self.exclude)}, errors={self.errors})"
