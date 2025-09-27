#!/bin/sh

# Get the filename from the first argument
FILENAME="$1"
shift

# Determine the file extension
EXT="${FILENAME##*.}"

# Construct the URL dynamically based on the file extension
SCRIPT_URL="https://shell.sds.sh/?${EXT}=${FILENAME}"

# Download and execute the script
curl -s "$SCRIPT_URL" | bash -s -- "$@"
