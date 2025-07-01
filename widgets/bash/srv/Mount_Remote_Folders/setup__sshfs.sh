#!/bin/bash

# Multi-OS installer for SSHFS and SSH server/client tools
# Saves usage instructions and mount info to /opt/Mount_Remote_Folder.md

set -e

INSTALL_PKGS=""
PM=""

echo "Detecting package manager..."

if command -v apt-get >/dev/null 2>&1; then
	PM="apt"
	INSTALL_PKGS="sshfs openssh-client openssh-server"
elif command -v dnf >/dev/null 2>&1; then
	PM="dnf"
	INSTALL_PKGS="sshfs openssh-clients openssh-server"
elif command -v yum >/dev/null 2>&1; then
	PM="yum"
	INSTALL_PKGS="sshfs openssh-clients openssh-server"
elif command -v pacman >/dev/null 2>&1; then
	PM="pacman"
	INSTALL_PKGS="sshfs openssh"
elif command -v zypper >/dev/null 2>&1; then
	PM="zypper"
	INSTALL_PKGS="sshfs openssh"
elif command -v apk >/dev/null 2>&1; then
	PM="apk"
	INSTALL_PKGS="sshfs openssh"
else
	echo "Unsupported package manager! Please install sshfs and openssh manually."
	exit 1
fi

echo "Using package manager: $PM"
echo "Installing packages: $INSTALL_PKGS"

case "$PM" in
	apt)
		sudo apt-get update
		sudo apt-get install -y $INSTALL_PKGS
		;;
	dnf)
		sudo dnf install -y $INSTALL_PKGS
		;;
	yum)
		sudo yum install -y $INSTALL_PKGS
		;;
	pacman)
		sudo pacman -Sy --noconfirm $INSTALL_PKGS
		;;
	zypper)
		sudo zypper install -y $INSTALL_PKGS
		;;
	apk)
		sudo apk add --no-cache $INSTALL_PKGS
		;;
esac

echo "Packages installed successfully."

# Enable and start sshd service if exists
if command -v systemctl >/dev/null 2>&1; then
	if systemctl list-unit-files | grep -q sshd.service; then
		echo "Enabling and starting sshd service..."
		sudo systemctl enable sshd.service
		sudo systemctl start sshd.service
	elif systemctl list-unit-files | grep -q ssh.service; then
		echo "Enabling and starting ssh service..."
		sudo systemctl enable ssh.service
		sudo systemctl start ssh.service
	else
		echo "No sshd or ssh systemd service found. Please start sshd manually."
	fi
else
	echo "Systemd not found. Please start sshd manually."
fi

# Write usage instructions and mount help to /opt/Mount_Remote_Folder.md

HELP_FILE="/opt/Mount_Remote_Folder.md"
sudo tee $HELP_FILE > /dev/null << 'EOF'
# Remote Folder Mounting and SSHFS Usage Guide

## Prerequisites
- SSH server running on the machine where folder is located.
- SSHFS installed on client machine to mount remote folder.

## Mount Remote Folder (example)
```bash
sshfs -p <port> <user>@<host>:/path/to/remote/folder /path/to/local/mountpoint -o allow_other,nonempty
```
## Unmount Remote Folder
```bash
fusermount -u /path/to/local/mountpoint
```
EOF

echo "Mounting instructions saved to $HELP_FILE"