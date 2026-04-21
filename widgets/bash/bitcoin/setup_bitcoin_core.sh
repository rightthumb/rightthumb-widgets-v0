#!/bin/bash

# Bitcoin Core Setup Script
set -e  # Exit on any error

echo "====================="
echo "Bitcoin Core Setup"
echo "====================="

# Check for Snap
if ! command -v snap &>/dev/null; then
	echo "Snap is not installed. Installing Snap..."
	sudo apt update
	sudo apt install snapd -y
fi

# Install Bitcoin Core via Snap
if ! snap list | grep -q bitcoin-core; then
	echo "Installing Bitcoin Core via Snap..."
	sudo snap install bitcoin-core
else
	echo "Bitcoin Core is already installed. Skipping installation."
fi

# Create symbolic links in /usr/local/bin for convenience
echo "Creating symbolic links for Bitcoin Core commands..."
sudo ln -sf /snap/bin/bitcoin-core.cli /usr/local/bin/bitcoin-cli
sudo ln -sf /snap/bin/bitcoin-core.daemon /usr/local/bin/bitcoind

# Verify installation
echo "Verifying Bitcoin Core installation..."
if command -v bitcoin-cli &>/dev/null && command -v bitcoind &>/dev/null; then
	echo "Bitcoin Core installed successfully."
else
	echo "Failed to install Bitcoin Core. Please check the setup."
	exit 1
fi

# Configure bitcoin.conf
BITCOIN_CONF_DIR=~/.bitcoin
BITCOIN_CONF_FILE=$BITCOIN_CONF_DIR/bitcoin.conf

echo "Configuring Bitcoin Core..."
mkdir -p "$BITCOIN_CONF_DIR"
if [ ! -f "$BITCOIN_CONF_FILE" ]; then
	# Generate a strong RPC password
	RPC_PASSWORD=$(openssl rand -base64 32)
	cat <<EOF >"$BITCOIN_CONF_FILE"
# Bitcoin Core Configuration
server=1
daemon=1
rpcuser=bitcoinrpc
rpcpassword=$RPC_PASSWORD
rpcallowip=127.0.0.1
rpcport=8332
disablewallet=0
prune=550
EOF
	echo "Configuration file created at $BITCOIN_CONF_FILE."
	echo "Your RPC credentials are:"
	echo "  rpcuser=bitcoinrpc"
	echo "  rpcpassword=$RPC_PASSWORD"
else
	echo "Configuration file already exists at $BITCOIN_CONF_FILE. No changes made."
fi

# Provide instructions if the user changes the credentials
echo "=================================================================="
echo "IMPORTANT: If you change the RPC user or password in:"
echo "  $BITCOIN_CONF_FILE"
echo "You must use the updated credentials when running bitcoin-cli commands."
echo "Example:"
echo "  bitcoin-cli -rpcuser=<your_new_user> -rpcpassword=<your_new_password> getblockchaininfo"
echo "=================================================================="

# Start Bitcoin Core daemon
echo "Starting Bitcoin Core daemon..."
if ! /snap/bin/bitcoin-core.daemon &>/dev/null; then
	echo "Failed to start Bitcoin Core daemon. Check logs with 'snap logs bitcoin-core'."
	exit 1
fi

# Wait for the daemon to start
echo "Waiting for Bitcoin Core daemon to start..."
sleep 10

# Verify daemon is running
if ps aux | grep -q '[b]itcoind'; then
	echo "Bitcoin Core daemon is running."
else
	echo "Failed to start Bitcoin Core daemon. Check logs for more details."
	snap logs bitcoin-core
	exit 1
fi

# Test RPC connection
echo "Testing RPC connection..."
RPC_USER=$(grep -m1 "^rpcuser" "$BITCOIN_CONF_FILE" | cut -d'=' -f2)
RPC_PASSWORD=$(grep -m1 "^rpcpassword" "$BITCOIN_CONF_FILE" | cut -d'=' -f2)

if bitcoin-cli -rpcuser="$RPC_USER" -rpcpassword="$RPC_PASSWORD" getblockchaininfo &>/dev/null; then
	echo "Bitcoin Core is running, and the RPC connection is successful."
else
	echo "Failed to connect to Bitcoin Core daemon. Check your configuration and logs."
	snap logs bitcoin-core
	exit 1
fi

echo "========================="
echo "Bitcoin Core Setup Complete"
echo "========================="
echo "Configuration file path: $BITCOIN_CONF_FILE"
echo "You can now use the following commands:"
echo "  - bitcoin-cli: Interact with Bitcoin Core (e.g., bitcoin-cli getblockchaininfo)"
echo "  - bitcoind: Manage the Bitcoin Core daemon"