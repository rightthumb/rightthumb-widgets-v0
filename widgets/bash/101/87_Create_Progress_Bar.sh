#!/bin/bash
# Script to create a progress bar

progress_bar() {
  for i in {1..50}; do
    sleep 0.1
    printf "#"
  done
  echo ""
}

echo "Progress:"
progress_bar
