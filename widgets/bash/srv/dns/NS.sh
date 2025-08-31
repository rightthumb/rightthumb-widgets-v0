#!/bin/bash

# Check if the domain argument is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <domain>"
	exit 1
fi

domain="$1"

# Execute dig command, filter out comment lines, and store the result in a variable
records=$(dig +nocomments "$domain" NS | grep -v '^;')

# Iterate over each line
while IFS= read -r line; do
	# Split the line by whitespace into an array
	read -ra fields <<< "$line"

	# Check if the second field is "0" (TTL field)
	if [ "${fields[1]}" = "0" ]; then
		# Replace " 0 " with "  86400 " in the TTL field
		fields[1]="86400"
	fi

	# Print the modified line
	echo "${fields[@]}"
done <<< "$records"