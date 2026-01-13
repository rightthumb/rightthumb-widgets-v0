#!/bin/bash
# Script to enable and disable services

SERVICE="ssh"

# Enable the service
sudo systemctl enable "$SERVICE"

# Disable the service
sudo systemctl disable "$SERVICE"
