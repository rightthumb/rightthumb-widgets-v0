#!/bin/bash

# Function to start ProFTPD
start() {
	sudo systemctl start proftpd
}

# Function to stop ProFTPD
stop() {
	sudo systemctl stop proftpd
}

# Function to check the status of ProFTPD
status() {
	sudo systemctl status proftpd
}

# Function to restart ProFTPD
restart() {
	sudo systemctl restart proftpd
}

# Main script logic
case "$1" in
	start)
		start
		;;
	stop)
		stop
		;;
	status)
		status
		;;
	restart)
		restart
		;;
	*)
		echo "Usage: $0 {start|stop|status|restart}"
		exit 1
		;;
esac

exit 0