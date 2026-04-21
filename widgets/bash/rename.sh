#!/bin/bash

# Check if directory is provided
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 <directory_path>"
	exit 1
fi

directory="$1"

# Check if provided path is a directory
if [ ! -d "$directory" ]; then
	echo "Error: The provided path is not a directory."
	exit 1
fi

# Loop through each file in the directory
find "$directory" -type f | while read -r file; do
	# Extract the directory and filename
	dir=$(dirname "$file")
	base=$(basename "$file")

	# Remove the trailing underscore
	new_name="${base%_}"

	# Rename the file
	if [ "$base" != "$new_name" ]; then
		mv -n "$file" "$dir/$new_name"
	fi
done

echo "Renaming process completed!"
