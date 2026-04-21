#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanitize a doskey macro file:
- Detect and fix unescaped special chars (^| ^> ^< ^&)
- Convert batch-style args %1..%9 or %~1 to $1..$9
- Flag suspicious constructs
- Categorize macros by intent
Outputs:
  - aliases.fixed.doskey
  - aliases.report.txt
"""

import re
from pathlib import Path

SRC = Path("aliases.tmp.bat")
OUT_FIXED = Path("aliases.bat")
OUT_REPORT = Path("aliases.report.txt")

# Categories (add/adjust as you like)
CATS = {
	"Python":        [r"\bpython(\d+)?\b", r"%py%", r"\.py\b", r"\bpyth?\b", r"\bpip(\.|3|2)?\b"],
	"Browser/Web":   [r"chrome\.exe", r"start .*https?://", r"\bopen-url\b", r"\burg(an)?\b"],
	"Search/Everything": [r"\bes\.exe\b", r"\bEverything\.exe\b", r"\bes\s"],
	"SSH/SCP/Remote": [r"\bssh\b", r"\bscp\.?exe\b", r"\bOpenSSH\\scp\.exe\b", r"\bsshpass\b"],
	"WezTerm/Tmux":  [r"\bwezterm\b", r"\bwezmux\b", r"\bta\b", r"\btn\b", r"\bwn\b"],
	"PHP":           [r"\bphp(\.|\.py)?\b", r"%php%", r"\.php\b"],
	"Java":          [r"\bjavac?(\.exe)?\b", r"\bjpackage(\.exe)?\b", r"jdk-"],
	"Media":         [r"\bvlc\.exe\b", r"\bffmpeg\b", r"\bmp3\b", r"\byoutube-dl\.exe\b", r"\bOpenRGB\.exe\b"],
	"Networking":    [r"\bnetstat\b", r"\bipconfig\b", r"\bOpenVPN\b", r"\bwhois\b", r"\barin\b"],
	"File Ops":      [r"\brsync\b", r"\btar\b", r"\bzip\b", r"\bcopy\b", r"\bmove\b", r"\brmdir\b", r"\bdel\b"],
	"Crypto/Secrets":[r"\bcryptstring\b", r"\bkeychain\b", r"\bcryptFile\b"],
	"Cloud/Sync":    [r"\bcloud\b", r"\bwebdav\b", r"\bvps\b", r"\bHarTool\b", r"\binline\b"],
	"System/Win":    [r"\bwmic\b", r"\btasklist\b", r"\btaskkill\b", r"\breg\b", r"\bdriverquery\b", r"\bcolor\b"],
	"Editors/Tools": [r"Notepad\+\+|notepad\.", r"\bcode_editor\b", r"\bSublime\b", r"\beditpad\b"],
	"DB/Index":      [r"\bdirdb\b", r"\bindex\.db\b", r"\bsqlite\b", r"\bmd5\b"],
}

name_re = re.compile(r'^\s*doskey\s+([^\s=]+)\s*=\s*(.+?)\s*$', re.IGNORECASE)
# lousy but serviceable quote-aware escaper:
SPEC = {'|': r'^|', '>': r'^>', '<': r'^<', '&': r'^&'}

def needs_escape(s: str) -> bool:
	# Check for special chars that are not escaped and not inside quotes
	# We'll do a lightweight scan toggling quote states.
	in_s = in_d = False
	i = 0
	while i < len(s):
		ch = s[i]
		if ch == "'" and not in_d: in_s = not in_s
		elif ch == '"' and not in_s: in_d = not in_d
		elif ch in SPEC and not in_s and not in_d:
			# if not escaped with caret
			if i == 0 or s[i-1] != '^':
				return True
		i += 1
	return False

def escape_specials(s: str) -> str:
	out = []
	in_s = in_d = False
	i = 0
	while i < len(s):
		ch = s[i]
		if ch == "'" and not in_d:
			in_s = not in_s
			out.append(ch)
		elif ch == '"' and not in_s:
			in_d = not in_d
			out.append(ch)
		elif ch in SPEC and not in_s and not in_d:
			# leave existing escapes alone
			if i > 0 and s[i-1] == '^':
				out.append(ch)
			else:
				out.append('^' + ch)
		else:
			out.append(ch)
		i += 1
	return ''.join(out)

def fix_args(s: str) -> (str, bool):
	"""Convert %1 or %~1..%~9 to $1..$9. Return (new, changed?)."""
	changed = False
	def repl(m):
		nonlocal changed
		changed = True
		return f"${m.group(2)}"
	new = re.sub(r'%(~)?([1-9])', repl, s)
	return new, changed

def categorize(cmd: str):
	hits = []
	for cat, pats in CATS.items():
		for p in pats:
			if re.search(p, cmd, re.IGNORECASE):
				hits.append(cat); break
	return hits or ["Misc"]

def main():
	src = SRC.read_text(encoding='utf-8', errors='ignore').splitlines()

	fixed_lines = []
	bad = []    # list of (name, reason)
	cat_map = {}  # name -> categories

	for raw in src:
		m = name_re.match(raw)
		if not m:
			# pass-through non-doskey lines (comments, blank, IF EXIST guards, etc.)
			fixed_lines.append(raw)
			continue

		name, body = m.group(1), m.group(2)

		# Track issues
		reasons = []

		# Fix batch-style args %1 → $1
		new_body, changed_args = fix_args(body)
		if changed_args:
			reasons.append("converted %1..%9 to $1..$9")
		body = new_body

		# Escape unescaped specials outside quotes
		if needs_escape(body):
			body = escape_specials(body)
			reasons.append("escaped special chars ^| ^> ^< ^&")

		# Some guardrails: double spaces collapse
		body = re.sub(r'\s+', ' ', body).strip()

		# Save fixed macro
		fixed_line = f"doskey {name}={body}"
		fixed_lines.append(fixed_line)

		# Categorize
		cat_map[name] = categorize(body)

		# If we changed anything, mark as “would not work as-is”
		if reasons:
			bad.append((name, "; ".join(reasons)))

	# Write outputs
	# OUT_FIXED.write_text("\n".join(fixed_lines) + "\n", encoding='utf-8')

	# Reorder by category and add REM headers
	cat_inv = {}
	for n, cats in cat_map.items():
		for c in cats:
			cat_inv.setdefault(c, []).append(n)

	ordered = []
	for c in sorted(cat_inv):
		ordered.append(f"\n\n\n:: === {c} ===")
		for n in sorted(cat_inv[c]):
			# find the fixed line for this macro
			for fl in fixed_lines:
				if fl.lower().startswith(f"doskey {n.lower()}="):
					ordered.append(fl)
					break
	ordered.append("")  # final newline
	OUT_FIXED.write_text("\n".join(ordered), encoding="utf-8")




	with OUT_REPORT.open("w", encoding="utf-8") as r:
		r.write("WILL NOT WORK AS-IS (fixed in aliases.fixed.doskey):\n")
		if not bad:
			r.write("- none -\n")
		else:
			for n, why in bad:
				r.write(f"{n} = {why}\n")

		r.write("\nCATEGORIES:\n")
		# invert categories -> names
		cat_inv = {}
		for n, cats in cat_map.items():
			for c in cats:
				cat_inv.setdefault(c, []).append(n)
		for c in sorted(cat_inv):
			r.write(f"\n[{c}]\n")
			r.write(", ".join(sorted(cat_inv[c])) + "\n")

if __name__ == "__main__":
	main()