#!/bin/bash
# Script to monitor a directory for changes

DIRECTORY="/path/to/monitor"

inotifywait -m -r "$DIRECTORY" -e create -e delete -e modify |
while read -r event; do
    echo "Change detected: $event"
done
