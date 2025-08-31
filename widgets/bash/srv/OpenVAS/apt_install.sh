#!/bin/bash

# OpenVAS (Greenbone Vulnerability Management) Installation Script for Ubuntu 22.04+
# Author: ChatGPT
# Version: 1.0

echo "Starting OpenVAS (GVM) Installation on Ubuntu..."

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Use sudo ./install-openvas.sh"
   exit 1
fi

# Update System
echo "Updating system packages..."
apt update && apt upgrade -y

# Install Required Dependencies
echo "Installing required dependencies..."
apt install -y \
	software-properties-common apt-transport-https curl wget \
	postgresql postgresql-contrib postgresql-server-dev-all \
	gpg gpg-agent cmake pkg-config gcc g++ bison flex \
	libglib2.0-dev libgnutls28-dev libpcap-dev libsqlite3-dev \
	libgpgme-dev libjson-glib-dev libmicrohttpd-dev \
	libnet1-dev libssh-gcrypt-dev redis-server \
	libldap2-dev libxml2-dev libxslt1-dev python3 python3-pip python3-setuptools

# Install Greenbone Vulnerability Management (GVM)
echo "Installing OpenVAS / GVM..."
apt install -y gvm

# Initialize the GVM database and update feeds
echo "Setting up GVM..."
gvm-setup

# Start Services
echo "Starting OpenVAS services..."
systemctl enable --now postgresql
systemctl enable --now gsad gvmd ospd-openvas redis-server

# Check if GVM is properly set up
echo "Checking GVM setup..."
gvm-check-setup

# Get Admin Password
echo "Fetching GVM Admin Password..."
PASSWORD_FILE="/var/lib/gvm/users/admin/password"
if [ -f "$PASSWORD_FILE" ]; then
	echo "Admin Password: $(cat $PASSWORD_FILE)"
else
	echo "Failed to retrieve admin password. Run 'gvm-setup' manually if needed."
fi

echo "✅ OpenVAS Installation Completed!"
echo "🌍 Access the Web UI at: https://localhost:9392"