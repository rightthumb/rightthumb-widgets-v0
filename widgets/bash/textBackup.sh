#!/bin/bash

# Check if the first argument is provided
if [ "$#" -lt 1 ]; then
	echo "Usage: $0 <folder/path> [output/folder]"
	exit 1
fi

# Check if the provided directory exists
if [ ! -d "$1" ]; then
	echo "Error: Directory $1 does not exist."
	exit 1
fi

# If the second argument (output folder) is provided and exists
OUTPUT_DIR="."
if [ "$#" -eq 2 ]; then
	if [ ! -d "$2" ]; then
		echo "Error: Output directory $2 does not exist."
		exit 1
	else
		OUTPUT_DIR="$2"
	fi
fi

# Extract the last two folder names from the path
BASE_NAME=$(echo "$1" | awk -F'/' '{print $(NF-1)"-"$NF}')
TIMESTAMP=$(date +%s)
OUTPUT_NAME="${OUTPUT_DIR}/${BASE_NAME}_${TIMESTAMP}.tar.xz"

# Find all text files based on their MIME type and tar them
find "$1" -type f -exec sh -c 'file --brief --mime-type "$1" | grep -q "^text/"' _ {} \; -print0 | tar --null -T - -cJf "$OUTPUT_NAME"

echo "Backup saved as $OUTPUT_NAME"