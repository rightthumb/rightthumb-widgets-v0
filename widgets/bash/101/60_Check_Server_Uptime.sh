#!/bin/bash
# Script to check server uptime and system load

# Check uptime
echo "Server Uptime:"
uptime

# Check system load
echo "System Load (Last 1, 5, 15 minutes):"
uptime | awk -F 'load average: ' '{print $2}'

# Check system reboot history
echo "Reboot History:"
last reboot