#!/usr/bin/env python3
import os
import sys
import time

def wait_for_download_complete(
    filename: str,
    stable_seconds: float = 5.0,
    poll_interval: float = 0.25,
) -> None:
    """
    Monitor `filename` in the current working directory.
    When its size stops changing for `stable_seconds`, print 'done' and exit.
    """

    path = os.path.abspath(filename)

    last_size = None
    stable_start = None

    while True:
        try:
            size = os.path.getsize(path)
        except FileNotFoundError:
            # File not created yet (common during download start)
            last_size = None
            stable_start = None
            time.sleep(poll_interval)
            continue

        now = time.monotonic()

        if last_size is None:
            last_size = size
            stable_start = None
        elif size != last_size:
            # Still growing/changing
            last_size = size
            stable_start = None
        else:
            # Size unchanged
            if stable_start is None:
                stable_start = now
            elif (now - stable_start) >= stable_seconds:
                print("done")
                return

        time.sleep(poll_interval)

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <filename> [stable_seconds] [poll_interval]")
        sys.exit(2)

    filename = sys.argv[1]
    stable_seconds = float(sys.argv[2]) if len(sys.argv) >= 3 else 5.0
    poll_interval = float(sys.argv[3]) if len(sys.argv) >= 4 else 0.25

    wait_for_download_complete(
        filename=filename,
        stable_seconds=stable_seconds,
        poll_interval=poll_interval,
    )

if __name__ == "__main__":
    main()
