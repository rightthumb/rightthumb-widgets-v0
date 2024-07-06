#!/bin/bash

# Function to display swap information
display_swap_info() {
	echo "Current Swap Information:"
	sudo swapon --show
	echo ""
}

# Function to create and activate a new swap file
create_swap() {
	echo "Creating a new swap file of size ${SWAP_SIZE_MB}MB..."
	sudo dd if=/dev/zero of=$SWAP_FILE bs=1M count=$SWAP_SIZE_MB
	sudo chmod 600 $SWAP_FILE
	sudo mkswap $SWAP_FILE
	sudo swapon $SWAP_FILE
	echo "New swap memory adjusted to ${SWAP_SIZE_MB}MB."
}

# Check for recover option
if [ "$1" == "--recover" ]; then
	if [ -f "$HOME/swap.bk" ]; then
		echo "Recovering old swap file..."
		sudo swapoff $SWAP_FILE
		sudo mv "$HOME/swap.bk" $SWAP_FILE
		sudo swapon $SWAP_FILE
		echo "Old swap file restored."
	else
		echo "No backup swap file found at $HOME/swap.bk."
	fi
	exit 0
fi

# Define the percentage of disk space to use for swap
PERCENTAGE=20

# Get available disk space in MB
AVAILABLE_DISK_SPACE=$(df --output=avail / | tail -n 1)

# Calculate swap size in MB
SWAP_SIZE_MB=$((AVAILABLE_DISK_SPACE * PERCENTAGE / 100))

# Define swap file path
SWAP_FILE="/swapfile"

# Display current swap info
display_swap_info

# Check if swap file already exists and display its size
if [ -f $SWAP_FILE ]; then
	OLD_SWAP_SIZE=$(sudo du -m $SWAP_FILE | cut -f1)
	echo "Current swap file size: ${OLD_SWAP_SIZE}MB"
else
	echo "No existing swap file found."
fi

# Echo the size of the new swap file and the reason for choosing that size
echo "New swap file size will be: ${SWAP_SIZE_MB}MB"
echo "This size was chosen based on ${PERCENTAGE}% of the available disk space."

# Ask for user confirmation
read -p "Do you want to proceed? (y/n): " choice

if [ "$choice" == "y" ]; then
	# Back up old swap file if it exists
	if [ -f $SWAP_FILE ]; then
		echo "Backing up the old swap file to $HOME/swap.bk..."
		sudo swapoff $SWAP_FILE
		sudo mv $SWAP_FILE "$HOME/swap.bk"
	fi

	# Create and activate the new swap file
	create_swap

	# Verify swap file is active
	sudo swapon --show

	# Optional: Add swap file to /etc/fstab for automatic mounting at boot
	if ! grep -q "$SWAP_FILE" /etc/fstab; then
		echo "$SWAP_FILE none swap sw 0 0" | sudo tee -a /etc/fstab
	fi

	echo "Swap configuration complete."
else
	echo "No changes made."
fi