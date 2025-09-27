#!/bin/bash

# Usage check
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <existing.ovpn template> <new client name>"
	exit 1
fi

EXISTING_OVPN_TEMPLATE="$1"
NEW_CLIENT_NAME="$2"

# Detect distro-specific EasyRSA path
if [[ -d "/etc/openvpn/server/easy-rsa" ]]; then
	EASYRSA_DIR="/etc/openvpn/server/easy-rsa"
elif [[ -d "/etc/easy-rsa" ]]; then
	EASYRSA_DIR="/etc/easy-rsa"
else
	echo "EasyRSA directory not found"
	exit 1
fi

# Destination for client .ovpn files (standardize across distros)
CLIENT_CONFIGS_DIR="/etc/openvpn/client-configs/files"

# Ensure the EasyRSA environment is available
cd "$EASYRSA_DIR" || exit 1

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

# Append the certificates and key to the .ovpn file
{
	echo "<ca>"
	cat "$EASYRSA_DIR/pki/ca.crt"
	echo "</ca>"
	echo "<cert>"
	sed -ne '/-BEGIN CERTIFICATE-/,/-END CERTIFICATE-/p' "$EASYRSA_DIR/pki/issued/$NEW_CLIENT_NAME.crt"
	echo "</cert>"
	echo "<key>"
	cat "$EASYRSA_DIR/pki/private/$NEW_CLIENT_NAME.key"
	echo "</key>"
} >> "$NEW_OVPN_FILE"

echo "New .ovpn file for client $NEW_CLIENT_NAME has been generated: $NEW_OVPN_FILE"