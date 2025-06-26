#!/bin/bash

# Function to display help
display_help() {
    echo "Usage: $0 [-force] [-h]"
    echo
    echo "Options:"
    echo "  -force           Force reinstall requests with '--upgrade --no-cache-dir --break-system-packages'"
    echo "  -h               Display this help message"
}

# Function to uninstall python-requests
uninstall_requests() {
    echo "Uninstalling python-requests..."
    pip uninstall -y requests
}

force_uninstall_requests() {
    echo "Uninstalling python-requests with '--break-system-packages'..."
    pip uninstall -y requests --break-system-packages
}

# Function to reinstall python-requests normally
reinstall_requests() {
    echo "Reinstalling python-requests..."
    pip install -y requests
}

# Function to force reinstall python-requests with --break-system-packages
force_reinstall_requests() {
    echo "Reinstalling python-requests with '--upgrade --no-cache-dir --break-system-packages'..."
    pip install -y requests --upgrade --no-cache-dir --break-system-packages
}

# Parse command-line options
FORCE=false
while [[ "$1" != "" ]]; do
    case $1 in
        -force )  FORCE=true
                  ;;
        -h | --help )  
                  display_help
                  exit 0
                  ;;
        * )       
                  echo "Unknown option: $1"
                  display_help
                  exit 1
                  ;;
    esac
    shift
done

# Reinstall the requests package based on the options provided
if [ "$FORCE" = true ]; then
    force_uninstall_requests
    force_reinstall_requests
else
    uninstall_requests
    reinstall_requests
fi

echo "Done!"
