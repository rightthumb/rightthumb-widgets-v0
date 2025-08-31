#!/bin/bash
# Script to modify file permissions and ownership

FILE="example.txt"

# Set execute permission
chmod +x "$FILE"
echo "Execute permission set for $FILE."

# Change ownership to a specific user and group
chown user:group "$FILE"
echo "Ownership changed for $FILE."