#!/bin/bash

# Function to display usage
usage() {
	echo "Usage: $0 <ftp_host> <ftp_user> <ftp_pass> <local_file> <remote_dir>"
	echo "Example: $0 ftp.example.com user password local_file.txt /remote/directory"
	exit 1
}

# Check if the correct number of arguments is provided
if [ "$#" -ne 5 ]; then
	usage
fi

# Assign arguments to variables
FTP_HOST="$1"
FTP_USER="$2"
FTP_PASS="$3"
LOCAL_FILE="$4"
REMOTE_DIR="$5"

# Function to upload file via FTP
upload_file() {
	ftp -n $FTP_HOST <<END_SCRIPT
	quote USER $FTP_USER
	quote PASS $FTP_PASS
	put $LOCAL_FILE $REMOTE_DIR/$(basename $LOCAL_FILE)
	quit
END_SCRIPT
}

# Main script logic
upload_file