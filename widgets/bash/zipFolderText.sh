#!/bin/bash

# Check for valid arguments
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <source_directory> <output_zip_file>"
	exit 1
fi

# Input parameters
SOURCE_DIR="$1"
OUTPUT_ZIP="$2"
TMP_DIR="tmp_non_binary_zip_$(date +%s)"

# Create temporary directory
mkdir "$TMP_DIR"

# Function to process files
process_files() {
	local src="$1"
	local dest="$2"
	
	for file in "$src"/*; do
		if [ -d "$file" ]; then
			local subdir="${file#$SOURCE_DIR/}"
			mkdir -p "$dest/$subdir"
			process_files "$file" "$dest"
		else
			# Check if file is non-binary
			if ! file "$file" | grep -q "binary"; then
				local link_dest="${file#$SOURCE_DIR/}"
				ln -s "$(realpath "$file")" "$dest/$link_dest"
			fi
		fi
	done
}

# Process source directory
process_files "$SOURCE_DIR" "$TMP_DIR"

# Zip the temporary directory
zip -r "$OUTPUT_ZIP" "$TMP_DIR"

# Remove temporary directory
rm -rf "$TMP_DIR"

echo "Zipped non-binary files to $OUTPUT_ZIP"