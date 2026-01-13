#!/bin/bash

# Check if tor is installed
if ! command -v tor &> /dev/null
then
	echo "Tor is not installed. Please install it first."
	exit 1
fi

# Stop the Tor service
sudo systemctl stop tor

# Check the status
if sudo systemctl is-active --quiet tor
then
	echo "Failed to stop Tor."
else
	echo "Tor is now OFF."
fi