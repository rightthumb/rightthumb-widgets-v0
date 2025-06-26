#!/bin/bash

bleachbit --clean system.cache

# Ensure the script is run as root
if [[ "$EUID" -ne 0 ]]; then
	echo "Please run as root"
	exit 1
fi


echo "Starting cleanup of temporary and cache directories..."

# Define directories to clean
TEMP_DIRS=(
	"/tmp"
	"/var/cache/davfs2"
	"/var/tmp"
	"/var/cache/apt/archives"
	"/var/cache/apt/archives/partial"
	"/var/cache/debconf"
	"/var/cache/dictionaries-common"
	"/var/cache/fontconfig"
	"/var/cache/ldconfig"
	"/var/cache/lightdm"
	"/var/cache/man"
	"/var/cache/nginx"
	"/var/cache/apt-xapian-index"
	"/var/log/journal" # Clean old system logs
	"/root/.cache" # Root cache
	"/home/*/.cache" # User cache
	"/var/cache/webrtc" # WebRTC cache
	"/var/cache/webdav" # WebDAV temp/cache (assumed path)
)

# Additional specific files to clean
SPECIFIC_FILES=(
	"/opt/cpanel/ea-php82/root/usr/var/log/php-fpm/error.log"
	"/var/log/nginx/access.log"
	"/var/log/nginx/error.log"
	"/var/log/syslog"
	"/var/log/auth.log"
)

# Function to remove files in each directory
clean_directory() {
	local DIR=$1
	if [[ -d "$DIR" ]]; then
		echo "Cleaning $DIR ..."
		rm -rf "$DIR"/*
		echo "$DIR cleaned."
	else
		echo "Directory $DIR does not exist, skipping."
	fi
}

# Function to remove specific files
clean_files() {
	local FILE=$1
	if [[ -f "$FILE" ]]; then
		echo "Removing $FILE ..."
		rm -f "$FILE"
		echo "$FILE removed."
	else
		echo "File $FILE does not exist, skipping."
	fi
}

# Clean directories
for DIR in "${TEMP_DIRS[@]}"; do
	clean_directory "$DIR"
done

# Clean specific files
for FILE in "${SPECIFIC_FILES[@]}"; do
	clean_files "$FILE"
done

# Clear systemd journal logs older than 7 days
echo "Cleaning systemd journal logs older than 7 days..."
journalctl --vacuum-time=7d
echo "Systemd journal logs cleaned."

# Clean APT cache
echo "Cleaning APT cache..."
apt-get clean
echo "APT cache cleaned."

# Remove old unused packages
echo "Removing old unused packages..."
apt-get autoremove -y
echo "Unused packages removed."

# Update and upgrade system (optional, uncomment if desired)
# echo "Updating and upgrading system packages..."
# apt-get update && apt-get upgrade -y
# echo "System packages updated and upgraded."

echo "Temporary and cache cleanup completed!"
exit 0