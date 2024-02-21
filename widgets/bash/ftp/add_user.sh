#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <username> <password> <ftp_directory>" 1>&2
	exit 1
fi

username=$1
password=$2
ftp_directory=$3

# Check if the user already exists
if id "$username" &>/dev/null; then
	echo "User '$username' already exists." 1>&2
	exit 1
fi

# Create the user with the provided password and disable shell access
useradd -m -s /sbin/nologin "$username"
echo "$username:$password" | chpasswd

# Create the FTP directory and set permissions
mkdir -p "$ftp_directory"
chown -R ftp:ftp "$ftp_directory"
chmod -R 755 "$ftp_directory"

echo "User '$username' created with password '$password' and FTP directory '$ftp_directory'."