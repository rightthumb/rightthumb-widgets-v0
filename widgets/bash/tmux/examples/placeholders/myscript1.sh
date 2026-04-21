#!/bin/bash
# Placeholder script that prints system information continuously

echo "Running myscript1.sh"
echo "System Information:"
while true; do
	echo "Date and Time: $(date)"
	echo "Uptime:"
	uptime
	sleep 2
	clear
done