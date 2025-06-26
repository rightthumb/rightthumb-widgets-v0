#!/bin/bash

# Define the path to the requirements file
REQUIREMENTS_FILE="../require.txt"

# Check if the requirements file exists
if [ -f "$REQUIREMENTS_FILE" ]; then
	echo "Attempting to install/update packages from $REQUIREMENTS_FILE with forceful options..."
	while IFS= read -r package; do
		echo "Processing package: $package"
		
		pip3 install "$package"
		
	done < "$REQUIREMENTS_FILE"
	echo "Forceful package installation/update attempt complete."
else
	echo "Requirements file does not exist at $REQUIREMENTS_FILE."
fi