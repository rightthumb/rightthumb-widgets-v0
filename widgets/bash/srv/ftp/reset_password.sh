#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

# Check if the script is run as root
if [ "$(id -u)" -ne 0 ]; then
	echo "This script must be run as root" 1>&2
	exit 1
fi

# Check if three arguments are provided
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <username> <ftp_directory>" 1>&2
	exit 1
fi

sudo ftpasswd --passwd --file /etc/proftpd/ftpd.passwd --name $1 --uid 1001 --gid 1001 --home $2 --shell /bin/false