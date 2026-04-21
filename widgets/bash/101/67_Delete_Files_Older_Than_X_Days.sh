#!/bin/bash
# Script to delete files older than X days

DIRECTORY="/path/to/folder"
DAYS=30

find "$DIRECTORY" -type f -mtime +$DAYS -exec rm -f {} \;
echo "Deleted files older than $DAYS days in $DIRECTORY."
