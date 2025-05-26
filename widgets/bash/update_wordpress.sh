#!/bin/bash

# Check if the WordPress path and domain are provided as arguments
if [ -z "$1" ] || [ -z "$2" ]; then
	echo "Usage: $0 /path/to/your/wordpress yourdomain.com"
	exit 1
fi

# Define the WordPress installation path from the first argument
WP_PATH="$1"

# Define the domain from the second argument
DOMAIN="$2"

# Define the path to the wp-cli command
WP_CLI="/usr/local/bin/wp"

# Define the log file path
LOG_FILE="/opt/wp_updates_${DOMAIN}.log"

# Check if wp-cli is installed
if ! command -v $WP_CLI &> /dev/null; then
	echo "wp-cli could not be found, please install it first."
	exit 1
fi

# Move to the WordPress installation directory
if ! cd "$WP_PATH"; then
	echo "WordPress path not found!"
	exit 1
fi

# Write date and time to the log file
echo "===== $(date) =====" >> $LOG_FILE

# Function to log timeout
log_timeout() {
	if [ $? -eq 124 ]; then
		echo "The command timed out." >> $LOG_FILE
	fi
}

# Update WordPress core and log the output
echo "Updating WordPress core..." >> $LOG_FILE
timeout 300 $WP_CLI core update --force --debug >> $LOG_FILE 2>&1
log_timeout

# Update plugins and log the output
echo "Updating plugins..." >> $LOG_FILE
timeout 300 $WP_CLI plugin update --all --debug >> $LOG_FILE 2>&1
log_timeout

# Update themes and log the output
echo "Updating themes..." >> $LOG_FILE
timeout 300 $WP_CLI theme update --all --debug >> $LOG_FILE 2>&1
log_timeout

# Update translations and log the output
echo "Updating translations..." >> $LOG_FILE
timeout 300 $WP_CLI language core update --debug >> $LOG_FILE 2>&1
log_timeout

echo "All updates completed successfully!" >> $LOG_FILE

# End of log entry
echo "===== End of Update =====" >> $LOG_FILE