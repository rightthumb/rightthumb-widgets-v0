#!/bin/bash
# This script starts a new tmux session with four panes.
# If an argument is provided, it names the session accordingly.
# If no argument is provided, it names the session "4-square".

# Check if an argument is provided for the session name, else use "4-square"
SESSION_NAME="${1:-t4}"

# Start a new tmux session with the specified or default name
tmux new-session -d -s "$SESSION_NAME"

# Split the window into two horizontal panes
tmux split-window -h -t "$SESSION_NAME"

# Split each pane vertically to create a total of four panes
tmux select-pane -t "$SESSION_NAME":0.0
tmux split-window -v -t "$SESSION_NAME"
tmux select-pane -t "$SESSION_NAME":0.2
tmux split-window -v -t "$SESSION_NAME"

# Attach to the session
tmux attach-session -t "$SESSION_NAME"