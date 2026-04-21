#!/bin/bash
# Script to automate system updates

echo "Starting system update..."

# Update package lists
sudo apt update

# Upgrade installed packages
sudo apt upgrade -y

# Clean up unnecessary files
sudo apt autoremove -y
sudo apt clean

echo "System update completed!"
