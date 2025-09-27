#!/bin/bash
# This script creates a tmux session with three horizontal stripes/panes.
# Default session name is "HorizStripes" unless specified.

SESSION_NAME="${1:-th}"

tmux new-session -d -s "$SESSION_NAME"
tmux split-window -v
tmux select-pane -t 0
tmux split-window -v
tmux select-layout even-horizontal
tmux attach-session -t "$SESSION_NAME"