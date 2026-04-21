#!/bin/bash

# Check if Bitcoin address is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <bitcoin_address>"
    exit 1
fi

ADDRESS=$1
WALLET_PASSWORD=""  # Placeholder for wallet password or private key

# Function to securely prompt for the wallet password or private key
function prompt_password() {
    if [ -z "$WALLET_PASSWORD" ]; then
        read -s -p "Enter your wallet password or private key: " WALLET_PASSWORD
        echo
    fi
}

# Functions for Bitcoin operations
function check_balance() {
    echo "Checking balance for address: $ADDRESS"
    bitcoin-cli getreceivedbyaddress "$ADDRESS"
}

function send_bitcoin() {
    prompt_password
    read -p "Enter recipient address: " RECIPIENT
    read -p "Enter amount to send: " AMOUNT
    echo "Sending $AMOUNT BTC from $ADDRESS to $RECIPIENT..."
    bitcoin-cli sendtoaddress "$RECIPIENT" "$AMOUNT"
}

function generate_address() {
    prompt_password
    echo "Generating new address..."
    bitcoin-cli getnewaddress
}

function list_transactions() {
    prompt_password
    echo "Listing transactions for wallet..."
    bitcoin-cli listtransactions
}

# Menu
while true; do
    echo "Select an action:"
    echo "1. Check balance"
    echo "2. Send Bitcoin"
    echo "3. Generate new address"
    echo "4. List transactions"
    echo "5. Exit"
    read -p "Enter your choice (1-5): " CHOICE

    case $CHOICE in
        1)
            check_balance
            ;;
        2)
            send_bitcoin
            ;;
        3)
            generate_address
            ;;
        4)
            list_transactions
            ;;
        5)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done
