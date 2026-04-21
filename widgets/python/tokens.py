#!/usr/bin/env python3

# 694a4aba-0694-8330-833b-ba97a378d69a

import sys
import os
import math
import argparse
import tiktoken


# These are practical chunk sizes people tend to have success with in web chat.
# Not guarantees—just good operational defaults.
SPLIT_TARGETS = [6000, 8000, 10000, 12000, 16000]


def human(n):
    # Simple human formatter without extra deps
    for unit in ["", "K", "M", "B"]:
        if abs(n) < 1000:
            return f"{n}{unit}"
        n = n / 1000
    return f"{n:.2f}T"


def load_input(path=None):
    # If path provided, read file. Else read stdin.
    if path:
        with open(path, "rb") as f:
            b = f.read()
        # best-effort decode (avoid crashing on odd encodings)
        try:
            s = b.decode("utf-8")
        except UnicodeDecodeError:
            s = b.decode("utf-8", errors="replace")
        return s, b
    else:
        # stdin text (pipe)
        if sys.stdin.isatty():
            return "", b""
        s = sys.stdin.read()
        try:
            b = s.encode("utf-8")
        except Exception:
            b = bytes(s, "utf-8", errors="replace")
        return s, b


def try_enc(name):
    try:
        return tiktoken.get_encoding(name)
    except Exception:
        return None


def count_tokens(text, enc):
    # encode_ordinary is slightly faster and avoids special-token weirdness
    try:
        return len(enc.encode_ordinary(text))
    except Exception:
        return len(enc.encode(text))


def paste_risk_band(tokens, encoding_hint=""):
    # IMPORTANT: This is guidance, not law.
    # Web UI paste limits vary; we label as probability bands.
    if tokens <= 8000:
        return "Web paste: usually OK (still depends on chat length/formatting)"
    if tokens <= 12000:
        return "Web paste: hit-or-miss (often works in fresh chat, fails in long threads)"
    if tokens <= 18000:
        return "Web paste: often fails unless chat is short and text is simple"
    return "Web paste: likely fails as a single message; plan to split/upload"


def split_plan(tokens):
    lines = []
    for target in SPLIT_TARGETS:
        splits = math.ceil(tokens / target)
        lines.append((target, splits))
    return lines


def main():
    p = argparse.ArgumentParser(
        description="Count GPT-ish tokens from stdin (pipe) or a file, and print practical paste/splitting guidance."
    )
    p.add_argument("path", nargs="?", help="Optional input file path. If omitted, reads from stdin.")
    args = p.parse_args()

    text, raw_bytes = load_input(args.path)

    if not text.strip():
        print("No input (empty).")
        print("Tokens: 0")
        return

    # Try both common encodings; many modern model families align better with o200k_base,
    # but cl100k_base is still widely used.
    enc_o200k = try_enc("o200k_base")
    enc_cl100k = try_enc("cl100k_base")

    results = []
    if enc_o200k is not None:
        results.append(("o200k_base", count_tokens(text, enc_o200k)))
    if enc_cl100k is not None:
        results.append(("cl100k_base", count_tokens(text, enc_cl100k)))

    if not results:
        print("tiktoken encodings unavailable. Is tiktoken installed correctly?")
        print("Try: pip install -U tiktoken")
        return

    chars = len(text)
    bytes_len = len(raw_bytes)
    lines = text.count("\n") + 1

    print("=== INPUT SIZE ===")
    if args.path:
        print(f"Source: file: {args.path}")
    else:
        print("Source: stdin (pipe)")
    print(f"Chars: {chars}   Lines: {lines}   UTF-8 bytes: {bytes_len}")

    print("\n=== TOKEN COUNTS (multiple encodings) ===")
    for name, n in results:
        print(f"{name}: {n} tokens")

    # Choose a “primary” token count for guidance:
    # prefer o200k_base if present, else cl100k_base
    primary_name, primary_tokens = results[0]

    # If both exist, also show variance
    if len(results) == 2:
        a_name, a = results[0]
        b_name, b = results[1]
        diff = a - b
        pct = (diff / b) * 100 if b else 0
        print("\n=== ENCODING VARIANCE ===")
        sign = "+" if diff >= 0 else ""
        print(f"{a_name} vs {b_name}: {sign}{diff} tokens ({sign}{pct:.2f}%)")

    print("\n=== PRACTICAL WEB-CHAT GUIDANCE (NOT A GUARANTEE) ===")
    print(f"Using {primary_name} as primary estimate: {primary_tokens} tokens")
    print(paste_risk_band(primary_tokens, primary_name))

    print("\n=== SPLIT SUGGESTIONS (by token chunks) ===")
    for target, splits in split_plan(primary_tokens):
        if splits <= 1:
            note = "no split"
        else:
            note = f"{splits} parts"
        print(f"~{target} tokens/part -> {note}")

    print("\n=== NOTES / WHY YOUR EARLIER RESULT FELT WRONG ===")
    print("- Token count is NOT the same as paste size; the web UI can block by chars/bytes or UI heuristics.")
    print("- Your chat history consumes context; what fits in a fresh chat may fail in a long thread.")
    print("- Different tokenizers (cl100k_base vs o200k_base) can shift counts enough to flip a verdict.")
    print("- Formatting (especially lots of code blocks, markdown, or weird Unicode) can change behavior.")

    print("\nTip: If you need reliability, file upload beats paste 100% of the time.")

if __name__ == "__main__":
    main()
