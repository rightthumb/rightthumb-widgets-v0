#!/bin/bash
# Script to handle command timeout using timeout command

echo "Running a command with a 10-second timeout..."
timeout 10s sleep 30

if [ $? -eq 124 ]; then
    echo "The command timed out."
else
    echo "The command completed successfully."
fi
