#!/bin/bash
# This script creates a tmux session with four evenly divided panes.
# Default session name is "Quadrants" unless specified.

SESSION_NAME="${1:-tq}"

tmux new-session -d -s "$SESSION_NAME"
tmux split-window -h
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v
tmux attach-session -t "$SESSION_NAME"