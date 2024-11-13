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

# Step 1: Update and Install OpenVPN and Easy-RSA
echo "Installing OpenVPN and Easy-RSA..."
apt update
apt install -y openvpn easy-rsa curl

# Step 2: Get the Server's Public IP Address
SERVER_IP=$(curl -s ifconfig.me)
if [[ -z "$SERVER_IP" ]]; then
	echo "Unable to detect server's public IP. Please set SERVER_IP manually."
	exit 1
fi
echo "Detected server IP: $SERVER_IP"

# Step 3: Create a Password File for Authentication
echo "Creating password file..."
cat <<EOF > $PSW_FILE
user1 password1
user2 password2
EOF
chmod 600 $PSW_FILE
echo "Password file created at $PSW_FILE with sample users."

# Step 4: Set Up the Easy-RSA PKI
echo "Setting up PKI..."
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
./easyrsa init-pki
echo -e "\n" | ./easyrsa build-ca nopass
./easyrsa gen-req server nopass
./easyrsa sign-req server server <<EOF
yes
EOF
./easyrsa gen-dh
openvpn --genkey --secret ta.key

# Copy certificates and keys to OpenVPN directory
cp pki/ca.crt pki/issued/server.crt pki/private/server.key ta.key /etc/openvpn/
cp pki/dh.pem /etc/openvpn/dh2048.pem

# Step 5: Create the Authentication Script
echo "Creating authentication script..."
cat <<'EOF' > $CHECK_PSW_SCRIPT
#!/bin/bash
PSW_FILE="/etc/openvpn/psw-file"

# Read username and password from the file specified by $1
USER_NAME=$(head -n 1 "$1")
PASS_WORD=$(tail -n 1 "$1")

# Check credentials
CORRECT_CREDS=$(grep -E "^$USER_NAME $PASS_WORD$" $PSW_FILE)
if [ -n "$CORRECT_CREDS" ]; then
	exit 0  # Authentication success
else
	exit 1  # Authentication failure
fi
EOF

# Make the authentication script executable
chmod +x $CHECK_PSW_SCRIPT
echo "Authentication script created at $CHECK_PSW_SCRIPT."

# Step 6: Configure OpenVPN Server
echo "Configuring OpenVPN server..."
cat <<EOF > $SERVER_CONF
port 1194
proto udp
dev tun
ca /etc/openvpn/ca.crt
cert /etc/openvpn/server.crt
key /etc/openvpn/server.key
dh /etc/openvpn/dh2048.pem
auth SHA256
cipher AES-256-CBC
data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305:AES-256-CBC
tls-auth /etc/openvpn/ta.key 0
topology subnet
server 10.8.0.0 255.255.255.0
ifconfig-pool-persist /etc/openvpn/ipp.txt
push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 1.1.1.1"
push "dhcp-option DNS 1.0.0.1"
keepalive 10 120
persist-key
persist-tun
status /etc/openvpn/openvpn-status.log
log-append /var/log/openvpn.log
verb 3

# Enable username and password authentication
auth-user-pass-verify $CHECK_PSW_SCRIPT via-file
verify-client-cert none
username-as-common-name
EOF

# Step 7: Enable IP Forwarding and Configure Firewall
echo "Enabling IP forwarding and configuring firewall..."
sed -i '/net.ipv4.ip_forward=1/s/^#//g' /etc/sysctl.conf
sysctl -p
ufw allow 1194/udp
iptables -t nat -A POSTROUTING -s 10.8.0.0/24 -o eth0 -j MASQUERADE
iptables-save > /etc/iptables/rules.v4

# Step 8: Start and Enable OpenVPN Service
echo "Starting OpenVPN service..."
systemctl enable openvpn@server
systemctl start openvpn@server

# Step 9: Create Client Head Configuration
echo "Creating client head configuration at $CLIENT_HEAD..."
cat <<EOF > $CLIENT_HEAD
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
EOF

echo "OpenVPN setup with username and password authentication is complete."
echo "Client head configuration saved to $CLIENT_HEAD."
echo "To add users, edit $PSW_FILE in the format: username password"
echo "Client configurations should include 'auth-user-pass' to prompt for username and password."