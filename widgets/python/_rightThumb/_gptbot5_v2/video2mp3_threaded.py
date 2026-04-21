#!/usr/bin/env python3
import argparse
import os
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Set

VIDEO_EXTENSIONS: Set[str] = {
    ".mp4", ".mkv", ".avi", ".mov", ".m4v", ".wmv",
    ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".ts"
}

def is_video_file(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS

def convert_to_mp3(video_path: Path, bitrate: str = "192k") -> str:
    if not video_path.is_file():
        return f"[ERROR] Not a file: {video_path}"

    if not is_video_file(video_path):
        return f"[SKIP ] Not a video: {video_path}"

    out_path = video_path.with_suffix(".mp3")

    if out_path.exists():
        return f"[SKIP ] MP3 already exists: {out_path}"

    cmd = [
        "ffmpeg",
        "-y",
        "-i", str(video_path),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", bitrate,
        str(out_path),
    ]

    try:
        proc = subprocess.run(cmd, capture_output=True, text=True)
    except Exception as e:
        return f"[ERROR] Exception running ffmpeg on {video_path}: {e}"

    if proc.returncode != 0:
        return f"[FAIL ] ffmpeg failed on {video_path}:\n{proc.stderr}"

    return f"[OK   ] {video_path} -> {out_path}"

def iter_videos(root: Path, recursive: bool) -> Set[Path]:
    videos: Set[Path] = set()
    if recursive:
        for p in root.rglob("*"):
            if p.is_file() and is_video_file(p):
                videos.add(p)
    else:
        for p in root.iterdir():
            if p.is_file() and is_video_file(p):
                videos.add(p)
    return videos

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Threaded video->mp3 converter using ffmpeg."
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Root folder to scan for videos (default: current folder).",
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Recurse into subfolders.",
    )
    parser.add_argument(
        "-b", "--bitrate",
        default="192k",
        help="MP3 bitrate (default: 192k).",
    )
    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=8,
        help="Max number of worker threads (default: 8).",
    )

    args = parser.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"[ERROR] Path does not exist: {root}")
        return 1

    videos = sorted(iter_videos(root, recursive=args.recursive))
    if not videos:
        print(f"[INFO ] No video files found under {root}")
        return 0

    print(f"[INFO ] Found {len(videos)} video(s) under {root}")
    print(f"[INFO ] Using up to {args.threads} threads, bitrate={args.bitrate}")

    results = []
    with ThreadPoolExecutor(max_workers=args.threads) as pool:
        future_map = {
            pool.submit(convert_to_mp3, v, args.bitrate): v
            for v in videos
        }
        for fut in as_completed(future_map):
            res = fut.result()
            print(res)
            results.append(res)

    # simple summary
    ok = sum(1 for r in results if r.startswith("[OK"))
    fail = sum(1 for r in results if r.startswith("[FAIL"))
    skip = sum(1 for r in results if r.startswith("[SKIP"))

    print(f"[SUMMARY] OK={ok} FAIL={fail} SKIP={skip}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
