#!/bin/bash

# Function to display usage
usage() {
	echo "Usage: $0 <ftp_host> <ftp_user> <ftp_pass> <remote_file> <local_dir> [<local_file>]"
	echo "Example: $0 ftp.example.com user password /remote/file.txt /local/directory"
	exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -lt 5 ] || [ "$#" -gt 6 ]; then
	usage
fi

# Assign arguments to variables
FTP_HOST="$1"
FTP_USER="$2"
FTP_PASS="$3"
REMOTE_FILE="$4"
LOCAL_DIR="$5"
LOCAL_FILE="$6"

# Function to download file via FTP
download_file() {
	if [ -z "$LOCAL_FILE" ]; then
		LOCAL_FILE=$(basename "$REMOTE_FILE")
	fi

	ftp -n $FTP_HOST <<END_SCRIPT
	quote USER $FTP_USER
	quote PASS $FTP_PASS
	lcd $LOCAL_DIR
	get $REMOTE_FILE $LOCAL_FILE
	quit
END_SCRIPT
}

# Main script logic
download_file