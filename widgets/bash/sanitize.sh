#!/bin/bash

# Usage:
# ./sanitize.sh secret1 secret2 anotherSecret ...

if [ "$#" -eq 0 ]; then
	echo "Usage: $0 string1 string2 ..."
	echo "Removes all given strings from files in current directory recursively."
	exit 1
fi

# Loop over all files recursively (excluding binary files and the script itself)
find . -type f ! -name "$(basename "$0")" | while read -r file; do
	# Skip binary files
	if file "$file" | grep -qE 'binary'; then
		continue
	fi

	modified=false

	tmpfile="$(mktemp)"
	cp "$file" "$tmpfile"

	for str in "$@"; do
		if grep -qF "$str" "$tmpfile"; then
			sed -i "s|$str||g" "$tmpfile"
			modified=true
		fi
	done

	if [ "$modified" = true ]; then
		mv "$tmpfile" "$file"
		echo "Sanitized: $file"
	else
		rm "$tmpfile"
	fi
done