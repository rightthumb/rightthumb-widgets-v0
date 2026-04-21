#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DocPipe
=======

A flexible importable Python library for document/text ingestion, normalization,
table inference, profiling, and pandas-based querying.

Design goals
------------
1. Every public function accepts a SINGLE DICT argument.
2. Auto behavior:
   - If no file/path/raw text is given, assume STDIN / pipe.
   - If a file is given, infer type from extension unless explicitly set.
3. Be useful right now for:
   - PDF -> text (layout-ish)
   - PDF -> prominent table JSON
   - tasklist / fixed-width text -> rows / DataFrame / JSON
   - profile fields for future regex / vector / schema work
4. Be easy to build out later for:
   - DOCX / HTML / Markdown / XLSX / CSV / etc.
   - heading path trees
   - semantic sections
   - table memory / learned extraction profiles
   - invoice totals / subtotals outside formal table boxes
   - vector workflows

Dependencies
------------
Core:
    pip install pandas

Optional:
    pip install pdfminer.six
    pip install pdfplumber
    pip install pymupdf4llm

Current philosophy
------------------
For now, pandas handles grouping, selecting, aggregation, and sorting.
That gets us to "tasklist2table equivalent" much faster than building a full
custom query framework.

Future direction
----------------
You may later want to add:
- a profile store keyed by source/type/header signature
- heading-path extraction:
    h1 > h2 > h3
- table context extraction:
    table rows + nearby totals/subtotals
- source adapters that all emit the same normalized block structure
- learned "view configs" so repeated document types auto-parse similarly

Public class
------------
    dp = DocPipe({...})
    text = dp.extract_text({...})
    rows = dp.extract_rows({...})
    report = dp.profile_fields({...})
    result = dp.query_table({...})

Common public patterns
----------------------
    from docpipe import DocPipe

    dp = DocPipe({"path": "invoice.pdf"})
    print(dp.extract_text({}))

    dp = DocPipe({})
    result = dp.query_table({
        "group_by": ["Name"],
        "aggregate": {
            "MemUsage": "sum"
        }
    })

    dp = DocPipe({"raw_text": some_text})
    rows = dp.extract_rows({"mode": "fixed_width"})
"""

import sys
import os
import re
import io
import json
import math
import mimetypes
from collections import defaultdict, Counter
from typing import Any, Dict, List, Optional, Tuple

try:
    import pandas as pd
except ImportError:
    pd = None


class DocPipe:
    """
    Main orchestrator class.

    All configuration is passed as a single dict.
    The class tries to auto-detect source and format on init.

    Example:
        dp = DocPipe({
            "path": "file.pdf",
            "debug": True,
        })

    Notes:
    - If "path" is absent and "raw_text" is absent, stdin is attempted.
    - If stdin is empty and nothing else is provided, the object still initializes,
      but some methods will return empty data until content is provided.
    """

    def __init__(self, cfg: Optional[Dict[str, Any]] = None):
        self.cfg = self._defaults(cfg, {
            "path": None,
            "raw_text": None,
            "raw_bytes": None,
            "kind": "auto",
            "encoding": "utf-8",
            "errors": "replace",
            "debug": False,
            "prefer_pdf_table": True,
            "prefer_pdf_markdown": False,
            "stdin_if_missing": True,
            "table_profile_name": None,
        })

        self.state = {
            "source": None,
            "path": self.cfg.get("path"),
            "kind": None,
            "raw_text": None,
            "raw_bytes": None,
            "text": None,
            "markdown": None,
            "rows": None,
            "df": None,
            "meta": {},
            "profiles": {},
        }

        self._init_source({})

    # -------------------------------------------------------------------------
    # Initialization / auto-detect
    # -------------------------------------------------------------------------

    def _init_source(self, cfg: Dict[str, Any]) -> Dict[str, Any]:
        """
        Initialize source on object construction.

        Priority:
        1. raw_text
        2. raw_bytes
        3. path
        4. stdin (if enabled)

        This is deliberately conservative: it does not fully parse everything
        during init. It just loads enough state so later methods can operate.
        """
        merged = self._merge_cfg(cfg)

        raw_text = merged.get("raw_text")
        raw_bytes = merged.get("raw_bytes")
        path = merged.get("path")

        if raw_text is not None:
            self.state["source"] = "raw_text"
            self.state["raw_text"] = raw_text
            self.state["text"] = raw_text
            self.state["kind"] = self._infer_kind({"path": path, "raw_text": raw_text, "kind": merged.get("kind")})
            return self.state

        if raw_bytes is not None:
            self.state["source"] = "raw_bytes"
            self.state["raw_bytes"] = raw_bytes
            try:
                self.state["text"] = raw_bytes.decode(
                    merged.get("encoding", "utf-8"),
                    errors=merged.get("errors", "replace")
                )
            except Exception:
                self.state["text"] = None
            self.state["kind"] = self._infer_kind({"path": path, "raw_bytes": raw_bytes, "kind": merged.get("kind")})
            return self.state

        if path:
            self.state["source"] = "path"
            self.state["kind"] = self._infer_kind({"path": path, "kind": merged.get("kind")})
            return self.state

        if merged.get("stdin_if_missing", True):
            # Auto-read stdin only if data appears to be piped.
            if not sys.stdin.isatty():
                data = sys.stdin.read()
                self.state["source"] = "stdin"
                self.state["raw_text"] = data
                self.state["text"] = data
                self.state["kind"] = self._infer_kind({"raw_text": data, "kind": merged.get("kind")})
                return self.state

        self.state["source"] = "empty"
        self.state["kind"] = self._infer_kind({"kind": merged.get("kind")})
        return self.state

    def _infer_kind(self, cfg: Dict[str, Any]) -> str:
        """
        Infer source type.

        Current simple logic:
        - explicit kind wins unless "auto"
        - otherwise infer from file extension
        - fallback to text

        Future build-out:
        - sniff MIME by bytes
        - inspect magic numbers
        - route DOCX/HTML/XLSX/etc. through adapters
        """
        kind = cfg.get("kind", "auto")
        path = cfg.get("path")

        if kind and kind != "auto":
            return str(kind).lower()

        if path:
            ext = os.path.splitext(path)[1].lower().strip(".")
            if ext:
                return ext

        return "text"

    # -------------------------------------------------------------------------
    # Public helper / state
    # -------------------------------------------------------------------------

    def info(self, cfg: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Return current internal state summary.

        Handy for debugging or for seeing what auto-init did.
        """
        _ = self._merge_cfg(cfg)
        return {
            "source": self.state.get("source"),
            "path": self.state.get("path"),
            "kind": self.state.get("kind"),
            "has_text": self.state.get("text") is not None,
            "has_rows": self.state.get("rows") is not None,
            "has_df": self.state.get("df") is not None,
            "meta": self.state.get("meta", {}),
        }

    # -------------------------------------------------------------------------
    # Main extraction APIs
    # -------------------------------------------------------------------------

    def extract_text(self, cfg: Optional[Dict[str, Any]] = None) -> str:
        """
        Extract text from current source.

        Current support:
        - raw text / stdin / bytes -> returns text directly
        - PDF -> attempts layout-aware extraction
        - fallback file reading for text-like files

        Args dict keys:
            path: optional override
            kind: optional override
            layout: bool (default True for PDF)
            cache: bool
        """
        merged = self._merge_cfg(cfg, {
            "layout": True,
            "cache": True,
        })

        if merged["cache"] and self.state.get("text"):
            return self.state["text"]

        kind = self._infer_kind(merged)
        path = merged.get("path") or self.state.get("path")

        if kind == "pdf" and path:
            text = self._extract_pdf_text({
                "path": path,
                "layout": merged.get("layout", True),
            })
            if merged["cache"]:
                self.state["text"] = text
            return text

        # If text was already loaded from stdin/raw_text, just use it.
        if self.state.get("text") is not None:
            return self.state["text"]

        # Simple file fallback for plain text-ish sources.
        if path:
            try:
                with open(path, "r", encoding=merged.get("encoding", "utf-8"), errors=merged.get("errors", "replace")) as f:
                    text = f.read()
                if merged["cache"]:
                    self.state["text"] = text
                return text
            except Exception:
                # Binary or unsupported fallback.
                return ""

        return ""

    def extract_markdown(self, cfg: Optional[Dict[str, Any]] = None) -> str:
        """
        Attempt Markdown extraction.

        Current behavior:
        - PDF: if pymupdf4llm exists, use it
        - otherwise fallback to plain text

        Future:
        - DOCX -> semantic markdown
        - HTML -> cleaned markdown
        - heading path enrichment
        """
        merged = self._merge_cfg(cfg, {
            "cache": True,
        })

        if merged["cache"] and self.state.get("markdown"):
            return self.state["markdown"]

        kind = self._infer_kind(merged)
        path = merged.get("path") or self.state.get("path")

        md = ""

        if kind == "pdf" and path:
            md = self._extract_pdf_markdown({
                "path": path,
            })

        if not md:
            md = self.extract_text(merged)

        if merged["cache"]:
            self.state["markdown"] = md

        return md

    def extract_rows(self, cfg: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Extract rows from text or document content.

        Modes:
        - auto
        - fixed_width
        - pdf_prominent_table

        Args dict keys:
            mode: auto|fixed_width|pdf_prominent_table|pdf_all_tables
            path: optional
            text: optional override text
            header_row_index: int
            cache: bool
        """
        merged = self._merge_cfg(cfg, {
            "mode": "auto",
            "header_row_index": 0,
            "cache": True,
        })

        if merged["cache"] and self.state.get("rows") is not None and merged.get("mode") == "auto":
            return self.state["rows"]

        mode = merged.get("mode", "auto")
        kind = self._infer_kind(merged)
        path = merged.get("path") or self.state.get("path")

        rows = []

        if mode == "pdf_prominent_table":
            rows = self._extract_pdf_prominent_table_rows({
                "path": path,
            })
        elif mode == "pdf_all_tables":
            rows = self._extract_pdf_all_tables_rows({
                "path": path,
            })
        else:
            # Auto mode logic:
            # If PDF and table preference enabled, try prominent table first.
            if kind == "pdf" and path and merged.get("prefer_pdf_table", self.cfg.get("prefer_pdf_table", True)):
                rows = self._extract_pdf_prominent_table_rows({"path": path})

            # If no rows from PDF table extraction, parse text as fixed-width table.
            if not rows:
                text = merged.get("text")
                if text is None:
                    text = self.extract_text(merged)
                rows = self._parse_fixed_width_text_table({
                    "text": text,
                    "header_row_index": merged.get("header_row_index", 0),
                })

        if merged["cache"] and mode == "auto":
            self.state["rows"] = rows

        return rows

    def to_df(self, cfg: Optional[Dict[str, Any]] = None):
        """
        Convert rows to pandas DataFrame.

        Returns:
            pandas.DataFrame

        Raises:
            RuntimeError if pandas is missing
        """
        if pd is None:
            raise RuntimeError("pandas is required for to_df(). pip install pandas")

        merged = self._merge_cfg(cfg, {
            "rows": None,
            "cache": True,
        })

        rows = merged.get("rows")
        if rows is None:
            rows = self.extract_rows(merged)

        df = pd.DataFrame(rows)

        if merged["cache"]:
            self.state["df"] = df

        return df

    # -------------------------------------------------------------------------
    # Query / select / group / aggregate
    # -------------------------------------------------------------------------

    def query_table(self, cfg: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Generic query pipeline for row/table data using pandas.

        This is the "good enough now" replacement for custom switch-framework logic.

        Args dict keys:
            rows: optional explicit rows
            select: list[str]
            rename: dict
            where: list[dict]
            group_by: list[str]
            sort_by: list[str]
            ascending: bool|list[bool]
            aggregate: dict[str, str|list|callable]
            fillna: dict|scalar
            as_json: bool
            records: bool
            coerce_numeric: list[str]
            strip_chars: dict[field] -> regex/string to remove before numeric conversion

        Example:
            result = dp.query_table({
                "select": ["Name", "MemUsage"],
                "group_by": ["Name"],
                "coerce_numeric": ["MemUsage"],
                "strip_chars": {"MemUsage": r"[^0-9\.\-]"},
                "aggregate": {"MemUsage": "sum"},
                "sort_by": ["MemUsage"],
                "ascending": False,
            })
        """
        if pd is None:
            raise RuntimeError("pandas is required for query_table(). pip install pandas")

        merged = self._merge_cfg(cfg, {
            "rows": None,
            "select": None,
            "rename": None,
            "where": [],
            "group_by": None,
            "sort_by": None,
            "ascending": True,
            "aggregate": None,
            "fillna": None,
            "as_json": True,
            "records": True,
            "coerce_numeric": [],
            "strip_chars": {},
        })

        df = self.to_df({"rows": merged.get("rows")})

        if df.empty:
            return {
                "ok": True,
                "rows": [],
                "columns": [],
                "count": 0,
            }

        # Optional column rename early
        if merged.get("rename"):
            df = df.rename(columns=merged["rename"])

        # Optional select early
        if merged.get("select"):
            existing = [c for c in merged["select"] if c in df.columns]
            df = df[existing]

        # Optional fillna
        if merged.get("fillna") is not None:
            df = df.fillna(merged["fillna"])

        # Optional numeric coercion
        for field in merged.get("coerce_numeric", []):
            if field in df.columns:
                series = df[field].astype(str)
                strip_pattern = merged.get("strip_chars", {}).get(field)
                if strip_pattern:
                    series = series.str.replace(strip_pattern, "", regex=True)
                df[field] = pd.to_numeric(series, errors="coerce")

        # Apply simple where filters
        df = self._apply_where_df({
            "df": df,
            "where": merged.get("where", []),
        })

        # Group / aggregate
        if merged.get("group_by") and merged.get("aggregate"):
            group_cols = [c for c in merged["group_by"] if c in df.columns]
            agg_map = merged["aggregate"]
            if group_cols:
                df = df.groupby(group_cols, dropna=False).agg(agg_map).reset_index()

        # Sort
        if merged.get("sort_by"):
            sort_cols = [c for c in merged["sort_by"] if c in df.columns]
            if sort_cols:
                df = df.sort_values(by=sort_cols, ascending=merged.get("ascending", True))

        if merged.get("as_json", True):
            rows = df.to_dict(orient="records" if merged.get("records", True) else "split")
            return {
                "ok": True,
                "rows": rows,
                "columns": list(df.columns),
                "count": len(df),
            }

        return {
            "ok": True,
            "df": df,
            "columns": list(df.columns),
            "count": len(df),
        }

    # -------------------------------------------------------------------------
    # Profiling / shape inference
    # -------------------------------------------------------------------------

    def profile_fields(self, cfg: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Profile fields across extracted or provided records.

        This is intended as the beginning of a future "learn how this kind of table
        behaves" system.

        Args dict keys:
            records: list[dict]
            include_regex: bool
            include_examples: int
        """
        merged = self._merge_cfg(cfg, {
            "records": None,
            "include_regex": True,
            "include_examples": 3,
        })

        records = merged.get("records")
        if records is None:
            records = self.extract_rows({})

        by_field = defaultdict(list)
        for rec in records:
            if isinstance(rec, dict):
                for k, v in rec.items():
                    by_field[k].append(v)

        report = {}

        for field, values in by_field.items():
            str_values = [str(v) for v in values if v is not None]
            shapes = [tuple(self.compress_shape({"value": v})) for v in str_values]
            common_shape = Counter(shapes).most_common(1)[0][0] if shapes else None

            report[field] = {
                "count": len(values),
                "types": sorted({type(v).__name__ for v in values}),
                "examples": str_values[:merged.get("include_examples", 3)],
                "common_shape": common_shape,
                "regex_candidate": self.shape_to_regex({"shape": common_shape}) if (common_shape and merged.get("include_regex", True)) else None,
                "simple_pattern_examples": [self.infer_pattern({"value": v}) for v in str_values[:merged.get("include_examples", 3)]],
            }

        self.state["profiles"]["last"] = report
        return report

    def infer_pattern(self, cfg: Optional[Dict[str, Any]] = None) -> str:
        """
        Simple character-by-character pattern inference.

        Example:
            ABC-1234 -> [A-Z][A-Z][A-Z]\\-\\d\\d\\d\\d

        This is intentionally literal and useful for quick profiling.
        """
        merged = self._merge_cfg(cfg, {
            "value": "",
        })

        s = str(merged.get("value", ""))
        patterns = {
            r"[A-Z]": r"[A-Z]",
            r"[a-z]": r"[a-z]",
            r"[0-9]": r"\d",
            r"\s": r"\s",
        }

        result = []
        for c in s:
            matched = False
            for k, v in patterns.items():
                if re.match(k, c):
                    result.append(v)
                    matched = True
                    break
            if not matched:
                result.append(re.escape(c))

        return "".join(result)

    def compress_shape(self, cfg: Optional[Dict[str, Any]] = None) -> List[Tuple[str, int]]:
        """
        Compress string into token/count shape.

        Example:
            INV-2024-001 -> [('A', 3), ('-', 1), ('9', 4), ('-', 1), ('9', 3)]

        Tokens:
            A = uppercase
            a = lowercase
            9 = digit
            ' ' = whitespace
            literal punctuation kept as-is
        """
        merged = self._merge_cfg(cfg, {
            "value": "",
        })

        s = merged.get("value")
        if s is None:
            return []

        raw = [self._classify_char(c) for c in str(s)]
        out = []
        i = 0
        while i < len(raw):
            j = i
            while j < len(raw) and raw[j] == raw[i]:
                j += 1
            token = raw[i]
            count = j - i
            out.append((token, count))
            i = j
        return out

    def shape_to_regex(self, cfg: Optional[Dict[str, Any]] = None) -> Optional[str]:
        """
        Convert compressed shape to regex candidate.
        """
        merged = self._merge_cfg(cfg, {
            "shape": None,
        })

        shape = merged.get("shape")
        if not shape:
            return None

        parts = []
        for token, count in shape:
            if token == "A":
                parts.append(rf"[A-Z]{{{count}}}")
            elif token == "a":
                parts.append(rf"[a-z]{{{count}}}")
            elif token == "9":
                parts.append(rf"\d{{{count}}}")
            elif token == " ":
                parts.append(rf"\s{{{count}}}")
            else:
                parts.append(re.escape(token) + (rf"{{{count}}}" if count > 1 else ""))

        return "^" + "".join(parts) + "$"

    # -------------------------------------------------------------------------
    # PDF extraction
    # -------------------------------------------------------------------------

    def _extract_pdf_text(self, cfg: Dict[str, Any]) -> str:
        """
        Extract PDF text with layout-aware preference.

        Current implementation:
        - tries pdfminer.six first
        - falls back to empty string if unavailable

        You can later expand this to:
        - select extraction engine
        - expose LAParams knobs
        - preserve lines/coordinates in JSON
        """
        path = cfg.get("path")
        if not path:
            return ""

        try:
            from pdfminer.high_level import extract_text
            text = extract_text(path)
            return text or ""
        except Exception as e:
            self._debug(f"pdfminer extraction failed: {e}")
            return ""

    def _extract_pdf_markdown(self, cfg: Dict[str, Any]) -> str:
        """
        Extract Markdown from PDF if pymupdf4llm is installed.

        Future:
        - attach heading paths
        - preserve tables separately
        - capture links and page metadata
        """
        path = cfg.get("path")
        if not path:
            return ""

        try:
            import pymupdf4llm
            md = pymupdf4llm.to_markdown(path)
            return md or ""
        except Exception as e:
            self._debug(f"pymupdf4llm markdown extraction failed: {e}")
            return ""

    def _extract_pdf_prominent_table_rows(self, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract the most prominent table from a PDF and return rows as list[dict].

        Strategy:
        - gather table candidates page by page
        - score them
        - choose best one
        - convert first row to headers if sensible

        Notes:
        - This is intentionally heuristic.
        - Future build-out should preserve:
            * page number
            * bbox
            * nearby lines
            * subtotal/total lines outside formal table box
        """
        path = cfg.get("path")
        if not path:
            return []

        candidates = self._extract_pdf_table_candidates({"path": path})
        if not candidates:
            return []

        best = sorted(candidates, key=lambda x: x.get("_score", 0), reverse=True)[0]
        matrix = best.get("matrix", [])
        return self._matrix_to_rows({
            "matrix": matrix,
        })

    def _extract_pdf_all_tables_rows(self, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Extract all PDF tables and flatten them into one row stream.

        Future:
        - maybe return grouped by table id instead of flattening
        """
        path = cfg.get("path")
        if not path:
            return []

        candidates = self._extract_pdf_table_candidates({"path": path})
        out = []

        for idx, item in enumerate(candidates):
            matrix = item.get("matrix", [])
            rows = self._matrix_to_rows({"matrix": matrix})
            for row in rows:
                row["_table_index"] = idx
                row["_page"] = item.get("page")
                out.append(row)

        return out

    def _extract_pdf_table_candidates(self, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Use pdfplumber to gather candidate tables.

        Scoring favors:
        - more rows
        - more cols
        - more filled cells

        Future:
        - numeric density
        - header-likeness
        - proximity of totals/subtotals
        - repeated invoice patterns
        """
        path = cfg.get("path")
        if not path:
            return []

        candidates = []

        try:
            import pdfplumber
        except Exception as e:
            self._debug(f"pdfplumber not available: {e}")
            return []

        try:
            with pdfplumber.open(path) as pdf:
                for page_num, page in enumerate(pdf.pages, start=1):
                    tables = page.extract_tables() or []
                    for tbl in tables:
                        if not tbl:
                            continue

                        row_count = len(tbl)
                        col_count = max((len(r) for r in tbl if r), default=0)
                        non_empty = sum(
                            1 for r in tbl for c in (r or []) if c not in (None, "", " ")
                        )
                        score = (row_count * 3) + (col_count * 2) + non_empty

                        candidates.append({
                            "page": page_num,
                            "matrix": tbl,
                            "_score": score,
                        })
        except Exception as e:
            self._debug(f"pdfplumber table extraction failed: {e}")

        return candidates

    # -------------------------------------------------------------------------
    # Text table parsing
    # -------------------------------------------------------------------------

    def _parse_fixed_width_text_table(self, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Parse fixed-width / column-spaced text into rows.

        This is intended for:
        - tasklist
        - command output
        - copied tables from terminals
        - layout-ish text where columns are mostly spacing-based

        Current heuristic:
        1. split lines
        2. find a likely header row
        3. infer column ranges from runs of 2+ spaces
        4. slice remaining lines into same ranges

        Future:
        - smarter multi-line headers
        - tolerance for wrapped cells
        - profile-driven reparse memory
        """
        text = cfg.get("text", "") or ""
        header_row_index = int(cfg.get("header_row_index", 0))

        lines = [line.rstrip("\n\r") for line in text.splitlines()]
        lines = [line for line in lines if line.strip()]

        if not lines:
            return []

        # If caller explicitly picked a header row, use it when possible.
        if 0 <= header_row_index < len(lines):
            header_line = lines[header_row_index]
        else:
            header_line = self._guess_header_line({"lines": lines})

        if not header_line:
            return []

        ranges = self._infer_column_ranges_from_line({"line": header_line})
        if not ranges:
            return []

        headers = self._slice_line_by_ranges({
            "line": header_line,
            "ranges": ranges,
        })

        headers = [self._clean_header_name({"value": h}) for h in headers]

        data_started = False
        rows = []

        for line in lines:
            if line == header_line:
                data_started = True
                continue

            # ignore obvious underline separator rows
            if re.fullmatch(r"[\-\=\s]+", line):
                continue

            if not data_started:
                continue

            cells = self._slice_line_by_ranges({
                "line": line,
                "ranges": ranges,
            })

            # Skip lines that are basically empty.
            if not any(str(c).strip() for c in cells):
                continue

            row = {}
            for i, header in enumerate(headers):
                header_name = header if header else f"col_{i + 1}"
                value = cells[i] if i < len(cells) else ""
                row[header_name] = value.strip()

            rows.append(row)

        return rows

    def _guess_header_line(self, cfg: Dict[str, Any]) -> str:
        """
        Guess header line from text lines.

        Current heuristic:
        - prefer lines with several chunks separated by 2+ spaces
        - prefer alphabetic chunk density
        """
        lines = cfg.get("lines", [])
        best_score = -1
        best_line = ""

        for line in lines[:20]:
            chunks = re.split(r"\s{2,}", line.strip())
            if len(chunks) < 2:
                continue

            alpha_chunks = sum(1 for c in chunks if re.search(r"[A-Za-z]", c))
            score = (len(chunks) * 5) + (alpha_chunks * 3)

            if score > best_score:
                best_score = score
                best_line = line

        return best_line

    def _infer_column_ranges_from_line(self, cfg: Dict[str, Any]) -> List[Tuple[int, int]]:
        """
        Infer column character ranges from a header line using 2+ spaces as separators.

        Example:
            Name      PID      Mem Usage
        becomes rough positional spans for slicing data rows.

        Future:
        - allow padding tolerance
        - consider vertical consistency across multiple lines
        """
        line = cfg.get("line", "")
        if not line:
            return []

        # Find non-space runs separated by 2+ spaces.
        parts = []
        start = None
        in_text = False

        for i, ch in enumerate(line):
            if not ch.isspace():
                if not in_text:
                    start = i
                    in_text = True
            else:
                # if currently in text, check whether next chars imply a separator
                if in_text:
                    # actual boundary handled below by regex fallback
                    pass

        ranges = []
        for m in re.finditer(r"\S(?:.*?\S)?(?=\s{2,}|\s*$)", line):
            ranges.append((m.start(), m.end()))

        # Expand each range to begin/end midpoint between columns.
        if not ranges:
            return []

        expanded = []
        for idx, (s, e) in enumerate(ranges):
            left = s
            right = e
            if idx < len(ranges) - 1:
                next_s, _ = ranges[idx + 1]
                mid = (e + next_s) // 2
                right = mid
            expanded.append((left, right))

        # Final column extends to line end plus padding.
        if expanded:
            last_s, last_e = expanded[-1]
            expanded[-1] = (last_s, max(last_e, len(line)))

        return expanded

    def _slice_line_by_ranges(self, cfg: Dict[str, Any]) -> List[str]:
        """
        Slice a line by character ranges.
        """
        line = cfg.get("line", "")
        ranges = cfg.get("ranges", [])
        cells = []
        for start, end in ranges:
            cells.append(line[start:end].strip())
        return cells

    def _matrix_to_rows(self, cfg: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Convert matrix/list-of-lists table into list-of-dict rows.

        Current assumption:
        - first row is header

        Future:
        - header detection scoring
        - multi-row header flattening
        - table profile memory
        """
        matrix = cfg.get("matrix", [])
        if not matrix:
            return []

        header = matrix[0] or []
        header = [self._clean_header_name({"value": h}) or f"col_{i+1}" for i, h in enumerate(header)]

        rows = []
        for raw_row in matrix[1:]:
            if raw_row is None:
                continue
            row = {}
            for i, key in enumerate(header):
                val = raw_row[i] if i < len(raw_row) else None
                row[key] = "" if val is None else str(val).strip()
            rows.append(row)

        return rows

    # -------------------------------------------------------------------------
    # Filtering helpers
    # -------------------------------------------------------------------------

    def _apply_where_df(self, cfg: Dict[str, Any]):
        """
        Apply where filters to a pandas DataFrame.

        Supported ops:
            eq, ne, gt, gte, lt, lte, contains, regex, in

        Example:
            "where": [
                {"field": "Name", "op": "contains", "value": "chrome"},
                {"field": "MemUsage", "op": "gt", "value": 100000}
            ]
        """
        df = cfg.get("df")
        where = cfg.get("where", [])

        if df is None or not where:
            return df

        for rule in where:
            field = rule.get("field")
            op = rule.get("op", "eq")
            value = rule.get("value")

            if field not in df.columns:
                continue

            series = df[field]

            try:
                if op == "eq":
                    df = df[series == value]
                elif op == "ne":
                    df = df[series != value]
                elif op == "gt":
                    df = df[series > value]
                elif op == "gte":
                    df = df[series >= value]
                elif op == "lt":
                    df = df[series < value]
                elif op == "lte":
                    df = df[series <= value]
                elif op == "contains":
                    df = df[series.astype(str).str.contains(str(value), na=False, regex=False)]
                elif op == "regex":
                    df = df[series.astype(str).str.contains(str(value), na=False, regex=True)]
                elif op == "in":
                    vals = value if isinstance(value, (list, tuple, set)) else [value]
                    df = df[series.isin(vals)]
            except Exception as e:
                self._debug(f"where rule failed: {rule} :: {e}")

        return df

    # -------------------------------------------------------------------------
    # Utility helpers
    # -------------------------------------------------------------------------

    def _classify_char(self, c: str) -> str:
        if c.isupper():
            return "A"
        if c.islower():
            return "a"
        if c.isdigit():
            return "9"
        if c.isspace():
            return " "
        return c

    def _clean_header_name(self, cfg: Dict[str, Any]) -> str:
        """
        Normalize header names into something stable but readable.

        Example:
            "Mem Usage" -> "MemUsage"
            "Session#" -> "Session"
        """
        value = cfg.get("value")
        if value is None:
            return ""

        s = str(value).strip()
        if not s:
            return ""

        # Remove obvious punctuation except spaces/underscores.
        s = re.sub(r"[^\w\s]", "", s)
        parts = s.split()
        if not parts:
            return ""

        # Camel-ish collapse
        return "".join(p[:1].upper() + p[1:] for p in parts)

    def _merge_cfg(self, cfg: Optional[Dict[str, Any]], extra_defaults: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Merge object config + method config + optional defaults.
        Method cfg wins over object cfg.
        """
        base = dict(self.cfg)
        if extra_defaults:
            for k, v in extra_defaults.items():
                if k not in base:
                    base[k] = v
        if cfg:
            for k, v in cfg.items():
                base[k] = v
        return base

    def _defaults(self, cfg: Optional[Dict[str, Any]], defaults: Dict[str, Any]) -> Dict[str, Any]:
        out = dict(defaults)
        if cfg:
            out.update(cfg)
        return out

    def _debug(self, msg: str) -> None:
        if self.cfg.get("debug"):
            sys.stderr.write(f"[DocPipe] {msg}\n")


# -----------------------------------------------------------------------------
# Usage examples
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    """
    Minimal self-test / example area.

    Example 1: parse stdin fixed-width table
        tasklist | python docpipe.py

    Example 2: import style in another file
        from docpipe import DocPipe

        dp = DocPipe({})
        rows = dp.extract_rows({"mode": "fixed_width"})
        print(rows[:3])

    Example 3: PDF text
        dp = DocPipe({"path": "doc.pdf"})
        print(dp.extract_text({}))

    Example 4: PDF prominent table
        dp = DocPipe({"path": "invoice.pdf"})
        rows = dp.extract_rows({"mode": "pdf_prominent_table"})
        print(json.dumps(rows, indent=4))

    Example 5: tasklist-style aggregation
        dp = DocPipe({})
        result = dp.query_table({
            "rows": dp.extract_rows({"mode": "fixed_width"}),
            "select": ["ImageName", "MemUsage"],
            "coerce_numeric": ["MemUsage"],
            "strip_chars": {"MemUsage": r"[^0-9\.\-]"},
            "group_by": ["ImageName"],
            "aggregate": {"MemUsage": "sum"},
            "sort_by": ["MemUsage"],
            "ascending": False,
        })
        print(json.dumps(result, indent=4))

    Example 6: field profiling
        records = [
            {"invoice": "INV-2024-001", "amount": "123.45", "zip": "33761"},
            {"invoice": "INV-2024-002", "amount": "99.00", "zip": "34695"},
            {"invoice": "INV-2025-003", "amount": "25.50", "zip": "33764"},
        ]
        dp = DocPipe({})
        profile = dp.profile_fields({"records": records})
        print(json.dumps(profile, indent=4, default=str))
    """

    dp = DocPipe({})
    rows = dp.extract_rows({"mode": "fixed_width"})
    print(json.dumps(rows, indent=4))