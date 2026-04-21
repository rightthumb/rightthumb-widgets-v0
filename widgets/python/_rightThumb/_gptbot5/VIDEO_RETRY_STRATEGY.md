# Video Conversion Retry Strategy

This project uses `video2mp3_threaded.py` for conversion.

## Retry approach

- Each run of the script:
  - Skips videos that already have a `.mp3` next to them.
  - Reports `[FAIL]` for ffmpeg errors (non-zero return code).
- To retry failures:
  - Fix underlying issues (missing codecs, corrupt files, etc.).
  - Re-run the script on the same root folder; only videos without `.mp3`
    will be retried.

## Suggested workflow

1. Run with a small `--threads` value first (e.g. 4).
2. Watch for `[FAIL]` lines and adjust your ffmpeg command if needed.
3. Increase `--threads` once stable.
4. Use shell logs to capture full stderr if debugging specific files.
