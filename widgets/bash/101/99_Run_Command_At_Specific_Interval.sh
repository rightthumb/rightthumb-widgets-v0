#!/bin/bash
# Script to run a command at a specific interval

COMMAND="echo 'Hello, World!'"
INTERVAL=5

while true; do
    eval "$COMMAND"
    sleep "$INTERVAL"
done
