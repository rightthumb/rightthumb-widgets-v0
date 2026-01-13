#!/bin/bash
# Script to handle signals

# Trap SIGINT and SIGTERM
trap 'echo "Interrupt received, exiting..."; exit 1' SIGINT SIGTERM

# Infinite loop to keep the script running
while true; do
	sleep 1
done