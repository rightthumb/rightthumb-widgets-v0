# pattern_db.py (enhanced)
# Python 3.9+
from __future__ import annotations
import sqlite3
from typing import Iterable, List, Tuple, Union, Optional, Dict, Any
import json
import os
import re
import math
from contextlib import contextmanager
from collections import defaultdict, Counter

DocInput = Union[str, List[str]]

class PatternDB:
	def __init__(self, path: str = "patterns.sqlite"):
		self.path = path
		create = not os.path.exists(path) or path == ":memory:"
		self.con = sqlite3.connect(path)
		self.con.execute("PRAGMA journal_mode=WAL;")
		self.con.execute("PRAGMA synchronous=NORMAL;")
		self.con.execute("PRAGMA temp_store=MEMORY;")
		try:
			self.con.execute("PRAGMA mmap_size=30000000000;")
		except Exception:
			pass
		if create:
			self._init_schema()

	def _init_schema(self):
		cur = self.con.cursor()
		cur.executescript(
			"""
			CREATE TABLE IF NOT EXISTS documents (
				id INTEGER PRIMARY KEY,
				name TEXT,
				kind TEXT CHECK(kind IN ('string','list')) NOT NULL,
				length INTEGER NOT NULL,
				meta TEXT NOT NULL
			);

			CREATE TABLE IF NOT EXISTS grams (
				doc_id INTEGER NOT NULL,
				n INTEGER NOT NULL,
				skip INTEGER NOT NULL,
				pos INTEGER NOT NULL,
				gram TEXT NOT NULL,
				PRIMARY KEY (doc_id, n, skip, pos),
				FOREIGN KEY (doc_id) REFERENCES documents(id) ON DELETE CASCADE
			);

			CREATE INDEX IF NOT EXISTS idx_grams_lookup ON grams(gram, n, skip);
			CREATE INDEX IF NOT EXISTS idx_grams_doc ON grams(doc_id);

			-- Corpus stats for ranking
			CREATE TABLE IF NOT EXISTS ngram_stats (
				n INTEGER NOT NULL,
				gram TEXT NOT NULL,
				cf INTEGER NOT NULL, -- collection frequency (total occurrences)
				df INTEGER NOT NULL, -- document frequency (in how many docs)
				PRIMARY KEY (n, gram)
			);
			CREATE INDEX IF NOT EXISTS idx_ngram_stats_df ON ngram_stats(n, df DESC, cf DESC);

			-- Cross-document matches (quotes / overlaps)
			CREATE TABLE IF NOT EXISTS matches (
				id INTEGER PRIMARY KEY,
				a_doc INTEGER NOT NULL,
				b_doc INTEGER NOT NULL,
				a_pos INTEGER NOT NULL,
				b_pos INTEGER NOT NULL,
				n INTEGER NOT NULL,        -- n-gram base used
				length INTEGER NOT NULL,   -- length in tokens (approx)
				score REAL NOT NULL,       -- ranking score
				method TEXT NOT NULL,      -- e.g., 'contiguous', 'backoff'
				chosen_n INTEGER NOT NULL, -- after backoff
				original_n INTEGER NOT NULL,
				details TEXT,
				FOREIGN KEY(a_doc) REFERENCES documents(id) ON DELETE CASCADE,
				FOREIGN KEY(b_doc) REFERENCES documents(id) ON DELETE CASCADE
			);
			CREATE INDEX IF NOT EXISTS idx_matches_pair ON matches(a_doc,b_doc);
			CREATE INDEX IF NOT EXISTS idx_matches_score ON matches(score DESC);

			-- Keyphrase table
			CREATE TABLE IF NOT EXISTS keyphrases (
				doc_id INTEGER NOT NULL,
				phrase TEXT NOT NULL,
				n INTEGER NOT NULL,
				freq INTEGER NOT NULL,
				score REAL NOT NULL,
				method TEXT NOT NULL,
				PRIMARY KEY (doc_id, phrase),
				FOREIGN KEY(doc_id) REFERENCES documents(id) ON DELETE CASCADE
			);

			-- Query log (optional)
			CREATE TABLE IF NOT EXISTS query_log (
				id INTEGER PRIMARY KEY,
				original_n INTEGER,
				chosen_n INTEGER,
				allow_skip INTEGER,
				hits INTEGER,
				payload TEXT,
				created_at DATETIME DEFAULT CURRENT_TIMESTAMP
			);
			"""
		)
		self.con.commit()

	@contextmanager
	def _tx(self):
		cur = self.con.cursor()
		try:
			cur.execute("BEGIN;")
			yield cur
			self.con.commit()
		except Exception:
			self.con.rollback()
			raise

	# ---------------------------
	# Public API
	# ---------------------------
	def add_document(
		self,
		data: DocInput,
		*,
		name: Optional[str] = None,
		n_values: Iterable[int] = (2,),
		max_skip: int = 0,
		normalize: bool = True,
		meta: Optional[Dict[str, Any]] = None
	) -> int:
		kind, seq, tokens = self._normalize_for_index(data, normalize)
		grams = self._make_all_grams(seq, n_values, max_skip)

		doc_meta = {"raw": data, "kind": kind, "tokens": tokens}
		if meta:
			doc_meta.update(meta)

		with self._tx() as cur:
			cur.execute(
				"INSERT INTO documents(name, kind, length, meta) VALUES(?,?,?,?)",
				(name, kind, len(seq), json.dumps(doc_meta, ensure_ascii=False)),
			)
			doc_id = cur.lastrowid
			if grams:
				cur.executemany(
					"INSERT INTO grams(doc_id, n, skip, pos, gram) VALUES(?,?,?,?,?)",
					[(doc_id, n, skip, pos, gram) for (n, skip, pos, gram) in grams],
				)
		return doc_id

	def add_bulk(self, items: Iterable[Tuple[str, DocInput]], **kwargs) -> List[int]:
		ids = []
		for name, data in items:
			ids.append(self.add_document(data, name=name, **kwargs))
		return ids

	def rebuild_stats(self):
		"""Recompute corpus ngram_stats from grams (contiguous only, skip=0)."""
		cur = self.con.cursor()
		cur.execute("DELETE FROM ngram_stats;")
		# Count collection frequency and doc frequency per (n, gram)
		cur.executescript(
			"""
			WITH base AS (
				SELECT n, gram, doc_id FROM grams WHERE skip=0
			)
			INSERT INTO ngram_stats(n, gram, cf, df)
			SELECT g.n, g.gram, COUNT(*) AS cf, COUNT(DISTINCT g.doc_id) AS df
			FROM grams g
			WHERE g.skip=0
			GROUP BY g.n, g.gram;
			"""
		)
		self.con.commit()

	def find_ngram(
		self,
		gram: Union[str, List[str]],
		*,
		n: Optional[int] = None,
		skip: Optional[int] = 0,
		like: bool = False
	) -> List[Dict[str, Any]]:
		key = self._gram_key(gram)
		params = []
		where = []
		if like:
			where.append("gram LIKE ?")
			params.append(key)
		else:
			where.append("gram = ?")
			params.append(key)
		if n is not None:
			where.append("n = ?")
			params.append(n)
		if skip is not None:
			where.append("skip = ?")
			params.append(skip)
		sql = f"SELECT doc_id, pos, n, skip, gram FROM grams WHERE {' AND '.join(where)} ORDER BY doc_id, pos"
		cur = self.con.cursor()
		return [
			{"doc_id": d, "pos": p, "n": nn, "skip": s, "gram": g}
			for (d, p, nn, s, g) in cur.execute(sql, params).fetchall()
		]

	def probe_sequence_with_backoff(
		self,
		sequence: Union[str, List[str]],
		*,
		n_max: int = 6,
		min_hits: int = 5,
		allow_skip: int = 0,
		normalize: bool = True,
		log: bool = True,
	) -> Dict[str, Any]:
		"""
		Try decreasing n from n_max..2 until we hit >= min_hits documents.
		Log both original_n and chosen_n. Returns {chosen_n, original_n, hits, docs}.
		"""
		original_n = n_max
		chosen_n = None
		hits = []
		for n in range(n_max, 1, -1):
			hits = self.find_sequence(sequence, n=n, allow_skip=allow_skip, normalize=normalize)
			if len(hits) >= min_hits:
				chosen_n = n
				break
		if chosen_n is None:
			chosen_n = 2  # worst-case fallback

		payload = {
			"sequence": sequence if not isinstance(sequence, list) else list(sequence),
			"allow_skip": allow_skip,
			"results": hits,
		}
		if log:
			with self._tx() as cur:
				cur.execute(
					"INSERT INTO query_log(original_n, chosen_n, allow_skip, hits, payload) VALUES(?,?,?,?,?)",
					(original_n, chosen_n, allow_skip, len(hits), json.dumps(payload, ensure_ascii=False)),
				)
		return {"chosen_n": chosen_n, "original_n": original_n, "hits": hits}

	def find_sequence(
		self,
		sequence: Union[str, List[str]],
		*,
		n: int = 2,
		allow_skip: int = 0,
		normalize: bool = True
	) -> List[Dict[str, Any]]:
		kind, seq, _ = self._normalize_for_index(sequence, normalize)
		probe = list(self._make_ngrams(seq, n=n, skip=0))
		if not probe:
			return []
		cur = self.con.cursor()
		doc_sets: List[set] = []
		for (_, _, _, gram_key) in probe:
			if allow_skip == 0:
				rows = cur.execute(
					"SELECT DISTINCT doc_id FROM grams WHERE gram=? AND n=? AND skip=0",
					(gram_key, n),
				).fetchall()
			else:
				rows = cur.execute(
					"SELECT DISTINCT doc_id FROM grams WHERE gram=? AND n=? AND skip BETWEEN 0 AND ?",
					(gram_key, n, allow_skip),
				).fetchall()
			doc_sets.append({r[0] for r in rows})
		if not doc_sets:
			return []
		candidate_docs = set.intersection(*doc_sets) if doc_sets else set()
		results = []
		if not candidate_docs:
			return results
		probe_keys = [g for *_, g in probe]
		if allow_skip == 0:
			q = (
				"SELECT doc_id, COUNT(*) FROM grams WHERE n=? AND skip=0 AND gram IN ({}) AND doc_id IN ({}) GROUP BY doc_id"
			).format(
				",".join("?" * len(probe_keys)),
				",".join("?" * len(candidate_docs)),
			)
			args = (n, *probe_keys, *candidate_docs)
		else:
			q = (
				"SELECT doc_id, COUNT(*) FROM grams WHERE n=? AND skip BETWEEN 0 AND ? AND gram IN ({}) AND doc_id IN ({}) GROUP BY doc_id"
			).format(
				",".join("?" * len(probe_keys)),
				",".join("?" * len(candidate_docs)),
			)
			args = (n, allow_skip, *probe_keys, *candidate_docs)
		for did, cnt in cur.execute(q, args).fetchall():
			results.append({"doc_id": did, "score": int(cnt)})
		results.sort(key=lambda x: (-x["score"], x["doc_id"]))
		return results

	def find_cross_quotes(
		self,
		*,
		min_n: int = 4,
		allow_skip: int = 0,
		min_length: int = 6,
		top_k_per_pair: int = 50,
		store: bool = True,
	) -> List[Dict[str, Any]]:
		"""
		Discover cross-document overlaps (Bible self-quotes, etc.).
		Strategy:
		1) Use contiguous grams (skip=0) with n>=min_n that occur in >=2 docs.
		2) For each pair of docs sharing a gram, extend alignment forward while grams align (same (n,skip) and relative offsets).
		3) Score longer, rarer chains higher using length * IDF(avg).
		Save to matches table with ranking & details.
		"""
		cur = self.con.cursor()
		# Ensure stats exist
		self.rebuild_stats()
		# Candidate grams (rare-ish, in >=2 docs)
		grams_cand = cur.execute(
			"SELECT n, gram, df FROM ngram_stats WHERE n>=? AND df>=2 ORDER BY df ASC, n DESC LIMIT 200000",
			(min_n,),
		).fetchall()
		results: List[Dict[str, Any]] = []
		# group occurrences for speed
		for n, gram, df in grams_cand:
			occ = cur.execute(
				"SELECT doc_id, pos FROM grams WHERE n=? AND skip=0 AND gram=? ORDER BY doc_id, pos",
				(n, gram),
			).fetchall()
			if len(occ) < 2:
				continue
			# For each pair of docs, try to extend alignment
			by_doc: Dict[int, List[int]] = defaultdict(list)
			for did, pos in occ:
				by_doc[did].append(pos)
			doc_ids = sorted(by_doc.keys())
			inv_df = 1.0 / float(df)
			for i in range(len(doc_ids)):
				for j in range(i + 1, len(doc_ids)):
					a, b = doc_ids[i], doc_ids[j]
					apos_list, bpos_list = by_doc[a], by_doc[b]
					# two-pointer over positions to find equal deltas
					ia = 0
					ib = 0
					while ia < len(apos_list) and ib < len(bpos_list):
						da = apos_list[ia]
						db = bpos_list[ib]
						# Align on this seed
						length = n
						step = 1
						extended = 0
						while True:
							na = da + step
							nb = db + step
							gnext = cur.execute(
								"SELECT 1 FROM grams WHERE doc_id=? AND n=? AND skip=0 AND pos=? AND gram IN (SELECT gram FROM grams WHERE doc_id=? AND n=? AND skip=0 AND pos=?)",
								(a, n, na, b, n, nb),
							).fetchone()
							if gnext:
								length += 1
								step += 1
								extended += 1
							else:
								break
						if length >= max(min_length, n):
							# score: length * idf (rarer grams better)
							score = float(length) * math.log(1.0 + inv_df)
							rec = {
								"a_doc": a,
								"b_doc": b,
								"a_pos": da,
								"b_pos": db,
								"n": n,
								"length": length,
								"score": score,
								"method": "contiguous",
								"chosen_n": n,
								"original_n": n,
								"details": json.dumps({"df": df, "seed": gram}),
							}
							results.append(rec)
						# advance pointers
						if ia + 1 < len(apos_list) and (ib + 1 == len(bpos_list) or apos_list[ia + 1] <= bpos_list[ib + 1]):
							ia += 1
						else:
							ib += 1
		# Rank and optionally keep top_k per doc pair
		results.sort(key=lambda r: (-r["score"], -r["length"]))
		if top_k_per_pair is not None:
			trimmed: List[Dict[str, Any]] = []
			buckets: Dict[Tuple[int, int], int] = defaultdict(int)
			for r in results:
				key = (r["a_doc"], r["b_doc"]) if r["a_doc"] < r["b_doc"] else (r["b_doc"], r["a_doc"]) 
				if buckets[key] < top_k_per_pair:
					trimmed.append(r)
					buckets[key] += 1
			results = trimmed
		if store and results:
			with self._tx() as cur:
				cur.executemany(
					"INSERT INTO matches(a_doc,b_doc,a_pos,b_pos,n,length,score,method,chosen_n,original_n,details) VALUES(?,?,?,?,?,?,?,?,?,?,?)",
					[(
						r["a_doc"], r["b_doc"], r["a_pos"], r["b_pos"], r["n"], r["length"], r["score"], r["method"], r["chosen_n"], r["original_n"], r["details"]
					) for r in results],
				)
		return results

	def extract_keyphrases(
		self,
		doc_id: int,
		*,
		n_range: Tuple[int, int] = (1, 3),
		min_freq: int = 2,
		top_k: int = 50,
		method: str = "npmi",
		save: bool = True,
	) -> List[Tuple[str, int, float]]:
		"""Simple automatic keyphrase scoring.
		- For n=1: score by normalized TF * IDF.
		- For n=2: NPMI (pointwise mutual information normalized to [-1,1]).
		- For n=3: average of bigram NPMIs across its edges, weighted by freq.
		"""
		cur = self.con.cursor()
		row = cur.execute("SELECT meta FROM documents WHERE id=?", (doc_id,)).fetchone()
		if not row:
			raise KeyError(f"doc {doc_id} not found")
		meta = json.loads(row[0])
		tokens = meta.get("tokens") or []
		tokens = [t for t in tokens if t.strip()]
		if not tokens:
			return []

		start_n, end_n = n_range
		# local counts
		local_counts: Dict[Tuple[int, str], int] = Counter()
		for n in range(start_n, end_n + 1):
			for _, key in self._iter_contiguous(tokens, n):
				local_counts[(n, key)] += 1
		# global stats (from ngram_stats)
		stats = {
			(n, gram): (cf, df)
			for (n, gram, cf, df) in cur.execute(
				"SELECT n, gram, cf, df FROM ngram_stats WHERE n BETWEEN ? AND ?",
				(start_n, end_n),
			).fetchall()
		}
		# total positions for probabilities (approximate by sum cf for 1-grams)
		total_unigrams = sum(cf for (n, g, cf, df) in cur.execute(
			"SELECT n, gram, cf, df FROM ngram_stats WHERE n=1").fetchall()) or 1

		def p1(key: str) -> float:
			cf, _ = stats.get((1, key), (0, 0))
			return max(cf, 1) / total_unigrams

		def p2(key: str) -> float:
			cf, _ = stats.get((2, key), (0, 0))
			return max(cf, 1) / max(total_unigrams - 1, 1)

		scored: List[Tuple[str, int, float]] = []
		for (n, key), freq in local_counts.items():
			if freq < min_freq:
				continue
			if n == 1:
				cf, df = stats.get((1, key), (0, 1))
				idf = math.log(1 + (1 + self._doc_count()) / (1 + df))
				score = (freq / max(1, len(tokens))) * idf
			elif n == 2:
				w1, w2 = key.split("\x1f") if "\x1f" in key else [key[:1], key[1:]]
				p_x = p1(w1)
				p_y = p1(w2)
				p_xy = p2(key)
				pmi = math.log(max(p_xy / (p_x * p_y), 1e-12))
				npmi = pmi / -math.log(max(p_xy, 1e-12))
				score = npmi * freq
			else:
				parts = key.split("\x1f") if "\x1f" in key else [c for c in key]
				if len(parts) < 3:
					continue
				b1 = "\x1f".join(parts[0:2])
				b2 = "\x1f".join(parts[1:3])
				# average bigram NPMI
				def npmi_bigram(bkey: str) -> float:
					x, y = bkey.split("\x1f") if "\x1f" in bkey else [bkey[:1], bkey[1:]]
					px, py, pxy = p1(x), p1(y), p2(bkey)
					pmi = math.log(max(pxy / (px * py), 1e-12))
					return pmi / -math.log(max(pxy, 1e-12))
				score = ((npmi_bigram(b1) + npmi_bigram(b2)) / 2.0) * freq
			scored.append((key, n, float(score)))
		scored.sort(key=lambda x: (-x[2], -x[1]))
		if top_k:
			scored = scored[:top_k]
		if save and scored:
			with self._tx() as cur:
				cur.executemany(
					"INSERT OR REPLACE INTO keyphrases(doc_id, phrase, n, freq, score, method) VALUES(?,?,?,?,?,?)",
					[
						(doc_id, key, n, local_counts[(n, key)], score, method)
						for (key, n, score) in scored
					],
				)
		return scored

	def get_document(self, doc_id: int) -> Dict[str, Any]:
		cur = self.con.cursor()
		row = cur.execute(
			"SELECT id, name, kind, length, meta FROM documents WHERE id=?", (doc_id,)
		).fetchone()
		if not row:
			raise KeyError(f"doc {doc_id} not found")
		id_, name, kind, length, meta = row
		return {"id": id_, "name": name, "kind": kind, "length": length, "meta": json.loads(meta)}

	# ---------------------------
	# Internals
	# ---------------------------
	def _doc_count(self) -> int:
		return int(self.con.execute("SELECT COUNT(*) FROM documents").fetchone()[0])

	def _normalize_for_index(self, data: DocInput, normalize: bool) -> Tuple[str, List[str], List[str]]:
		"""
		Returns: (kind, seq_for_grams, token_list_for_keyphrases)
		- Strings: seq is list of chars; tokens are word tokens.
		- Lists: seq is tokens; tokens are tokens.
		"""
		if isinstance(data, str):
			s = data
			if normalize:
				s = s.lower()
			# tokens for keyphrases
			tokens = re.findall(r"[a-z0-9']+", s)
			# sequence for grams = characters (including spaces collapsed)
			s = re.sub(r"\s+", " ", s.strip())
			seq = list(s)
			return "string", seq, tokens
		elif isinstance(data, list):
			toks = [str(x) for x in data]
			if normalize:
				toks = [t.lower() for t in toks]
			return "list", toks, toks
		else:
			raise TypeError("data must be str or list[str]")

	def _gram_key(self, gram: Union[str, List[str]]) -> str:
		if isinstance(gram, list):
			return "\x1f".join(gram)
		elif isinstance(gram, str):
			return gram
		else:
			raise TypeError("gram must be str or list[str]")

	def _make_all_grams(
		self,
		seq: List[str],
		n_values: Iterable[int],
		max_skip: int
	) -> List[Tuple[int, int, int, str]]:
		out: List[Tuple[int, int, int, str]] = []
		for n in n_values:
			for (pos, key) in self._iter_contiguous(seq, n):
				out.append((n, 0, pos, key))
			if n == 2 and max_skip > 0:
				for k in range(1, max_skip + 1):
					for (pos, key) in self._iter_skip_bigrams(seq, k):
						out.append((2, k, pos, key))
		return out

	def _make_ngrams(self, seq: List[str], n: int, skip: int = 0):
		if n == 2 and skip > 0:
			for (pos, key) in self._iter_skip_bigrams(seq, skip):
				yield (n, skip, pos, key)
		else:
			for (pos, key) in self._iter_contiguous(seq, n):
				yield (n, 0, pos, key)

	def _iter_contiguous(self, seq: List[str], n: int) -> Iterable[Tuple[int, str]]:
		if n <= 0 or n > len(seq):
			return []
		is_list_ngram = not all(len(x) == 1 for x in seq)
		for i in range(0, len(seq) - n + 1):
			chunk = seq[i : i + n]
			key = "\x1f".join(chunk) if is_list_ngram else "".join(chunk)
			yield (i, key)

	def _iter_skip_bigrams(self, seq: List[str], skip: int) -> Iterable[Tuple[int, str]]:
		is_list_ngram = not all(len(x) == 1 for x in seq)
		jstep = skip + 1
		limit = len(seq) - (1 + jstep - 1)
		for i in range(0, max(0, limit)):
			j = i + jstep
			key = ("\x1f".join([seq[i], seq[j]]) if is_list_ngram else seq[i] + seq[j])
			yield (i, key)

# 689769bc-e6c8-832c-b0de-cadfe5cd5b6a

# ---------------------------
# Minimal usage example
# ---------------------------
if __name__ == "__main__":
	pdb = PatternDB(":memory:")

	# Ingest a few Bible-like snippets (token lists per verse)
	v1 = ["in", "the", "beginning", "was", "the", "word"]
	v2 = ["the", "word", "was", "with", "god"]
	v3 = ["in", "the", "beginning", "god", "created", "the", "heavens", "and", "the", "earth"]

	id1 = pdb.add_document(v1, name="John 1:1a", n_values=(1,2,3,4), max_skip=1)
	id2 = pdb.add_document(v2, name="John 1:1b", n_values=(1,2,3,4), max_skip=1)
	id3 = pdb.add_document(v3, name="Genesis 1:1", n_values=(1,2,3,4), max_skip=1)

	pdb.rebuild_stats()

	# Cross-quote discovery
	hits = pdb.find_cross_quotes(min_n=3, min_length=4)
	print(f"cross-quote matches: {len(hits)}")

	# Backoff probe example
	probe = pdb.probe_sequence_with_backoff(["in","the","beginning","was","the","word"], n_max=4, min_hits=1)
	print("probe:", probe["original_n"], "->", probe["chosen_n"], "hits:", len(probe["hits"]))

	# Keyphrases
	kp = pdb.extract_keyphrases(id3, n_range=(1,3), min_freq=1, top_k=10)
	print("keyphrases (Genesis 1:1):", kp[:5])