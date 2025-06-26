#!/bin/bash

# OpenVAS Installation Script for AlmaLinux 9
# Author: ChatGPT
# Version: 1.0

echo "Starting OpenVAS (GVM) Installation on AlmaLinux 9..."

# Ensure the script is run as root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root. Use sudo ./install-openvas.sh"
   exit 1
fi

# Enable Required Repositories
echo "Enabling required repositories..."
dnf config-manager --set-enabled crb
dnf install -y epel-release dnf-plugins-core

# Install PostgreSQL
echo "Installing PostgreSQL..."
dnf install -y postgresql-server postgresql-contrib
postgresql-setup --initdb
systemctl enable --now postgresql

# Install Required Dependencies
echo "Installing dependencies..."
dnf install -y \
	rsync curl wget net-tools bzip2 \
	glibc-static psmisc bison flex redis \
	cmake gcc-c++ gpgme-devel libmicrohttpd-devel \
	libxml2-devel libxslt-devel gnupg gnutls-utils \
	perl perl-base tar python3-pip python3-paramiko \
	python3-psutil python3-setuptools python3-venv \
	openldap-devel

# Install Greenbone Vulnerability Management (GVM)
echo "Installing Greenbone Vulnerability Management..."
dnf install -y gvm gvm-tools gvmd openvas-scanner greenbone-security-assistant

# Set Up GVM (OpenVAS)
echo "Initializing GVM..."
gvm-setup

# Start Services
echo "Starting GVM services..."
systemctl enable --now gvmd gsad ospd-openvas redis

# Check Setup
echo "Checking GVM Setup..."
gvm-check-setup

# Get Admin Password
echo "Fetching GVM Admin Password..."
PASSWORD_FILE="/var/lib/gvm/users/admin/password"
if [ -f "$PASSWORD_FILE" ]; then
	echo "Admin Password: $(cat $PASSWORD_FILE)"
else
	echo "Failed to retrieve admin password. Run 'gvm-setup' manually if needed."
fi

echo "OpenVAS Installation Completed!"
echo "Access the Web UI at: https://localhost:9392"