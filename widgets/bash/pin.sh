#!/bin/bash

# Function to handle the noask logic
noask() {
	if [ -f "${stmp}/pin_ask" ]; then
		rm "${stmp}/pin_ask"
		echo "ask setting removed"
	else
		echo "no ask setting found"
	fi
}

# Main script logic
if [ "$1" == "-ask" ]; then
	echo "ask" > "${stmp}/pin_ask"
fi

if [ "$1" == "-noask" ]; then
	noask
fi

if [ -z "$vault_pin" ]; then
	# Run the loginPIN command stored in the variable $p
	$p loginPIN

	# cat "${stmp}/pin"
	# Read the PIN from the temporary file
	if [ -f "${stmp}/pin" ]; then
		vault_pin=$(cat "${stmp}/pin")

		# Export the vault_pin environment variable
		export vault_pin="$vault_pin"

		# Securely delete the PIN file (overwrite with zeros)
		shred -u "${stmp}/pin"

		echo "PIN set and file removed securely."
	else
		echo "PIN file not found at ${stmp}/pin!"
		exit 1
	fi
else
	echo "PIN already set."
fi