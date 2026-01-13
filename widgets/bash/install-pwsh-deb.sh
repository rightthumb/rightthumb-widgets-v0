#!/bin/bash

# Script to install PowerShell on Ubuntu

# Download the Microsoft repository GPG keys
wget -q "https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/packages-microsoft-prod.deb"

# Register the Microsoft repository GPG keys
sudo dpkg -i packages-microsoft-prod.deb

# Update the package list
sudo apt-get update

# Install PowerShell
sudo apt-get install -y powershell

# Clean up
rm packages-microsoft-prod.deb

echo "PowerShell has been installed successfully."
