#!/bin/bash
# Script: firstline.sh
# Usage: ./firstline.sh /path/to/folder

FOLDER=${1:-.}   # default to current directory if none given

for file in "$FOLDER"/*.py; do
	if [ -f "$file" ]; then
		echo -n "$file: "
		head -n 1 "$file"
	fi
done