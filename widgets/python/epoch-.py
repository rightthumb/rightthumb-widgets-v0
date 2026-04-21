#!/usr/bin/env python3
import sys
import time
from datetime import datetime

# --- Color helper: hex → ANSI escape ---
def c(hex_color):
    """Convert #RRGGBB into ANSI escape code."""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"\033[38;2;{r};{g};{b}m"

RESET = "\033[0m"

# Prettier colors
COL_TIMESTAMP = c("#62c1ff")
COL_EPOCH = c("#00ffaa")
COL_LABEL = c("#ffaa00")
COL_VALUE = c("#ffffff")
COL_PAST = c("#ff5555")
COL_FUTURE = c("#55ff55")

def print_current_epoch():
    if '--c' in sys.argv:
        print(f"{COL_EPOCH}{int(time.time())}{RESET}")
    else:
        print(f"{COL_EPOCH}{time.time()}{RESET}")

def main():
    args = sys.argv[1:]

    if "-epoch" not in args:
        print_current_epoch()
        return

    idx = args.index("-epoch")

    if idx + 1 >= len(args):
        print_current_epoch()
        return

    epoch_str = args[idx + 1]
    try:
        epoch_val = int(epoch_str)
    except ValueError:
        print_current_epoch()
        return

    # Convert epoch → timestamp
    dt = datetime.fromtimestamp(epoch_val)
    timestamp_str = dt.strftime("%Y-%m-%d %H:%M:%S")

    # Calculate difference
    now = time.time()
    diff = now - epoch_val
    direction = "past" if diff >= 0 else "future"
    direction_color = COL_PAST if diff >= 0 else COL_FUTURE

    seconds = abs(int(diff))

    years, seconds = divmod(seconds, 365 * 24 * 3600)
    months, seconds = divmod(seconds, 30 * 24 * 3600)
    weeks, seconds = divmod(seconds, 7 * 24 * 3600)
    days, seconds = divmod(seconds, 24 * 3600)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    components = [
        ("years", years),
        ("months", months),
        ("weeks", weeks),
        ("days", days),
        ("hours", hours),
        ("minutes", minutes),
        ("seconds", seconds),
    ]

    # --- PRETTY COLORIZED YAML OUTPUT ---
    print(f"{COL_LABEL}timestamp:{RESET} {COL_TIMESTAMP}{timestamp_str}{RESET}")
    print(f"{COL_LABEL}epoch:{RESET} {COL_EPOCH}{epoch_val}{RESET}")
    print(f"{COL_LABEL}diff:{RESET}")
    print(f"    {COL_LABEL}direction:{RESET} {direction_color}{direction}{RESET}")

    for name, value in components:
        if value != 0:
            print(f"    {COL_LABEL}{name}:{RESET} {COL_VALUE}{value}{RESET}")

if __name__ == "__main__":
    main()
