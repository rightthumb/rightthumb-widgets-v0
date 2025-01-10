#!/bin/bash
# Script to log system stats (CPU, memory, disk usage) periodically

LOG_FILE="system_stats.log"
INTERVAL=60  # Time interval in seconds

echo "Logging system stats to $LOG_FILE every $INTERVAL seconds..."

while true; do
    echo "=========================" >> "$LOG_FILE"
    echo "Date: $(date)" >> "$LOG_FILE"
    echo "Uptime:" >> "$LOG_FILE"
    uptime >> "$LOG_FILE"
    echo "CPU and Memory Usage:" >> "$LOG_FILE"
    top -b -n 1 | head -n 10 >> "$LOG_FILE"
    echo "Disk Usage:" >> "$LOG_FILE"
    df -h >> "$LOG_FILE"
    echo "=========================" >> "$LOG_FILE"

    sleep "$INTERVAL"
done
