#!/bin/bash

# Define the FTP server service name
FTP_SERVICE="vsftpd"

# Function to start the FTP server
start_ftp_server() {
	sudo systemctl start $FTP_SERVICE
	echo "FTP server started."
}

# Function to stop the FTP server
stop_ftp_server() {
	sudo systemctl stop $FTP_SERVICE
	echo "FTP server stopped."
}

# Function to check the status of the FTP server
status_ftp_server() {
	sudo systemctl status $FTP_SERVICE
}

# Main script
case "$1" in
	-start)
		start_ftp_server
		;;
	-stop)
		stop_ftp_server
		;;
	-status)
		status_ftp_server
		;;
	*)
		echo "Usage: $0 {-start|-stop|-status}"
		exit 1
		;;
esac

exit 0