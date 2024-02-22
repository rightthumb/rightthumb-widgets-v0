#!/bin/bash

# Function to display usage
usage() {
	echo "Usage: $0 {start|stop|restart|status}"
	exit 1
}

# Check if the script is run with an argument
if [ $# -ne 1 ]; then
	usage
fi

# Perform action based on the argument
case $1 in
	start)
		echo "Starting Postfix..."
		service postfix start || systemctl start postfix
		;;
	stop)
		echo "Stopping Postfix..."
		service postfix stop || systemctl stop postfix
		;;
	restart)
		echo "Restarting Postfix..."
		service postfix restart || systemctl restart postfix
		;;
	status)
		echo "Checking Postfix status..."
		service postfix status || systemctl status postfix
		;;
	*)
		usage
		;;
esac