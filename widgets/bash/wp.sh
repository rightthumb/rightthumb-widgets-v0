#!/bin/bash

# Install WP-CLI for managing WordPress installations via the command line

# Download WP-CLI
echo "Downloading WP-CLI..."
curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-cli.phar

# Check if the WP-CLI.phar file works
php wp-cli.phar --info

# Make WP-CLI executable
chmod +x wp-cli.phar

# Move WP-CLI to a global location
sudo mv wp-cli.phar /usr/local/bin/wp

# Check if WP-CLI is properly installed
echo "Verifying WP-CLI installation..."
wp --info

echo "WP-CLI installation completed."