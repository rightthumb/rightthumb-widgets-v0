#!/bin/bash
# Script to monitor a log file in real-time

LOG_FILE="/var/log/syslog"
echo "Monitoring $LOG_FILE..."
tail -f "$LOG_FILE"
