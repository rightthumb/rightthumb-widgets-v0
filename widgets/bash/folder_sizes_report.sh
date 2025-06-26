#!/bin/bash

# Define the output file
output_file="folder_sizes_report.txt"

# Create or overwrite the output file
> "$output_file"

# Loop through all directories in the current directory
for dir in */; do
	dir_name=$(basename "$dir")
	size=$(du -sh "$dir" | cut -f1)
	
	# Append the folder name and size to the output file
	echo "Folder: $dir_name, Size: $size" >> "$output_file"
done

echo "Report generated in $output_file"