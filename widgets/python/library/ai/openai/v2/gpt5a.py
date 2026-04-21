from __future__ import annotations
"""
mygpt - Unified GPT helper library (one-file version).

FEATURES (all via this one module)
==================================
Core client:
    - GPTClient: full-featured client wrapping OpenAI chat + embeddings.

One-off chat:
    - chat(prompt, **opts)

Session management:
    - start_session(session_id=None, system=None) -> str
    - close_session(sid)
    - reset_session(sid, system=None)
    - add_message(sid, role, content)
    - get_session_messages(sid) -> list[dict]
    - set_session_label(sid, label)
    - get_session_label(sid) -> str | None
    - get_session_parent(sid) -> str | None
    - get_session_children(sid) -> list[str]
    - get_session_fork_graph() -> dict

Session chat:
    - chat_session(sid, user_message, **opts) -> str
    - chat_session_rag(sid, user_message, **opts) -> str  # RAG over session vectors

Embeddings (global + per-session):
    - embed(input_texts, **opts) -> {"model", "vectors", "dims"}
    - set_session_vectors(sid, entries)
    - get_session_vectors(sid) -> list[dict]
    - session_embed_add(sid, texts, **opts) -> list[int]
    - session_embed_search(sid, query, k=5, **opts) -> list[dict]
    - session_embed_count(sid) -> int
    - session_embed_clear(sid)

Layout (global) embeddings:
    - layout_embed_add(layout_id, texts, **opts) -> list[int]
    - layout_embed_search(layout_id, query, k=5, **opts) -> list[dict]

Checkpoints & session forking:
    - create_checkpoint(sid, label, **opts) -> dict
    - get_checkpoints(sid) -> list[dict]
    - set_checkpoints(sid, cps)
    - fork_session(parent_sid, checkpoint_id=None, **opts) -> str
    - set_session_relations(parent_id, children, sid)

Persistence:
    - dump_state() -> dict
    - load_state(state: dict) -> None

Introspection / config:
    - get_last_call_info() -> dict
    - set_api_url(url)
    - resolve_token_limit(mode_or_int, model=None) -> int

Low-level utils (from this module, not the class):
    - load_openai_api_key()
    - cosine(a, b)
    - top_k(vectors, q, k=5)
"""

import os, json, time, math, random, typing as t
from dataclasses import dataclass, field

# OpenAI SDK (modern style). If you use an older SDK, adjust create() calls below.
try:
    from openai import OpenAI
except Exception:  # pragma: no cover
    OpenAI = None  # Allows tests to run without the SDK installed


# ---------------------------
# API key loader (exact flow)
# ---------------------------
def load_openai_api_key() -> str:
    rt_path = os.path.expanduser('~/.rt')
    key_file = os.path.join(rt_path, 'openai.key')
    config_file = os.path.join(rt_path, '.config.hash')
    api_key = None

    if os.path.exists(key_file):
        with open(key_file, 'r', encoding='utf-8') as f:
            api_key = f.read().strip()
    elif os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            try:
                cfg = json.load(f)
                api_key = cfg.get('openai') if isinstance(cfg, dict) else None
            except json.JSONDecodeError:
                api_key = None

    if not api_key:
        raise ValueError("File ~/.rt/openai.key not found.")
    return api_key


# ---------------------------
# Utilities / math
# ---------------------------
def _l2_normalize(v: t.List[float]) -> t.List[float]:
    s = sum(x * x for x in v); n = math.sqrt(s) or 1.0
    return [x / n for x in v]


def cosine(a: t.List[float], b: t.List[float]) -> float:
    n = min(len(a), len(b))
    return sum(a[i] * b[i] for i in range(n))


def top_k(vectors: t.List[t.List[float]], q: t.List[float], k: int = 5) -> t.List[dict]:
    scored = [{'index': i, 'score': cosine(q, v)} for i, v in enumerate(vectors)]
    scored.sort(key=lambda r: r['score'], reverse=True)
    return scored[: max(1, k)]


# ---------------------------
# Client
# ---------------------------
@dataclass
class GPTClient:
    api_key: t.Optional[str] = None
    api_url: str = "https://api.openai.com/v1"

    # debug / inspection
    last_request_meta: dict = field(default_factory=dict)
    last_high_level_meta: dict = field(default_factory=dict)

    # sessions & graphs
    sessions: dict = field(default_factory=dict)  # session_id -> list[{'role','content'}]
    session_vecs: dict = field(default_factory=dict)  # session_id -> [{'text','vec','meta'}]
    session_parents: dict = field(default_factory=dict)  # session_id -> parent_id
    session_children: dict = field(default_factory=dict)  # parent_id -> [child_id,...]
    session_checkpoints: dict = field(default_factory=dict)  # session_id -> [checkpoint dicts]
    session_labels: dict = field(default_factory=dict)  # session_id -> label

    # layout/global vectors
    layout_vecs: dict = field(default_factory=dict)  # layout_id -> [{'text','vec','meta'}]

    default_chunk_size: int = 2048

    def __post_init__(self):
        # Keep your exact key-loading semantics by default
        if self.api_key is None:
            self.api_key = load_openai_api_key()
        if OpenAI is None:
            # SDK not installed; allow logic tests to proceed
            self._client = None
        else:
            self._client = OpenAI(api_key=self.api_key, base_url=self.api_url)

    # ---------------------------
    # Config knobs / heuristics
    # ---------------------------
    def set_api_url(self, url: str) -> None:
        self.api_url = url.rstrip("/")
        if self._client is not None:
            self._client = OpenAI(api_key=self.api_key, base_url=self.api_url)

    @staticmethod
    def _gpt_timeouts(model: t.Optional[str] = None, stream: bool = False) -> dict:
        m = (model or "").lower()
        tier = "small"
        if "gpt-3.5" in m or m.endswith("mini"):
            tier = "small"
        elif "gpt-4o" in m or "gpt-4" in m:
            tier = "medium"
        if "turbo" in m or "gpt-5" in m or "4.1" in m or "1m" in m:
            tier = "large"
        overall = {"small": 60, "medium": 180, "large": 300}.get(tier, 120)
        if stream:
            overall = max(overall, 300)
        return {
            "connect_timeout": 5,
            "overall_timeout": overall,
            "low_speed_limit": 100,
            "low_speed_time": 20,
        }

    @staticmethod
    def _prefers_completion_tokens(model: str) -> bool:
        m = (model or "").lower()
        return any(x in m for x in ("gpt-5", "gpt-4.1", "o3", "o4", "1m"))

    @staticmethod
    def _model_locks_sampling(model: str) -> bool:
        m = (model or "").lower()
        return any(x in m for x in ("gpt-5", "gpt-4.1", "o1", "o2", "o3", "o4"))

    # ---------------------------
    # Tokens sizing
    # ---------------------------
    @staticmethod
    def resolve_token_limit(mode_or_int: t.Union[str, int], model: t.Optional[str] = None) -> int:
        if isinstance(mode_or_int, int):
            return int(mode_or_int)
        m = (mode_or_int or "").strip().lower()
        mapping = {
            "t": 4096,
            "tiny": 4096,
            "s": 32000,
            "small": 32000,
            "m": 128000,
            "medium": 128000,
            "l": 256000,
            "large": 256000,
            "h": 1000000,
            "huge": 1000000,
            "x": 1000000,
            "extra": 1000000,
        }
        return mapping.get(m[:1] if m else "l", 256000)

    # ---------------------------
    # Low-level call (retries + heuristics)
    # ---------------------------
    def _sleep_backoff(self, backoff: float) -> float:
        time.sleep(backoff)
        return min(8.0, backoff * 2.0) + (random.randint(0, 200) / 1000.0)

    def _call_once(
        self,
        messages: t.List[dict],
        model: str,
        max_tokens: int,
        temperature: float,
        top_p: float,
        timeouts: dict,
        retries: int,
    ) -> str:
        attempts = 0
        backoff = 1.0
        forced_param_key: t.Optional[str] = None
        omit_sampling = self._model_locks_sampling(model)

        while True:
            attempts += 1
            param_key = forced_param_key or ("max_completion_tokens" if self._prefers_completion_tokens(model) else "max_tokens")

            payload = {
                "model": model,
                "messages": messages,
            }
            if param_key == "max_tokens":
                payload["max_tokens"] = max_tokens
            else:
                payload["max_completion_tokens"] = max_tokens

            if not omit_sampling:
                payload["temperature"] = temperature
                payload["top_p"] = top_p

            self.last_request_meta = {
                "api_url": self.api_url,
                "model": model,
                "token_param": param_key,
                "token_value": max_tokens,
                "sampling": {
                    "omitted": omit_sampling,
                    "temperature": None if omit_sampling else temperature,
                    "top_p": None if omit_sampling else top_p,
                },
                "timeouts": timeouts,
                "retries": retries,
                "messages_count": len(messages),
                "messages_roles": [m.get("role", "unknown") for m in messages],
            }

            try:
                if self._client is None:  # SDK missing; return stub for tests
                    return "(mocked-assistant)"
                # Chat Completions
                resp = self._client.chat.completions.create(**payload)
                # Usage metadata when present
                usage = getattr(resp, "usage", None)
                if usage:
                    self.last_request_meta["response"] = {
                        "id": getattr(resp, "id", None),
                        "created": getattr(resp, "created", None),
                        "usage": {
                            "prompt_tokens": getattr(usage, "prompt_tokens", None),
                            "completion_tokens": getattr(usage, "completion_tokens", None),
                            "total_tokens": getattr(usage, "total_tokens", None),
                        },
                    }
                content = ""
                if getattr(resp, "choices", None):
                    msg = resp.choices[0].message
                    content = getattr(msg, "content", "") or ""
                return str(content)

            except Exception as e:  # Network / API errors
                msg = str(e)
                # Switch token parameter if server hints
                if (param_key == "max_tokens") and ("max_completion_tokens" in msg) and (forced_param_key != "max_completion_tokens"):
                    forced_param_key = "max_completion_tokens"
                    self.last_request_meta["note"] = "Switched to max_completion_tokens due to server hint."
                    backoff = self._sleep_backoff(backoff)
                    if attempts <= retries + 1:
                        continue

                # Omit sampling if model enforces defaults
                if (not omit_sampling) and ("Only the default (1) value is supported" in msg) and (
                    "temperature" in msg or "top_p" in msg
                ):
                    omit_sampling = True
                    self.last_request_meta["note"] = "Omitted sampling params due to model restrictions."
                    backoff = self._sleep_backoff(backoff)
                    if attempts <= retries + 1:
                        continue

                # Transient HTTP-ish errors we can retry on
                transient = any(code in msg for code in ("408", "409", "425", "429", "500", "502", "503", "504"))
                if attempts <= retries + 1 and transient:
                    self.last_request_meta["note"] = "Retrying due to transient error."
                    backoff = self._sleep_backoff(backoff)
                    continue
                raise

    # ---------------------------
    # Sessions
    # ---------------------------
    def _ensure_session(self, sid: str) -> None:
        if sid not in self.sessions:
            self.sessions[sid] = []

    def start_session(self, session_id: t.Optional[str] = None, system: t.Optional[str] = None) -> str:
        sid = session_id or os.urandom(12).hex()
        if sid not in self.sessions or not isinstance(self.sessions[sid], list):
            self.sessions[sid] = []
        if system:
            self.sessions[sid].append({"role": "system", "content": str(system)})
        if sid not in self.session_vecs:
            self.session_vecs[sid] = []
        if sid not in self.session_checkpoints:
            self.session_checkpoints[sid] = []
        if sid not in self.session_children:
            self.session_children[sid] = []
        return sid

    def close_session(self, sid: str) -> None:
        self.sessions.pop(sid, None)
        self.session_vecs.pop(sid, None)
        self.session_checkpoints.pop(sid, None)
        self.session_labels.pop(sid, None)
        parent = self.session_parents.pop(sid, None)
        if parent and parent in self.session_children:
            self.session_children[parent] = [c for c in self.session_children[parent] if c != sid]
        self.session_children.pop(sid, None)

    def reset_session(self, sid: str, system: t.Optional[str] = None) -> None:
        self.sessions[sid] = []
        self.session_vecs[sid] = []
        self.session_checkpoints[sid] = []
        if system is not None:
            self.sessions[sid].append({"role": "system", "content": str(system)})

    def add_message(self, sid: str, role: str, content: str) -> None:
        self._ensure_session(sid)
        if str(content).strip():
            self.sessions[sid].append({"role": role, "content": content})

    def get_session_messages(self, sid: str) -> t.List[dict]:
        self._ensure_session(sid)
        return self.sessions[sid]

    def set_session_label(self, sid: str, label: t.Optional[str]) -> None:
        if label:
            self.session_labels[sid] = label
        else:
            self.session_labels.pop(sid, None)

    def get_session_label(self, sid: str) -> t.Optional[str]:
        return self.session_labels.get(sid)

    def get_session_parent(self, sid: str) -> t.Optional[str]:
        return self.session_parents.get(sid)

    def get_session_children(self, sid: str) -> t.List[str]:
        return list(self.session_children.get(sid, []))

    def get_session_fork_graph(self) -> dict:
        return {"parents": dict(self.session_parents), "children": dict(self.session_children)}

    # ---------------------------
    # Embeddings
    # ---------------------------
    def embed(self, input_texts: t.Union[str, t.List[str]], *, model: str = "text-embedding-3-small", normalize: bool = True,
              timeout: int = 60, retries: int = 2) -> dict:
        inputs = [input_texts] if isinstance(input_texts, str) else list(input_texts or [])
        inputs = [str(x).strip() for x in inputs if str(x).strip()]
        if not inputs:
            self.last_request_meta = {
                "api_url": self.api_url,
                "endpoint": "embeddings.create",
                "model": model,
                "inputs": 0,
                "dims": 0,
                "skipped": "empty_inputs",
                "timeouts": {"overall_timeout": timeout},
            }
            self.last_high_level_meta = {"mode": "embeddings", "model": model, "count": 0, "dims": 0, "normalize": normalize}
            return {"model": model, "vectors": [], "dims": 0}

        attempts = 0
        backoff = 1.0
        while True:
            attempts += 1
            try:
                if self._client is None:  # SDK missing; return unit-length mocks
                    vecs = [[1.0] + [0.0] * 3 for _ in inputs]
                else:
                    resp = self._client.embeddings.create(model=model, input=inputs)
                    rows = getattr(resp, "data", None) or getattr(resp, "embeddings", None)
                    if not rows:
                        # Attempt to coerce from dict-like
                        try:
                            arr = resp.to_dict()  # type: ignore
                        except Exception:
                            arr = {}
                        rows = arr.get("data") or arr.get("embeddings") or []
                    vecs = []
                    for row in rows:
                        emb = row.get("embedding") if isinstance(row, dict) else getattr(row, "embedding", None)
                        if isinstance(emb, list):
                            vecs.append(emb)
                if not vecs:
                    raise RuntimeError("Embeddings call succeeded but returned zero vectors.")
                if normalize:
                    vecs = [_l2_normalize(v) for v in vecs]
                dims = len(vecs[0]) if vecs else 0

                self.last_request_meta = {
                    "api_url": self.api_url,
                    "endpoint": "embeddings.create",
                    "model": model,
                    "inputs": len(inputs),
                    "dims": dims,
                    "timeouts": {"overall_timeout": timeout},
                }
                self.last_high_level_meta = {"mode": "embeddings", "model": model, "count": len(inputs), "dims": dims, "normalize": normalize}
                return {"model": model, "vectors": vecs, "dims": dims}

            except Exception as e:
                msg = str(e)
                transient = any(code in msg for code in ("408", "409", "425", "429", "500", "502", "503", "504"))
                if attempts <= retries + 1 and transient:
                    backoff = self._sleep_backoff(backoff)
                    continue
                raise

    def set_session_vectors(self, sid: str, entries: t.List[dict]) -> None:
        self.session_vecs[sid] = list(entries)

    def get_session_vectors(self, sid: str) -> t.List[dict]:
        return list(self.session_vecs.get(sid, []))

    def session_embed_add(self, sid: str, texts: t.Union[str, t.List[str]], **opts) -> t.List[int]:
        self._ensure_session(sid)
        if sid not in self.session_vecs:
            self.session_vecs[sid] = []
        items = [texts] if isinstance(texts, str) else list(texts or [])
        items = [s for s in items if str(s).strip()]
        if not items:
            return []
        emb = self.embed(items, **opts)
        meta_base = opts.get("meta", {})
        idxs = []
        for i, vec in enumerate(emb["vectors"]):
            self.session_vecs[sid].append({"text": items[i], "vec": vec, "meta": meta_base})
            idxs.append(len(self.session_vecs[sid]) - 1)
        return idxs

    def session_embed_count(self, sid: str) -> int:
        return len(self.session_vecs.get(sid, []))

    def session_embed_clear(self, sid: str) -> None:
        self.session_vecs[sid] = []

    def session_embed_search(self, sid: str, query: str, k: int = 5, **opts) -> t.List[dict]:
        entries = self.session_vecs.get(sid, [])
        if not entries:
            return []
        emb = self.embed(query, **opts)
        q = emb["vectors"][0]
        vecs = [e["vec"] for e in entries]
        hits = top_k(vecs, q, min(k, len(vecs)))
        for h in hits:
            e = entries[h["index"]]
            h["text"] = e["text"]
            h["meta"] = e["meta"]
        return hits

    # ---------------------------
    # Checkpoints & forking
    # ---------------------------
    def set_session_relations(self, parent_id: t.Optional[str], children: t.List[str], sid: str) -> None:
        if parent_id:
            self.session_parents[sid] = parent_id
            self.session_children.setdefault(parent_id, [])
        self.session_children[sid] = list(children)

    def set_checkpoints(self, sid: str, cps: t.List[dict]) -> None:
        self.session_checkpoints[sid] = list(cps)

    def get_checkpoints(self, sid: str) -> t.List[dict]:
        return list(self.session_checkpoints.get(sid, []))

    def create_checkpoint(
        self,
        sid: str,
        label: str,
        summary: t.Optional[str] = None,
        message_id: t.Optional[int] = None,
        keep_last: int = 12,
        **opts,
    ) -> dict:
        self._ensure_session(sid)
        msgs = self.sessions[sid]

        if message_id is not None and msgs:
            idx = int(message_id)
            if opts.get("one_based") is True:
                idx -= 1
            if idx not in range(len(msgs)) and (idx - 1) in range(len(msgs)):
                idx -= 1
            idx = max(0, min(idx, len(msgs) - 1))
            slice_msgs = msgs[: idx + 1]
        else:
            slice_msgs = msgs[-keep_last:] if keep_last > 0 else msgs[:]
            idx = None

        if summary is None:
            model = opts.get("model", "gpt-5")
            max_tokens_raw = opts.get("max_tokens", 300)
            max_tokens = self.resolve_token_limit(max_tokens_raw, model) if isinstance(max_tokens_raw, str) else int(max_tokens_raw)
            timeouts = self._gpt_timeouts(model, False)
            if "timeout" in opts:
                timeouts["overall_timeout"] = int(opts["timeout"])
            sys = {
                "role": "system",
                "content": (
                    "Summarize the following conversation into a concise checkpoint memory. "
                    "Keep entities, goals, decisions, constraints, and open tasks. Omit chit-chat. Plain text only."
                ),
            }
            summary = self._call_once([sys] + slice_msgs, model, max_tokens, 0.2, 1.0, timeouts, int(opts.get("retries", 1)))

        cp = {
            "id": os.urandom(8).hex(),
            "label": label,
            "summary": str(summary).strip(),
            "message_id": idx,
            "ts": int(time.time()),
        }
        self.session_checkpoints.setdefault(sid, []).append(cp)
        return cp

    def fork_session(self, parent_sid: str, checkpoint_id: t.Optional[str] = None, **opts) -> str:
        self._ensure_session(parent_sid)
        keep_last = int(opts.get("keep_last", 8))
        inherit_vectors = bool(opts.get("inherit_vectors", True))
        child_label = str(opts.get("label", "") or "")

        seed_system = None
        if checkpoint_id:
            for c in self.session_checkpoints.get(parent_sid, []):
                if c.get("id") == checkpoint_id:
                    seed_system = f"Forked from {parent_sid}\nCheckpoint: {c.get('label')}\n—\n{c.get('summary')}"
                    break

        child = self.start_session(system=seed_system)
        if child_label:
            self.set_session_label(child, child_label)
            self.sessions[child].append({"role": "system", "content": f"Branch label: {child_label}"})

        parent_msgs = list(self.sessions[parent_sid])
        tail = parent_msgs[-keep_last:] if keep_last > 0 else parent_msgs

        inserted_system = bool(seed_system) or bool(child_label)
        for m in tail:
            if inserted_system and m.get("role") == "system":
                # avoid duplicate system rows at the front
                continue
            self.sessions[child].append(m)

        # relations
        self.session_parents[child] = parent_sid
        self.session_children.setdefault(parent_sid, []).append(child)

        # vectors
        if inherit_vectors:
            self.session_vecs[child] = list(self.session_vecs.get(parent_sid, []))

        # child initial checkpoint (seed)
        if seed_system:
            self.session_checkpoints.setdefault(child, []).append({
                "id": os.urandom(6).hex(),
                "label": "Fork seed: " + (child_label or "from checkpoint"),
                "summary": seed_system,
                "message_id": None,
                "ts": int(time.time()),
            })

        return child

    # ---------------------------
    # Layout embeddings (global)
    # ---------------------------
    def layout_embed_add(self, layout_id: str, texts: t.Union[str, t.List[str]], **opts) -> t.List[int]:
        self.layout_vecs.setdefault(layout_id, [])
        items = [texts] if isinstance(texts, str) else list(texts or [])
        items = [s for s in items if str(s).strip()]
        if not items:
            return []
        emb = self.embed(items, **opts)
        added = []
        for i, vec in enumerate(emb["vectors"]):
            self.layout_vecs[layout_id].append({"text": items[i], "vec": vec, "meta": opts.get("meta", {})})
            added.append(len(self.layout_vecs[layout_id]) - 1)
        return added

    def layout_embed_search(self, layout_id: str, query: str, k: int = 5, **opts) -> t.List[dict]:
        entries = self.layout_vecs.get(layout_id, [])
        if not entries:
            return []
        emb = self.embed(query, **opts)
        q = emb["vectors"][0]
        vecs = [e["vec"] for e in entries]
        hits = top_k(vecs, q, k)
        for h in hits:
            e = entries[h["index"]]
            h["text"] = e["text"]
            h["meta"] = e["meta"]
        return hits

    # ---------------------------
    # Chat entry points
    # ---------------------------
    @staticmethod
    def _mb_split(text: str, chunk: int) -> t.List[str]:
        return [text[i:i + chunk] for i in range(0, len(text), chunk)]

    def chat(self, prompt: str, **opts) -> str:
        model = opts.get("model", "gpt-5")
        temperature = float(opts.get("temperature", 0.7))
        top_p = float(opts.get("top_p", 0.9))

        max_tokens_raw = opts.get("max_tokens", opts.get("tokens", opts.get("t", 2048)))
        max_tokens = self.resolve_token_limit(max_tokens_raw, model) if isinstance(max_tokens_raw, str) else int(max_tokens_raw)

        timeouts = self._gpt_timeouts(model, False)
        if "timeout" in opts:
            timeouts["overall_timeout"] = int(opts["timeout"])

        auto_split = bool(opts.get("auto_split", True))
        chunk_size = int(opts.get("chunk_size", self.default_chunk_size))
        retries = int(opts.get("retries", 2))

        plen = len(prompt)
        do_split = auto_split and chunk_size > 0 and plen > chunk_size

        self.last_high_level_meta = {
            "mode": "one_off",
            "model": model,
            "max_tokens_in": max_tokens,
            "auto_split": auto_split,
            "chunk_size": chunk_size,
            "prompt_length": plen,
            "timeouts": timeouts,
            "retries": retries,
            "api_url": self.api_url,
            "split_count": 0,
        }

        if not do_split:
            return self._call_once([{"role": "user", "content": prompt}], model, max_tokens, temperature, top_p, timeouts, retries)

        chunks = self._mb_split(prompt, chunk_size)
        self.last_high_level_meta["split_count"] = len(chunks)
        parts = []
        for ch in chunks:
            parts.append(self._call_once([{"role": "user", "content": ch}], model, max_tokens, temperature, top_p, timeouts, retries))
        return "\n".join(parts)

    def chat_session(self, sid: str, user_message: str, **opts) -> str:
        self._ensure_session(sid)
        model = opts.get("model", "gpt-5")
        temperature = float(opts.get("temperature", 0.7))
        top_p = float(opts.get("top_p", 0.9))
        max_tokens_raw = opts.get("max_tokens", opts.get("tokens", opts.get("t", 2048)))
        max_tokens = self.resolve_token_limit(max_tokens_raw, model) if isinstance(max_tokens_raw, str) else int(max_tokens_raw)
        timeouts = self._gpt_timeouts(model, False)
        if "timeout" in opts:
            timeouts["overall_timeout"] = int(opts["timeout"])
        retries = int(opts.get("retries", 2))
        trim_n = int(opts.get("trim_history", 0))

        if str(user_message).strip():
            self.sessions[sid].append({"role": "user", "content": user_message})

        if trim_n > 0 and len(self.sessions[sid]) > trim_n:
            base = self.sessions[sid]
            head = [base[0]] if base and base[0].get("role") == "system" else []
            tail = base[-trim_n:]
            self.sessions[sid] = head + tail if head else tail

        self.last_high_level_meta = {
            "mode": "session",
            "session_id": sid,
            "model": model,
            "max_tokens_in": max_tokens,
            "trim_history": trim_n,
            "messages_total": len(self.sessions[sid]),
            "timeouts": timeouts,
            "retries": retries,
            "api_url": self.api_url,
        }

        assistant = self._call_once(self.sessions[sid], model, max_tokens, temperature, top_p, timeouts, retries)
        if isinstance(assistant, str):
            self.sessions[sid].append({"role": "assistant", "content": assistant})
        return assistant

    def chat_session_rag(self, sid: str, user_message: str, **opts) -> str:
        self._ensure_session(sid)

        model = opts.get("model", "gpt-5")
        temperature = float(opts.get("temperature", 0.7))
        top_p = float(opts.get("top_p", 0.9))
        k = int(opts.get("k", 4))
        embed_model = str(opts.get("embed_model", "text-embedding-3-small"))

        max_tokens_raw = opts.get("max_tokens", opts.get("tokens", opts.get("t", 2048)))
        max_tokens = self.resolve_token_limit(max_tokens_raw, model) if isinstance(max_tokens_raw, str) else int(max_tokens_raw)
        timeouts = self._gpt_timeouts(model, False)
        if "timeout" in opts:
            timeouts["overall_timeout"] = int(opts["timeout"])
        retries = int(opts.get("retries", 2))
        trim_n = int(opts.get("trim_history", 0))

        self.sessions[sid].append({"role": "user", "content": user_message})

        if trim_n > 0 and len(self.sessions[sid]) > trim_n:
            base = self.sessions[sid]
            head = [base[0]] if base and base[0].get("role") == "system" else []
            tail = base[-trim_n:]
            self.sessions[sid] = head + tail if head else tail

        hits = []
        entries = self.session_vecs.get(sid, [])
        if entries:
            hits = self.session_embed_search(sid, user_message, k, model=embed_model)

        context = ""
        if hits:
            parts = [h["text"] for h in hits]
            context = "Use the following context. If it is insufficient, say you are unsure.\n---\n" + "\n---\n".join(parts) + "\n---"

        messages = list(self.sessions[sid])
        if context:
            if not messages:
                messages = [{"role": "system", "content": context}]
            else:
                messages[-1:-1] = [{"role": "system", "content": context}]  # insert before last user turn

        self.last_high_level_meta = {
            "mode": "session_rag",
            "session_id": sid,
            "model": model,
            "max_tokens_in": max_tokens,
            "trim_history": trim_n,
            "messages_total": len(self.sessions[sid]),
            "timeouts": timeouts,
            "retries": retries,
            "api_url": self.api_url,
            "k": k,
            "embed_model": embed_model,
            "retrieved": len(hits),
        }

        assistant = self._call_once(messages, model, max_tokens, temperature, top_p, timeouts, retries)
        if isinstance(assistant, str) and assistant:
            self.sessions[sid].append({"role": "assistant", "content": assistant})
        return str(assistant)

    # ---------------------------
    # Persistence (dict round-trip)
    # ---------------------------
    def dump_state(self) -> dict:
        return {
            "sessions": self.sessions,
            "session_vecs": self.session_vecs,
            "session_checkpoints": self.session_checkpoints,
            "session_parents": self.session_parents,
            "session_children": self.session_children,
            "session_labels": self.session_labels,
        }

    def load_state(self, state: dict) -> None:
        self.sessions = dict(state.get("sessions", {}))
        self.session_vecs = dict(state.get("session_vecs", {}))
        self.session_checkpoints = dict(state.get("session_checkpoints", {}))
        self.session_parents = dict(state.get("session_parents", {}))
        self.session_children = dict(state.get("session_children", {}))
        self.session_labels = dict(state.get("session_labels", {}))

    # ---------------------------
    # Introspection
    # ---------------------------
    def get_last_call_info(self) -> dict:
        return {"call": self.last_high_level_meta, "request": self.last_request_meta}


# ============================================================
# Shared singleton + wrapper functions (ONE IMPORT SURFACE)
# ============================================================

_default_client: GPTClient | None = None


def get_client() -> GPTClient:
    """Return the shared default GPTClient, creating it lazily."""
    global _default_client
    if _default_client is None:
        _default_client = GPTClient()
    return _default_client


# --- Basic chat ---
def chat(prompt: str, **opts) -> str:
    return get_client().chat(prompt, **opts)


# --- Sessions ---
def start_session(session_id: str | None = None, system: str | None = None) -> str:
    return get_client().start_session(session_id=session_id, system=system)


def close_session(sid: str) -> None:
    get_client().close_session(sid)


def reset_session(sid: str, system: str | None = None) -> None:
    get_client().reset_session(sid, system)


def add_message(sid: str, role: str, content: str) -> None:
    get_client().add_message(sid, role, content)


def get_session_messages(sid: str) -> list[dict]:
    return get_client().get_session_messages(sid)


def set_session_label(sid: str, label: str | None) -> None:
    get_client().set_session_label(sid, label)


def get_session_label(sid: str) -> str | None:
    return get_client().get_session_label(sid)


def get_session_parent(sid: str) -> str | None:
    return get_client().get_session_parent(sid)


def get_session_children(sid: str) -> list[str]:
    return get_client().get_session_children(sid)


def get_session_fork_graph() -> dict:
    return get_client().get_session_fork_graph()


# --- Session chat ---
def chat_session(sid: str, user_message: str, **opts) -> str:
    return get_client().chat_session(sid, user_message, **opts)


def chat_session_rag(sid: str, user_message: str, **opts) -> str:
    return get_client().chat_session_rag(sid, user_message, **opts)


# --- Embeddings (global + per-session) ---
def embed(input_texts, **opts) -> dict:
    return get_client().embed(input_texts, **opts)


def set_session_vectors(sid: str, entries: list[dict]) -> None:
    get_client().set_session_vectors(sid, entries)


def get_session_vectors(sid: str) -> list[dict]:
    return get_client().get_session_vectors(sid)


def session_embed_add(sid: str, texts, **opts) -> list[int]:
    return get_client().session_embed_add(sid, texts, **opts)


def session_embed_search(sid: str, query: str, k: int = 5, **opts) -> list[dict]:
    return get_client().session_embed_search(sid, query, k, **opts)


def session_embed_count(sid: str) -> int:
    return get_client().session_embed_count(sid)


def session_embed_clear(sid: str) -> None:
    get_client().session_embed_clear(sid)


# --- Layout (global) embeddings ---
def layout_embed_add(layout_id: str, texts, **opts) -> list[int]:
    return get_client().layout_embed_add(layout_id, texts, **opts)


def layout_embed_search(layout_id: str, query: str, k: int = 5, **opts) -> list[dict]:
    return get_client().layout_embed_search(layout_id, query, k, **opts)


# --- Checkpoints & forking ---
def create_checkpoint(sid: str, label: str, **opts) -> dict:
    return get_client().create_checkpoint(sid, label, **opts)


def get_checkpoints(sid: str) -> list[dict]:
    return get_client().get_checkpoints(sid)


def set_checkpoints(sid: str, cps: list[dict]) -> None:
    get_client().set_checkpoints(sid, cps)


def fork_session(parent_sid: str, checkpoint_id: str | None = None, **opts) -> str:
    return get_client().fork_session(parent_sid, checkpoint_id, **opts)


def set_session_relations(parent_id: str | None, children: list[str], sid: str) -> None:
    get_client().set_session_relations(parent_id, children, sid)


# --- Persistence ---
def dump_state() -> dict:
    return get_client().dump_state()


def load_state(state: dict) -> None:
    get_client().load_state(state)


# --- Introspection / config ---
def get_last_call_info() -> dict:
    return get_client().get_last_call_info()


def set_api_url(url: str) -> None:
    get_client().set_api_url(url)


def resolve_token_limit(mode_or_int: str | int, model: str | None = None) -> int:
    return GPTClient.resolve_token_limit(mode_or_int, model)


__all__ = [
    # core class + client access
    "GPTClient", "get_client",
    # chat
    "chat",
    # sessions
    "start_session", "close_session", "reset_session",
    "add_message", "get_session_messages",
    "set_session_label", "get_session_label",
    "get_session_parent", "get_session_children", "get_session_fork_graph",
    # session chat modes
    "chat_session", "chat_session_rag",
    # embeddings
    "embed", "set_session_vectors", "get_session_vectors",
    "session_embed_add", "session_embed_search",
    "session_embed_count", "session_embed_clear",
    # layout embeddings
    "layout_embed_add", "layout_embed_search",
    # checkpoints & forking
    "create_checkpoint", "get_checkpoints", "set_checkpoints",
    "fork_session", "set_session_relations",
    # persistence
    "dump_state", "load_state",
    # config / introspection
    "get_last_call_info", "set_api_url", "resolve_token_limit",
    # low-level helpers
    "load_openai_api_key", "cosine", "top_k",
]
