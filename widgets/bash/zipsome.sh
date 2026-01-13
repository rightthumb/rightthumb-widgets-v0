#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -lt 2 ]; then
	echo "Usage: $0 <directory-path> <file-pattern1> [<file-pattern2> ...]"
	exit 1
fi

DIRECTORY="$1"
shift  # Remove the directory from the argument list
TEMPDIR=$(mktemp -d)

# Function to replicate the directory structure and copy the files
replicate_structure() {
	local src="$1"
	local dest="$2"
	local pattern="$3"
	find "$src" -type d | while read -r dir; do
		mkdir -p "$dest/${dir#$src}"
		find "$dir" -maxdepth 1 -type f -name "$pattern" | while read -r file; do
			cp "$file" "$dest/${file#$src}"
		done
	done
}

# For each pattern, replicate the directory structure and copy the files
for pattern in "$@"; do
	replicate_structure "$DIRECTORY" "$TEMPDIR" "$pattern"
done

# Zip the temporary directory
zip -9 -r "${DIRECTORY}.zip" -j "$TEMPDIR"

# Clean up
rm -rf "$TEMPDIR"

echo "Archive created: ${DIRECTORY}.zip"