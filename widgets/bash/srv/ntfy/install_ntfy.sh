#!/bin/bash

# Update package list and install prerequisites
echo "Updating packages and installing prerequisites..."
sudo apt update -y
sudo apt install -y curl

# Define the latest release URL for ntfy
RELEASE_URL="https://github.com/binwiederhier/ntfy/releases/latest/download/ntfy_$(uname -m).deb"

# Download ntfy .deb package
echo "Downloading ntfy package..."
curl -Lo ntfy.deb $RELEASE_URL

# Install ntfy
echo "Installing ntfy..."
sudo dpkg -i ntfy.deb

# Clean up
rm ntfy.deb

# Set up a systemd service
echo "Setting up ntfy as a systemd service..."

sudo tee /etc/systemd/system/ntfy.service > /dev/null <<EOL
[Unit]
Description=ntfy push notification service
After=network.target

[Service]
ExecStart=/usr/bin/ntfy serve
Restart=on-failure
User=$USER

[Install]
WantedBy=multi-user.target
EOL

# Reload systemd, enable, and start the ntfy service
sudo systemctl daemon-reload
sudo systemctl enable ntfy.service
sudo systemctl start ntfy.service

echo "ntfy installation complete. Service is running!"