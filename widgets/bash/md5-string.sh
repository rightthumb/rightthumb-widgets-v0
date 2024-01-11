#!/bin/bash

# Check if a string is provided
if [ $# -eq 0 ]; then
	echo "No string provided. Usage: $0 <string>"
	exit 1
fi

# Read the string from the argument
input_string=$1

# Convert the string to MD5 hash
echo -n $input_string | md5sum | awk '{ print $1 }'