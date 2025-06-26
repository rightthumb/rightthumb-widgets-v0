#!/bin/bash

# Check if tor is installed
if ! command -v tor &> /dev/null
then
	echo "Tor is not installed. Please install it first."
	exit 1
fi

# Start the Tor service
sudo systemctl start tor

# Check the status
if sudo systemctl is-active --quiet tor
then
	echo "Tor is now ON."
else
	echo "Failed to start Tor."
fi