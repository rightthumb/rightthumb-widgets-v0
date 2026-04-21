#!/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 <username>"
	exit 1
fi

username="$1"

# Remove user from /etc/sudoers
sudo sed -i "/^$username /d" /etc/sudoers

# Remove /etc/sudoers.d/$username file if it exists
sudo rm -f "/etc/sudoers.d/$username"

echo "User $username removed from sudoers, and /etc/sudoers.d/$username deleted if it existed."





folder_path="/home/$username/public_html"

# Check if the folder exists
if [ -d "$folder_path" ]; then
	# If the folder exists, run the commands
	sudo chmod -R 755 "$folder_path"
	echo "Folder permissions and ownership updated."
else
	echo "Folder not found: $folder_path"
fi