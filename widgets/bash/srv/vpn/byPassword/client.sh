#!/bin/bash

# Check if a client name is provided
if [ -z "$1" ]; then
	echo "Usage: $0 <client-name>"
	exit 1
fi

CLIENT_NAME=$1
OUTPUT_BASE_DIR=/opt/clients
CLIENT_DIR=$OUTPUT_BASE_DIR/$CLIENT_NAME
CLIENT_CONFIG=$CLIENT_DIR/${CLIENT_NAME}.ovpn

# Easy-RSA directory
EASYRSA_DIR=~/openvpn-ca

# Ensure the output directory for the client exists
sudo mkdir -p "$CLIENT_DIR"

# Navigate to the Easy-RSA directory
cd "$EASYRSA_DIR" || { echo "Easy-RSA directory not found: $EASYRSA_DIR"; exit 1; }

# Initialize PKI if not already initialized
if [ ! -d "$EASYRSA_DIR/pki" ]; then
	echo "Initializing PKI..."
	./easyrsa init-pki
	./easyrsa build-ca nopass
fi

# Generate the server certificates and keys if missing
if [ ! -f "$EASYRSA_DIR/pki/private/server.key" ]; then
	echo "Generating server certificate and key..."
	./easyrsa gen-req server nopass
	./easyrsa sign-req server server
	./easyrsa gen-dh
	openvpn --genkey secret "$EASYRSA_DIR/pki/ta.key"
fi

# Generate the client certificate and key if they do not exist
if [[ ! -f "$EASYRSA_DIR/pki/issued/${CLIENT_NAME}.crt" || ! -f "$EASYRSA_DIR/pki/private/${CLIENT_NAME}.key" ]]; then
	echo "Generating client certificate and key..."
	./easyrsa gen-req "$CLIENT_NAME" nopass
	./easyrsa sign-req client "$CLIENT_NAME"
fi

# Copy the client certificate and key to the client's unique directory
sudo cp -u "$EASYRSA_DIR/pki/issued/${CLIENT_NAME}.crt" "$CLIENT_DIR/"
sudo cp -u "$EASYRSA_DIR/pki/private/${CLIENT_NAME}.key" "$CLIENT_DIR/"

# Copy the CA certificate and ta.key (TLS auth key) to the client's unique directory
if [ ! -f "$CLIENT_DIR/ca.crt" ]; then
	sudo cp -u /etc/openvpn/ca.crt "$CLIENT_DIR/" || sudo cp -u "$EASYRSA_DIR/pki/ca.crt" "$CLIENT_DIR/"
fi

if [ ! -f "$CLIENT_DIR/ta.key" ]; then
	sudo cp -u /etc/openvpn/ta.key "$CLIENT_DIR/" || sudo cp -u "$EASYRSA_DIR/pki/ta.key" "$CLIENT_DIR/"
fi

# Get the server's public IP address for the configuration
PUBLIC_IP=$(curl -s http://checkip.amazonaws.com)

# Create the client configuration file with embedded certificates and keys
if [ ! -f "$CLIENT_CONFIG" ]; then
	echo "Creating client configuration file..."
	cat <<EOF | sudo tee "$CLIENT_CONFIG"
client
dev tun
proto udp
remote $PUBLIC_IP 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth-user-pass
auth SHA256
data-ciphers AES-256-GCM:AES-128-GCM:AES-256-CBC
data-ciphers-fallback AES-256-CBC
verb 3
tls-auth ta.key 1
<ca>
EOF

	# Embed the CA certificate
	sudo cat "$CLIENT_DIR/ca.crt" | sudo tee -a "$CLIENT_CONFIG"

	cat <<EOF | sudo tee -a "$CLIENT_CONFIG"
</ca>
<cert>
EOF

	# Embed the client certificate
	sudo cat "$CLIENT_DIR/${CLIENT_NAME}.crt" | sudo tee -a "$CLIENT_CONFIG"

	cat <<EOF | sudo tee -a "$CLIENT_CONFIG"
</cert>
<key>
EOF

	# Embed the client private key
	sudo cat "$CLIENT_DIR/${CLIENT_NAME}.key" | sudo tee -a "$CLIENT_CONFIG"

	cat <<EOF | sudo tee -a "$CLIENT_CONFIG"
</key>
<tls-auth>
EOF

	# Embed the TLS key (ta.key)
	sudo cat "$CLIENT_DIR/ta.key" | sudo tee -a "$CLIENT_CONFIG"

	cat <<EOF | sudo tee -a "$CLIENT_CONFIG"
</tls-auth>
EOF
else
	echo "Client configuration already exists: $CLIENT_CONFIG"
fi

# Output success message
echo "Client configuration for $CLIENT_NAME created at $CLIENT_CONFIG"
echo "All related files are stored in $CLIENT_DIR"