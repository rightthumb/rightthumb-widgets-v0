#!/bin/bash
# This script creates a tmux session with one large pane on the left and three smaller stacked panes on the right.
# Default session name is "MainThreeStack" unless specified.

SESSION_NAME="${1:-t3}"

tmux new-session -d -s "$SESSION_NAME"
tmux split-window -h -p 70
tmux select-pane -t 1
tmux split-window -v
tmux select-pane -t 1
tmux split-window -v
tmux attach-session -t "$SESSION_NAME"