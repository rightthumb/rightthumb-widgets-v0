#!/bin/bash

# Check if a directory argument was provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path-to-directory>"
    exit 1
fi

TARGET_DIR=$1

# Check if the provided directory exists
if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Directory '$TARGET_DIR' does not exist."
    exit 1
fi

# Change permissions of directories to 755
echo "Setting permissions of directories to 755..."
find "$TARGET_DIR" -type d -exec chmod 755 {} +

# Change permissions of files to 644
echo "Setting permissions of files to 644..."
find "$TARGET_DIR" -type f -exec chmod 644 {} +

echo "Permissions have been updated."

