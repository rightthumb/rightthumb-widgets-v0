#!/bin/bash
# Placeholder script that displays a countdown from 100

echo "Running myscript2.sh"
count=100
while [ $count -ge 0 ]; do
	echo "Countdown: $count"
	((count--))
	sleep 1
	clear
done