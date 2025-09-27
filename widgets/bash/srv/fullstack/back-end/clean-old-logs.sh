#!/bin/bash

# Default configuration values
LOG_DIRECTORY="/var/log"
RETENTION_DAYS=7
DRY_RUN=false

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help                Show this help menu"
  echo "  -v, --version             Show script version"
  echo "  -d, --directory <dir>     Directory containing logs to clean (default: /var/log)"
  echo "  -r, --retention <days>    Number of days to retain logs (default: 7)"
  echo "  -n, --dry-run             Perform a dry run without deleting anything"
  echo ""
  echo "Examples:"
  echo "  $0 -d /path/to/logs -r 30    Clean logs older than 30 days in /path/to/logs"
  echo "  $0 -n                        Perform a dry run"
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "clean-old-logs.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-d|--directory)
	shift
	LOG_DIRECTORY=$1
	;;
	-r|--retention)
	shift
	RETENTION_DAYS=$1
	;;
	-n|--dry-run)
	DRY_RUN=true
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Ensure the log directory exists
if [ ! -d "$LOG_DIRECTORY" ]; then
  echo "Error: Directory '$LOG_DIRECTORY' does not exist."
  exit 1
fi

# Log cleaning function
clean_logs() {
  echo "Cleaning log files older than $RETENTION_DAYS days in $LOG_DIRECTORY..."

  # Find and list files older than the specified retention period
  LOG_FILES=$(find "$LOG_DIRECTORY" -type f -name "*.log" -mtime +$RETENTION_DAYS)

  if [ -z "$LOG_FILES" ]; then
	echo "No log files older than $RETENTION_DAYS days found."
	return
  fi

  for FILE in $LOG_FILES; do
	if [ "$DRY_RUN" = true ]; then
	echo "[Dry Run] Would delete: $FILE"
	else
	echo "Deleting: $FILE"
	rm -f "$FILE"
	fi
  done
}

# Perform log cleaning
clean_logs

echo "Log cleaning completed."


# ./clean-old-logs.sh -r 30
# ./clean-old-logs.sh -d /path/to/logs -r 30
# ./clean-old-logs.sh -n
# ./clean-old-logs.sh -v
# ./clean-old-logs.sh -h
# sudo ./clean-old-logs.sh -r 30
# sudo ./clean-old-logs.sh -r 30 -n