import mygpt

# One-off
print(mygpt.chat("Hello", model="gpt-5"))

# Session + RAG + forking
sid = mygpt.start_session(system="You are a coding assistant.")
mygpt.session_embed_add(sid, ["doc A", "doc B"], meta={"kind": "notes"})
print(mygpt.chat_session_rag(sid, "Use my notes to answer this question."))

cp = mygpt.create_checkpoint(sid, "branch point")
child = mygpt.fork_session(sid, checkpoint_id=cp["id"], label="experiment A")
print("Forked:", child, "from", sid)
