#!/bin/bash

# Bitcoin Core Configuration Editor Script
# Opens bitcoin.conf for editing and automatically restarts bitcoind after saving.

CONF_FILE="$HOME/.bitcoin/bitcoin.conf"

# Ensure the configuration file exists
if [ ! -f "$CONF_FILE" ]; then
	echo "Configuration file not found at $CONF_FILE."
	echo "Creating a default bitcoin.conf file..."
	mkdir -p "$HOME/.bitcoin"
	cat <<EOF >"$CONF_FILE"
# Bitcoin Core Configuration
server=1
daemon=1
rpcuser=bitcoinrpc
rpcpassword=changeme
rpcallowip=127.0.0.1
rpcport=8332
disablewallet=0
EOF
	echo "Default configuration file created at $CONF_FILE."
fi

# Inform user
echo "Opening $CONF_FILE in nano for editing."
echo "Make your changes, save (Ctrl+O), and close (Ctrl+X)."

# Open the configuration file in nano
nano "$CONF_FILE"

# Restart the Bitcoin daemon
echo "Restarting Bitcoin Core daemon to apply changes..."
pkill -f bitcoind 2>/dev/null || true  # Stop the daemon if running
echo "Restart the daemon: /snap/bin/bitcoin-core.daemon"
echo "Restart the daemon: /snap/bin/bitcoin-core.daemon"
echo "Restart the daemon: /snap/bin/bitcoin-core.daemon"

# Wait for the daemon to initialize
echo "Waiting for Bitcoin Core daemon to start..."
sleep 10

# Test the RPC connection
echo "Testing RPC connection with updated configuration..."
RPC_USER=$(grep -m1 "^rpcuser" "$CONF_FILE" | cut -d'=' -f2)
RPC_PASSWORD=$(grep -m1 "^rpcpassword" "$CONF_FILE" | cut -d'=' -f2)

if /snap/bin/bitcoin-core.cli -rpcuser="$RPC_USER" -rpcpassword="$RPC_PASSWORD" getblockchaininfo &>/dev/null; then
	echo "Bitcoin Core is running, and the RPC connection is successful."
else
	echo "Failed to connect to Bitcoin Core daemon. Check logs for more details."
	tail -f "$HOME/.bitcoin/debug.log"
	exit 1
fi

echo "========================="
echo "Bitcoin Core Configuration Updated Successfully"
echo "========================="