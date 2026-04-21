#!/usr/bin/env python3
from __future__ import annotations

import json
import shlex
import sys
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple
from urllib.parse import parse_qsl, urlparse


# =============================================================================
# Data model
# =============================================================================

@dataclass
class HarRequest:
    index: int
    started: str
    method: str
    url: str
    status: Optional[int]
    mime: str
    domain: str
    path: str
    query: Dict[str, str] = field(default_factory=dict)
    headers: Dict[str, str] = field(default_factory=dict)
    cookies: Dict[str, str] = field(default_factory=dict)
    post_text: Optional[str] = None
    post_mime: Optional[str] = None
    raw_entry: Dict[str, Any] = field(default_factory=dict)

    @property
    def path_parts(self) -> List[str]:
        return [p for p in self.path.split("/") if p]


# =============================================================================
# Switch manager
# =============================================================================

class Switches:
    def __init__(self, argv: List[str]) -> None:
        self.argv = argv[:]
        self.flags: set[str] = set()
        self.values: Dict[str, Any] = {}
        self.get_items: List[str] = []
        self.errors: List[str] = []
        self._parse()

    def _parse(self) -> None:
        args = self.argv[:]
        i = 0

        while i < len(args):
            token = args[i]

            if token in ("-get",):
                # Must be last. Everything after belongs to -get.
                self.get_items = args[i + 1:]
                break

            if token in ("-h", "--help", "-help"):
                self.flags.add("help")
                i += 1
                continue

            if token in ("-nc", "-noComment"):
                self.flags.add("no_comment")
                i += 1
                continue

            if token in ("-ncget", "-getnc"):
                self.flags.add("no_comment_get")
                i += 1
                continue

            if token in ("-mergeRelatedCookies", "-mrc"):
                self.flags.add("merge_related_cookies")
                i += 1
                continue

            if token in ("-keepUserAgent", "-kua"):
                self.flags.add("keep_user_agent")
                i += 1
                continue

            if token in ("-json",):
                self.flags.add("json")
                i += 1
                continue

            if token in ("-f", "-har"):
                if i + 1 >= len(args):
                    self.errors.append(f"Missing value for {token}")
                    break
                self.values["har"] = args[i + 1]
                i += 2
                continue

            if token in ("-u", "-url"):
                if i + 1 >= len(args):
                    self.errors.append(f"Missing value for {token}")
                    break
                self.values["url"] = args[i + 1]
                i += 2
                continue

            if token in ("-output", "-o"):
                if i + 1 >= len(args):
                    self.errors.append(f"Missing value for {token}")
                    break
                self.values["output"] = args[i + 1].strip().lower()
                i += 2
                continue

            if token in ("-pathPopThreshold", "-ppt"):
                if i + 1 >= len(args):
                    self.errors.append(f"Missing value for {token}")
                    break
                try:
                    self.values["path_pop_threshold"] = int(args[i + 1])
                except Exception:
                    self.errors.append(f"Invalid integer for {token}: {args[i + 1]}")
                    break
                i += 2
                continue

            if token in ("-maxRelated", "-mr"):
                if i + 1 >= len(args):
                    self.errors.append(f"Missing value for {token}")
                    break
                try:
                    self.values["max_related"] = int(args[i + 1])
                except Exception:
                    self.errors.append(f"Invalid integer for {token}: {args[i + 1]}")
                    break
                i += 2
                continue

            self.errors.append(f"Unknown switch or argument: {token}")
            i += 1

    def has(self, key: str) -> bool:
        return key in self.flags

    def get(self, key: str, default: Any = None) -> Any:
        return self.values.get(key, default)


# =============================================================================
# HAR loading
# =============================================================================

def load_har(path: str) -> List[HarRequest]:
    with open(path, "r", encoding="utf-8") as f:
        har = json.load(f)

    entries = har.get("log", {}).get("entries", [])
    out: List[HarRequest] = []

    for i, entry in enumerate(entries):
        req = entry.get("request", {}) or {}
        res = entry.get("response", {}) or {}
        raw_url = req.get("url", "") or ""
        parsed = urlparse(raw_url)

        headers: Dict[str, str] = {}
        for h in req.get("headers", []) or []:
            name = h.get("name")
            value = h.get("value")
            if name is not None:
                headers[str(name)] = "" if value is None else str(value)

        cookies: Dict[str, str] = {}
        for c in req.get("cookies", []) or []:
            name = c.get("name")
            value = c.get("value")
            if name is not None:
                cookies[str(name)] = "" if value is None else str(value)

        query: Dict[str, str] = {}
        for q in req.get("queryString", []) or []:
            name = q.get("name")
            value = q.get("value")
            if name is not None:
                query[str(name)] = "" if value is None else str(value)

        if not query and parsed.query:
            query = dict(parse_qsl(parsed.query, keep_blank_values=True))

        post_data = req.get("postData", {}) or {}
        post_text = post_data.get("text")
        post_mime = post_data.get("mimeType")

        out.append(
            HarRequest(
                index=i,
                started=entry.get("startedDateTime", ""),
                method=str(req.get("method", "GET")).upper(),
                url=raw_url,
                status=res.get("status"),
                mime=(res.get("content", {}) or {}).get("mimeType", "") or "",
                domain=parsed.netloc,
                path=parsed.path or "/",
                query=query,
                headers=headers,
                cookies=cookies,
                post_text=post_text,
                post_mime=post_mime,
                raw_entry=entry,
            )
        )

    return out


# =============================================================================
# Utility
# =============================================================================

def q(value: str) -> str:
    return shlex.quote(value)


def py_repr(value: Any) -> str:
    return repr(value)


def lower_keys(d: Dict[str, str]) -> Dict[str, str]:
    return {str(k).lower(): str(v) for k, v in d.items()}


def common_path_prefix_depth(a: str, b: str) -> int:
    a_parts = [p for p in a.split("/") if p]
    b_parts = [p for p in b.split("/") if p]
    depth = 0
    for x, y in zip(a_parts, b_parts):
        if x == y:
            depth += 1
        else:
            break
    return depth


def yaml_scalar(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float)):
        return str(value)
    s = str(value)
    if s == "":
        return '""'
    if any(ch in s for ch in [":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", ">", "-", "%", "@", "!", "\n", "\r", "\t"]) or s.strip() != s:
        return json.dumps(s)
    return s


def print_yaml_block(name: str, data: Any, indent: int = 0) -> None:
    prefix = " " * indent
    if isinstance(data, dict):
        print(f"{prefix}{name}:")
        if not data:
            print(f"{prefix}  {{}}")
            return
        for k, v in data.items():
            if isinstance(v, (dict, list)):
                print_yaml_block(str(k), v, indent + 2)
            else:
                print(f"{prefix}  {k}: {yaml_scalar(v)}")
        return

    if isinstance(data, list):
        print(f"{prefix}{name}:")
        if not data:
            print(f"{prefix}  []")
            return
        for item in data:
            if isinstance(item, dict):
                print(f"{prefix}  -")
                for k, v in item.items():
                    if isinstance(v, (dict, list)):
                        print_yaml_block(str(k), v, indent + 6)
                    else:
                        print(f"{prefix}    {k}: {yaml_scalar(v)}")
            else:
                print(f"{prefix}  - {yaml_scalar(item)}")
        return

    print(f"{prefix}{name}: {yaml_scalar(data)}")


def filter_headers_for_output(headers: Dict[str, str], keep_user_agent: bool = False) -> Dict[str, str]:
    blocked = {
        "host",
        "content-length",
        "cookie",
        ":authority",
        ":method",
        ":path",
        ":scheme",
    }
    if not keep_user_agent:
        blocked.add("user-agent")

    out: Dict[str, str] = {}
    for k, v in headers.items():
        if k.lower().strip() in blocked:
            continue
        out[k] = v
    return out


def find_target(requests: List[HarRequest], target_url: str) -> Optional[HarRequest]:
    exact = [r for r in requests if r.url == target_url]
    if exact:
        return exact[-1]

    p = urlparse(target_url)
    loose = [r for r in requests if r.domain == p.netloc and r.path == (p.path or "/")]
    if loose:
        return loose[-1]

    return None


def collect_prior_relevant(
    requests: List[HarRequest],
    target: HarRequest,
    path_pop_threshold: int,
    max_results: int
) -> List[Tuple[int, HarRequest]]:
    out: List[Tuple[int, HarRequest]] = []

    for r in requests:
        if r.index >= target.index:
            continue
        if r.domain != target.domain:
            continue

        depth = common_path_prefix_depth(r.path, target.path)
        if depth < path_pop_threshold:
            continue

        score = depth * 100
        if r.method == target.method:
            score += 25
        if r.status and 200 <= r.status < 400:
            score += 10
        if r.path != target.path:
            score += 15

        out.append((score, r))

    out.sort(key=lambda x: (x[0], x[1].index), reverse=True)
    return out[:max_results]


def merge_cookies(target: HarRequest, related: List[Tuple[int, HarRequest]]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for _, r in sorted(related, key=lambda x: x[1].index):
        for k, v in r.cookies.items():
            out[k] = v
    for k, v in target.cookies.items():
        out[k] = v
    return out


def cookie_header(cookies: Dict[str, str]) -> Optional[str]:
    if not cookies:
        return None
    return "; ".join(f"{k}={v}" for k, v in cookies.items())


def choose_get_params(query: Dict[str, str], include_all_get: bool, selected_get_items: List[str]) -> Dict[str, str]:
    if not query:
        return {}

    if include_all_get:
        return dict(query)

    if selected_get_items:
        out: Dict[str, str] = {}
        for key in selected_get_items:
            if key in query:
                out[key] = query[key]
        return out

    return {}


# =============================================================================
# Generators
# =============================================================================

def make_curl(
    target: HarRequest,
    headers: Dict[str, str],
    cookies: Dict[str, str],
    include_comment: bool,
    include_get_in_comment: bool,
    shown_get: Dict[str, str]
) -> str:
    lines: List[str] = []

    if include_comment:
        lines.append("## Request extracted from HAR")
        lines.append(f"## URL: {target.url}")
        lines.append(f"## Method: {target.method}")
        if include_get_in_comment and shown_get:
            lines.append("## Selected query parameters included below for inspection")
        lines.append("")

    lines.append(f"curl {q(target.url)} \\")
    lines.append(f"  -X {target.method} \\")

    ch = cookie_header(cookies)
    if ch:
        lines.append(f"  -H {q('Cookie: ' + ch)} \\")

    for k, v in headers.items():
        lines.append(f"  -H {q(f'{k}: {v}')} \\")

    if target.post_text is not None:
        if target.post_mime and "content-type" not in lower_keys(headers):
            lines.append(f"  -H {q('Content-Type: ' + target.post_mime)} \\")
        lines.append(f"  --data-raw {q(target.post_text)} \\")

    if lines[-1].endswith(" \\"):
        lines[-1] = lines[-1][:-2]

    return "\n".join(lines)


def make_python(
    target: HarRequest,
    headers: Dict[str, str],
    cookies: Dict[str, str],
    include_comment: bool,
    include_get_in_comment: bool,
    shown_get: Dict[str, str]
) -> str:
    lines: List[str] = []

    lines.append("import requests")
    lines.append("")
    lines.append("")

    lines.append("def run_har_request():")

    if include_comment:
        doc = [
            '    """',
            "    Execute a request reconstructed from a HAR entry.",
            f"    URL: {target.url}",
            f"    Method: {target.method}",
        ]
        if include_get_in_comment and shown_get:
            doc.append(f"    Query keys shown: {', '.join(shown_get.keys())}")
        if target.post_text is not None:
            doc.append("    Includes captured request body from the HAR entry.")
        if cookies:
            doc.append("    Includes cookies associated with this request chain.")
        doc.append('    """')
        lines.extend(doc)

    lines.append(f"    url = {py_repr(target.url)}")
    lines.append(f"    method = {py_repr(target.method)}")
    lines.append(f"    headers = {py_repr(headers)}")
    lines.append(f"    cookies = {py_repr(cookies)}")

    if target.post_text is not None:
        lines.append(f"    data = {py_repr(target.post_text)}")
    else:
        lines.append("    data = None")

    lines.append("")
    lines.append("    response = requests.request(")
    lines.append("        method=method,")
    lines.append("        url=url,")
    lines.append("        headers=headers,")
    lines.append("        cookies=cookies,")
    lines.append("        data=data,")
    lines.append("        timeout=30,")
    lines.append("    )")
    lines.append("")
    lines.append("    print('status:', response.status_code)")
    lines.append("    print('content-type:', response.headers.get('Content-Type', ''))")
    lines.append("    print(response.text)")
    lines.append("    return response")
    lines.append("")
    lines.append("")

    if include_comment:
        lines.append('"""')
        lines.append("Execute the generated request function.")
        lines.append("This runs the reconstructed HAR request immediately.")
        lines.append('"""')

    lines.append("run_har_request()")

    return "\n".join(lines)


# =============================================================================
# Output helpers
# =============================================================================

def print_help() -> None:
    text = r"""
harTool.py

Purpose:
  Extract a request from a HAR and output either:
  - a curl command
  - executable Python code
  - or, if -output is omitted, a structured YAML-like summary

Required:
  -f <har_file>
  -u <url>

Optional:
  -output <curl|python>
      Output format. If omitted, prints YAML-like structured data.

  -nc
  -noComment
      Suppress comments/docstrings in generated output.

  -ncget
  -getnc
      Include GET/query items in summary or comments.
      Without this switch, GET is kept stingy by default.

  -get <key1> <key2> ...
      Include only specific GET/query keys.
      This switch must be last so all remaining space-delimited items
      are treated as GET keys to include.

  -ppt
  -pathPopThreshold <int>
      Minimum shared path depth for related prior same-domain requests.
      Default: 2

  -mr
  -maxRelated <int>
      Max related prior requests to include in analysis.
      Default: 15

  -mrc
  -mergeRelatedCookies
      Merge cookies from related prior same-domain requests.

  -kua
  -keepUserAgent
      Keep User-Agent in the generated output.

Examples:
  python harTool.py -f site.har -u https://www.ecompute.com/api/v2/cities

  python harTool.py -f site.har -u https://www.ecompute.com/api/v2/cities -ncget

  python harTool.py -f site.har -u https://www.ecompute.com/api/v2/cities -output curl -nc

  python harTool.py -f site.har -u https://www.ecompute.com/api/v2/cities -output python -ncget

  python harTool.py -f site.har -u https://www.ecompute.com/api/v2/cities -get search state

Notes:
  - If -output is omitted, the tool prints a YAML-like inspection view.
  - Use -ncget or -getnc when you want all GET/query values shown.
  - Use -get last when you want only selected GET/query keys shown.
"""
    print(text.strip())


def print_missing_required_help(missing: List[str]) -> None:
    print("Missing required argument(s): " + ", ".join(missing))
    print("")
    print_help()


def print_yaml_summary(
    target: HarRequest,
    related: List[Tuple[int, HarRequest]],
    shown_get: Dict[str, str],
    headers: Dict[str, str],
    cookies: Dict[str, str]
) -> None:
    payload: Dict[str, Any] = {
        "target": {
            "index": target.index,
            "started": target.started,
            "method": target.method,
            "url": target.url,
            "status": target.status,
            "mime": target.mime,
            "domain": target.domain,
            "path": target.path,
        },
        "relevant": {
            "cookies": cookies,
            "headers": headers,
        },
        "related_prior_same_domain": [
            {
                "score": score,
                "index": r.index,
                "method": r.method,
                "status": r.status,
                "url": r.url,
                "path": r.path,
                "shared_path_depth": common_path_prefix_depth(r.path, target.path),
            }
            for score, r in related
        ],
    }

    if shown_get:
        payload["relevant"]["get"] = shown_get

    if target.post_text is not None:
        payload["relevant"]["post"] = {
            "mime": target.post_mime,
            "text": target.post_text,
        }

    print_yaml_block("result", payload)


# =============================================================================
# Main
# =============================================================================

def main() -> int:
    sw = Switches(sys.argv[1:])

    if sw.errors:
        for err in sw.errors:
            print(f"ERROR: {err}", file=sys.stderr)
        print("", file=sys.stderr)
        print_help()
        return 1

    if not sys.argv[1:] or sw.has("help"):
        print_help()
        return 0

    missing: List[str] = []
    if not sw.get("har"):
        missing.append("-f")
    if not sw.get("url"):
        missing.append("-u")

    if missing:
        print_missing_required_help(missing)
        return 1

    output = sw.get("output")
    if output not in (None, "curl", "python"):
        print(f"ERROR: Invalid -output value: {output}", file=sys.stderr)
        print("Allowed values: curl, python", file=sys.stderr)
        return 1

    path_pop_threshold = sw.get("path_pop_threshold", 2)
    max_related = sw.get("max_related", 15)
    keep_user_agent = sw.has("keep_user_agent")
    include_comments = not sw.has("no_comment")
    include_all_get = sw.has("no_comment_get")
    selected_get = sw.get_items[:]

    try:
        requests = load_har(sw.get("har"))
    except FileNotFoundError:
        print(f"ERROR: HAR file not found: {sw.get('har')}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"ERROR: Failed to load HAR: {e}", file=sys.stderr)
        return 1

    target = find_target(requests, sw.get("url"))
    if target is None:
        print(f"ERROR: Target URL not found in HAR: {sw.get('url')}", file=sys.stderr)
        return 1

    related = collect_prior_relevant(
        requests=requests,
        target=target,
        path_pop_threshold=path_pop_threshold,
        max_results=max_related,
    )

    cookies = dict(target.cookies)
    if sw.has("merge_related_cookies"):
        cookies = merge_cookies(target, related)

    headers = filter_headers_for_output(target.headers, keep_user_agent=keep_user_agent)
    shown_get = choose_get_params(
        query=target.query,
        include_all_get=include_all_get,
        selected_get_items=selected_get,
    )

    if output is None:
        print_yaml_summary(
            target=target,
            related=related,
            shown_get=shown_get,
            headers=headers,
            cookies=cookies,
        )
        return 0

    if output == "curl":
        print(
            make_curl(
                target=target,
                headers=headers,
                cookies=cookies,
                include_comment=include_comments,
                include_get_in_comment=(include_all_get or bool(selected_get)),
                shown_get=shown_get,
            )
        )
        return 0

    if output == "python":
        print(
            make_python(
                target=target,
                headers=headers,
                cookies=cookies,
                include_comment=include_comments,
                include_get_in_comment=(include_all_get or bool(selected_get)),
                shown_get=shown_get,
            )
        )
        return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())