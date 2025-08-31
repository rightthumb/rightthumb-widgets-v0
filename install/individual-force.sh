#!/bin/bash

# Check if a package name was provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <package_name>"
    exit 1
fi

# Assign the first argument to a variable for clarity
PACKAGE_NAME="$1"

# Force install or upgrade the package using pip3
echo "Attempting to install or upgrade $PACKAGE_NAME..."
pip3 install --upgrade --no-cache-dir "$PACKAGE_NAME"

echo "$PACKAGE_NAME installation or upgrade attempt complete."
