#!/bin/bash

# Bitcoin CLI Manager Script
# Interacts with bitcoin-cli, dynamically reads RPC credentials from bitcoin.conf, and provides a menu-driven interface.

CONF_FILE="$HOME/.bitcoin/bitcoin.conf"

# Function to read RPC credentials from bitcoin.conf
function load_rpc_credentials() {
	if [ ! -f "$CONF_FILE" ]; then
		echo "Configuration file not found at $CONF_FILE."
		echo "Please run the setup script or create a valid bitcoin.conf file."
		exit 1
	fi

	# Extract rpcuser and rpcpassword from the configuration file
	RPC_USER=$(grep -m1 "^rpcuser" "$CONF_FILE" | cut -d'=' -f2)
	RPC_PASSWORD=$(grep -m1 "^rpcpassword" "$CONF_FILE" | cut -d'=' -f2)

	# Check if credentials were found
	if [ -z "$RPC_USER" ] || [ -z "$RPC_PASSWORD" ]; then
		echo "Error: RPC credentials not found in $CONF_FILE."
		exit 1
	fi
}

# Function to print the menu
function print_menu() {
	echo "==================== Bitcoin CLI Manager ===================="
	echo "1. Get Blockchain Info"
	echo "2. Get Network Info"
	echo "3. List Wallets"
	echo "4. Create a New Wallet"
	echo "5. Generate a New Address"
	echo "6. Send Bitcoin"
	echo "7. List Transactions"
	echo "8. Check Wallet Balance"
	echo "9. Exit"
	echo "============================================================="
}

# Base command for bitcoin-cli with credentials
function bitcoin_cli() {
	/snap/bin/bitcoin-core.cli -rpcuser="$RPC_USER" -rpcpassword="$RPC_PASSWORD" "$@"
}

# Function to get blockchain info
function get_blockchain_info() {
	bitcoin_cli getblockchaininfo
}

# Function to get network info
function get_network_info() {
	bitcoin_cli getnetworkinfo
}

# Function to list wallets
function list_wallets() {
	bitcoin_cli listwallets
}

# Function to create a new wallet
function create_wallet() {
	echo "Enter the name for the new wallet:"
	read -r WALLET_NAME
	bitcoin_cli createwallet "$WALLET_NAME"
	echo "Wallet '$WALLET_NAME' created successfully!"
}

# Function to generate a new receiving address
function generate_address() {
	echo "Enter the wallet name (or leave blank for default):"
	read -r WALLET_NAME
	if [ -z "$WALLET_NAME" ]; then
		bitcoin_cli getnewaddress
	else
		bitcoin_cli -rpcwallet="$WALLET_NAME" getnewaddress
	fi
}

# Function to send Bitcoin
function send_bitcoin() {
	echo "Enter recipient address:"
	read -r RECIPIENT
	echo "Enter amount to send (in BTC):"
	read -r AMOUNT
	echo "Enter the wallet name (or leave blank for default):"
	read -r WALLET_NAME
	if [ -z "$WALLET_NAME" ]; then
		bitcoin_cli sendtoaddress "$RECIPIENT" "$AMOUNT"
	else
		bitcoin_cli -rpcwallet="$WALLET_NAME" sendtoaddress "$RECIPIENT" "$AMOUNT"
	fi
	echo "Sent $AMOUNT BTC to $RECIPIENT."
}

# Function to list transactions
function list_transactions() {
	echo "Enter the wallet name (or leave blank for default):"
	read -r WALLET_NAME
	if [ -z "$WALLET_NAME" ]; then
		bitcoin_cli listtransactions
	else
		bitcoin_cli -rpcwallet="$WALLET_NAME" listtransactions
	fi
}

# Function to check wallet balance
function check_balance() {
	echo "Enter the wallet name (or leave blank for default):"
	read -r WALLET_NAME
	if [ -z "$WALLET_NAME" ]; then
		bitcoin_cli getbalance
	else
		bitcoin_cli -rpcwallet="$WALLET_NAME" getbalance
	fi
}

# Load RPC credentials
load_rpc_credentials

# Main program loop
while true; do
	print_menu
	echo "Enter your choice:"
	read -r CHOICE
	case $CHOICE in
		1) get_blockchain_info ;;
		2) get_network_info ;;
		3) list_wallets ;;
		4) create_wallet ;;
		5) generate_address ;;
		6) send_bitcoin ;;
		7) list_transactions ;;
		8) check_balance ;;
		9) echo "Exiting Bitcoin CLI Manager. Goodbye!"; exit 0 ;;
		*) echo "Invalid choice. Please try again." ;;
	esac
done