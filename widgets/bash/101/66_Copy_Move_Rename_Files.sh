#!/bin/bash
# Script to copy, move, and rename files

SOURCE="file.txt"
DEST="backup/"

# Copy the file
cp "$SOURCE" "$DEST"

# Move the file
mv "$SOURCE" "$DEST"

# Rename the file
mv "oldname.txt" "newname.txt"
