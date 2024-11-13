#!/bin/bash

# Check if client name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <client-name>"
    exit 1
fi

CLIENT_NAME=$1
OUTPUT_DIR=/opt/clients
CLIENT_CONFIG=$OUTPUT_DIR/${CLIENT_NAME}.ovpn

# Ensure output directory exists
sudo mkdir -p $OUTPUT_DIR

# Navigate to Easy-RSA directory
cd ~/openvpn-ca
source vars

# Build the client certificate and key
./build-key --batch $CLIENT_NAME

# Create the client configuration file
echo "Generating client configuration for $CLIENT_NAME..."

# Get the server's public IP address
PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)

cat <<EOF | sudo tee $CLIENT_CONFIG
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
tls-auth [inline] 1
verb 3
<ca>
EOF

# Embed the CA certificate
sudo cat /etc/openvpn/ca.crt | sudo tee -a $CLIENT_CONFIG

cat <<EOF | sudo tee -a $CLIENT_CONFIG
</ca>
<cert>
EOF

# Embed the client certificate
sudo cat ~/openvpn-ca/keys/${CLIENT_NAME}.crt | sudo tee -a $CLIENT_CONFIG

cat <<EOF | sudo tee -a $CLIENT_CONFIG
</cert>
<key>
EOF

# Embed the client key
sudo cat ~/openvpn-ca/keys/${CLIENT_NAME}.key | sudo tee -a $CLIENT_CONFIG

cat <<EOF | sudo tee -a $CLIENT_CONFIG
</key>
<tls-auth>
EOF

# Embed the TLS key
sudo cat /etc/openvpn/ta.key | sudo tee -a $CLIENT_CONFIG

cat <<EOF | sudo tee -a $CLIENT_CONFIG
</tls-auth>
EOF

echo "Client configuration for $CLIENT_NAME created at $CLIENT_CONFIG"
