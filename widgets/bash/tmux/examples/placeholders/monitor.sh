#!/bin/bash
# Placeholder script showing system monitoring

echo "Running monitor.sh"
echo "Monitoring system..."
while true; do
	top -b -n 1 | head -15
	sleep 2
	clear
done