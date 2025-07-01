#!/bin/bash

# Check for root privileges
if [ "$(id -u)" -ne 0 ]; then
  echo "Please run as root or use sudo."
  exit 1
fi

echo "Updating package lists..."
apt update

echo "Installing OpenSSH server..."
apt install -y openssh-server

echo "Configuring SSH server..."

# Ensure the SSH daemon config directory and file exist
mkdir -p /var/run/sshd

# Permit root login (optional, adjust if needed)
sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# Allow password authentication (optional, recommended to disable later if using keys)
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

# Change default SSH port if you want (optional)
# sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config

echo "Starting SSH server..."
service ssh start

echo "Enable SSH server to start on WSL boot (requires WSL 2 with systemd enabled or manual start)"

# Check if systemd is available (optional)
if pidof systemd >/dev/null; then
  systemctl enable ssh
  echo "SSH enabled to start on boot."
else
  echo "Systemd not detected. To start ssh automatically, add 'service ssh start' to your ~/.profile or WSL startup scripts."
fi

echo "SSH server setup complete. You can now SSH into this WSL instance."