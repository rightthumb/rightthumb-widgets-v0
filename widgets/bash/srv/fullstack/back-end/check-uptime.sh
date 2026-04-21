#!/bin/bash

# Default configuration values
UPTIME_FORMAT="human"  # Options: human or raw
THRESHOLD=86400        # Default threshold: 24 hours (in seconds)
DRY_RUN=false

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help              Show this help menu"
  echo "  -v, --version           Show script version"
  echo "  -f, --format <format>   Specify uptime format (default: human). Options: human, raw"
  echo "  -t, --threshold <sec>   Set a threshold for alerting in seconds (default: 86400 for 24 hours)"
  echo "  -n, --dry-run           Perform a dry run without triggering alerts"
  echo ""
  echo "Examples:"
  echo "  $0 -f raw -t 3600        Show raw uptime and set a threshold of 1 hour"
  echo "  $0 -n                    Perform a dry run"
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
	echo "check-uptime.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-f|--format)
	shift
	UPTIME_FORMAT=$1
	;;
	-t|--threshold)
	shift
	THRESHOLD=$1
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

# Function to check system uptime
check_uptime() {
  # Get the uptime in seconds
  UPTIME_SECONDS=$(awk '{print $1}' /proc/uptime)

  # Show uptime based on the selected format
  if [ "$UPTIME_FORMAT" == "human" ]; then
	# Convert uptime to human-readable format
	UPTIME_HOURS=$(echo "$UPTIME_SECONDS / 3600" | bc)
	UPTIME_MINUTES=$(echo "($UPTIME_SECONDS % 3600) / 60" | bc)
	UPTIME_SECONDS_REMAIN=$(echo "$UPTIME_SECONDS % 60" | bc)

	echo "Uptime: ${UPTIME_HOURS}h ${UPTIME_MINUTES}m ${UPTIME_SECONDS_REMAIN}s"
  elif [ "$UPTIME_FORMAT" == "raw" ]; then
	echo "Uptime: ${UPTIME_SECONDS} seconds"
  else
	echo "Invalid format. Use 'human' or 'raw'."
	exit 1
  fi

  # Check if the uptime exceeds the threshold
  if [ "$UPTIME_SECONDS" -ge "$THRESHOLD" ]; then
	if [ "$DRY_RUN" = true ]; then
	echo "[Dry Run] Uptime has exceeded the threshold of $THRESHOLD seconds."
	else
	echo "ALERT: System uptime has exceeded the threshold of $THRESHOLD seconds."
	fi
  else
	echo "Uptime is below the threshold of $THRESHOLD seconds."
  fi
}

# Run the uptime check
check_uptime


# ./check-uptime.sh
# ./check-uptime.sh -f raw
# ./check-uptime.sh -t 3600
# ./check-uptime.sh -n
# ./check-uptime.sh -v
# ./check-uptime.sh -t 1800
# ./check-uptime.sh -f raw -n