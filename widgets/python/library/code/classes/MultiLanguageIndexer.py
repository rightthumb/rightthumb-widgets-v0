from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple



class MultiLanguageIndexer:
    """
    Multi-language code/string/comment indexer.

    Main goals:
        - Track start/end char indexes for strings, comments, and paired delimiters.
        - Respect language-specific comment styles.
        - Respect language-specific multi-line quote styles.
        - Avoid treating comment markers inside strings as comments.
        - Return indexes as {startCharID:endCharID}-style spans.

    Notes:
        - end is inclusive.
        - For inline comments, the newline is included if present.
        - For bracket pairs, the open and close indexes are both included.
        - Angle brackets can be enabled per language, but they are disabled by default
          for many languages because they are often operators or generics rather than
          structural pairs.
    """

    LANGUAGE_PROFILES = {
        "python": {
            "line_comments": ["#"],
            "block_comments": [],
            "string_delims": ["'''", '"""', "'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "javascript": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"', "`"],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "typescript": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"', "`"],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "php": {
            "line_comments": ["//", "#"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "c": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "cpp": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "java": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "go": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"', "`"],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "rust": {
            "line_comments": ["//"],
            "block_comments": [("/*", "*/")],
            "string_delims": ["'", '"', 'r"', 'r#"', 'r##"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "shell": {
            "line_comments": ["#"],
            "block_comments": [],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "powershell": {
            "line_comments": ["#"],
            "block_comments": [("<#", "#>")],
            "string_delims": ["'", '"'],
            "escape_char": "`",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": False,
        },
        "html": {
            "line_comments": [],
            "block_comments": [],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": True,
            "html_comments": True,
        },
        "xml": {
            "line_comments": [],
            "block_comments": [],
            "string_delims": ["'", '"'],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": True,
            "html_comments": True,
        },
        "generic": {
            "line_comments": ["//", "#"],
            "block_comments": [("/*", "*/"), ("<!--", "-->")],
            "string_delims": ["'''", '"""', "'", '"', "`"],
            "escape_char": "\\",
            "pair_tokens": [("(", ")"), ("[", "]"), ("{", "}")],
            "angle_brackets": False,
            "html_comments": True,
        },
    }

    def __init__(self, language: str = "generic", enable_angle_brackets: Optional[bool] = None):
        language = language.lower()
        if language not in self.LANGUAGE_PROFILES:
            language = "generic"

        self.language = language
        self.profile = dict(self.LANGUAGE_PROFILES[language])

        if enable_angle_brackets is not None:
            self.profile["angle_brackets"] = enable_angle_brackets

        self.reset()

    def reset(self) -> None:
        self.text: str = ""
        self.spans: Dict[str, List[Span]] = {
            "line_comments": [],
            "block_comments": [],
            "strings": [],
            "pairs": [],
            "unclosed": [],
            "mismatched": [],
        }

    def index(self, text: str) -> Dict[str, List[dict]]:
        self.reset()
        self.text = text

        i = 0
        n = len(text)

        pair_stack: List[Tuple[str, int]] = []
        opening_to_closing = {o: c for o, c in self.profile["pair_tokens"]}
        closing_to_opening = {c: o for o, c in self.profile["pair_tokens"]}

        if self.profile["angle_brackets"]:
            opening_to_closing["<"] = ">"
            closing_to_opening[">"] = "<"

        string_delims = sorted(self.profile["string_delims"], key=len, reverse=True)
        line_comments = sorted(self.profile["line_comments"], key=len, reverse=True)
        block_comments = sorted(self.profile["block_comments"], key=lambda x: len(x[0]), reverse=True)

        while i < n:
            # 1. block comments
            block_match = self._match_block_comment(text, i, block_comments)
            if block_match is not None:
                start_token, end_token = block_match
                end_idx = self._consume_until(text, i + len(start_token), end_token)
                if end_idx is None:
                    self.spans["unclosed"].append(
                        Span(
                            kind="block_comment",
                            start=i,
                            end=n - 1,
                            open_token=start_token,
                            close_token=end_token,
                            meta={"reason": "unclosed block comment"},
                        )
                    )
                    break

                end = end_idx + len(end_token) - 1
                self.spans["block_comments"].append(
                    Span(
                        kind="block_comment",
                        start=i,
                        end=end,
                        open_token=start_token,
                        close_token=end_token,
                    )
                )
                i = end + 1
                continue

            # 2. html comments if enabled
            if self.profile["html_comments"] and text.startswith("<!--", i):
                end_idx = self._consume_until(text, i + 4, "-->")
                if end_idx is None:
                    self.spans["unclosed"].append(
                        Span(
                            kind="html_comment",
                            start=i,
                            end=n - 1,
                            open_token="<!--",
                            close_token="-->",
                            meta={"reason": "unclosed html comment"},
                        )
                    )
                    break

                end = end_idx + 3 - 1
                self.spans["block_comments"].append(
                    Span(
                        kind="html_comment",
                        start=i,
                        end=end,
                        open_token="<!--",
                        close_token="-->",
                    )
                )
                i = end + 1
                continue

            # 3. line comments
            line_match = self._match_line_comment(text, i, line_comments)
            if line_match is not None:
                start_token = line_match
                end = self._line_comment_end(text, i)
                self.spans["line_comments"].append(
                    Span(
                        kind="line_comment",
                        start=i,
                        end=end,
                        open_token=start_token,
                        close_token="\\n" if end < n - 1 and text[end] == "\n" else "EOF",
                    )
                )
                i = end + 1
                continue

            # 4. strings
            string_match = self._match_string_delim(text, i, string_delims)
            if string_match is not None:
                start_token = string_match
                result = self._consume_string(text, i, start_token)
                if result is None:
                    self.spans["unclosed"].append(
                        Span(
                            kind="string",
                            start=i,
                            end=n - 1,
                            open_token=start_token,
                            close_token=start_token,
                            meta={"reason": "unclosed string"},
                        )
                    )
                    break

                end = result
                self.spans["strings"].append(
                    Span(
                        kind="string",
                        start=i,
                        end=end,
                        open_token=start_token,
                        close_token=start_token,
                    )
                )
                i = end + 1
                continue

            # 5. pairs
            ch = text[i]

            if ch in opening_to_closing:
                pair_stack.append((ch, i))
                i += 1
                continue

            if ch in closing_to_opening:
                expected_open = closing_to_opening[ch]
                if pair_stack and pair_stack[-1][0] == expected_open:
                    open_char, open_idx = pair_stack.pop()
                    self.spans["pairs"].append(
                        Span(
                            kind="pair",
                            start=open_idx,
                            end=i,
                            open_token=open_char,
                            close_token=ch,
                        )
                    )
                else:
                    self.spans["mismatched"].append(
                        Span(
                            kind="mismatched_close",
                            start=i,
                            end=i,
                            open_token="",
                            close_token=ch,
                            meta={"expected_open": expected_open},
                        )
                    )
                i += 1
                continue

            i += 1

        # anything left open in stack is unclosed
        for open_char, open_idx in pair_stack:
            self.spans["unclosed"].append(
                Span(
                    kind="pair",
                    start=open_idx,
                    end=open_idx,
                    open_token=open_char,
                    close_token=opening_to_closing[open_char],
                    meta={"reason": "unclosed pair"},
                )
            )

        return self.to_dict()

    def to_dict(self) -> Dict[str, List[dict]]:
        return {k: [span.as_dict() for span in v] for k, v in self.spans.items()}

    def as_range_maps(self) -> Dict[str, Dict[int, int]]:
        """
        Returns a simpler view:
            {
                "line_comments": {start: end, ...},
                "block_comments": {start: end, ...},
                "strings": {start: end, ...},
                "pairs": {start: end, ...},
                ...
            }
        """
        out: Dict[str, Dict[int, int]] = {}
        for group, spans in self.spans.items():
            out[group] = {span.start: span.end for span in spans}
        return out

    def _match_block_comment(self, text: str, i: int, block_comments: List[Tuple[str, str]]) -> Optional[Tuple[str, str]]:
        for start_token, end_token in block_comments:
            if text.startswith(start_token, i):
                return start_token, end_token
        return None

    def _match_line_comment(self, text: str, i: int, line_comments: List[str]) -> Optional[str]:
        for token in line_comments:
            if text.startswith(token, i):
                return token
        return None

    def _match_string_delim(self, text: str, i: int, string_delims: List[str]) -> Optional[str]:
        for delim in string_delims:
            if text.startswith(delim, i):
                return delim
        return None

    def _consume_until(self, text: str, i: int, target: str) -> Optional[int]:
        idx = text.find(target, i)
        return idx if idx != -1 else None

    def _line_comment_end(self, text: str, start: int) -> int:
        nl = text.find("\n", start)
        if nl == -1:
            return len(text) - 1
        return nl

    def _consume_string(self, text: str, start: int, delim: str) -> Optional[int]:
        """
        Returns inclusive end index of the string.

        Handles:
            - normal escaping with configured escape_char
            - triple quotes
            - basic raw Rust-like prefixes that end with "
        """
        n = len(text)
        i = start + len(delim)
        escape_char = self.profile["escape_char"]

        # special handling for Rust-ish raw strings like r"..." / r#"..."# / r##"..."##
        if delim.startswith("r") and delim.endswith('"') and len(delim) >= 2:
            hashes = delim.count("#")
            close = '"' + ("#" * hashes)
            idx = text.find(close, i)
            if idx == -1:
                return None
            return idx + len(close) - 1

        triple_quote = delim in ("'''", '"""')

        while i < n:
            if triple_quote:
                if text.startswith(delim, i):
                    return i + len(delim) - 1
                i += 1
                continue

            ch = text[i]

            if ch == escape_char:
                i += 2
                continue

            if text.startswith(delim, i):
                return i + len(delim) - 1

            i += 1

        return None


@dataclass
class Span:
    kind: str
    start: int
    end: int
    open_token: str
    close_token: str
    meta: dict = field(default_factory=dict)

    def as_dict(self) -> dict:
        return {
            "kind": self.kind,
            "start": self.start,
            "end": self.end,
            "open_token": self.open_token,
            "close_token": self.close_token,
            "meta": self.meta,
        }




if __name__ == "__main__":
    py_code = r'''def x():
    a = "hello # not a comment"
    b = """multi
line
string"""
    c = 'single quote'
    # real comment
    d = {'k': [1, 2, (3)]}
'''

    js_code = r"""function test() {
    let a = "hello // not comment";
    let b = `template ${x}`;
    // real comment
    let c = [1, 2, {x: 3}];
    /*
      block comment
    */
}"""

    print("=== PYTHON ===")
    idx = MultiLanguageIndexer("python")
    result = idx.index(py_code)
    print(idx.as_range_maps())

    print("\n=== JAVASCRIPT ===")
    idx = MultiLanguageIndexer("javascript")
    result = idx.index(js_code)
    print(idx.as_range_maps())