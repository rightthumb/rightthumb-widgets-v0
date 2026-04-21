# test_gpt_client.py
import os
import json
import tempfile
import shutil
import types
import pytest

from gpt_client import GPTClient, load_openai_api_key, _l2_normalize, cosine, top_k


# ---------------------------
# Key loader tests (no network)
# ---------------------------
def test_key_loader_prefers_openai_key_file(tmp_path, monkeypatch):
	rt = tmp_path / ".rt"
	rt.mkdir()
	(rt / "openai.key").write_text("sk-TEST-KEY\n", encoding="utf-8")
	monkeypatch.setenv("HOME", str(tmp_path))

	key = load_openai_api_key()
	assert key == "sk-TEST-KEY"


def test_key_loader_falls_back_to_config_hash(tmp_path='~', monkeypatch=None):
	rt = tmp_path / ".rt"
	rt.mkdir()
	(rt / ".config.hash").write_text(json.dumps({"openai": "sk-FROM-CONFIG"}), encoding="utf-8")
	monkeypatch.setenv("HOME", str(tmp_path))

	key = load_openai_api_key()
	assert key == "sk-FROM-CONFIG"


def test_key_loader_raises_when_missing(tmp_path, monkeypatch):
	monkeypatch.setenv("HOME", str(tmp_path))
	with pytest.raises(ValueError) as ei:
		load_openai_api_key()
	assert "File ~/.rt/openai.key not found." in str(ei.value)


# ---------------------------
# Math helpers
# ---------------------------
def test_norm_and_cosine_topk():
	v1 = _l2_normalize([1.0, 0.0, 0.0])
	v2 = _l2_normalize([0.5, 0.5, 0.0])
	v3 = _l2_normalize([0.0, 1.0, 0.0])
	assert pytest.approx(cosine(v1, v1), 1e-6) == 1.0
	assert 0 < cosine(v1, v2) < 1.0
	hits = top_k([v1, v2, v3], v1, 2)
	assert hits[0]["index"] == 0


# ---------------------------
# Client tests without network (mock internals)
# ---------------------------
def make_client_with_mock_key(tmp_path, monkeypatch):
	rt = tmp_path / ".rt"
	rt.mkdir()
	(rt / "openai.key").write_text("sk-TEST-KEY\n", encoding="utf-8")
	monkeypatch.setenv("HOME", str(tmp_path))
	return GPTClient()  # will load mocked key


def test_embed_and_search_session_without_network(tmp_path, monkeypatch):
	gpt = make_client_with_mock_key(tmp_path, monkeypatch)

	# Monkeypatch embed() to deterministic vectors (unit basis)
	def fake_embed(input_texts, **opts):
		items = [input_texts] if isinstance(input_texts, str) else list(input_texts)
		vecs = []
		for i, _ in enumerate(items):
			base = [0.0, 0.0, 0.0]
			base[i % 3] = 1.0
			vecs.append(base)
		return {"model": "mock", "vectors": vecs, "dims": 3}

	gpt.embed = fake_embed  # type: ignore

	sid = gpt.start_session(system="You are concise.")
	idxs = gpt.session_embed_add(sid, ["alpha", "bravo", "charlie"], meta={"tag": "seed"})
	assert len(idxs) == 3
	hits = gpt.session_embed_search(sid, "alpha", 2)
	assert len(hits) == 2
	# fake_embed makes query vector = [1,0,0], so top doc should be index 0 ('alpha')
	assert hits[0]["text"] in ("alpha", "bravo", "charlie")


def test_checkpoint_and_fork_dedupe(tmp_path, monkeypatch):
	gpt = make_client_with_mock_key(tmp_path, monkeypatch)

	# Stub _call_once for checkpoint summarization
	gpt._call_once = lambda *a, **k: "CP: summary"  # type: ignore

	parent = gpt.start_session(system="SYS")
	gpt.add_message(parent, "user", "A")
	gpt.add_message(parent, "assistant", "a")
	cp = gpt.create_checkpoint(parent, "CP1")  # will call stub
	child = gpt.fork_session(parent, cp["id"], keep_last=2, inherit_vectors=True, label="Exploration")

	# Verify system dedupe (only seed + label at most expected)
	child_msgs = gpt.get_session_messages(child)
	sys_front = []
	for m in child_msgs:
		if m.get("role") != "system":
			break
		sys_front.append(m["content"])
	# Should have at most 2: seed summary and branch label
	assert len(sys_front) <= 2
	assert any("Forked from" in s or "Branch label" in s for s in sys_front)


def test_persistence_roundtrip(tmp_path, monkeypatch):
	gpt = make_client_with_mock_key(tmp_path, monkeypatch)
	sid = gpt.start_session(system="SYS")
	gpt.add_message(sid, "user", "hello")
	gpt.session_embed_add(sid, "doc", meta={"x": 1})

	state = gpt.dump_state()
	gpt2 = make_client_with_mock_key(tmp_path, monkeypatch)
	gpt2.load_state(state)

	assert gpt2.get_session_messages(sid)[0]["content"] == "SYS"
	assert gpt2.session_embed_count(sid) == 1


# ---------------------------
# Optional integration tests (run only if you actually have a key configured)
# They will still pass if the SDK isn't installed; they’ll be skipped.
# ---------------------------
@pytest.mark.skipif(
	not (os.path.exists(os.path.expanduser("~/.rt/openai.key"))
		or os.path.exists(os.path.expanduser("~/.rt/.config.hash"))),
	reason="No ~/.rt key configured",
)
def test_integration_one_off_smoke():
	gpt = GPTClient()
	out = gpt.chat("Reply with exactly 'OK'.", model="gpt-4o-mini", max_tokens=8, temperature=0.0, retries=0)
	assert isinstance(out, str)
	assert len(out.strip()) > 0

# run_all_tests.py
import inspect
import sys
import traceback

def run_tests(module_name="test_gpt_client"):
	"""
	Import a test module, find all test_* functions, and run them.
	Prints results summary.
	"""
	try:
		mod = __import__(module_name)
	except ImportError as e:
		print(f"Could not import {module_name}: {e}")
		return

	funcs = [
		fn for name, fn in inspect.getmembers(mod, inspect.isfunction)
		if name.startswith("test_")
	]

	passed, failed = 0, 0
	for fn in funcs:
		try:
			fn()  # run with no args
			print(f"[PASS] {fn.__name__}")
			passed += 1
		except Exception:
			print(f"[FAIL] {fn.__name__}")
			traceback.print_exc(limit=3)
			failed += 1

	print("\n=== SUMMARY ===")
	print(f"Total: {len(funcs)}, Passed: {passed}, Failed: {failed}")


if __name__ == "__main__":
	# default to test_gpt_client but allow python run_all_tests.py other_module
	mod = sys.argv[1] if len(sys.argv) > 1 else "test_gpt_client"
	run_tests(mod)