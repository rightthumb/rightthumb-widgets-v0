# autoproj/tools/media.py
import subprocess
from pathlib import Path

def download_youtube1(url: str, dest_dir: str = ".") -> dict:
    Path(dest_dir).mkdir(parents=True, exist_ok=True)
    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "-o", f"{dest_dir}/%(title)s.%(ext)s",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": " ".join(cmd),
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
    }
# autoproj/tools/media.py
import subprocess
from pathlib import Path
from typing import Dict

def download_youtube(url: str, dest_dir: str = ".") -> Dict[str, object]:
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)

    # Quick heuristic: if *any* mkv/mp4/webm from this video already exists, skip.
    # (You can make this smarter later by matching IDs.)
    existing = list(dest.glob("*.mkv")) + list(dest.glob("*.mp4")) + list(dest.glob("*.webm"))
    if existing:
        return {
            "cmd": None,
            "returncode": 0,
            "stdout": f"[download_youtube] Existing media found, skipping download: {existing[0].name}",
            "stderr": "",
            "skipped": True,
        }

    cmd = [
        "yt-dlp",
        "-f", "bestvideo+bestaudio/best",
        "-o", f"{dest}/%(title)s.%(ext)s",
        url,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {
        "cmd": " ".join(cmd),
        "returncode": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr,
        "skipped": False,
    }
