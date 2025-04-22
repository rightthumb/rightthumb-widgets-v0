#!/bin/bash

# OpenVPN Installation and Configuration Script

# Ensure the script is run with superuser privileges
if [[ "$EUID" -ne 0 ]]; then
	echo "This script must be run as root. Use sudo."
	exit 1
fi

echo "Starting OpenVPN installation..."

# Install required packages
apt-get update
apt-get install -y openvpn easy-rsa curl ufw

# Directories and variables
EASYRSA_DIR=~/openvpn-ca
OPENVPN_DIR=/etc/openvpn
LOG_DIR=/var/log/openvpn
PSW_FILE="$OPENVPN_DIR/psw-file"
AUTH_SCRIPT="$OPENVPN_DIR/check_user.sh"
SERVER_CONF="$OPENVPN_DIR/server.conf"

# Ensure Easy-RSA directory exists and is initialized
if [ ! -d "$EASYRSA_DIR" ]; then
	echo "Initializing Easy-RSA..."
	make-cadir "$EASYRSA_DIR"
	cd "$EASYRSA_DIR" || exit
	./easyrsa init-pki
	./easyrsa build-ca nopass
	./easyrsa gen-req server nopass
	./easyrsa sign-req server server
	./easyrsa gen-dh
	openvpn --genkey secret "$EASYRSA_DIR/ta.key"
else
	echo "Easy-RSA directory already exists. Skipping initialization."
fi

# Ensure required files are in place
echo "Copying certificates and keys..."
mkdir -p "$OPENVPN_DIR"
cp -u "$EASYRSA_DIR/pki/ca.crt" "$OPENVPN_DIR/"
cp -u "$EASYRSA_DIR/pki/issued/server.crt" "$OPENVPN_DIR/"
cp -u "$EASYRSA_DIR/pki/private/server.key" "$OPENVPN_DIR/"
cp -u "$EASYRSA_DIR/pki/dh.pem" "$OPENVPN_DIR/dh2048.pem"
cp -u "$EASYRSA_DIR/ta.key" "$OPENVPN_DIR/"

# Create or verify the password file
if [ ! -f "$PSW_FILE" ]; then
	echo "Creating password file at $PSW_FILE..."
	touch "$PSW_FILE"
	chmod 600 "$PSW_FILE"
	echo "# Format: username password" >> "$PSW_FILE"
	echo "testuser testpassword" >> "$PSW_FILE" # Example credentials
else
	echo "Password file already exists. Skipping."
fi

# Download the authentication script if missing
if [ ! -f "$AUTH_SCRIPT" ]; then
	echo "Downloading authentication script..."
	curl -o "$AUTH_SCRIPT" https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/refs/heads/main/widgets/bash/srv/vpn/byPassword/login_script.sh
	chmod +x "$AUTH_SCRIPT"
else
	echo "Authentication script already exists. Skipping."
fi

# Generate server configuration
if [ ! -f "$SERVER_CONF" ]; then
	echo "Creating server configuration..."
	cat > "$SERVER_CONF" <<EOF
port 1194
proto udp
dev tun
ca ca.crt
cert server.crt
key server.key
dh dh2048.pem
auth SHA256
tls-auth ta.key 0
topology subnet
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist ipp.txt
keepalive 10 120
persist-key
persist-tun
status $LOG_DIR/openvpn-status.log
log $LOG_DIR/openvpn.log
verb 3

# Enable external authentication script
auth-user-pass-verify $AUTH_SCRIPT via-file
script-security 3
EOF
else
	echo "Server configuration already exists. Skipping."
fi

# Setup logging directory
if [ ! -d "$LOG_DIR" ]; then
	echo "Setting up log directory..."
	mkdir -p "$LOG_DIR"
	chmod 750 "$LOG_DIR"
	touch "$LOG_DIR/openvpn-status.log"
	touch "$LOG_DIR/openvpn.log"
	chmod 640 "$LOG_DIR/openvpn-status.log"
	chmod 640 "$LOG_DIR/openvpn.log"
fi

# Enable IP forwarding and setup NAT
echo "Configuring IP forwarding and NAT..."
echo 1 > /proc/sys/net/ipv4/ip_forward
sed -i '/^#net.ipv4.ip_forward=1/c\net.ipv4.ip_forward=1' /etc/sysctl.conf
sysctl -p

# Configure UFW
echo "Setting up UFW rules..."
ufw allow 1194/udp
ufw allow OpenSSH
ufw disable
ufw enable

# Start and enable OpenVPN service
echo "Starting OpenVPN service..."
systemctl enable openvpn@server
systemctl start openvpn@server

# Verify service status
if systemctl is-active --quiet openvpn@server; then
	echo "OpenVPN server is running successfully."
else
	echo "OpenVPN server failed to start. Check logs for details."
fi

# Output relevant details
echo "Installation complete! Relevant files and directories:"
echo "-------------------------------------------------------"
echo "Server configuration: $SERVER_CONF"
echo "Password file (for user authentication): $PSW_FILE"
echo "Authentication script: $AUTH_SCRIPT"
echo "Log directory: $LOG_DIR"
echo "Certificates and keys directory: $OPENVPN_DIR"
echo "Easy-RSA directory: $EASYRSA_DIR"
echo "-------------------------------------------------------"
echo "To add a new client, use your client generator script."