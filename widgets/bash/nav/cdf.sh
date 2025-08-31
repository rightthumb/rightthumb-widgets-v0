#!/bin/bash

# Check if argument was provided
if [ -z "$1" ]; then
	# Read content of file into cdf_path
	read -r cdf_path < "$tt/file-open.last"
else
	cdf_path="$1"
fi

# Run command and redirect output to tmpf
$p popFile -f "$cdf_path" > "$tmpf0"

# Read content of tmpf into folder variable
read -r folder < "$tmpf0"

# Change directory and print its name
cd "$folder" || return 1
echo "$folder"
echo