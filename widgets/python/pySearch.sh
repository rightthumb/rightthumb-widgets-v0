#!/bin/bash

# Define usage function
usage() {
	echo "Usage: $0 --search <term> [--print]"
	exit 1
}

# Parse arguments
SEARCH_TERM=""
PRINT_LINES=false

while [[ $# -gt 0 ]]; do
	case "$1" in
		--search)
			SEARCH_TERM="$2"
			shift 2
			;;
		--print)
			PRINT_LINES=true
			shift
			;;
		*)
			usage
			;;
	esac
done

# Ensure a search term is provided
if [[ -z "$SEARCH_TERM" ]]; then
	usage
fi

# Get the directory where the script is executed
directory="$(pwd)"

# Initialize an array to store filenames with matches
matching_files=()

# Search Python files in the directory (non-recursively)
for file in "$directory"/*.py; do
	# Skip if no Python files are found
	[ -e "$file" ] || continue

	# Check if the file contains the search term (ignoring lines with # before the term)
	if grep -q "^[^#]*\b$SEARCH_TERM\b" "$file"; then
		relative_file="${file#$directory/}"
		matching_files+=("$relative_file")

		if $PRINT_LINES; then
			echo "$relative_file:"
			# Print matching lines, excluding those with # before the term
			grep "^[^#]*\b$SEARCH_TERM\b" "$file" | sed 's/^\s*//;s/^/\t/'
			echo
		fi
	fi
done

# Print the list of filenames if --print is not specified
if ! $PRINT_LINES; then
	for file in "${matching_files[@]}"; do
		echo "$file"
	done
fi