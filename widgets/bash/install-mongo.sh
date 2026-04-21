#!/bin/bash

# Ensure the script is executed with superuser privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root"
   exit 1
fi

# Import the MongoDB public GPG Key
wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -

# Check for the existence of the file /etc/apt/sources.list.d/mongodb-org-5.0.list
# and create it if it doesn't exist
if [ ! -f /etc/apt/sources.list.d/mongodb-org-5.0.list ]; then
    echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list
fi

# Update the package database
apt-get update

# Install MongoDB packages
apt-get install -y mongodb-org

# Start MongoDB and enable it to start on boot
systemctl start mongod
systemctl enable mongod

# Display a completion message
echo "MongoDB installation completed"
