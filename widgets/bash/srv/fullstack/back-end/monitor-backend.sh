#!/bin/bash

# Function to check if a backend service is running
check_backend_service() {
  SERVICE_NAME=$1
  if systemctl is-active --quiet $SERVICE_NAME; then
	echo "$SERVICE_NAME is running."
  else
	echo "$SERVICE_NAME is not running. Attempting to restart..."
	restart_backend_service $SERVICE_NAME
  fi
}

# Function to restart the backend service
restart_backend_service() {
  SERVICE_NAME=$1
  echo "Restarting $SERVICE_NAME..."
  sudo systemctl restart $SERVICE_NAME
  if systemctl is-active --quiet $SERVICE_NAME; then
	echo "$SERVICE_NAME has been restarted successfully."
  else
	echo "Failed to restart $SERVICE_NAME. Please check logs."
	send_alert "Failed to restart $SERVICE_NAME"
  fi
}

# Function to check CPU and Memory usage
check_system_usage() {
  CPU_THRESHOLD=80
  MEM_THRESHOLD=80

  CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
  MEM_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')

  echo "Current CPU Usage: $CPU_USAGE%"
  echo "Current Memory Usage: $MEM_USAGE%"

  if (( $(echo "$CPU_USAGE > $CPU_THRESHOLD" | bc -l) )); then
	echo "Warning: CPU usage is above $CPU_THRESHOLD%."
	send_alert "High CPU usage: $CPU_USAGE%"
  fi

  if (( $(echo "$MEM_USAGE > $MEM_THRESHOLD" | bc -l) )); then
	echo "Warning: Memory usage is above $MEM_THRESHOLD%."
	send_alert "High Memory usage: $MEM_USAGE%"
  fi
}

# Function to check disk space usage
check_disk_space() {
  DISK_THRESHOLD=90
  DISK_USAGE=$(df / | grep / | awk '{ print $5 }' | sed 's/%//g')

  echo "Current Disk Space Usage: $DISK_USAGE%"

  if [ $DISK_USAGE -gt $DISK_THRESHOLD ]; then
	echo "Warning: Disk usage is above $DISK_THRESHOLD%."
	send_alert "High disk space usage: $DISK_USAGE%"
  fi
}

# Function to send alert (email or logging)
send_alert() {
  MESSAGE=$1
  echo "Sending alert: $MESSAGE"
  # You can modify this function to send emails or log alerts to a monitoring system
  # For example, using `mail` command for email alerts:
  # echo "$MESSAGE" | mail -s "Backend Alert" admin@example.com
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help              Show this help menu"
  echo "  -v, --version           Display script version"
  echo "  -s, --service <name>    Specify the backend service name to monitor"
  echo ""
  echo "Examples:"
  echo "  $0 -s backend-service-name"
}

# Script version
SCRIPT_VERSION="1.0.0"
SERVICE_NAME=""

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "monitor-backend.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-s|--service)
	shift
	SERVICE_NAME=$1
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Validate service input
if [ -z "$SERVICE_NAME" ]; then
  echo "Error: Backend service name is required."
  show_help
  exit 1
fi

# Check backend service
check_backend_service $SERVICE_NAME

# Check system health (CPU, Memory, Disk)
check_system_usage
check_disk_space

echo "Backend monitoring completed."


# node, nginx, apache
# sudo ./monitor-backend.sh -s backend-service-name
# ./monitor-backend.sh -v
# ./monitor-backend.sh -h