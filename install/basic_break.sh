#!/bin/bash

# Read each line from the requirements file
while IFS= read -r package || [[ -n "$package" ]]; do
  # Attempt to install the package, continue on error
  pip3 install --upgrade --break-system-packages "$package" || echo "Failed to install $package, continuing..."
done < "../require.txt"