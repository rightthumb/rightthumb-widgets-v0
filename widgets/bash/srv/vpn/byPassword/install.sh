#!/bin/bash

# Update and install OpenVPN
sudo apt-get update
sudo apt-get install -y openvpn easy-rsa curl

# Set up the Easy-RSA environment
make-cadir ~/openvpn-ca
cd ~/openvpn-ca
source vars
./clean-all
./build-ca --batch

# Build the server certificate, key, and encryption files
./build-key-server --batch server
./build-dh
openvpn --genkey --secret keys/ta.key

# Copy server certificates and keys
sudo cp ~/openvpn-ca/keys/{server.crt,server.key,ca.crt,dh2048.pem,ta.key} /etc/openvpn

# Download the custom password check script
sudo curl -o /etc/openvpn/check_user.sh https://raw.githubusercontent.com/rightthumb/rightthumb-widgets-v0/refs/heads/main/widgets/bash/srv/vpn/byPassword/login_script.sh
sudo chmod +x /etc/openvpn/check_user.sh

# Generate server configuration file
cat <<EOF | sudo tee /etc/openvpn/server.conf
port 1194
proto tcp
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
client-to-client
keepalive 10 120
cipher AES-256-CBC
user nobody
group nogroup
persist-key
persist-tun
status openvpn-status.log
verb 3

# Enable external authentication script
auth-user-pass-verify /etc/openvpn/check_user.sh via-file
script-security 3
EOF

# Enable IP forwarding
echo 1 | sudo tee /proc/sys/net/ipv4/ip_forward
sudo sed -i 's/#net.ipv4.ip_forward=1/net.ipv4.ip_forward=1/' /etc/sysctl.conf
sudo sysctl -p

# Configure firewall rules
sudo ufw allow 1194/tcp
sudo ufw allow OpenSSH
sudo ufw disable
sudo ufw enable

# Start and enable OpenVPN service
sudo systemctl start openvpn@server
sudo systemctl enable openvpn@server

# Get the public IP address
PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)

# Create the client configuration header
cat <<EOF | sudo tee /opt/client_head.ovpn
client
dev tun
proto tcp
remote $PUBLIC_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth-user-pass
auth SHA256
cipher AES-256-CBC
tls-auth ta.key 1
verb 3
EOF

# Copy necessary keys and certificates to /opt for client configuration
sudo cp /etc/openvpn/ca.crt /etc/openvpn/ta.key /opt/

echo "OpenVPN installation complete. Client header configuration created at /opt/client_head.ovpn with server IP $PUBLIC_IP."