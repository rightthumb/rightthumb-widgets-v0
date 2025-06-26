#!/bin/bash
# High-activity developer's console with scripts running in a visually engaging layout.

# Start a new tmux session named 'HackConsole'
tmux new-session -d -s HackConsole

# Split the window vertically then horizontally
tmux split-window -v -p 40
tmux split-window -h -p 50

# Select the first vertical pane and split it horizontally again
tmux select-pane -t 0
tmux split-window -h -p 50

# Load placeholder scripts
tmux send-keys -t 0 'bash ./placeholders/build.sh' C-m
tmux send-keys -t 1 'bash ./placeholders/test.sh' C-m
tmux send-keys -t 2 'bash ./placeholders/myscript1.sh' C-m
tmux send-keys -t 3 'bash ./placeholders/myscript2.sh' C-m

# Attach to the session
tmux attach-session -t HackConsole