#!/bin/bash

while IFS= read -r line; do
	# Strip leading and trailing whitespaces
	line=$(echo "$line" | sed 's/^[ \t]*//;s/[ \t]*$//')
	
	# Check if the line is non-blank
	if [ -n "$line" ]; then
		# If the directory does not exist, create it
		if [ ! -d "$line" ]; then
			mkdir -p "$line"
		fi
	fi
done