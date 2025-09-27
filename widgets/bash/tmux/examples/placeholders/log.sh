#!/bin/bash
# Placeholder script displaying logs in real-time

echo "Running log.sh"
echo "Displaying logs..."
while true; do
	dmesg | tail -10
	sleep 3
	clear
done