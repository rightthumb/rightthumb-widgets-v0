#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ai_search_builder.py
- Query your DB for records by type (e.g., 'video')
- Send two prompts to GPT (init + records batch)
- Store generated search terms + app suggestions into ai_search_catalog

Columns:
  type          TEXT PRIMARY KEY        -- e.g., 'video'
  search_terms  TEXT (JSON list[str])   -- queries/phrases to search for
  apps          TEXT (JSON list[str])   -- apps that can create/edit the files
  model         TEXT
  updated_at    TEXT (ISO8601)
"""

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


# ---------------------------------------------------------------------
# 1) GPT adapter
# Replace this with your real GPT class import + usage.
# Must expose .chat(messages: list[dict]) -> str (assistant content)
# ---------------------------------------------------------------------

class DummyGPT:
	"""
	Minimal drop-in if your GPT class isn't wired yet.
	Replace with your own class (e.g., from gpt_client import GPTClient).
	Required method: chat(messages) -> assistant_text
	"""
	def __init__(self, model: str = "gpt-4o-mini", **kwargs):
		self.model = model

	def chat(self, messages: List[Dict[str, str]]) -> str:
		# Returns deterministic placeholder JSON
		payload = {
			"search_terms": [
				"high bitrate mp4",
				"4k h.264 sample",
				"lossless video container examples",
				"open source video editors comparison",
				"subtitle embedded mkv test",
			],
			"apps": [
				"Adobe Premiere Pro",
				"DaVinci Resolve",
				"Final Cut Pro",
				"Avidemux",
				"ffmpeg",
				"Shotcut",
				"HandBrake"
			]
		}
		return json.dumps(payload, ensure_ascii=False, indent=2)


def get_gpt(model: str, **kwargs):
	"""
	Swap this to your real client, e.g.:

		from gpt_client import GPTClient
		return GPTClient(model=model, **kwargs)

	The returned object must have:
		.chat(messages: List[{"role": "...", "content": "..."}]) -> str
	"""
	return DummyGPT(model=model, **kwargs)


# ---------------------------------------------------------------------
# 2) SQLite helpers
# ---------------------------------------------------------------------

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS ai_search_catalog (
	type         TEXT PRIMARY KEY,
	search_terms TEXT NOT NULL,   -- JSON array of strings
	apps         TEXT NOT NULL,   -- JSON array of strings
	model        TEXT,
	updated_at   TEXT             -- ISO8601
);
"""

def ensure_schema(conn: sqlite3.Connection) -> None:
	conn.executescript(SCHEMA_SQL)
	conn.commit()


def fetch_records_for_type(
	conn: sqlite3.Connection,
	type_label: str,
	source_sql: str,
	limit: int
) -> List[Dict[str, Any]]:
	"""
	Fetch sample records for a given type_label using user-provided SQL.

	The SQL should contain a named parameter :type (and optional :limit),
	and must SELECT columns you want to show GPT. We convert rows to dicts.
	"""
	sql = source_sql.strip()
	# If caller didn't use :limit in SQL, enforce via wrapper
	if ":limit" not in sql.lower():
		# Wrap in a subquery to apply LIMIT safely
		sql = f"SELECT * FROM ({sql}) LIMIT :limit"

	cur = conn.execute(sql, {"type": type_label, "limit": limit})
	cols = [c[0] for c in cur.description] if cur.description else []
	out: List[Dict[str, Any]] = []
	for row in cur.fetchall():
		item = {}
		for i, col in enumerate(cols):
			item[col] = row[i]
		out.append(item)
	return out


def upsert_ai_suggestions(
	conn: sqlite3.Connection,
	type_label: str,
	search_terms: List[str],
	apps: List[str],
	model: str
) -> None:
	now = datetime.utcnow().isoformat(timespec="seconds") + "Z"
	conn.execute(
		"""
		INSERT INTO ai_search_catalog (type, search_terms, apps, model, updated_at)
		VALUES (:type, :search_terms, :apps, :model, :updated_at)
		ON CONFLICT(type) DO UPDATE SET
			search_terms = excluded.search_terms,
			apps         = excluded.apps,
			model        = excluded.model,
			updated_at   = excluded.updated_at
		""",
		{
			"type": type_label,
			"search_terms": json.dumps(search_terms, ensure_ascii=False),
			"apps": json.dumps(apps, ensure_ascii=False),
			"model": model,
			"updated_at": now,
		},
	)
	conn.commit()


# ---------------------------------------------------------------------
# 3) Prompting
# ---------------------------------------------------------------------

DEFAULT_INIT_PROMPT = """You are an expert content librarian and media workflow architect.
Your job: given a media type label (e.g., "video") and a sample of records from a database,
propose two compact JSON arrays:

1) "search_terms": precise queries/keywords/phrases that help someone find or cluster this type of content.
   - Include common file extensions, codecs, containers, workflows, and troubleshooting keywords.
   - Include generic + specific phrases. 20–60 items, no duplicates.

2) "apps": names of desktop/CLI applications that can create or edit this type of content.
   - Prefer widely-used or high-signal tools. Include open-source and commercial where relevant.
   - 10–40 items, no duplicates.

Return ONLY a JSON object with keys "search_terms" and "apps".
No commentary.
"""

DEFAULT_RECORDS_INSTRUCTION = """Type label: "{type_label}"

Sample records (JSON lines):
{records_json}

Return ONLY:
{
  "search_terms": [...],
  "apps": [...]
}
"""


def run_gpt_workflow(
	gpt,
	type_label: str,
	sample_records: List[Dict[str, Any]],
	init_prompt: Optional[str] = None,
	records_instruction_tmpl: Optional[str] = None,
) -> Dict[str, Any]:
	init_prompt = init_prompt or DEFAULT_INIT_PROMPT
	records_instruction_tmpl = records_instruction_tmpl or DEFAULT_RECORDS_INSTRUCTION

	# Serialize a compact sample (JSON Lines inside a single string)
	records_lines = "\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in sample_records)
	second_msg = records_instruction_tmpl.format(
		type_label=type_label,
		records_json=records_lines or "(no records)"
	)

	messages = [
		{"role": "system", "content": init_prompt},
		{"role": "user", "content": second_msg}
	]

	raw = gpt.chat(messages)
	# Be forgiving: handle stray text before/after JSON
	parsed = try_parse_json_loose(raw)
	if not isinstance(parsed, dict):
		raise ValueError("GPT response did not parse to an object.")
	# Normalize keys
	search_terms = ensure_string_list(parsed.get("search_terms", []))
	apps = ensure_string_list(parsed.get("apps", []))
	return {"search_terms": search_terms, "apps": apps}


def try_parse_json_loose(s: str) -> Any:
	"""
	Try strict parse first; if it fails, attempt to extract the first JSON object.
	"""
	s = s.strip()
	try:
		return json.loads(s)
	except Exception:
		# Find the first top-level {...} block heuristically
		start = s.find("{")
		end = s.rfind("}")
		if start != -1 and end != -1 and end > start:
			chunk = s[start:end+1]
			try:
				return json.loads(chunk)
			except Exception:
				pass
		raise


def ensure_string_list(v: Any) -> List[str]:
	if v is None:
		return []
	if isinstance(v, list):
		out = []
		for x in v:
			if x is None:
				continue
			out.append(str(x).strip())
		# dedupe while preserving order
		seen = set()
		uniq = []
		for item in out:
			low = item.lower()
			if low in seen or not item:
				continue
			seen.add(low)
			uniq.append(item)
		return uniq
	# If GPT returned newline-separated string, split it
	if isinstance(v, str):
		parts = [p.strip() for p in v.splitlines() if p.strip()]
		return ensure_string_list(parts)
	return []


# ---------------------------------------------------------------------
# 4) CLI
# ---------------------------------------------------------------------

def build_argparser() -> argparse.ArgumentParser:
	p = argparse.ArgumentParser(
		description="Generate search terms + app suggestions by type using GPT, and store in ai_search_catalog."
	)
	p.add_argument("--db", default="mime_map.db",
				help="Path to SQLite DB (will create ai_search_catalog if not exists).")
	p.add_argument("--type", required=True,
				help="Type label to process (e.g., video, audio, image).")
	p.add_argument("--model", default="gpt-4o-mini",
				help="Model name for your GPT client.")
	p.add_argument("--limit", type=int, default=100,
				help="Max sample records to send to GPT.")
	p.add_argument("--source-sql", default=(
		# Default source SQL: change to match your schema
		# Must include a :type parameter (and optionally :limit).
		# This example assumes a 'files' table with a 'type' column.
		"SELECT id, path, mime, extension, size_bytes, duration_sec "
		"FROM files WHERE type = :type ORDER BY id"
	), help="SQL to fetch sample records for the given :type. "
			"If you omit :limit in the SQL, a LIMIT will be applied automatically.")
	p.add_argument("--init-prompt", default=None,
				help="Override the default init prompt (path to a text file or literal string).")
	p.add_argument("--records-prompt", default=None,
				help="Override the records instruction template (path to a text file or literal string).")
	return p


def load_prompt_override(val: Optional[str]) -> Optional[str]:
	if not val:
		return None
	p = Path(val)
	if p.exists():
		return p.read_text(encoding="utf-8")
	return val  # treat as literal


def main():
	ap = build_argparser()
	args = ap.parse_args()

	db_path = Path(args.db)
	type_label = args.type.strip()
	model = args.model
	limit = max(1, args.limit)

	# Create GPT client
	gpt = get_gpt(model=model)

	# Open DB and ensure table
	conn = sqlite3.connect(str(db_path))
	try:
		ensure_schema(conn)

		# Fetch sample records using the provided SQL
		records = fetch_records_for_type(conn, type_label, args.source_sql, limit)
		if not records:
			print(f"[warn] No source records found for type='{type_label}'. "
				f"Proceeding anyway (GPT can still produce generic lists).", file=sys.stderr)

		init_prompt = load_prompt_override(args.init_prompt)
		records_prompt = load_prompt_override(args.records_prompt)

		# Run the 2-message GPT workflow
		result = run_gpt_workflow(
			gpt=gpt,
			type_label=type_label,
			sample_records=records,
			init_prompt=init_prompt,
			records_instruction_tmpl=records_prompt
		)

		# Persist
		upsert_ai_suggestions(
			conn,
			type_label=type_label,
			search_terms=result["search_terms"],
			apps=result["apps"],
			model=model
		)

		print(json.dumps({
			"type": type_label,
			"rows_sampled": len(records),
			"inserted_or_updated": True,
			"model": model
		}, indent=2, ensure_ascii=False))

	finally:
		conn.close()


if __name__ == "__main__":
	main()