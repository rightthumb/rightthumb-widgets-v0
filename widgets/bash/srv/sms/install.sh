#!/bin/bash

# Exit script on error
set -e

# Update and install dependencies
echo "Updating package lists..."
sudo apt-get update
echo "Installing build essentials and libxml2-dev..."
sudo apt-get install -y build-essential libxml2-dev

# Download Kannel
echo "Downloading Kannel..."
wget http://www.kannel.org/download/1.4.4/gateway-1.4.4.tar.gz

# Extract the Kannel tarball
echo "Extracting Kannel..."
tar -xzf gateway-1.4.4.tar.gz

# Navigate into the Kannel directory
cd gateway-1.4.4

# Configure Kannel
echo "Configuring Kannel..."
./configure --prefix=/usr/local/kannel

# Compile Kannel
echo "Compiling Kannel..."
make

# Install Kannel
echo "Installing Kannel..."
sudo make install

# Cleanup downloaded files
cd ..
rm -rf gateway-1.4.4 gateway-1.4.4.tar.gz

echo "Kannel installation completed successfully."
echo "Please configure Kannel by editing the configuration files in /usr/local/kannel/etc/"