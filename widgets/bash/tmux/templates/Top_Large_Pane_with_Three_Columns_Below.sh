#!/bin/bash
# This script creates a tmux session with a large top pane and three smaller columns beneath.
# Default session name is "TopLargeThreeCols" unless specified.

SESSION_NAME="${1:-t3}"

tmux new-session -d -s "$SESSION_NAME"
tmux split-window -v -p 66
tmux select-pane -t 1
tmux split-window -h
tmux select-pane -t 1
tmux split-window -h
tmux attach-session -t "$SESSION_NAME"