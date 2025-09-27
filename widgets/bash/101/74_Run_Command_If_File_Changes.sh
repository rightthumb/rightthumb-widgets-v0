#!/bin/bash
# Script to run a command if a file changes

FILE="example.txt"
COMMAND="echo 'File changed!'"

inotifywait -m -e modify "$FILE" |
while read -r; do
    eval "$COMMAND"
done
