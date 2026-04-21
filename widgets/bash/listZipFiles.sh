#!/bin/bash

# Function to list contents of a directory recursively
list_directory_contents() {
	local dir="$1"
	for item in "$dir"/*; do
		local relpath="${item#"$TMP_DIR/"}"
		echo "$relpath"
		if [[ -d "$item" ]]; then
			list_directory_contents "$item"
		elif [[ "$item" == *.zip ]]; then
			list_zip_contents_recursive "$item"
		fi
	done
}

# Function to list contents of a zip file recursively
list_zip_contents_recursive() {
	local zipfile="$1"
	local dir
	dir=$(mktemp -d)
	unzip -q "$zipfile" -d "$dir"
	list_directory_contents "$dir"
	rm -rf "$dir"
}

# Main execution starts here
TMP_DIR=$(mktemp -d)
trap 'rm -rf "$TMP_DIR"' EXIT
list_zip_contents_recursive "$1"