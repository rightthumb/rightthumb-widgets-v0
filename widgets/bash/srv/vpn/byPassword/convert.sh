#!/bin/bash

# Variables
PSW_FILE="/etc/openvpn/psw-file"
CHECK_PSW_SCRIPT="/etc/openvpn/check_psw.sh"
SERVER_CONF="/etc/openvpn/server.conf"
CLIENT_HEAD="/opt/client_head.ovpn"

# Ensure script is run with sudo privileges
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root or with sudo privileges."
   exit 1
fi

# Step 1: Create a Password File for Authentication
echo "Setting up password file..."
sudo bash -c "cat <<EOF > $PSW_FILE
user1 password1
user2 password2
EOF"
sudo chmod 600 $PSW_FILE
echo "Password file created at $PSW_FILE with sample users."

# Step 2: Create the Authentication Script
echo "Creating authentication script..."
sudo bash -c "cat <<'EOF' > $CHECK_PSW_SCRIPT
#!/bin/bash
PSW_FILE="/etc/openvpn/psw-file"

# Read username and password from the file specified by \$1
USER_NAME=\$(head -n 1 "\$1")
PASS_WORD=\$(tail -n 1 "\$1")

# Check credentials
CORRECT_CREDS=\$(grep -E "^\\\$USER_NAME \\\$PASS_WORD\$" \$PSW_FILE)
if [ -n "\$CORRECT_CREDS" ]; then
	exit 0  # Authentication success
else
	exit 1  # Authentication failure
fi
EOF"

# Make the authentication script executable
sudo chmod +x $CHECK_PSW_SCRIPT
echo "Authentication script created at $CHECK_PSW_SCRIPT."

# Step 3: Modify OpenVPN Server Configuration
echo "Configuring OpenVPN server for password authentication..."
if grep -q "auth-user-pass-verify" $SERVER_CONF; then
	sudo sed -i '/auth-user-pass-verify/d' $SERVER_CONF
fi

# Add the necessary lines for username/password authentication
sudo bash -c "cat <<EOF >> $SERVER_CONF

# Enable username and password authentication
auth-user-pass-verify $CHECK_PSW_SCRIPT via-file
verify-client-cert none
username-as-common-name
EOF"

echo "OpenVPN server configuration updated."

# Step 4: Restart OpenVPN Service
echo "Restarting OpenVPN service..."
sudo systemctl restart openvpn@server

# Step 5: Get the Server's Public IP Address
SERVER_IP=$(curl -s ifconfig.me)
if [[ -z "$SERVER_IP" ]]; then
	echo "Unable to detect server's public IP. Please set SERVER_IP manually."
	exit 1
fi
echo "Detected server IP: $SERVER_IP"

# Step 6: Create Client Head Configuration
echo "Creating client head configuration at $CLIENT_HEAD..."
sudo bash -c "cat <<EOF > $CLIENT_HEAD
client
dev tun
proto udp
remote $SERVER_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth SHA256
cipher AES-256-CBC
key-direction 1
auth-user-pass
verb 3
EOF"

echo "Conversion to password-based OpenVPN server is complete."
echo "Client head configuration saved to $CLIENT_HEAD."
echo "To add users, edit $PSW_FILE in the format: username password"
echo "Client configurations should include 'auth-user-pass' to prompt for username and password."