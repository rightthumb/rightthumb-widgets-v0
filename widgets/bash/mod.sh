#!/bin/bash

# Check if a file name is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <filename>"
	exit 1
fi

# Check if the file exists
if [ ! -f "$1" ]; then
	echo "File not found: $1"
	exit 1
fi

# Get the modification date of the file
mod_date=$(stat -c "%y" "$1")
echo "Modification date of $1: $mod_date"