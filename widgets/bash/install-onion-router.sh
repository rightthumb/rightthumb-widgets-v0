#!/bin/bash

# Exit on any error
set -e

# Adding the Tor Project's GPG key and repository
echo "Adding Tor Project repository..."
curl -s https://deb.torproject.org/torproject.org/A3C4F0F979CAA22CDBA8F512EE8CBC9E886DDD89.asc | sudo gpg --dearmor -o /usr/share/keyrings/tor-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/tor-archive-keyring.gpg] https://deb.torproject.org/torproject.org $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/tor.list > /dev/null

# Update and install Tor, keyring, and torsocks
echo "Updating package list and installing Tor..."
sudo apt update
sudo apt install -y tor deb.torproject.org-keyring torsocks

# Starting Tor and enabling it at boot
echo "Starting and enabling Tor service..."
sudo systemctl start tor
sudo systemctl enable tor

# Optional: Download and install Tor Browser
read -p "Do you want to install Tor Browser? [y/N] " choice
case "$choice" in
  y|Y ) 
	echo "Downloading and extracting Tor Browser..."
	curl -LO https://www.torproject.org/download/tor/
	tar -xvf tor-browser-linux64-*_en-US.tar.xz
	echo "Tor Browser is extracted. Navigate to 'tor-browser_en-US' directory and run './start-tor-browser.desktop' to start it."
	;;
  * ) 
	echo "Skipping Tor Browser installation."
	;;
esac

echo "Tor setup is complete!"