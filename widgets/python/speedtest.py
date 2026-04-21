from __future__ import annotations

#!/usr/bin/env python3
"""
speed_blaster.py
- Download test: https://sds.sh/speed/50MB.bin
- Upload test:   https://sds.sh/speed/upload.php

Examples:
  python speed_blaster.py
  python speed_blaster.py --upload-mb 200
  python speed_blaster.py --no-upload
  python speed_blaster.py --field upload --upload-mb 50
  python speed_blaster.py --json

Optional (makes visuals extra spicy):
  pip install rich
"""


import argparse
import json
import os
import sys
import time
import math
import secrets
from dataclasses import dataclass
from typing import List, Optional, Tuple

# ---- Optional "Rich" visuals ----
HAVE_RICH = False
try:
	from rich.console import Console
	from rich.live import Live
	from rich.panel import Panel
	from rich.progress import Progress, BarColumn, TextColumn, TimeElapsedColumn, TimeRemainingColumn
	from rich.table import Table
	from rich.text import Text
	HAVE_RICH = True
except Exception:
	HAVE_RICH = False

# ---- HTTP client (requests preferred) ----
HAVE_REQUESTS = False
try:
	import requests
	HAVE_REQUESTS = True
except Exception:
	HAVE_REQUESTS = False

# ------------------ Helpers ------------------

def now() -> float:
	return time.perf_counter()

def bytes_to_bits_per_sec(bps_bytes: float) -> float:
	return bps_bytes * 8.0

def fmt_mbps(mbps: float) -> str:
	return f"{mbps:,.2f} Mbps"

def fmt_mb(nbytes: int) -> str:
	return f"{nbytes / (1024*1024):,.2f} MB"

def clamp(v: float, lo: float, hi: float) -> float:
	return max(lo, min(hi, v))

def sparkline(values: List[float], width: int = 36) -> str:
	"""Unicode sparkline from a list of values."""
	if not values:
		return ""
	# resample to width
	if len(values) > width:
		step = len(values) / width
		sampled = []
		for i in range(width):
			a = int(i * step)
			b = int((i + 1) * step)
			b = max(b, a + 1)
			sampled.append(sum(values[a:b]) / (b - a))
		values = sampled

	blocks = "▁▂▃▄▅▆▇█"
	vmin = min(values)
	vmax = max(values)
	if math.isclose(vmin, vmax):
		return blocks[0] * len(values)

	out = []
	for v in values:
		t = (v - vmin) / (vmax - vmin)
		idx = int(round(t * (len(blocks) - 1)))
		idx = int(clamp(idx, 0, len(blocks) - 1))
		out.append(blocks[idx])
	return "".join(out)

def percentile(values: List[float], p: float) -> float:
	if not values:
		return 0.0
	s = sorted(values)
	k = (len(s) - 1) * p
	f = math.floor(k)
	c = math.ceil(k)
	if f == c:
		return s[int(k)]
	return s[f] + (s[c] - s[f]) * (k - f)

# ------------------ Results ------------------

@dataclass
class SpeedResult:
	kind: str                  # "download" or "upload"
	url: str
	bytes_total: int
	seconds: float
	avg_mbps: float
	per_sec_mbps: List[float]
	status_code: Optional[int] = None
	note: str = ""

	def to_dict(self) -> dict:
		return {
			"kind": self.kind,
			"url": self.url,
			"bytes_total": self.bytes_total,
			"seconds": self.seconds,
			"avg_mbps": self.avg_mbps,
			"per_sec_mbps": self.per_sec_mbps,
			"status_code": self.status_code,
			"note": self.note,
		}

# ------------------ Core tests ------------------

def download_test_requests(url: str, timeout: int, chunk_kb: int, max_mb: Optional[int]) -> SpeedResult:
	chunk = chunk_kb * 1024
	per_sec = []
	bytes_total = 0

	t0 = now()
	last_tick = t0
	sec_bytes = 0

	r = requests.get(url, stream=True, timeout=timeout)
	status = r.status_code

	limit_bytes = None if max_mb is None else max_mb * 1024 * 1024

	for part in r.iter_content(chunk_size=chunk):
		if not part:
			continue
		n = len(part)
		bytes_total += n
		sec_bytes += n

		t = now()
		if t - last_tick >= 1.0:
			bps = sec_bytes / (t - last_tick)
			mbps = bytes_to_bits_per_sec(bps) / 1_000_000.0
			per_sec.append(mbps)
			last_tick = t
			sec_bytes = 0

		if limit_bytes is not None and bytes_total >= limit_bytes:
			break

	t1 = now()
	seconds = max(1e-6, t1 - t0)
	avg_mbps = bytes_to_bits_per_sec(bytes_total / seconds) / 1_000_000.0

	return SpeedResult(
		kind="download",
		url=url,
		bytes_total=bytes_total,
		seconds=seconds,
		avg_mbps=avg_mbps,
		per_sec_mbps=per_sec,
		status_code=status,
	)

def upload_test_requests(
	url: str,
	timeout: int,
	chunk_kb: int,
	upload_mb: int,
	field: str,
	mode: str,
) -> SpeedResult:
	"""
	mode:
	- "multipart": sends as multipart/form-data with files={field: (...)}
	- "raw": sends application/octet-stream body
	- "auto": tries multipart first then raw if server rejects or errors
	"""
	chunk = chunk_kb * 1024
	target_bytes = upload_mb * 1024 * 1024

	# Generate payload (random) — avoid compressibility skew.
	# Build in chunks so memory isn’t insane for huge tests.
	def gen_bytes(total: int):
		remaining = total
		while remaining > 0:
			n = min(chunk, remaining)
			yield secrets.token_bytes(n)
			remaining -= n

	def do_multipart() -> Tuple[Optional[requests.Response], Optional[Exception], int]:
		# For multipart, requests wants a file-like. We'll spool to a temp file for stability.
		# (Streaming multipart with unknown server behavior is more fragile.)
		import tempfile
		sent = 0
		try:
			with tempfile.NamedTemporaryFile(prefix="speed_", suffix=".bin", delete=True) as f:
				remaining = target_bytes
				while remaining > 0:
					n = min(1024 * 1024, remaining)  # write 1MB blocks
					f.write(secrets.token_bytes(n))
					sent += n
					remaining -= n
				f.flush()
				f.seek(0)

				files = {field: ("speed_test.bin", f, "application/octet-stream")}
				resp = requests.post(url, files=files, timeout=timeout)
				return resp, None, sent
		except Exception as e:
			return None, e, sent

	def do_raw() -> Tuple[Optional[requests.Response], Optional[Exception], int, List[float]]:
		per_sec = []
		bytes_total = 0
		t0 = now()
		last_tick = t0
		sec_bytes = 0

		class RawStream:
			def __iter__(self):
				nonlocal bytes_total, sec_bytes, last_tick, per_sec
				for block in gen_bytes(target_bytes):
					n = len(block)
					bytes_total += n
					sec_bytes += n
					t = now()
					if t - last_tick >= 1.0:
						bps = sec_bytes / (t - last_tick)
						mbps = bytes_to_bits_per_sec(bps) / 1_000_000.0
						per_sec.append(mbps)
						last_tick = t
						sec_bytes = 0
					yield block

		headers = {"Content-Type": "application/octet-stream"}
		try:
			resp = requests.post(url, data=RawStream(), headers=headers, timeout=timeout)
			return resp, None, bytes_total, per_sec
		except Exception as e:
			return None, e, bytes_total, per_sec

	# Execute
	note = ""
	status = None
	per_sec = []

	t0 = now()

	if mode in ("multipart", "auto"):
		resp, err, sent = do_multipart()
		if resp is not None:
			status = resp.status_code
			note = f"multipart field='{field}'"
			t1 = now()
			seconds = max(1e-6, t1 - t0)
			avg_mbps = bytes_to_bits_per_sec(sent / seconds) / 1_000_000.0
			return SpeedResult("upload", url, sent, seconds, avg_mbps, per_sec_mbps=[], status_code=status, note=note)

		if mode == "multipart":
			raise RuntimeError(f"Upload multipart failed: {err}")

		note = f"multipart failed ({err}); falling back to raw"

	# raw
	resp, err, bytes_total, per_sec = do_raw()
	if resp is None:
		raise RuntimeError(f"Upload raw failed: {err}")

	status = resp.status_code
	t1 = now()
	seconds = max(1e-6, t1 - t0)
	avg_mbps = bytes_to_bits_per_sec(bytes_total / seconds) / 1_000_000.0
	return SpeedResult("upload", url, bytes_total, seconds, avg_mbps, per_sec_mbps=per_sec, status_code=status, note=note or "raw")

# ------------------ Terminal UI (no deps) ------------------

def bar(p: float, width: int = 28) -> str:
	p = clamp(p, 0.0, 1.0)
	fill = int(round(p * width))
	return "█" * fill + "░" * (width - fill)

def print_summary_plain(results: List[SpeedResult]):
	print("\n=== SUMMARY ===")
	for r in results:
		p50 = percentile(r.per_sec_mbps, 0.50) if r.per_sec_mbps else 0.0
		p90 = percentile(r.per_sec_mbps, 0.90) if r.per_sec_mbps else 0.0
		print(f"\n[{r.kind.upper()}] {r.url}")
		if r.status_code is not None:
			print(f"  HTTP: {r.status_code}  ({r.note})")
		else:
			print(f"  NOTE: {r.note}")
		print(f"  Data: {fmt_mb(r.bytes_total)} in {r.seconds:,.2f}s")
		print(f"  Avg : {fmt_mbps(r.avg_mbps)}")
		if r.per_sec_mbps:
			print(f"  p50 : {fmt_mbps(p50)}   p90: {fmt_mbps(p90)}")
			print(f"  Graph: {sparkline(r.per_sec_mbps, width=48)}")

# ------------------ Rich UI ------------------

def print_summary_rich(console: "Console", results: List[SpeedResult]):
	table = Table(title="Speed Blaster Summary", show_lines=True)
	table.add_column("Type", style="bold")
	table.add_column("HTTP")
	table.add_column("Data")
	table.add_column("Time")
	table.add_column("Avg")
	table.add_column("p50 / p90")
	table.add_column("Graph")

	for r in results:
		p50 = percentile(r.per_sec_mbps, 0.50) if r.per_sec_mbps else 0.0
		p90 = percentile(r.per_sec_mbps, 0.90) if r.per_sec_mbps else 0.0
		http = f"{r.status_code}" if r.status_code is not None else "-"
		data = fmt_mb(r.bytes_total)
		t = f"{r.seconds:,.2f}s"
		avg = fmt_mbps(r.avg_mbps)
		pp = "-" if not r.per_sec_mbps else f"{fmt_mbps(p50)} / {fmt_mbps(p90)}"
		g = sparkline(r.per_sec_mbps, width=28) if r.per_sec_mbps else "-"
		table.add_row(r.kind.upper(), http, data, t, avg, pp, g)

	console.print(table)

# ------------------ Main ------------------

def parse_args():
	p = argparse.ArgumentParser(description="Test webserver speed (download + upload) with terminal visuals.")
	p.add_argument("--download-url", default="https://sds.sh/speed/50MB.bin")
	p.add_argument("--upload-url", default="https://sds.sh/speed/upload.php")
	p.add_argument("--upload-mb", type=int, default=100, help="Upload payload size in MB (default: 100)")
	p.add_argument("--max-download-mb", type=int, default=None, help="Stop download after N MB (default: full file)")
	p.add_argument("--timeout", type=int, default=60)
	p.add_argument("--chunk-kb", type=int, default=1024, help="Stream chunk size in KB (default: 1024=1MB)")

	p.add_argument("--no-download", action="store_true")
	p.add_argument("--no-upload", action="store_true")

	p.add_argument("--mode", choices=["auto", "multipart", "raw"], default="auto",
				help="Upload mode: auto tries multipart then raw (default: auto)")
	p.add_argument("--field", default="file", help="Multipart field name for upload.php (default: file)")

	p.add_argument("--json", action="store_true", help="Print results as JSON (in addition to visuals)")
	return p.parse_args()

def main():
	args = parse_args()

	if not HAVE_REQUESTS:
		print("ERROR: This script expects 'requests'. Install with:\n  pip install requests")
		sys.exit(2)

	results: List[SpeedResult] = []

	# ----- DOWNLOAD -----
	if not args.no_download:
		if HAVE_RICH:
			console = Console()
			console.print(Panel.fit("🧨  SPEED BLASTER  🧨\nDownload + Upload server throughput test", title="READY", subtitle="terminal war crimes (but legal)"))
			with console.status("Downloading...") as status:
				r = download_test_requests(args.download_url, args.timeout, args.chunk_kb, args.max_download_mb)
			results.append(r)
			console.print(Panel.fit(
				f"[bold]DOWNLOAD DONE[/bold]\n"
				f"HTTP: {r.status_code}\n"
				f"Data: {fmt_mb(r.bytes_total)}\n"
				f"Time: {r.seconds:,.2f}s\n"
				f"Avg : {fmt_mbps(r.avg_mbps)}\n"
				f"Graph: {sparkline(r.per_sec_mbps, width=48) if r.per_sec_mbps else '(short run)'}",
				title="DOWNLOAD",
			))
		else:
			print("=== SPEED BLASTER ===")
			print(f"Downloading: {args.download_url}")
			r = download_test_requests(args.download_url, args.timeout, args.chunk_kb, args.max_download_mb)
			results.append(r)
			print(f"Done. HTTP {r.status_code} | {fmt_mb(r.bytes_total)} in {r.seconds:,.2f}s | Avg {fmt_mbps(r.avg_mbps)}")
			if r.per_sec_mbps:
				print(f"Graph: {sparkline(r.per_sec_mbps, width=48)}")

	# ----- UPLOAD -----
	if not args.no_upload:
		if HAVE_RICH:
			console = Console()
			console.print(Panel.fit(
				f"Uploading to:\n{args.upload_url}\n\n"
				f"Size: {args.upload_mb} MB\n"
				f"Mode: {args.mode}\n"
				f"Field: {args.field} (multipart)",
				title="UPLOAD SETUP",
			))
			with console.status("Uploading...") as status:
				r = upload_test_requests(args.upload_url, args.timeout, args.chunk_kb, args.upload_mb, args.field, args.mode)
			results.append(r)
			console.print(Panel.fit(
				f"[bold]UPLOAD DONE[/bold]\n"
				f"HTTP: {r.status_code}\n"
				f"Note: {r.note}\n"
				f"Data: {fmt_mb(r.bytes_total)}\n"
				f"Time: {r.seconds:,.2f}s\n"
				f"Avg : {fmt_mbps(r.avg_mbps)}\n"
				f"Graph: {sparkline(r.per_sec_mbps, width=48) if r.per_sec_mbps else '(server-side measured / non-streamed multipart)'}",
				title="UPLOAD",
			))
		else:
			print(f"\nUploading: {args.upload_url} ({args.upload_mb} MB, mode={args.mode}, field={args.field})")
			r = upload_test_requests(args.upload_url, args.timeout, args.chunk_kb, args.upload_mb, args.field, args.mode)
			results.append(r)
			print(f"Done. HTTP {r.status_code} | {fmt_mb(r.bytes_total)} in {r.seconds:,.2f}s | Avg {fmt_mbps(r.avg_mbps)}")
			if r.per_sec_mbps:
				print(f"Graph: {sparkline(r.per_sec_mbps, width=48)}")
			if r.note:
				print(f"Note: {r.note}")

	# ----- SUMMARY -----
	if HAVE_RICH:
		console = Console()
		print_summary_rich(console, results)
	else:
		print_summary_plain(results)

	if args.json:
		payload = {"results": [r.to_dict() for r in results]}
		print("\n=== JSON ===")
		print(json.dumps(payload, indent=2))

if __name__ == "__main__":
	main()