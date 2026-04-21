#!/bin/bash
# This script creates a basic tmux session with a single window.
# If an argument is provided, it names the session accordingly.
# If no argument is provided, it names the session "SingleWindow".

SESSION_NAME="${1:-ts}"

# Start a new tmux session with the specified or default name
tmux new-session -d -s "$SESSION_NAME"

# Attach to the session
tmux attach-session -t "$SESSION_NAME"