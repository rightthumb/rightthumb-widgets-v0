#!/bin/bash
# Server monitoring setup with a focus on log and performance display.

# Start a new tmux session named 'ServerMonitor'
tmux new-session -d -s ServerMonitor

# Create a main horizontal split and then a vertical split in the bottom pane
tmux split-window -v -p 30
tmux select-pane -t 0
tmux split-window -h -p 50

# Load placeholder scripts into the panes
tmux send-keys -t 0 'bash ./placeholders/monitor.sh' C-m
tmux send-keys -t 1 'bash ./placeholders/log.sh' C-m
tmux send-keys -t 2 'bash ./placeholders/myscript2.sh' C-m

# Attach to the session
tmux attach-session -t ServerMonitor