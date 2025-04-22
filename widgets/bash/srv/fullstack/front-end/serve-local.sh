#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y nodejs npm
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y nodejs npm
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm nodejs npm
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'nodejs' and 'npm' manually."
	exit 1
	;;
  esac
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help             Show this help menu"
  echo "  -d, --directory <dir>  Serve a specific directory (default: current directory)"
  echo "  -p, --port <port>      Set the port number (default: 8080)"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -d ./public"
  echo "  $0 -p 3000"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
PORT=8080
DIRECTORY="."

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-d|--directory)
	shift
	DIRECTORY="$1"
	;;
	-p|--port)
	shift
	PORT="$1"
	;;
	-v|--version)
	echo "serve-local.sh version $SCRIPT_VERSION"
	exit 0
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Ensure the directory exists
if [ ! -d "$DIRECTORY" ]; then
  echo "Error: Directory '$DIRECTORY' not found."
  exit 1
fi

# Install necessary tools if not installed
if ! command -v http-server &> /dev/null; then
  echo "'http-server' not found. Installing..."
  npm install -g http-server
fi

# Start the server
echo "Serving '$DIRECTORY' on http://localhost:$PORT"
http-server "$DIRECTORY" -p "$PORT"

# ./serve-local.sh
# ./serve-local.sh -d ./public -p 3000
# ./serve-local.sh -v