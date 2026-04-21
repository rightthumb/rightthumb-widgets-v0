#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
webcopy_threaded.py — Threaded webpage copier & crawler (per-domain concurrency)
- Prompts are modular & easily swappable for CLI switches (see PROMPTING SECTION)
- Accepts pasted text OR line-separated URLs; extracts http(s):// links automatically
- Per-domain concurrency limit (Semaphore) + thread pool crawl
- Resolves redirects, accepts cookies, retries, SSL verify=False (curl -k)
- Rewrites assets to RELATIVE paths; anchors only if saved
- Final post-pass reopens saved HTML to rewrite anchors discovered later in parallel
- Handles CSS url()/@import/srcset; supports <meta http-equiv="refresh"> redirects
"""

from __future__ import annotations
import os
import re
import sys
import mimetypes
import pathlib
import hashlib
import urllib.parse as up
from dataclasses import dataclass
from typing import Optional, Tuple, Set, Dict, List
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from queue import Queue, Empty
from threading import Lock, Semaphore

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup

# =========================
# Constants & Small Helpers
# =========================

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
      "AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0.0.0 Safari/537.36")

DEFAULT_HEADERS = {
    "User-Agent": UA,
    "Accept": "*/*",
    "Connection": "keep-alive",
}

SAFE_EXT_BY_MIME = {
    "text/html": ".html",
    "text/css": ".css",
    "application/javascript": ".js",
    "text/javascript": ".js",
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "font/woff2": ".woff2",
    "font/woff": ".woff",
    "font/ttf": ".ttf",
    "font/otf": ".otf",
    "application/font-woff": ".woff",
    "audio/mpeg": ".mp3",
    "audio/ogg": ".ogg",
    "video/mp4": ".mp4",
    "video/webm": ".webm",
}

ASSET_TAG_ATTRS = {
    "link": ["href"],
    "script": ["src"],
    "img": ["src", "srcset"],
    "source": ["src", "srcset"],
    "video": ["poster", "src"],
    "audio": ["src"],
    "iframe": ["src"],
    "embed": ["src"],
    "track": ["src"],
}
NAV_TAG_ATTRS = {
    "a": ["href"],
}

CSS_URL_PATTERN = re.compile(r'''url\(\s*(['"]?)(?P<url>[^'")]+)\1\s*\)''', re.IGNORECASE)
CSS_IMPORT_PATTERN = re.compile(r'''@import\s+(?:url\()?['"]?(?P<url>[^'")\s]+)['"]?\)?''', re.IGNORECASE)
SRCSET_SPLIT = re.compile(r'\s*,\s*')
URL_FINDER = re.compile(r'https?://[^\s)>\]"}]+', re.IGNORECASE)

def _default_port(scheme: str) -> int:
    return 443 if scheme == "https" else 80

def _same_origin(u1: str, u2: str) -> bool:
    p1, p2 = up.urlparse(u1), up.urlparse(u2)
    return (p1.scheme, p1.hostname, (p1.port or _default_port(p1.scheme))) == \
           (p2.scheme, p2.hostname, (p2.port or _default_port(p2.scheme)))

def _normalize(url: str) -> str:
    p = up.urlparse(url)
    return p._replace(fragment="").geturl()

def _hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", errors="ignore")).hexdigest()[:16]

def _ensure_dir(p: pathlib.Path) -> None:
    p.mkdir(parents=True, exist_ok=True)

def _relpath(from_path: pathlib.Path, to_path: pathlib.Path) -> str:
    try:
        return os.path.relpath(to_path, start=from_path.parent)
    except Exception:
        return to_path.name

def _guess_is_html(content_type: Optional[str], url: str) -> bool:
    if content_type and "html" in content_type.lower():
        return True
    ext = os.path.splitext(up.urlparse(url).path)[1].lower()
    return ext in ("", ".html", ".htm", ".php", ".asp", ".aspx", ".jsp")


# ============
# Data Models
# ============

@dataclass
class CrawlPlan:
    start_urls: List[str]
    save_root: pathlib.Path
    crawl_local_depth: Optional[int]       # None = ALL
    follow_externals: bool
    crawl_external_depth: Optional[int]    # None = ALL
    max_threads_per_domain: int            # per-domain concurrency limit
    max_workers: int                       # overall threadpool size


# =================
# Core Threaded App
# =================

class WebpageCopier:
    """Threaded copier with per-domain concurrency, anchor-only-if-saved rewrites,
    and a final post-pass to tighten relative links."""

    def __init__(self, plan: CrawlPlan):
        self.plan = plan
        _ensure_dir(self.plan.save_root)

        self.session = self._build_session()

        # thread-safe caches & state
        self.cache = self.Cache(self.plan.save_root)
        self.visited_pages: Set[str] = set()
        self.visited_lock = Lock()

        self.enqueued: Set[Tuple[str, int, bool]] = set()  # (url, depth, is_ext) seen
        self.enqueued_lock = Lock()

        self.queue: "Queue[Tuple[str,int,bool,str]]" = Queue()  # (url, depth, is_ext, origin0)

        # domain limiters
        self.domain_semaphores: Dict[str, Semaphore] = defaultdict(
            lambda: Semaphore(self.plan.max_threads_per_domain)
        )

        # for final post-pass
        self.saved_html_paths: Set[pathlib.Path] = set()
        self.saved_html_lock = Lock()

    # ---------- Public orchestration ----------

    @classmethod
    def from_prompts(cls) -> "WebpageCopier":
        """
        PROMPTING SECTION:
        This block is designed to be **easily swapped** with your framework’s switches.
        Replace reads with your own config loader and return a CrawlPlan.

        Inputs accepted:
        - Single URL
        - Multiple URLs (one per line)
        - Pasted text containing links (we'll extract them)
        """
        def _in(prompt: str) -> str:
            try:
                return input(prompt).strip()
            except EOFError:
                return ""

        # 1) Collect URL(s) or pasted text (we auto-extract links)
        raw = _in("Start URL(s) or paste text with links (end with Enter):\n> ")
        if not raw:
            print("No input provided. Exiting.")
            sys.exit(1)

        # If it's a single URL without scheme, assume https
        candidates: List[str] = []
        if raw.lower().startswith(("http://", "https://")) and " " not in raw:
            candidates = [raw]
        else:
            # Split lines; collect urls on each line; and also scan free-form text.
            for line in raw.splitlines():
                line = line.strip()
                if not line:
                    continue
                if line.lower().startswith(("http://", "https://")):
                    candidates.append(line)
                else:
                    candidates.extend(URL_FINDER.findall(line))
        # Final fallback: scan entire blob
        if not candidates:
            candidates = URL_FINDER.findall(raw)

        # normalize + add https scheme if missing
        norm_urls = []
        for u in candidates:
            if not up.urlparse(u).scheme:
                u = "https://" + u
            norm_urls.append(_normalize(u))
        norm_urls = list(dict.fromkeys(norm_urls))  # de-dup preserve order
        if not norm_urls:
            print("No valid http(s) links found. Exiting.")
            sys.exit(1)

        follow_ext = _in("Follow external links? [y/N]: ").lower() in ("y", "yes")

        local_depth_str = _in("Local depth (blank = all): ")
        local_depth = None
        if local_depth_str:
            try:
                d = int(local_depth_str)
                local_depth = None if d < 0 else d
            except ValueError:
                local_depth = None

        folder = _in("Folder name to save in (will be created): ")
        if not folder:
            host = up.urlparse(norm_urls[0]).hostname or "site"
            folder = f"cache_{host}"

        # prompt external depth last, only if externals enabled
        external_depth = None
        if follow_ext:
            ext_depth_str = _in("External depth (blank = all): ")
            if ext_depth_str:
                try:
                    d = int(ext_depth_str)
                    external_depth = None if d < 0 else d
                except ValueError:
                    external_depth = None

        # per-domain threads
        per_domain_str = _in("Max threads per domain (default 4): ")
        try:
            max_per_domain = int(per_domain_str) if per_domain_str else 4
        except ValueError:
            max_per_domain = 4
        if max_per_domain < 1:
            max_per_domain = 1

        # overall pool size (sane default = domains * per-domain, capped)
        # You can make this a prompt if you like.
        max_workers = max(8, min(64, max_per_domain * 8))

        plan = CrawlPlan(
            start_urls=norm_urls,
            save_root=pathlib.Path(folder).resolve(),
            crawl_local_depth=local_depth,
            follow_externals=follow_ext,
            crawl_external_depth=external_depth,
            max_threads_per_domain=max_per_domain,
            max_workers=max_workers
        )
        return cls(plan)

    def run(self) -> None:
        self._print_settings()

        # Seed the queue with each start URL
        for u in self.plan.start_urls:
            self._enqueue(u, depth=0, is_ext=False, origin0=u)

        with ThreadPoolExecutor(max_workers=self.plan.max_workers) as pool:
            futures = []
            # Keep submitting tasks while queue has items and futures are running
            while True:
                # Try to drain the queue quickly into futures (bounded by executor)
                drained = 0
                while drained < self.plan.max_workers:
                    try:
                        job = self.queue.get_nowait()
                    except Empty:
                        break
                    drained += 1
                    futures.append(pool.submit(self._worker, job))

                # If nothing to do and no futures pending, we’re done
                if not futures and self.queue.empty():
                    break

                # As futures complete, remove from list (also drives progress)
                done, futures = self._split_done(futures)
                # Loop continues; will refill from queue

        # Final post-pass: update anchors in saved HTML that became available later
        self._finalize_anchor_rewrites()

        print("\nDone. Files saved under:", self.plan.save_root)

    # ---------- Network, session, concurrency ----------

    def _build_session(self) -> requests.Session:
        s = requests.Session()
        s.headers.update(DEFAULT_HEADERS)
        retries = Retry(
            total=5, connect=5, read=5, backoff_factor=2,
            status_forcelist=(500, 502, 503, 504, 522, 524, 408),
            allowed_methods=frozenset(["GET", "HEAD", "OPTIONS"]),
            raise_on_status=False,
        )
        adapter = HTTPAdapter(max_retries=retries, pool_connections=64, pool_maxsize=64)
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        s.verify = False  # curl -k
        s.max_redirects = 30
        return s

    def _domain_sem(self, url: str) -> Semaphore:
        host = up.urlparse(url).hostname or "site"
        return self.domain_semaphores[host]

    def _split_done(self, future_list):
        done = []
        pending = []
        for f in future_list:
            if f.done():
                try:
                    f.result()
                except Exception:
                    # Swallow per-task exceptions; they’re already isolated
                    pass
                done.append(f)
            else:
                pending.append(f)
        return done, pending

    # ---------- Cache (thread-safe) ----------

    class Cache:
        def __init__(self, root: pathlib.Path):
            self.root = root
            _ensure_dir(self.root)
            self.url_to_path: Dict[str, pathlib.Path] = {}
            self._taken: Set[str] = set()
            self.lock = Lock()

        def path_for(self, url: str, content_type: Optional[str], is_html: bool,
                     prefer_dir: Optional[pathlib.Path]) -> pathlib.Path:
            p = up.urlparse(url)
            host_dir = self.root / (p.hostname or "site")
            if prefer_dir is not None:
                subdir = prefer_dir
            else:
                rel_dir = (p.path.strip("/") if p.path.strip("/") else "")
                subdir = host_dir / (os.path.dirname(rel_dir) if rel_dir else "")
            _ensure_dir(subdir)

            name = self._safe_name(url, content_type, is_html)
            with self.lock:
                candidate = subdir / name
                idx = 1
                while str(candidate) in self._taken:
                    stem, ext = os.path.splitext(name)
                    candidate = subdir / f"{stem}_{idx}{ext}"
                    idx += 1
                self._taken.add(str(candidate))
            return candidate

        @staticmethod
        def _safe_name(url: str, content_type: Optional[str], is_html: bool) -> str:
            p = up.urlparse(url)
            base = os.path.basename(p.path.rstrip("/")) or ("index" if is_html else "file")
            root, ext = os.path.splitext(base)
            guessed = SAFE_EXT_BY_MIME.get((content_type or "").split(";")[0].strip(), "")
            if not ext and guessed:
                ext = guessed
            if is_html and ext.lower() not in (".html", ".htm", ""):
                ext = ".html"
            if not ext and not is_html:
                g = mimetypes.guess_extension((content_type or "").split(";")[0].strip())
                if g:
                    ext = g
            qfrag = f"{p.query}#{p.fragment}".strip()
            if qfrag:
                name = f"{root}~h{_hash(qfrag)}{ext}"
            else:
                name = f"{root}{ext}"
            name = re.sub(r'[^A-Za-z0-9._@\-+~]+', '_', name)
            return name or "index.html"

    # ---------- Crawl queueing ----------

    def _enqueue(self, url: str, depth: int, is_ext: bool, origin0: str) -> None:
        url = _normalize(url)
        key = (url, depth, is_ext)
        with self.enqueued_lock:
            if key in self.enqueued:
                return
            self.enqueued.add(key)
        self.queue.put((url, depth, is_ext, origin0))

    # ---------- Worker ----------

    def _worker(self, job: Tuple[str, int, bool, str]) -> None:
        url, depth, is_ext, origin0 = job

        # check visited
        with self.visited_lock:
            if url in self.visited_pages:
                return
            self.visited_pages.add(url)

        sem = self._domain_sem(url)
        with sem:
            local_path, ctype = self._download(url, prefer_dir=None)
        if not local_path:
            return

        # If HTML: process & enqueue new links
        if not _guess_is_html(ctype, url):
            return

        # Ensure .html extension for easy offline opening
        if local_path.suffix.lower() not in (".html", ".htm"):
            new_path = local_path.with_suffix(".html")
            try:
                local_path.rename(new_path)
                with self.cache.lock:
                    self.cache.url_to_path[url] = new_path
                local_path = new_path
            except Exception:
                pass

        self._parse_and_rewrite_html(page_url=url, html_path=local_path)

        with self.saved_html_lock:
            self.saved_html_paths.add(local_path)

        # Extract links & enqueue
        for link in sorted(self._extract_links(local_path, url)):
            external = not _same_origin(origin0, link)
            if external and not self.plan.follow_externals:
                continue
            next_depth = depth + 1
            if external:
                if self.plan.crawl_external_depth is not None and next_depth > self.plan.crawl_external_depth:
                    continue
            else:
                if self.plan.crawl_local_depth is not None and next_depth > self.plan.crawl_local_depth:
                    continue
            self._enqueue(link, next_depth, external, origin0)

    # ---------- Download ----------

    def _download(self, url: str, prefer_dir: Optional[pathlib.Path]) -> Tuple[Optional[pathlib.Path], Optional[str]]:
        url = _normalize(url)
        with self.cache.lock:
            existing = self.cache.url_to_path.get(url)
        if existing:
            return existing, None

        # HTTP GET with redirects/cookies/retries (verify=False)
        try:
            resp = self.session.get(url, allow_redirects=True, timeout=(10, 120), verify=False, stream=True)
        except requests.RequestException:
            return None, None

        # Handle meta refresh HTML that immediately redirects to another URL (link hubs sometimes do this)
        ctype = (resp.headers.get("Content-Type") or "").split(";")[0].strip()
        body_bytes = b""
        is_html = _guess_is_html(ctype, url)
        if is_html:
            # Buffer small HTML to inspect meta refresh; fallback stream for non-HTML
            try:
                body_bytes = resp.content
            except Exception:
                pass
            target = self._extract_meta_refresh_target(body_bytes, base_url=resp.url)
            if target:
                # Save small stub page (optional) then enqueue target (respecting depth rules via worker)
                # But since we don't have depth context here, we just continue saving current page
                pass

        # Save to cache path
        local_path = self.cache.path_for(url, ctype, is_html, prefer_dir)
        try:
            if body_bytes:
                local_path.write_bytes(body_bytes)
            else:
                with open(local_path, "wb") as f:
                    for chunk in resp.iter_content(chunk_size=64 * 1024):
                        if chunk:
                            f.write(chunk)
        except Exception:
            try:
                if local_path.exists():
                    local_path.unlink()
            except Exception:
                pass
            return None, None

        with self.cache.lock:
            self.cache.url_to_path[url] = local_path
        return local_path, ctype

    @staticmethod
    def _extract_meta_refresh_target(html_bytes: bytes, base_url: str) -> Optional[str]:
        if not html_bytes:
            return None
        try:
            soup = BeautifulSoup(html_bytes, "html.parser")
        except Exception:
            return None
        meta = soup.find("meta", attrs={"http-equiv": lambda v: v and v.lower() == "refresh"})
        if not meta:
            return None
        content = meta.get("content", "")
        # e.g., "0;url=https://example.com/next"
        m = re.search(r'url\s*=\s*([^;]+)$', content, flags=re.IGNORECASE)
        if not m:
            return None
        target = m.group(1).strip().strip('"\'')
        return _normalize(up.urljoin(base_url, target))

    # ---------- HTML/CSS rewriting ----------

    def _parse_and_rewrite_html(self, page_url: str, html_path: pathlib.Path) -> None:
        raw = html_path.read_bytes()
        soup = BeautifulSoup(raw, "html.parser")

        base_tag = soup.find("base", href=True)
        effective_base = up.urljoin(page_url, base_tag["href"]) if base_tag else page_url

        # 1) Assets: download & rewrite
        for tag_name, attrs in ASSET_TAG_ATTRS.items():
            for tag in soup.find_all(tag_name):
                for attr in attrs:
                    val = tag.get(attr)
                    if not val:
                        continue
                    if attr == "srcset":
                        new_srcset = self._rewrite_srcset_assets(effective_base, html_path, val, html_path.parent)
                        if new_srcset:
                            tag[attr] = new_srcset
                        continue
                    new_val = self._rewrite_asset_ref(effective_base, html_path, val, html_path.parent)
                    if new_val:
                        tag[attr] = new_val

        # 2) Navigational anchors: DO NOT download; rewrite only if cached
        for tag_name, attrs in NAV_TAG_ATTRS.items():
            for tag in soup.find_all(tag_name):
                for attr in attrs:
                    val = tag.get(attr)
                    if not val:
                        continue
                    new_val = self._rewrite_nav_if_cached(effective_base, html_path, val)
                    if new_val:
                        tag[attr] = new_val

        # 3) CSS in style attribute and <style> blocks
        for el in soup.find_all(style=True):
            el['style'] = self._rewrite_css_text(effective_base, html_path, el['style'], html_path.parent)

        for st in soup.find_all("style"):
            css_text = st.get_text()
            new_css = self._rewrite_css_text(effective_base, html_path, css_text, html_path.parent)
            st.clear()
            st.append(new_css)

        html_path.write_bytes(soup.encode(formatter="html"))

    def _rewrite_srcset_assets(self, base_url: str, owner_html: pathlib.Path, srcset_val: str,
                               prefer_dir: pathlib.Path) -> Optional[str]:
        parts = SRCSET_SPLIT.split(srcset_val)
        rewritten, changed = [], False
        for part in parts:
            sub = part.strip()
            if not sub:
                continue
            tokens = sub.split()
            if not tokens:
                continue
            u = tokens[0]
            if u.startswith(("data:", "blob:")):
                rewritten.append(part)
                continue
            abs_u = up.urljoin(base_url, u)
            # per-domain limit for assets too
            with self._domain_sem(abs_u):
                loc, _ = self._download(abs_u, prefer_dir)
            if loc:
                tokens[0] = _relpath(owner_html, loc)
                changed = True
            rewritten.append(" ".join(tokens))
        return ", ".join(rewritten) if changed else None

    def _rewrite_asset_ref(self, base_url: str, owner_html: pathlib.Path, ref: str,
                           prefer_dir: pathlib.Path) -> Optional[str]:
        ref = ref.strip()
        if not ref or ref.startswith(("data:", "blob:", "mailto:", "tel:")):
            return None
        abs_u = up.urljoin(base_url, ref)
        with self._domain_sem(abs_u):
            loc, ctype = self._download(abs_u, prefer_dir)
        if not loc:
            return None
        if ctype and "css" in ctype.lower():
            self._parse_css_file(abs_u, loc, prefer_dir)
        return _relpath(owner_html, loc)

    def _rewrite_nav_if_cached(self, base_url: str, owner_html: pathlib.Path, ref: str) -> Optional[str]:
        ref = ref.strip()
        if not ref or ref.startswith(("#", "mailto:", "tel:", "data:", "blob:")):
            return None
        abs_u = _normalize(up.urljoin(base_url, ref))
        with self.cache.lock:
            loc = self.cache.url_to_path.get(abs_u)
        if not loc:
            return None
        return _relpath(owner_html, loc)

    def _rewrite_css_text(self, base_url: str, owner_path: pathlib.Path, css_text: str,
                          prefer_dir: pathlib.Path) -> str:
        def _url_repl(m):
            u = m.group("url").strip()
            if u.startswith(("data:", "blob:")):
                return m.group(0)
            abs_u = up.urljoin(base_url, u)
            with self._domain_sem(abs_u):
                loc, ctype = self._download(abs_u, prefer_dir)
            if loc:
                if ctype and "css" in ctype.lower():
                    self._parse_css_file(abs_u, loc, prefer_dir)
                rel = _relpath(owner_path, loc)
                return f"url({rel})"
            return m.group(0)

        def _import_repl(m):
            u = m.group("url").strip()
            if u.startswith(("data:", "blob:")):
                return m.group(0)
            abs_u = up.urljoin(base_url, u)
            with self._domain_sem(abs_u):
                loc, _ = self._download(abs_u, prefer_dir)
            if loc:
                rel = _relpath(owner_path, loc)
                return f"@import url({rel})"
            return m.group(0)

        css_text = CSS_URL_PATTERN.sub(_url_repl, css_text)
        css_text = CSS_IMPORT_PATTERN.sub(_import_repl, css_text)
        return css_text

    def _parse_css_file(self, css_url: str, css_path: pathlib.Path, prefer_dir: pathlib.Path) -> None:
        try:
            text = css_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            return
        new_css = self._rewrite_css_text(css_url, css_path, text, prefer_dir)
        try:
            css_path.write_text(new_css, encoding="utf-8")
        except Exception:
            pass

    def _extract_links(self, html_path: pathlib.Path, page_url: str) -> Set[str]:
        try:
            data = html_path.read_bytes()
        except Exception:
            return set()
        soup = BeautifulSoup(data, "html.parser")
        out: Set[str] = set()

        # Normal anchors
        for a in soup.find_all("a", href=True):
            href = a["href"].strip()
            if href.startswith(("#", "mailto:", "tel:")):
                continue
            out.add(_normalize(up.urljoin(page_url, href)))

        # Meta refresh target links inside body (in case we saved the page)
        meta_target = self._extract_meta_refresh_target(data, page_url)
        if meta_target:
            out.add(meta_target)
        return out

    # ---------- Final post-pass ----------

    def _finalize_anchor_rewrites(self) -> None:
        """Re-open saved HTML and rewrite anchors that are now cached (common in threaded crawl)."""
        paths = []
        with self.saved_html_lock:
            paths = list(self.saved_html_paths)

        for html_path in paths:
            try:
                raw = html_path.read_bytes()
            except Exception:
                continue
            soup = BeautifulSoup(raw, "html.parser")
            # base for this page
            # We need the original URL → reverse map from cache.url_to_path
            base_url = self._reverse_lookup_url_for_path(html_path) or ""

            for a in soup.find_all("a", href=True):
                ref = a["href"].strip()
                if not ref or ref.startswith(("#", "mailto:", "tel:", "data:", "blob:")):
                    continue
                abs_u = _normalize(up.urljoin(base_url, ref))
                with self.cache.lock:
                    loc = self.cache.url_to_path.get(abs_u)
                if loc:
                    a["href"] = _relpath(html_path, loc)

            try:
                html_path.write_bytes(soup.encode(formatter="html"))
            except Exception:
                pass

    def _reverse_lookup_url_for_path(self, path: pathlib.Path) -> Optional[str]:
        with self.cache.lock:
            for u, p in self.cache.url_to_path.items():
                if p == path:
                    return u
        return None

    # ---------- UX ----------

    def _print_settings(self) -> None:
        p = self.plan
        print("=== Settings ===")
        print(f"Start URLs: {', '.join(p.start_urls[:3])}{' ...' if len(p.start_urls)>3 else ''}")
        print(f"Follow external: {'yes' if p.follow_externals else 'no'}")
        print(f"Local depth: {p.crawl_local_depth if p.crawl_local_depth is not None else 'ALL'}")
        if p.follow_externals:
            print(f"External depth: {p.crawl_external_depth if p.crawl_external_depth is not None else 'ALL'}")
        print(f"Save folder: {p.save_root}")
        print(f"Max threads per domain: {p.max_threads_per_domain}")
        print(f"Max workers (pool size): {p.max_workers}")
        print("================")


# =============
# Entrypoint
# =============

def main():
    mimetypes.init()
    mimetypes.add_type("application/javascript", ".js")
    copier = WebpageCopier.from_prompts()
    copier.run()

if __name__ == "__main__":
    main()



import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _; # type: ignore
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars')

def sw():
    pass
    _.switches.register( 'URLs', '-u,-url,-urls,-f','https://site.com/',  isData='name', description='URLs', isRequired=True )
    
_._default_settings_()

_.appInfo[focus()] = {
    'file': 'thisApp.py',
    'description': 'Changes the world',
    'categories': [
                        'DEFAULT',
                ],
    'examples': [
                        _.hp('p thisApp -file file.txt'),
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
    _.switches.trigger( 'DB', _.aliasesFi )
    _.switches.trigger( 'Folder', _.myFolderLocations )
    _.switches.trigger( 'Folders', _.myFolderLocations )
    __.SwitchesModifier.Trigger['Folders'] = _.myFolder
    _.switches.trigger( 'OutputFolder', _.aliasesFo )
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw )
########################################################################################
#n)--> start

def action():
    pass

########################################################################################
if __name__ == '__main__':
    action(); _.isExit(__file__)