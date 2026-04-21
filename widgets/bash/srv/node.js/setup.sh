#!/bin/bash

# Function to check if the script is run as root
check_root() {
  if [ "$(id -u)" -ne 0 ]; then
	echo "This script must be run as root or with sudo."
	exit 1
  fi
}

# Update the system
update_system() {
  echo "Updating package lists..."
  apt update -y
  apt upgrade -y
}

# Install curl if not installed
install_curl() {
  if ! command -v curl &> /dev/null; then
	echo "Installing curl..."
	apt install -y curl
  fi
}

# Add NodeSource repository and install Node.js
install_node() {
  echo "Adding NodeSource repository..."
  curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
  
  echo "Installing Node.js..."
  apt install -y nodejs

  echo "Node.js and npm installed successfully!"
}

# Verify installation
verify_installation() {
  echo "Verifying installation..."
  node_version=$(node -v)
  npm_version=$(npm -v)

  echo "Node.js version: $node_version"
  echo "npm version: $npm_version"
}

# Main script execution
main() {
  check_root
  update_system
  install_curl
  install_node
  verify_installation
}

# Run the main function
main