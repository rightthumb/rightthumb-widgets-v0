#!/bin/bash
# Dynamic development environment layout in tmux with multiple custom panes.

# Start a new tmux session named 'DevEnv'
tmux new-session -d -s DevEnv

# Split the window into three panes: one main vertical and two horizontal splits in the right pane
tmux split-window -h -p 65
tmux split-window -v -p 50

# Load placeholder scripts into the panes
tmux send-keys -t 0 'bash ./placeholders/edit.sh' C-m
tmux send-keys -t 1 'bash ./placeholders/myscript1.sh' C-m
tmux send-keys -t 2 'bash ./placeholders/server.sh' C-m

# Attach to the session
tmux attach-session -t DevEnv