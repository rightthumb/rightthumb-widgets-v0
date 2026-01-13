#!/bin/bash
# Script to search for patterns using grep

LOG_FILE="logfile.txt"

# Search for errors and warnings
grep -E 'error|warning' "$LOG_FILE"