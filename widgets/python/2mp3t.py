#!/usr/bin/env python3
import argparse
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor

# ---------------- Config ----------------
# Desired number of threads (will be capped by MAX_THREADS)
THREADS = 12
MAX_THREADS = 20

VIDEO_EXTENSIONS = {
	".mp4", ".mkv", ".avi", ".mov", ".m4v", ".wmv",
	".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".ts"
}


def is_video_file(path: str) -> bool:
	ext = os.path.splitext(path)[1].lower()
	return ext in VIDEO_EXTENSIONS


def convert_to_mp3(video_path: str, bitrate: str = "192k") -> None:
	if not os.path.isfile(video_path):
		print(f"[ERROR] Not a file: {video_path}")
		return

	if not is_video_file(video_path):
		print(f"[SKIP ] Not a video: {video_path}")
		return

	dir_name, file_name = os.path.split(video_path)
	base, _ = os.path.splitext(file_name)
	out_path = os.path.join(dir_name, f"{base}.mp3")

	if os.path.exists(out_path):
		print(f"[SKIP ] MP3 exists: {out_path}")
		return

	print(f"[RUN  ] {video_path} -> {out_path}")

	cmd = [
		"ffmpeg",
		"-hide_banner",
		"-loglevel", "error",
		"-i", video_path,
		"-vn",
		"-acodec", "libmp3lame",
		"-b:a", bitrate,
		out_path,
	]

	try:
		result = subprocess.run(cmd, check=False)
		if result.returncode == 0:
			print(f"[OK   ] Created: {out_path}")
		else:
			print(f"[FAIL ] ffmpeg exited with {result.returncode} for {video_path}")
			# If bad partial file was created, you can choose to delete it:
			# if os.path.exists(out_path):
			#     os.remove(out_path)
	except FileNotFoundError:
		print("[FATAL] ffmpeg not found in PATH.")
		sys.exit(1)
	except Exception as e:
		print(f"[ERROR] Exception for {video_path}: {e}")


def walk_and_convert(root: str, bitrate: str, dry_run: bool = False) -> None:
	root = os.path.abspath(root)
	print(f"[INFO ] Scanning recursively from: {root}")

	video_files = []

	for dirpath, dirnames, filenames in os.walk(root):
		for name in filenames:
			full_path = os.path.join(dirpath, name)
			if is_video_file(full_path):
				if dry_run:
					print(f"[DRY  ] Would convert: {full_path}")
				else:
					video_files.append(full_path)

	if dry_run:
		return

	if not video_files:
		print("[INFO ] No video files found.")
		return

	# Determine actual thread count
	threads = min(max(1, THREADS), MAX_THREADS)
	print(f"[INFO ] Converting {len(video_files)} files using {threads} threads (max {MAX_THREADS}).")

	with ThreadPoolExecutor(max_workers=threads) as executor:
		for path in video_files:
			executor.submit(convert_to_mp3, path, bitrate)


def main():
	parser = argparse.ArgumentParser(
		description="Recursively convert video files to MP3 using ffmpeg (threaded)."
	)
	parser.add_argument(
		"path",
		nargs="?",
		default=".",
		help="Root folder to scan recursively (default: current directory) or a single file",
	)
	parser.add_argument(
		"--dry-run",
		action="store_true",
		help="Only show what would be converted, don't run ffmpeg.",
	)
	parser.add_argument(
		"--bitrate",
		"-b",
		default="192k",
		help="Audio bitrate for MP3 (default: 192k)",
	)

	args = parser.parse_args()

	# Quick ffmpeg check
	try:
		subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL,
					stderr=subprocess.DEVNULL, check=False)
	except FileNotFoundError:
		print("[FATAL] ffmpeg not found in PATH.")
		sys.exit(1)

	if os.path.isfile(args.path):
		# Single file mode
		if args.dry_run:
			print(f"[DRY  ] Would convert single file: {args.path}")
		else:
			convert_to_mp3(args.path, bitrate=args.bitrate)
	else:
		# Directory mode (threaded)
		walk_and_convert(args.path, bitrate=args.bitrate, dry_run=args.dry_run)


if __name__ == "__main__":
	main()