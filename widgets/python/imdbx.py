#!/usr/bin/env python3
"""
imdbx.py - local IMDb graph/xref framework

Uses IMDb public TSV datasets, builds a local pickle graph, then lets you search,
select, xref, inspect episodes, and run Kevin-Bacon-style degree paths.

Brave Search API is optional. Set BRAVE_API_KEY to enable spelling/query correction.

Install: no external packages required.

Usage:
  python imdbx.py update
  python imdbx.py shell
  python imdbx.py movie "the matrix"
  python imdbx.py person "keanu reeves"
  python imdbx.py xref tt0133093 nm0000206
  python imdbx.py deg nm0000206 nm0000102 --depth 6
"""
from __future__ import annotations

import argparse
import csv
import gzip
import json
import os
import pickle
import re
import sys
import time
import urllib.parse
import urllib.request
import webbrowser
from collections import deque
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

BASE_URL = "https://datasets.imdbws.com"
DEFAULT_HOME = Path(os.environ.get("IMDBX_HOME", Path.home() / ".imdbx"))
DEFAULT_DATA_DIR = DEFAULT_HOME / "data"
DEFAULT_GRAPH_FILE = DEFAULT_HOME / "imdbx.graph.pkl"
DEFAULT_FRANCHISE_FILE = DEFAULT_HOME / "franchises.json"
DEFAULT_WATCHED_FILE = DEFAULT_HOME / "watched.json"
DEFAULT_EXPORT_DIR = DEFAULT_HOME / "exports"

FILES = [
    "title.basics.tsv.gz",
    "name.basics.tsv.gz",
    "title.principals.tsv.gz",
    "title.ratings.tsv.gz",
    "title.episode.tsv.gz",
    "title.crew.tsv.gz",
    "title.akas.tsv.gz",
]

ID_RE = re.compile(r"^(tt|nm)\d+$", re.I)
TT_RE = re.compile(r"^tt\d+$", re.I)
NM_RE = re.compile(r"^nm\d+$", re.I)
WORD_RE = re.compile(r"[a-z0-9]+", re.I)


def clean(v: Any) -> Optional[str]:
    if v is None:
        return None
    v = str(v)
    if v == r"\N":
        return None
    return v.strip()


def norm(s: str) -> str:
    return " ".join(WORD_RE.findall((s or "").lower()))


def tokens(s: str) -> List[str]:
    return [x for x in WORD_RE.findall((s or "").lower()) if len(x) >= 2]


def is_title_id(x: str) -> bool:
    return bool(TT_RE.match(x or ""))


def is_person_id(x: str) -> bool:
    return bool(NM_RE.match(x or ""))


def now_stamp() -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S")


def ensure_dirs() -> None:
    DEFAULT_HOME.mkdir(parents=True, exist_ok=True)
    DEFAULT_DATA_DIR.mkdir(parents=True, exist_ok=True)
    DEFAULT_EXPORT_DIR.mkdir(parents=True, exist_ok=True)


def download_file(url: str, out: Path, force: bool = False) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(out.suffix + ".tmp")
    if out.exists() and not force:
        print(f"exists {out}")
        return
    print(f"download {url}")
    req = urllib.request.Request(url, headers={"User-Agent": "imdbx/1.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(tmp, "wb") as f:
        while True:
            chunk = r.read(1024 * 1024)
            if not chunk:
                break
            f.write(chunk)
    tmp.replace(out)


def download_latest(force: bool = True, files: Sequence[str] = FILES) -> None:
    ensure_dirs()
    for f in files:
        download_file(f"{BASE_URL}/{f}", DEFAULT_DATA_DIR / f, force=force)
    meta = {"updated": now_stamp(), "files": list(files)}
    (DEFAULT_DATA_DIR / "download.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")


class Brave:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get("BRAVE_API_KEY")

    def correct(self, query: str) -> str:
        if not self.api_key or not query.strip():
            return query
        params = urllib.parse.urlencode({"q": query, "spellcheck": "true", "count": "1"})
        url = "https://api.search.brave.com/res/v1/web/search?" + params
        req = urllib.request.Request(
            url,
            headers={"Accept": "application/json", "X-Subscription-Token": self.api_key},
        )
        try:
            with urllib.request.urlopen(req, timeout=8) as r:
                data = json.loads(r.read().decode("utf-8", "replace"))
            altered = data.get("query", {}).get("altered")
            return altered or query
        except Exception:
            return query


@dataclass
class ImdbGraph:
    titles: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    people: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    ratings: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    crew: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    episodes: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    seasons: Dict[str, Dict[int, List[str]]] = field(default_factory=dict)
    akas: Dict[str, List[Dict[str, Any]]] = field(default_factory=dict)

    movie_to_people: Dict[str, Set[str]] = field(default_factory=dict)
    person_to_movies: Dict[str, Set[str]] = field(default_factory=dict)
    rel_info: Dict[Tuple[str, str], Dict[str, Any]] = field(default_factory=dict)

    title_index: Dict[str, Set[str]] = field(default_factory=dict)
    people_index: Dict[str, Set[str]] = field(default_factory=dict)
    built: Optional[str] = None

    def index_text(self, index: Dict[str, Set[str]], text: Optional[str], item_id: str) -> None:
        for t in tokens(text or ""):
            index.setdefault(t, set()).add(item_id)

    def require_files(self) -> None:
        missing = [f for f in FILES if not (DEFAULT_DATA_DIR / f).exists()]
        if missing:
            raise SystemExit("Missing IMDb files. Run: python imdbx.py update\n" + "\n".join(missing))

    def build(self, skip_akas: bool = False) -> None:
        self.require_files()
        self.load_titles()
        self.load_people()
        self.load_ratings()
        self.load_crew()
        self.load_episodes()
        self.load_principals()
        if not skip_akas:
            self.load_akas()
        self.built = now_stamp()
        self.save()

    def load_titles(self) -> None:
        print("load title.basics")
        with gzip.open(DEFAULT_DATA_DIR / "title.basics.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                tid = r["tconst"]
                rec = {
                    "id": tid,
                    "kind": clean(r.get("titleType")),
                    "title": clean(r.get("primaryTitle")),
                    "original": clean(r.get("originalTitle")),
                    "adult": clean(r.get("isAdult")),
                    "year": clean(r.get("startYear")),
                    "end": clean(r.get("endYear")),
                    "runtime": clean(r.get("runtimeMinutes")),
                    "genres": clean(r.get("genres")),
                }
                self.titles[tid] = rec
                self.index_text(self.title_index, rec["title"], tid)
                self.index_text(self.title_index, rec["original"], tid)

    def load_people(self) -> None:
        print("load name.basics")
        with gzip.open(DEFAULT_DATA_DIR / "name.basics.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                pid = r["nconst"]
                rec = {
                    "id": pid,
                    "name": clean(r.get("primaryName")),
                    "birth": clean(r.get("birthYear")),
                    "death": clean(r.get("deathYear")),
                    "profession": clean(r.get("primaryProfession")),
                    "known_for": clean(r.get("knownForTitles")),
                }
                self.people[pid] = rec
                self.index_text(self.people_index, rec["name"], pid)

    def load_ratings(self) -> None:
        print("load title.ratings")
        with gzip.open(DEFAULT_DATA_DIR / "title.ratings.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                try:
                    votes = int(r.get("numVotes") or 0)
                except Exception:
                    votes = 0
                self.ratings[r["tconst"]] = {
                    "rating": clean(r.get("averageRating")),
                    "votes": votes,
                }

    def load_crew(self) -> None:
        print("load title.crew")
        with gzip.open(DEFAULT_DATA_DIR / "title.crew.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                self.crew[r["tconst"]] = {
                    "directors": clean(r.get("directors")),
                    "writers": clean(r.get("writers")),
                }

    def load_episodes(self) -> None:
        print("load title.episode")
        with gzip.open(DEFAULT_DATA_DIR / "title.episode.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                eid = r["tconst"]
                parent = clean(r.get("parentTconst"))
                season = clean(r.get("seasonNumber"))
                ep = clean(r.get("episodeNumber"))
                rec = {"id": eid, "parent": parent, "season": season, "episode": ep}
                self.episodes[eid] = rec
                if parent and season:
                    try:
                        s = int(season)
                    except Exception:
                        s = -1
                    self.seasons.setdefault(parent, {}).setdefault(s, []).append(eid)

    def load_principals(self) -> None:
        print("load title.principals xref")
        with gzip.open(DEFAULT_DATA_DIR / "title.principals.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                tid = r["tconst"]
                pid = r["nconst"]
                self.movie_to_people.setdefault(tid, set()).add(pid)
                self.person_to_movies.setdefault(pid, set()).add(tid)
                self.rel_info[(tid, pid)] = {
                    "ordering": clean(r.get("ordering")),
                    "category": clean(r.get("category")),
                    "job": clean(r.get("job")),
                    "characters": clean(r.get("characters")),
                }

    def load_akas(self) -> None:
        print("load title.akas")
        with gzip.open(DEFAULT_DATA_DIR / "title.akas.tsv.gz", "rt", encoding="utf-8", newline="") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                tid = r["titleId"]
                title = clean(r.get("title"))
                if title:
                    self.akas.setdefault(tid, []).append({
                        "title": title,
                        "region": clean(r.get("region")),
                        "language": clean(r.get("language")),
                        "types": clean(r.get("types")),
                    })
                    self.index_text(self.title_index, title, tid)

    def save(self) -> None:
        ensure_dirs()
        print(f"save {DEFAULT_GRAPH_FILE}")
        with open(DEFAULT_GRAPH_FILE, "wb") as f:
            pickle.dump(self, f, protocol=pickle.HIGHEST_PROTOCOL)

    @staticmethod
    def load() -> "ImdbGraph":
        if not DEFAULT_GRAPH_FILE.exists():
            raise SystemExit("No graph cache. Run: python imdbx.py update")
        with open(DEFAULT_GRAPH_FILE, "rb") as f:
            return pickle.load(f)

    def title(self, tid: str) -> Dict[str, Any]:
        rec = dict(self.titles.get(tid, {"id": tid, "title": "?"}))
        rec.update(self.ratings.get(tid, {}))
        rec.update(self.crew.get(tid, {}))
        return rec

    def person(self, pid: str) -> Dict[str, Any]:
        return dict(self.people.get(pid, {"id": pid, "name": "?"}))

    def title_label(self, tid: str) -> str:
        t = self.title(tid)
        y = t.get("year") or ""
        return f"{tid} | {t.get('title')}" + (f" ({y})" if y else "")

    def person_label(self, pid: str) -> str:
        p = self.person(pid)
        b = p.get("birth") or ""
        return f"{pid} | {p.get('name')}" + (f" ({b})" if b else "")

    def title_url(self, tid: str) -> str:
        return f"https://www.imdb.com/title/{tid}/"

    def person_url(self, pid: str) -> str:
        return f"https://www.imdb.com/name/{pid}/"

    def search_index(self, index: Dict[str, Set[str]], q: str) -> Set[str]:
        parts = tokens(q)
        if not parts:
            return set()
        result: Optional[Set[str]] = None
        for part in parts:
            hits = index.get(part, set())
            if result is None:
                result = set(hits)
            else:
                result &= hits
        if result:
            return result
        # fallback OR search when AND fails
        out: Set[str] = set()
        for part in parts:
            out |= index.get(part, set())
        return out

    def search_titles(self, q: str, limit: int = 25, kind: Optional[str] = None) -> List[Dict[str, Any]]:
        ids = self.search_index(self.title_index, q)
        if kind:
            ids = {tid for tid in ids if (self.titles.get(tid, {}).get("kind") or "").lower() == kind.lower()}
        return self.sort_titles(ids)[:limit]

    def search_people(self, q: str, limit: int = 25) -> List[Dict[str, Any]]:
        ids = self.search_index(self.people_index, q)
        # rank people by number of credits, then name
        ranked = sorted(ids, key=lambda pid: (len(self.person_to_movies.get(pid, set())), self.people.get(pid, {}).get("name") or ""), reverse=True)
        return [self.person(pid) for pid in ranked[:limit]]

    def sort_titles(self, ids: Iterable[str]) -> List[Dict[str, Any]]:
        return [self.title(tid) for tid in sorted(ids, key=lambda tid: self.ratings.get(tid, {}).get("votes", 0), reverse=True)]

    def people_in_title(self, tid: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        pids = list(self.movie_to_people.get(tid, set()))
        pids.sort(key=lambda pid: int(self.rel_info.get((tid, pid), {}).get("ordering") or 999999))
        if limit:
            pids = pids[:limit]
        rows = []
        for pid in pids:
            rec = self.person(pid)
            rec.update(self.rel_info.get((tid, pid), {}))
            rows.append(rec)
        return rows

    def titles_for_person(self, pid: str, limit: Optional[int] = None) -> List[Dict[str, Any]]:
        rows = self.sort_titles(self.person_to_movies.get(pid, set()))
        if limit:
            rows = rows[:limit]
        for r in rows:
            r.update(self.rel_info.get((r["id"], pid), {}))
        return rows

    def episodes_for_series(self, parent: str, season: Optional[int] = None) -> List[Dict[str, Any]]:
        rows: List[Dict[str, Any]] = []
        season_map = self.seasons.get(parent, {})
        seasons = [season] if season is not None else sorted(season_map)
        for s in seasons:
            for eid in sorted(season_map.get(s, []), key=lambda e: int(self.episodes.get(e, {}).get("episode") or 0)):
                ep = dict(self.episodes[eid])
                ep.update(self.title(eid))
                rows.append(ep)
        return rows

    def episode(self, parent: str, season: int, episode: int) -> Optional[Dict[str, Any]]:
        for eid in self.seasons.get(parent, {}).get(season, []):
            rec = self.episodes.get(eid, {})
            try:
                if int(rec.get("episode") or -1) == episode:
                    out = dict(rec)
                    out.update(self.title(eid))
                    return out
            except Exception:
                pass
        return None

    def common_people(self, title_ids: Sequence[str]) -> List[Dict[str, Any]]:
        sets = [self.movie_to_people.get(tid, set()) for tid in title_ids]
        ids = set.intersection(*sets) if sets else set()
        rows = [self.person(pid) for pid in ids]
        rows.sort(key=lambda r: r.get("name") or "")
        return rows

    def common_titles(self, person_ids: Sequence[str]) -> List[Dict[str, Any]]:
        sets = [self.person_to_movies.get(pid, set()) for pid in person_ids]
        ids = set.intersection(*sets) if sets else set()
        return self.sort_titles(ids)

    def xref(self, ids: Sequence[str]) -> List[Dict[str, Any]]:
        title_ids = [x for x in ids if is_title_id(x)]
        person_ids = [x for x in ids if is_person_id(x)]
        if title_ids and not person_ids:
            return self.common_people(title_ids) if len(title_ids) > 1 else self.people_in_title(title_ids[0])
        if person_ids and not title_ids:
            return self.common_titles(person_ids) if len(person_ids) > 1 else self.titles_for_person(person_ids[0])
        rows: List[Dict[str, Any]] = []
        for tid in title_ids:
            cast = self.movie_to_people.get(tid, set())
            for pid in person_ids:
                if pid in cast:
                    rows.append({
                        "title_id": tid,
                        "title": self.titles.get(tid, {}).get("title"),
                        "person_id": pid,
                        "person": self.people.get(pid, {}).get("name"),
                        **self.rel_info.get((tid, pid), {}),
                    })
        return rows

    def degree_path(self, start_pid: str, target_pid: str, max_depth: int = 6, movie_limit: int = 400, cast_limit: int = 300) -> List[Tuple[str, str, str]]:
        if start_pid == target_pid:
            return []
        q = deque([(start_pid, [])])
        seen_people = {start_pid}
        seen_titles: Set[str] = set()
        for _depth in range(max_depth):
            for _ in range(len(q)):
                person, path = q.popleft()
                movies = sorted(self.person_to_movies.get(person, set()), key=lambda tid: self.ratings.get(tid, {}).get("votes", 0), reverse=True)[:movie_limit]
                for movie in movies:
                    if movie in seen_titles and len(path) > 0:
                        continue
                    seen_titles.add(movie)
                    cast = sorted(self.movie_to_people.get(movie, set()), key=lambda pid: len(self.person_to_movies.get(pid, set())), reverse=True)[:cast_limit]
                    for other in cast:
                        step = (person, movie, other)
                        if other == target_pid:
                            return path + [step]
                        if other not in seen_people:
                            seen_people.add(other)
                            q.append((other, path + [step]))
        return []

    def info(self, item_id: str) -> Dict[str, Any]:
        if is_title_id(item_id):
            rec = self.title(item_id)
            rec["url"] = self.title_url(item_id)
            rec["people_count"] = len(self.movie_to_people.get(item_id, set()))
            rec["episode_count"] = len(self.episodes_for_series(item_id))
            return rec
        if is_person_id(item_id):
            rec = self.person(item_id)
            rec["url"] = self.person_url(item_id)
            rec["credit_count"] = len(self.person_to_movies.get(item_id, set()))
            return rec
        raise ValueError("Unknown id")


class Store:
    def __init__(self, path: Path, default: Any):
        self.path = path
        self.default = default
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> Any:
        if not self.path.exists():
            return self.default
        try:
            return json.loads(self.path.read_text(encoding="utf-8"))
        except Exception:
            return self.default

    def save(self, data: Any) -> None:
        self.path.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


class FranchiseManager:
    def __init__(self):
        self.store = Store(DEFAULT_FRANCHISE_FILE, {})
        self.data: Dict[str, Any] = self.store.load()

    def save(self) -> None:
        self.store.save(self.data)

    def add(self, name: str, ids: Sequence[str]) -> None:
        key = norm(name).replace(" ", "_")
        cur = self.data.setdefault(key, {"name": name, "ids": [], "updated": now_stamp()})
        merged = set(cur.get("ids", [])) | set(ids)
        cur["ids"] = sorted(merged)
        cur["updated"] = now_stamp()
        self.save()

    def get(self, name: str) -> List[str]:
        key = norm(name).replace(" ", "_")
        return list(self.data.get(key, {}).get("ids", []))

    def list(self) -> List[Dict[str, Any]]:
        return [{"key": k, **v, "count": len(v.get("ids", []))} for k, v in sorted(self.data.items())]


class WatchedManager:
    def __init__(self):
        self.store = Store(DEFAULT_WATCHED_FILE, {})
        self.data: Dict[str, Any] = self.store.load()

    def mark(self, tid: str, label: str = "watched", location: Optional[str] = None, path: Optional[str] = None) -> None:
        self.data[tid] = {"date": now_stamp(), "label": label, "location": location, "path": path}
        self.store.save(self.data)

    def is_watched(self, tid: str) -> bool:
        return tid in self.data

    def list(self) -> Dict[str, Any]:
        return self.data


def print_rows(rows: Sequence[Dict[str, Any]], ids_only: bool = False, limit: int = 50) -> None:
    if not rows:
        print("No results")
        return
    for i, r in enumerate(rows[:limit], 1):
        rid = r.get("id") or r.get("title_id") or r.get("person_id") or r.get("tconst") or r.get("nconst")
        if ids_only:
            print(rid)
            continue
        if "title" in r and (r.get("kind") or r.get("year") or r.get("rating")):
            bits = [str(i).rjust(3) + ".", r.get("id") or r.get("title_id") or "", "|", r.get("title") or ""]
            if r.get("year"):
                bits += ["|", str(r.get("year"))]
            if r.get("kind"):
                bits += ["|", str(r.get("kind"))]
            if r.get("rating"):
                bits += ["|", f"⭐ {r.get('rating')} ({r.get('votes', 0)})"]
            if r.get("category"):
                bits += ["|", str(r.get("category"))]
            print(" ".join(bits))
        elif "name" in r:
            bits = [str(i).rjust(3) + ".", r.get("id") or r.get("person_id") or "", "|", r.get("name") or r.get("person") or ""]
            if r.get("birth"):
                bits += ["|", str(r.get("birth"))]
            if r.get("profession"):
                bits += ["|", str(r.get("profession"))]
            if r.get("category"):
                bits += ["|", str(r.get("category"))]
            if r.get("characters"):
                bits += ["|", str(r.get("characters"))]
            print(" ".join(bits))
        else:
            print(str(i).rjust(3) + ".", json.dumps(r, ensure_ascii=False))
    if len(rows) > limit:
        print(f"... {len(rows) - limit} more")


def print_info(g: ImdbGraph, item_id: str) -> None:
    rec = g.info(item_id)
    print(json.dumps(rec, indent=2, ensure_ascii=False))


def export_rows(rows: Sequence[Dict[str, Any]], name: str, fmt: str = "json") -> Path:
    ensure_dirs()
    safe = re.sub(r"[^a-zA-Z0-9_.-]+", "_", name).strip("_") or "export"
    path = DEFAULT_EXPORT_DIR / f"{safe}.{fmt}"
    if fmt == "json":
        path.write_text(json.dumps(list(rows), indent=2, ensure_ascii=False), encoding="utf-8")
    elif fmt == "csv":
        keys: List[str] = []
        for r in rows:
            for k in r.keys():
                if k not in keys:
                    keys.append(k)
        with open(path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=keys)
            w.writeheader()
            w.writerows(rows)
    elif fmt == "ids":
        ids = []
        for r in rows:
            rid = r.get("id") or r.get("title_id") or r.get("person_id") or r.get("tconst") or r.get("nconst")
            if rid:
                ids.append(str(rid))
        path.write_text("\n".join(ids) + "\n", encoding="utf-8")
    else:
        raise ValueError("fmt must be json/csv/ids")
    return path


class Shell:
    def __init__(self, g: ImdbGraph, use_brave: bool = True):
        self.g = g
        self.brave = Brave() if use_brave else Brave(api_key=None)
        self.last: List[Dict[str, Any]] = []
        self.current_id: Optional[str] = None
        self.franchise = FranchiseManager()
        self.watched = WatchedManager()

    def help(self) -> None:
        print("""
imdbx shell commands

Search / select:
  m <movie/show>                  search titles
  p <person>                      search people
  s <query>                       search both
  1                               select result number
  select <n>                      select result number

ID / xref:
  id                              print current id
  info [id]                       print full local info
  in <ttid>                       people in title
  by <nmid>                       titles for person
  x <id> [id id...]               ID-first xref
  common titles <nm...>           titles common to people
  common people <tt...>           people common to titles
  deg <nm1> <nm2> [depth]         degree path between people
  kb <nm> [depth]                 path to Kevin Bacon nm0000102

Episodes:
  eps <ttid> [season]             episode table
  ep <ttid> s:e                   one episode

Custom lists:
  franchise add <name> <ids...>   save list/franchise/hallmark group
  franchise list                  list saved groups
  franchise x <name> <ids...>     xref saved group with ids

Watched / labels:
  watched <ttid> [label]          mark watched
  watched list                    list watched records

Output:
  ids                             toggle ids-only printing
  export <name> [json|csv|ids]    export last results
  open [id]                       open IMDb page
  update                          download latest and rebuild
  help                            this menu
  exit                            quit
""")

    ids_only = False

    def run(self) -> None:
        self.help()
        while True:
            try:
                line = input("imdbx> ").strip()
            except EOFError:
                print()
                break
            if not line:
                continue
            if line.lower() in {"q", "quit", "exit", "x"}:
                break
            try:
                self.handle(line)
            except KeyboardInterrupt:
                print("interrupted")
            except Exception as e:
                print("ERROR:", e)

    def set_last(self, rows: List[Dict[str, Any]], limit: int = 50) -> None:
        self.last = rows
        print_rows(rows, ids_only=self.ids_only, limit=limit)

    def selected_id(self, item: Dict[str, Any]) -> Optional[str]:
        return item.get("id") or item.get("title_id") or item.get("person_id") or item.get("tconst") or item.get("nconst")

    def handle(self, line: str) -> None:
        parts = line.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in {"help", "?", "h"}:
            self.help(); return
        if cmd == "ids":
            self.ids_only = not self.ids_only
            print("ids-only:", self.ids_only); return
        if cmd == "update":
            download_latest(force=True)
            self.g = ImdbGraph(); self.g.build(); return
        if cmd in {"m", "movie", "ent"}:
            q = self.brave.correct(" ".join(args))
            print("search:", q)
            self.set_last(self.g.search_titles(q)); return
        if cmd in {"p", "person", "who", "actor"}:
            q = self.brave.correct(" ".join(args))
            print("search:", q)
            self.set_last(self.g.search_people(q)); return
        if cmd == "s":
            q = self.brave.correct(" ".join(args))
            print("titles")
            titles = self.g.search_titles(q, 10)
            print_rows(titles, ids_only=self.ids_only, limit=10)
            print("people")
            people = self.g.search_people(q, 10)
            print_rows(people, ids_only=self.ids_only, limit=10)
            self.last = titles + people
            return
        if cmd.isdigit() or cmd == "select":
            n = int(cmd if cmd.isdigit() else args[0]) - 1
            item = self.last[n]
            item_id = self.selected_id(item)
            self.current_id = item_id
            print("selected", item_id)
            if item_id and is_title_id(item_id):
                print_info(self.g, item_id)
                self.set_last(self.g.people_in_title(item_id, 100), limit=100)
            elif item_id and is_person_id(item_id):
                print_info(self.g, item_id)
                self.set_last(self.g.titles_for_person(item_id, 100), limit=100)
            return
        if cmd == "id":
            print(self.current_id or "No current selection"); return
        if cmd == "info":
            print_info(self.g, args[0] if args else self.current_id or ""); return
        if cmd in {"in", "cast"}:
            self.current_id = args[0]
            self.set_last(self.g.people_in_title(args[0], 500), limit=500); return
        if cmd in {"by", "filmography", "films"}:
            self.current_id = args[0]
            self.set_last(self.g.titles_for_person(args[0], 500), limit=500); return
        if cmd in {"x", "xref"}:
            self.set_last(self.g.xref(args), limit=500); return
        if cmd == "common":
            if args[0] == "titles":
                self.set_last(self.g.common_titles(args[1:]), limit=500); return
            if args[0] == "people":
                self.set_last(self.g.common_people(args[1:]), limit=500); return
        if cmd in {"deg", "degree"}:
            depth = int(args[2]) if len(args) > 2 else 6
            path = self.g.degree_path(args[0], args[1], depth)
            self.print_path(path); return
        if cmd == "kb":
            depth = int(args[1]) if len(args) > 1 else 6
            path = self.g.degree_path(args[0], "nm0000102", depth)
            self.print_path(path); return
        if cmd in {"eps", "episodes"}:
            tid = args[0]
            season = int(args[1]) if len(args) > 1 else None
            self.set_last(self.g.episodes_for_series(tid, season), limit=1000); return
        if cmd == "ep":
            s, e = args[1].split(":", 1)
            rec = self.g.episode(args[0], int(s), int(e))
            self.set_last([rec] if rec else []); return
        if cmd == "franchise":
            self.handle_franchise(args); return
        if cmd == "watched":
            if args and args[0] == "list":
                print(json.dumps(self.watched.list(), indent=2)); return
            tid = args[0]
            label = args[1] if len(args) > 1 else "watched"
            self.watched.mark(tid, label=label)
            print("marked", tid, label); return
        if cmd == "export":
            name = args[0] if args else "imdbx_export"
            fmt = args[1] if len(args) > 1 else "json"
            path = export_rows(self.last, name, fmt)
            print(path); return
        if cmd == "open":
            item_id = args[0] if args else self.current_id
            if not item_id:
                print("No id"); return
            webbrowser.open(self.g.title_url(item_id) if is_title_id(item_id) else self.g.person_url(item_id))
            return
        print("Unknown command. Type help.")

    def print_path(self, path: List[Tuple[str, str, str]]) -> None:
        if not path:
            print("No path found")
            return
        for a, movie, b in path:
            print(f"{self.g.person(a).get('name')} [{a}] -> {self.g.title(movie).get('title')} [{movie}] -> {self.g.person(b).get('name')} [{b}]")

    def handle_franchise(self, args: List[str]) -> None:
        op = args[0]
        if op == "list":
            print_rows(self.franchise.list(), limit=500); return
        if op == "add":
            name = args[1]
            ids = args[2:]
            self.franchise.add(name, ids)
            print("saved", name, len(ids)); return
        if op in {"x", "xref"}:
            name = args[1]
            ids = self.franchise.get(name) + args[2:]
            self.set_last(self.g.xref(ids), limit=1000); return
        print("franchise commands: list | add <name> <ids...> | x <name> <ids...>")


def handle_cli() -> None:
    ap = argparse.ArgumentParser(description="IMDb local graph/xref framework")
    sub = ap.add_subparsers(dest="cmd")

    sub.add_parser("download")
    b = sub.add_parser("build")
    b.add_argument("--skip-akas", action="store_true")
    u = sub.add_parser("update")
    u.add_argument("--skip-akas", action="store_true")
    sub.add_parser("shell")

    m = sub.add_parser("movie"); m.add_argument("query", nargs="+"); m.add_argument("-n", "--limit", type=int, default=25); m.add_argument("--ids", action="store_true")
    p = sub.add_parser("person"); p.add_argument("query", nargs="+"); p.add_argument("-n", "--limit", type=int, default=25); p.add_argument("--ids", action="store_true")
    x = sub.add_parser("xref"); x.add_argument("ids", nargs="+"); x.add_argument("--ids", action="store_true")
    inf = sub.add_parser("info"); inf.add_argument("id")
    inn = sub.add_parser("in"); inn.add_argument("ttid"); inn.add_argument("--ids", action="store_true")
    by = sub.add_parser("by"); by.add_argument("nmid"); by.add_argument("--ids", action="store_true")
    ep = sub.add_parser("episodes"); ep.add_argument("ttid"); ep.add_argument("season", nargs="?", type=int)
    oneep = sub.add_parser("ep"); oneep.add_argument("ttid"); oneep.add_argument("season_episode")
    deg = sub.add_parser("deg"); deg.add_argument("nm1"); deg.add_argument("nm2"); deg.add_argument("--depth", type=int, default=6)
    kb = sub.add_parser("kb"); kb.add_argument("nmid"); kb.add_argument("--depth", type=int, default=6)
    fr = sub.add_parser("franchise"); fr.add_argument("args", nargs="+")

    args = ap.parse_args()
    cmd = args.cmd or "shell"

    if cmd == "download":
        download_latest(force=True); return
    if cmd == "update":
        download_latest(force=True)
        g = ImdbGraph(); g.build(skip_akas=args.skip_akas); return
    if cmd == "build":
        g = ImdbGraph(); g.build(skip_akas=args.skip_akas); return

    g = ImdbGraph.load()
    brave = Brave()

    if cmd == "shell":
        Shell(g).run(); return
    if cmd == "movie":
        q = brave.correct(" ".join(args.query)); print_rows(g.search_titles(q, args.limit), ids_only=args.ids); return
    if cmd == "person":
        q = brave.correct(" ".join(args.query)); print_rows(g.search_people(q, args.limit), ids_only=args.ids); return
    if cmd == "xref":
        print_rows(g.xref(args.ids), ids_only=args.ids); return
    if cmd == "info":
        print_info(g, args.id); return
    if cmd == "in":
        print_rows(g.people_in_title(args.ttid, 500), ids_only=args.ids, limit=500); return
    if cmd == "by":
        print_rows(g.titles_for_person(args.nmid, 500), ids_only=args.ids, limit=500); return
    if cmd == "episodes":
        print_rows(g.episodes_for_series(args.ttid, args.season), limit=1000); return
    if cmd == "ep":
        s, e = args.season_episode.split(":", 1)
        rec = g.episode(args.ttid, int(s), int(e))
        print_rows([rec] if rec else []); return
    if cmd == "deg":
        Shell(g).print_path(g.degree_path(args.nm1, args.nm2, args.depth)); return
    if cmd == "kb":
        Shell(g).print_path(g.degree_path(args.nmid, "nm0000102", args.depth)); return
    if cmd == "franchise":
        sh = Shell(g); sh.handle_franchise(args.args); return


if __name__ == "__main__":
    handle_cli()
