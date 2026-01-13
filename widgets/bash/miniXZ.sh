#!/bin/bash

# Check for the number of arguments
if [ "$#" -lt 1 ]; then
	echo "Usage: $0 <folder> [archive_name]"
	exit 1
fi

# If only one argument is provided, set the archive name to be the same as the folder name
FOLDER="$1"
if [ "$#" -eq 1 ]; then
	ARCHIVE_NAME="$FOLDER"
else
	ARCHIVE_NAME="$2"
fi

# Create the compressed archive
tar -cf - "$FOLDER" | xz -9e > "$ARCHIVE_NAME".tar.xz

# Print a confirmation message
echo "Archive created as $ARCHIVE_NAME.tar.xz"