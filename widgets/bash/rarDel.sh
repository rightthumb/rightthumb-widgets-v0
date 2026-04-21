#!/bin/bash

# Loop through all directories in the current folder
for folder in */; do
	# Trim the trailing slash from the folder name
	foldername="${folder%/}"
	
	# Run micro_zip.sh on the folder
	$ww/widgets/bash/micro_zip.sh "${foldername}.rar" "${foldername}"

	# If the above command succeeds, remove the directory
	if [ $? -eq 0 ]; then
		rm -rf "${foldername}"
	else
		echo "Error processing ${foldername}. Skipping deletion."
	fi
done