#!/bin/bash

# Check if the file exists
if [ ! -f "full_requre.txt" ]; then
  echo "File full_requre.txt not found!"
  exit 1
fi

# Read the file line by line
while read -r package; do
  echo "Installing $package"
  
  # Try to install the package
  if ! pip3 install "$package"; then
	echo "Failed to install $package" >> error_log.txt
  fi
done < full_requre.txt

# Check if there were any errors
if [ -f "error_log.txt" ]; then
  echo "Some packages failed to install. Check error_log.txt for details."
else
  echo "All packages were installed successfully."
fi