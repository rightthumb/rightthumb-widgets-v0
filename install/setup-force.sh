#!/bin/bash

# Define the path to the requirements file
REQUIREMENTS_FILE="../require.txt"

# Check if the requirements file exists
if [ -f "$REQUIREMENTS_FILE" ]; then
	echo "Attempting to install/update packages from $REQUIREMENTS_FILE with forceful options..."
	while IFS= read -r package; do
		echo "Processing package: $package"
		
		# Attempt to forcefully install/update the package using a combination of options
		# --user: Install to the user directory
		# --upgrade: Upgrade the package to the latest version if it's already installed
		# --no-cache-dir: Avoid using the cache to ensure the latest package is fetched
		# --break-system-packages: Override the protections against modifying system-managed Python environments
		# pip3 install --user --upgrade --no-cache-dir --break-system-packages "$package"
                pip3 install --upgrade --no-cache-dir --break-system-packages "$package"
		
	done < "$REQUIREMENTS_FILE"
	echo "Forceful package installation/update attempt complete."
else
	echo "Requirements file does not exist at $REQUIREMENTS_FILE."
fi
