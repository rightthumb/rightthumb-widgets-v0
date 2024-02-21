#!/bin/bash

# Update package index
sudo apt update

# Install vsftpd
sudo apt install -y vsftpd

# Start vsftpd service
sudo systemctl start vsftpd

# Enable vsftpd service to start on boot
sudo systemctl enable vsftpd

# Print status message
echo "vsftpd installed and started successfully."