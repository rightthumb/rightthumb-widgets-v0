#!/usr/bin/env python3
"""
demo_video_pipeline.py

Small demo that uses the autoproj Agent to manage a threaded
video→mp3 pipeline as a real "project":

Tasks in the sprint:
  1. Download sample video from YouTube
  2. Scan current folder for video files
  3. Write threaded video->MP3 converter script
  4. Write retry strategy notes for failed ffmpeg runs

Run it multiple times; each run advances one task in the sprint:

    python3 demo_video_pipeline.py --goal "Threaded video/mp3 pipeline"
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import List

from autoproj.agent import Agent, AgentContext
from autoproj.session import Sprint, Task
from autoproj.tools.media import download_youtube


# --------------------------------------------------------------------
# Helper: get or create session by goal
# --------------------------------------------------------------------


def get_or_create_context(agent: Agent, goal: str) -> AgentContext:
    """
    If a session with this goal already exists, reuse it.
    Otherwise, create a new one.
    """
    for info in agent.list_sessions_summary():
        if info.get("goal") == goal:
            ctx = agent.load_session(info["id"])
            if ctx is not None:
                return ctx

    # No existing session: create a new project
    return agent.init_project(goal)


# --------------------------------------------------------------------
# Pipeline-specific helper functions
# --------------------------------------------------------------------


def _scan_videos() -> str:
    """
    Scan current directory for .mp4 / .mkv files.
    """
    exts = {".mp4", ".mkv", ".mov", ".avi", ".webm"}
    here = Path.cwd()
    vids: List[Path] = []
    for p in here.iterdir():
        if p.is_file() and p.suffix.lower() in exts:
            vids.append(p)

    if not vids:
        return "No video files found in current directory."

    lines = ["Found video files:"]
    for v in vids:
        lines.append(f"  - {v}")
    return "\n".join(lines)


def _write_threaded_converter() -> str:
    """
    Write video2mp3_threaded.py into the current directory
    (idempotent: will overwrite with the same content).
    """
    target = Path("video2mp3_threaded.py")

    script = r"""#!/usr/bin/env python3
import argparse
import concurrent.futures
import os
import subprocess
from pathlib import Path
from typing import List, Tuple

VIDEO_EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov", ".m4v", ".wmv",
    ".flv", ".webm", ".mpg", ".mpeg", ".3gp", ".ts"
}


def is_video_file(path: Path) -> bool:
    return path.suffix.lower() in VIDEO_EXTENSIONS


def find_videos(root: Path, recursive: bool) -> List[Path]:
    videos: List[Path] = []
    if recursive:
        for dirpath, _, filenames in os.walk(root):
            for name in filenames:
                p = Path(dirpath) / name
                if is_video_file(p):
                    videos.append(p)
    else:
        for p in root.iterdir():
            if p.is_file() and is_video_file(p):
                videos.append(p)
    return videos


def convert_to_mp3(video_path: Path, bitrate: str = "192k") -> Tuple[Path, bool, str]:
    """
   # Return (video_path, success, message)
    """
    if not video_path.is_file():
        return video_path, False, f"[ERROR] Not a file: {video_path}"

    out_path = video_path.with_suffix(".mp3")

    if out_path.exists():
        return video_path, False, f"[SKIP ] MP3 already exists: {out_path}"

    cmd = [
        "ffmpeg",
        "-y",  # overwrite silently
        "-i", str(video_path),
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", bitrate,
        str(out_path),
    ]
    try:
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except Exception as e:
        return video_path, False, f"[FAIL ] {video_path} (exception: {e})"

    if proc.returncode != 0:
        return video_path, False, f"[FAIL ] {video_path} (ffmpeg rc={proc.returncode})"

    return video_path, True, f"[OK   ] {video_path} -> {out_path}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Threaded video->MP3 converter using ffmpeg.",
    )
    parser.add_argument(
        "root",
        metavar="ROOT",
        help="Root directory to scan for videos.",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse into subdirectories.",
    )
    parser.add_argument(
        "-t",
        "--threads",
        type=int,
        default=8,
        help="Maximum number of conversion threads (default: 8).",
    )
    parser.add_argument(
        "-b",
        "--bitrate",
        default="192k",
        help="MP3 bitrate (default: 192k).",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"[ERROR] Not a directory: {root}")
        return 1

    videos = find_videos(root, recursive=args.recursive)
    print(f"[INFO ] Found {len(videos)} video(s) under {root}")
    print(f"[INFO ] Using up to {args.threads} threads, bitrate={args.bitrate}")

    ok = fail = skip = 0

    def _worker(v: Path) -> str:
        nonlocal ok, fail, skip
        v, success, msg = convert_to_mp3(v, bitrate=args.bitrate)
        print(msg)
        if "SKIP" in msg:
            skip += 1
        elif success:
            ok += 1
        else:
            fail += 1
        return msg

    if not videos:
        print("[SUMMARY] Nothing to do.")
        return 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as ex:
        list(ex.map(_worker, videos))

    print(f"[SUMMARY] OK={ok} FAIL={fail} SKIP={skip}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
"""

    target.write_text(script, encoding="utf-8")
    try:
        target.chmod(0o755)
    except Exception:
        pass

    return f"Wrote threaded converter script to {target}"


def _write_retry_readme() -> str:
    """
    Drop a small README describing retry strategy.
    """
    path = Path("video_retry_strategy.md")
    text = """# Video Conversion Retry Strategy

1. Run `video2mp3_threaded.py` once over the target tree.
2. For failed files:
   - Capture ffmpeg stderr and look for common signatures:
     - Codec not supported
     - Corrupt container
     - Permission denied
   - Log failures to a separate text file (path + error).
3. On second pass, only feed failed files back into the converter.
4. For still-failing files, try:
   - `ffmpeg -err_detect ignore_err` to salvage partial audio
   - Re-muxing the container with `-c copy` first.
"""
    path.write_text(text, encoding="utf-8")
    return f"Wrote retry strategy notes to {path}"


# --------------------------------------------------------------------
# Executor for our sprint tasks
# --------------------------------------------------------------------


def video_task_executor(task: Task, ctx: AgentContext) -> str:
    desc = task.description.lower()

    # 1) Download sample video
    if "download sample video from youtube" in desc:
        url = "https://youtu.be/nIwwD7XWueQ?si=NQmtifBwHelowxPC"
        res = download_youtube(url, dest_dir=".")
        lines = []

        if res.get("skipped"):
            lines.append("Download step skipped (existing media detected).")
            lines.append(str(res.get("stdout", "")).strip())
            return "\n".join(lines)

        lines.append("Ran yt-dlp:")
        lines.append(f"  cmd: {res.get('cmd')}")
        lines.append(f"  returncode: {res.get('returncode')}")

        stdout = str(res.get("stdout", ""))
        stderr = str(res.get("stderr", ""))

        if stdout:
            lines.append("  stdout (truncated):")
            lines.append("\n".join(stdout.splitlines()[:20]))
        if stderr:
            lines.append("  stderr (truncated):")
            lines.append("\n".join(stderr.splitlines()[:20]))

        return "\n".join(lines)

    # 2) Scan current folder for video files
    if "scan current folder for video files" in desc:
        return _scan_videos()

    # 3) Write threaded converter
    if "threaded video->mp3 converter script" in desc:
        return _write_threaded_converter()

    # 4) Write retry notes
    if "retry strategy notes for failed ffmpeg runs" in desc:
        return _write_retry_readme()

    return f"[NOOP] {task.description}"


# --------------------------------------------------------------------
# Main: wire everything together
# --------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Demo: use autoproj.Agent to drive a threaded video/mp3 pipeline.",
    )
    parser.add_argument(
        "--goal",
        default="Threaded video/mp3 pipeline",
        help="High-level project goal (used to find/reuse a session).",
    )
    args = parser.parse_args(argv)

    agent = Agent()
    ctx = get_or_create_context(agent, args.goal)

    # If this is a brand-new session, seed it with our custom sprint.
    if not ctx.session.sprints:
        sprint = Sprint(
            title="Threaded video/mp3 pipeline sprint",
            status="active",
            tasks=[
                Task(description="Download sample video from YouTube"),
                Task(description="Scan current folder for video files"),
                Task(description="Write threaded video->MP3 converter script"),
                Task(description="Write retry strategy notes for failed ffmpeg runs"),
            ],
        )
        agent.session_manager.add_sprint(ctx.session, sprint)

    # Run exactly one task per invocation
    result = agent.run_next_task(ctx, video_task_executor)
    print("\n=== Task result ===")
    print(result)
    print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
