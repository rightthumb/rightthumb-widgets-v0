#!/bin/bash

# Path to WebDAV user file
WEB_DAV_USER_FILE="/etc/apache2/webdav.users"

# Check for correct number of arguments
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <username> <password>"
    exit 1
fi

# Assign arguments to variables
username="$1"
password="$2"

# Ensure the user file exists
if [ ! -f "$WEB_DAV_USER_FILE" ]; then
    echo "Creating WebDAV user file at $WEB_DAV_USER_FILE"
    touch "$WEB_DAV_USER_FILE"
    chmod 640 "$WEB_DAV_USER_FILE"
    chown www-data:www-data "$WEB_DAV_USER_FILE"
fi

# Check if user already exists
if grep -q "^$username:" "$WEB_DAV_USER_FILE"; then
    echo "User '$username' already exists. Updating password..."
else
    echo "Adding new user '$username'..."
fi

# Add or update user with the provided password
htpasswd -bB "$WEB_DAV_USER_FILE" "$username" "$password"

# Restart Apache to apply changes
echo "Restarting Apache to apply changes..."
systemctl restart apache2

echo "User '$username' has been added/updated successfully."

