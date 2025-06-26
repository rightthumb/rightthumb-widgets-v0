#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <username>"
    exit 1
fi

username="$1"

# Add NOPASSWD entry to /etc/sudoers
echo "$username ALL=(ALL) NOPASSWD:ALL" | sudo tee -a /etc/sudoers

# Create a /etc/sudoers.d/ file with NOPASSWD entry based on the username
echo "$username ALL=(ALL) NOPASSWD:ALL" | sudo tee "/etc/sudoers.d/$username"

echo "User $username added to sudoers with NOPASSWD setting and a corresponding /etc/sudoers.d/$username file created."




folder_path="/home/$username/public_html"

# Check if the folder exists
if [ -d "$folder_path" ]; then
    # If the folder exists, run the commands
    sudo chmod -R 777 "$folder_path"
    sudo chown -R "$username:$username" "$folder_path"
    echo "Folder permissions and ownership updated."
else
    echo "Folder not found: $folder_path"
fi