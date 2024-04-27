#!/bin/bash
# This script starts a new tmux session with four panes.
# If an argument is provided, it names the session accordingly.
# If no argument is provided, it names the session "4-square".

# Check if an argument is provided for the session name, else use "4-square"
SESSION_NAME="${1:-4-square}"

# Start a new tmux session with the specified or default name
tmux new-session -d -s "$SESSION_NAME"

# Split the window into two horizontal panes
tmux split-window -h

# Split each pane vertically to create a total of four panes
tmux select-pane -t 0
tmux split-window -v
tmux select-pane -t 2
tmux split-window -v

# Attach to the session
tmux attach-session -t "$SESSION_NAME"