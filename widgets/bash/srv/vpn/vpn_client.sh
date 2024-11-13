#!/bin/bash

# Usage check
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <existing.ovpn template> <new client name>"
    exit 1
fi

EXISTING_OVPN_TEMPLATE="$1"
NEW_CLIENT_NAME="$2"
EASYRSA_DIR="/etc/openvpn/server/easy-rsa"
CLIENT_CONFIGS_DIR="/etc/openvpn/client-configs/files"

# Ensure the EasyRSA environment is available
if [ ! -d "$EASYRSA_DIR" ]; then
    echo "EasyRSA directory not found at $EASYRSA_DIR"
    exit 1
fi

# Initialize EasyRSA environment
cd "$EASYRSA_DIR"

# Generate new client keys and certificates
./easyrsa build-client-full "$NEW_CLIENT_NAME" nopass

if [ $? -ne 0 ]; then
    echo "Failed to generate client keys and certificates"
    exit 1
fi

# Create a directory for client configs if it doesn't exist
mkdir -p "$CLIENT_CONFIGS_DIR"

# Path to the new client's OVPN file
NEW_OVPN_FILE="$CLIENT_CONFIGS_DIR/$NEW_CLIENT_NAME.ovpn"

# Copy the existing template and modify it for the new client
cp "$EXISTING_OVPN_TEMPLATE" "$NEW_OVPN_FILE"

# Append the client and CA certificates and client key to the .ovpn file
echo "<ca>" >> "$NEW_OVPN_FILE"
cat "$EASYRSA_DIR/pki/ca.crt" >> "$NEW_OVPN_FILE"
echo "</ca>" >> "$NEW_OVPN_FILE"
echo "<cert>" >> "$NEW_OVPN_FILE"
sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' "$EASYRSA_DIR/pki/issued/$NEW_CLIENT_NAME.crt" >> "$NEW_OVPN_FILE"
echo "</cert>" >> "$NEW_OVPN_FILE"
echo "<key>" >> "$NEW_OVPN_FILE"
cat "$EASYRSA_DIR/pki/private/$NEW_CLIENT_NAME.key" >> "$NEW_OVPN_FILE"
echo "</key>" >> "$NEW_OVPN_FILE"

echo "New .ovpn file for client $NEW_CLIENT_NAME has been generated: $NEW_OVPN_FILE"
# cat ./pre.txt "$NEW_OVPN_FILE" > temp_file && mv temp_file "$NEW_OVPN_FILE"
# cat ./post.txt >> "$NEW_OVPN_FILE"
