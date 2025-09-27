#!/usr/bin/env python3
# Cross-platform MIME <-> extension SQLite builder/updater
# - Windows: reads HKCR extension info + MIME registry
# - Unix-like: reads /etc/mime.types + shared-mime-info globs2/aliases
# DB is incrementally updated if it already exists.

import os
import sys
import re
import sqlite3
from pathlib import Path
from typing import Dict, List, Tuple, Optional

DB_PATH_DEFAULT = "mime_map.db"

# ---------- Common SQLite schema ----------

SCHEMA_SQL = """
PRAGMA journal_mode=WAL;
PRAGMA synchronous=NORMAL;

CREATE TABLE IF NOT EXISTS content_types (
	content_type TEXT PRIMARY KEY,
	canonical    TEXT
);

CREATE TABLE IF NOT EXISTS extensions (
	extension TEXT PRIMARY KEY
);

-- Optional Windows-only details for .ext keys
CREATE TABLE IF NOT EXISTS ext_details (
	extension      TEXT PRIMARY KEY,
	progid         TEXT,
	content_type   TEXT,    -- from extension key (may differ from globs/mime.types)
	perceived_type TEXT,
	FOREIGN KEY (extension) REFERENCES extensions(extension)
);

-- Many-to-many mapping from MIME types to extensions, with source + optional weight (from globs2)
CREATE TABLE IF NOT EXISTS mime_extensions (
	content_type TEXT NOT NULL,
	extension    TEXT NOT NULL,
	source       TEXT NOT NULL, -- 'mime.types', 'globs2', 'win_hkcr_mime'
	weight       INTEGER,       -- only for globs2
	PRIMARY KEY (content_type, extension, source),
	FOREIGN KEY (content_type) REFERENCES content_types(content_type),
	FOREIGN KEY (extension)    REFERENCES extensions(extension)
);
"""

def init_db(conn: sqlite3.Connection) -> None:
	cur = conn.cursor()
	cur.executescript(SCHEMA_SQL)
	conn.commit()

def upsert_content_types(conn: sqlite3.Connection, types: Dict[str, str]) -> None:
	"""
	types: map of content_type -> canonical (may be same as key if no alias)
	"""
	cur = conn.cursor()
	for ct, canonical in types.items():
		cur.execute("""
			INSERT INTO content_types (content_type, canonical)
			VALUES (?, ?)
			ON CONFLICT(content_type) DO UPDATE SET canonical=excluded.canonical
		""", (ct, canonical))
	conn.commit()

def upsert_extensions(conn: sqlite3.Connection, exts: List[str]) -> None:
	cur = conn.cursor()
	for ext in exts:
		cur.execute("""
			INSERT INTO extensions (extension) VALUES (?)
			ON CONFLICT(extension) DO NOTHING
		""", (ext,))
	conn.commit()

def upsert_mappings(conn: sqlite3.Connection,
					rows: List[Tuple[str, str, str, Optional[int]]]) -> None:
	"""
	rows: list of (content_type, extension, source, weight)
	"""
	cur = conn.cursor()
	for ct, ext, src, weight in rows:
		cur.execute("""
			INSERT INTO mime_extensions (content_type, extension, source, weight)
			VALUES (?, ?, ?, ?)
			ON CONFLICT(content_type, extension, source) DO UPDATE SET
				weight=COALESCE(excluded.weight, mime_extensions.weight)
		""", (ct, ext, src, weight))
	conn.commit()

def upsert_ext_details(conn: sqlite3.Connection,
					details: Dict[str, Dict[str, Optional[str]]]) -> None:
	"""
	details: { ".ext": {"progid":..., "content_type":..., "perceived_type":...}, ... }
	"""
	if not details:
		return
	cur = conn.cursor()
	for ext, info in details.items():
		cur.execute("""
			INSERT INTO extensions (extension) VALUES (?)
			ON CONFLICT(extension) DO NOTHING
		""", (ext,))
		cur.execute("""
			INSERT INTO ext_details (extension, progid, content_type, perceived_type)
			VALUES (?, ?, ?, ?)
			ON CONFLICT(extension) DO UPDATE SET
				progid=excluded.progid,
				content_type=excluded.content_type,
				perceived_type=excluded.perceived_type
		""", (ext, info.get("progid"), info.get("content_type"), info.get("perceived_type")))
	conn.commit()

# ---------- Unix-like collectors ----------

MIME_TYPES_FILES = ["/etc/mime.types"]
GLOBS2_FILES = ["/usr/share/mime/globs2", str(Path.home() / ".local/share/mime/globs2")]
ALIASES_FILES = ["/usr/share/mime/aliases", str(Path.home() / ".local/share/mime/aliases")]

def read_lines(paths: List[str]):
	for p in paths:
		try:
			with open(p, "r", encoding="utf-8", errors="replace") as f:
				for line in f:
					yield p, line.rstrip("\n")
		except FileNotFoundError:
			continue

def parse_mime_types_file() -> List[Tuple[str, str, str, Optional[int]]]:
	"""
	Parse /etc/mime.types-like files. Lines: 'type ext1 ext2 ...'
	Returns rows for mime_extensions: (content_type, extension, 'mime.types', None)
	"""
	rows: List[Tuple[str, str, str, Optional[int]]] = []
	for path, line in read_lines(MIME_TYPES_FILES):
		line = line.strip()
		if not line or line.startswith("#"):
			continue
		parts = line.split()
		if len(parts) < 2:
			continue
		ctype, exts = parts[0], parts[1:]
		for ext in exts:
			e = ext if ext.startswith(".") else f".{ext}"
			rows.append((ctype, e.lower(), "mime.types", None))
	return rows

def parse_globs2_files() -> List[Tuple[str, str, str, Optional[int]]]:
	"""
	globs2 lines: 'weight:type:pattern'
	Only map patterns like "*.ext" to an extension.
	Returns rows: (content_type, extension, 'globs2', weight)
	"""
	rows: List[Tuple[str, str, str, Optional[int]]] = []
	for path, line in read_lines(GLOBS2_FILES):
		if not line or line.startswith("#"):
			continue
		parts = line.split(":", 2)
		if len(parts) != 3:
			continue
		weight_s, ctype, pattern = parts
		try:
			weight = int(weight_s)
		except ValueError:
			continue
		if pattern.startswith("*.") and "/" not in pattern:
			ext = pattern[1:]  # ".ext"
			rows.append((ctype, ext.lower(), "globs2", weight))
	return rows

def parse_aliases_files() -> Dict[str, str]:
	"""
	aliases lines: 'old-type new-type'
	Return dict old->new
	"""
	m: Dict[str, str] = {}
	for path, line in read_lines(ALIASES_FILES):
		s = line.strip()
		if not s or s.startswith("#"):
			continue
		parts = s.split()
		if len(parts) == 2:
			m[parts[0]] = parts[1]
	return m

def collect_unix_like() -> Tuple[Dict[str, str], List[str], List[Tuple[str, str, str, Optional[int]]]]:
	"""
	Returns:
	content_types map (type -> canonical),
	extensions list,
	mapping rows for mime_extensions
	"""
	mappings = []
	mappings.extend(parse_mime_types_file())
	mappings.extend(parse_globs2_files())
	aliases = parse_aliases_files()

	# Gather sets
	ctypes = {ct for (ct, _, _, _) in mappings}
	exts = {ext for (_, ext, _, _) in mappings}

	# Canonicalize via aliases (old -> new)
	type_to_canonical = {ct: aliases.get(ct, ct) for ct in ctypes}
	return type_to_canonical, sorted(exts), mappings

# ---------- Windows collectors ----------

def collect_windows() -> Tuple[Dict[str, str],
							List[str],
							List[Tuple[str, str, str, Optional[int]]],
							Dict[str, Dict[str, Optional[str]]]]:
	"""
	Returns:
	content_types map (type -> canonical identical),
	extensions list,
	mapping rows for mime_extensions (from MIME registry),
	ext_details dict for .ext keys (progid, content_type, perceived_type)
	"""
	type_to_canonical: Dict[str, str] = {}
	exts: set = set()
	mappings: List[Tuple[str, str, str, Optional[int]]] = []
	details: Dict[str, Dict[str, Optional[str]]] = {}

	try:
		import winreg
	except ImportError:
		return type_to_canonical, sorted(exts), mappings, details

	HKCR_FLAGS = winreg.KEY_READ
	try:
		HKCR_FLAGS |= winreg.KEY_WOW64_64KEY
	except AttributeError:
		pass

	def open_hkcr():
		return winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "", 0, HKCR_FLAGS)

	def enum_subkeys(key):
		i = 0
		while True:
			try:
				yield winreg.EnumKey(key, i)
				i += 1
			except OSError:
				break

	def get_value(key, name):
		try:
			v, _ = winreg.QueryValueEx(key, name)
			return v
		except FileNotFoundError:
			return None

	hkcr = open_hkcr()

	# Extensions branch
	for sub in enum_subkeys(hkcr):
		if not sub.startswith("."):
			continue
		try:
			sk = winreg.OpenKey(hkcr, sub)
		except OSError:
			continue
		progid = get_value(sk, "")
		ctype = get_value(sk, "Content Type")
		ptype = get_value(sk, "PerceivedType")
		ext = sub.lower()
		exts.add(ext)
		details[ext] = {
			"progid": progid,
			"content_type": ctype,
			"perceived_type": ptype,
		}
		winreg.CloseKey(sk)

		# If extension key declares a content type, store it as a mapping too
		if ctype:
			type_to_canonical.setdefault(ctype, ctype)
			mappings.append((ctype, ext, "win_hkcr_ext", None))

	# MIME registry: HKEY_CLASSES_ROOT\MIME\Database\Content Type
	mime_root_path = r"MIME\Database\Content Type"
	try:
		mime_root = winreg.OpenKey(hkcr, mime_root_path)
	except OSError:
		mime_root = None

	if mime_root:
		for mime in enum_subkeys(mime_root):
			try:
				sk = winreg.OpenKey(mime_root, mime)
			except OSError:
				continue
			ext = get_value(sk, "Extension")
			winreg.CloseKey(sk)
			if ext:
				e = ext if ext.startswith(".") else f".{ext}"
				e = e.lower()
				exts.add(e)
				type_to_canonical.setdefault(mime, mime)
				mappings.append((mime, e, "win_hkcr_mime", None))
		winreg.CloseKey(mime_root)

	winreg.CloseKey(hkcr)
	return type_to_canonical, sorted(exts), mappings, details

# ---------- Main orchestration ----------

def build_or_update(db_path: str) -> None:
	conn = sqlite3.connect(db_path)
	try:
		init_db(conn)

		if sys.platform == "win32":
			type_map_w, exts_w, map_rows_w, ext_details_w = collect_windows()
			if type_map_w or exts_w or map_rows_w or ext_details_w:
				upsert_content_types(conn, type_map_w)
				upsert_extensions(conn, exts_w)
				upsert_mappings(conn, map_rows_w)
				upsert_ext_details(conn, ext_details_w)

		# Always try Unix-like collectors too (in case WSL/macOS/etc.)
		type_map_u, exts_u, map_rows_u = collect_unix_like()
		if type_map_u or exts_u or map_rows_u:
			upsert_content_types(conn, type_map_u)
			upsert_extensions(conn, exts_u)
			upsert_mappings(conn, map_rows_u)

	finally:
		conn.close()

def usage() -> None:
	print(f"""Usage:
  {Path(sys.argv[0]).name} [DB_PATH]

Behavior:
  - Creates or updates (upserts) an SQLite DB with MIME <-> extension mappings.
  - On Windows: reads HKCR (.ext keys + MIME registry).
  - On Unix-like systems: reads /etc/mime.types, globs2, aliases.
  - If DB exists, new info is merged (no duplicate rows).

Example:
  {Path(sys.argv[0]).name}              # writes/updates {DB_PATH_DEFAULT}
  {Path(sys.argv[0]).name} my.db        # custom path

Example SQL queries:

  -- From extension to MIME (prefer globs2 weight if present):
  SELECT me.content_type, ct.canonical, me.source, me.weight
  FROM mime_extensions me
  JOIN content_types ct ON ct.content_type = me.content_type
  WHERE me.extension = '.pbm'
  ORDER BY (me.weight IS NULL), me.weight DESC;

  -- All extensions for a canonical MIME:
  SELECT DISTINCT me.extension
  FROM mime_extensions me
  JOIN content_types ct ON ct.content_type = me.content_type
  WHERE ct.canonical = 'video/mpeg'
  ORDER BY me.extension;

  -- Windows-only: inspect details declared on the extension key:
  SELECT * FROM ext_details WHERE extension = '.mp3';
""")

if __name__ == "__main__":
	if "-h" in sys.argv or "--help" in sys.argv:
		usage()
		sys.exit(0)

	db_path = sys.argv[1] if len(sys.argv) > 1 else DB_PATH_DEFAULT
	build_or_update(db_path)
	print(f"SQLite updated at: {db_path}")