#!/bin/bash

# Check if an argument was provided
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <archive_name.tar.xz>"
	exit 1
fi

# Name of the archive to extract
ARCHIVE_NAME="$1"

# Extract the archive
tar -xf "$ARCHIVE_NAME"

# Print a confirmation message
echo "Extracted $ARCHIVE_NAME successfully!"