#!/bin/bash

echo "Fixing permissions in: $(pwd)"
echo "Running as: $(whoami)"

# Set directory permissions to 755
find . -type d -exec chmod 755 {} \;

# Set file permissions to 644
find . -type f -exec chmod 644 {} \;

# (Optional) Harden PHP files to 640
find . -type f -name "*.php" -exec chmod 640 {} \;

echo "Permissions fixed."