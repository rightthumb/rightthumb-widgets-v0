#!/bin/bash

# Define the path to the requirements file
REQUIREMENTS_FILE="../require.txt"

# Check if the requirements file exists
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Attempting to install packages from $REQUIREMENTS_FILE..."
    while IFS= read -r package; do
        echo "Installing package: $package"
        pip3 install --user "$package" --break-system-packages
    done < "$REQUIREMENTS_FILE"
    echo "All packages have been attempted to install."
else
    echo "Requirements file does not exist at $REQUIREMENTS_FILE."
fi
