#!/bin/bash

# Get hostname from /etc/hostname
hostname=$(cat /etc/hostname)

# Check if arguments are provided
if [ $# -eq 0 ]; then
	echo "No package(s) specified for installation."
	exit 1
fi

# Install each package provided as an argument
for aptPackage in "$@"; do
	echo "Starting installation of $aptPackage on $hostname..."

	# Install the package
	sudo apt-get update -y
	if sudo apt-get install -y $aptPackage; then
		echo "Installation of $aptPackage successful on $hostname."
		curl -X POST -d "hostname=$hostname&apt=$aptPackage" https://sds.sh/apt/
	else
		echo "Failed to install $aptPackage on $hostname."
	fi
done