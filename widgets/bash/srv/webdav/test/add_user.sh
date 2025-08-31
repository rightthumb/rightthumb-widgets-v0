#!/bin/bash

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
	echo "This script must be run as root"
	exit 1
fi

# Variables
USERNAME="jon"
PASSWORD="your_password"
URL="https://server.com/webdav/jon"
MOUNTPOINT="/mnt/webdav"

# Install necessary packages
apt update
apt install apache2 apache2-utils davfs2 -y

# Add user to davfs2 group
usermod -aG davfs2 $USERNAME

# Create the mount point directory
mkdir -p $MOUNTPOINT
chown $USERNAME:$USERNAME $MOUNTPOINT
chmod 755 $MOUNTPOINT

# Update /etc/fstab
echo "$URL $MOUNTPOINT davfs rw,user,noauto 0 0" >> /etc/fstab

# Update /etc/davfs2/secrets
echo "$URL $USERNAME $PASSWORD" >> /etc/davfs2/secrets
chown root:root /etc/davfs2/secrets
chmod 600 /etc/davfs2/secrets

# Mount the WebDAV share
mount -t davfs $URL $MOUNTPOINT

echo "WebDAV share mounted at $MOUNTPOINT"