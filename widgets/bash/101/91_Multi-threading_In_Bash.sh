#!/bin/bash
# Script to demonstrate multi-threading in Bash

function task {
  echo "Task $1 running..."
  sleep 2
  echo "Task $1 completed."
}

# Run tasks in parallel
for i in {1..5}; do
  task "$i" &
done

# Wait for all tasks to complete
wait
echo "All tasks completed."
