#!/bin/bash

# Ensure the script is run as root
if [[ "$EUID" -ne 0 ]]; then
	echo "Please run as root"
	exit 1
fi

echo "Starting cleanup of temporary and cache directories..."

# Define directories to clean
TEMP_DIRS=(
	"/tmp"
	"/var/tmp"
	"/var/cache"
	"/var/log/journal" # Clean old system logs
	"/root/.cache" # Root cache
	"/home/*/.cache" # User cache
	"/var/cache/webrtc" # WebRTC cache
	"/var/cache/webdav" # WebDAV temp/cache (assumed path)
)

# Cleaning up each directory
for DIR in "${TEMP_DIRS[@]}"; do
	if [[ -d "$DIR" ]]; then
		echo "Cleaning $DIR ..."
		rm -rf "$DIR"/*
	else
		echo "Directory $DIR does not exist, skipping."
	fi
done

# Optionally clear journal logs if they are large (this is optional, uncomment if needed)
# journalctl --vacuum-time=7d  # Clears journal logs older than 7 days

# Optionally clear systemd journal logs older than a specific time
echo "Cleaning systemd journal logs older than 7 days..."
journalctl --vacuum-time=7d

echo "Temporary and cache cleanup completed!"

exit 0