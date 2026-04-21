#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y rsync ssh
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y rsync openssh-clients
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm rsync openssh
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'rsync' and 'ssh' manually."
	exit 1
	;;
  esac
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options] <path>"
  echo ""
  echo "Options:"
  echo "  -h, --help             Show this help menu"
  echo "  -f, --file <file>      Deploy a specific file"
  echo "  -d, --directory <dir>  Deploy all files in a directory"
  echo "  -v, --version          Display script version"
  echo "  -s, --server <host>    Specify the server to deploy to (user@hostname)"
  echo "  -p, --path <path>      Remote path to deploy files to"
  echo ""
  echo "Examples:"
  echo "  $0 -f index.html -s user@yourserver.com -p /var/www/html"
  echo "  $0 -d ./build -s user@yourserver.com -p /var/www/html"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
ACTION=""
SERVER=""
REMOTE_PATH=""
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-f|--file)
	ACTION="file"
	shift
	FILE_PATH="$1"
	;;
	-d|--directory)
	ACTION="directory"
	shift
	DIR_PATH="$1"
	;;
	-v|--version)
	echo "deploy-front-end.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-s|--server)
	shift
	SERVER="$1"
	;;
	-p|--path)
	shift
	REMOTE_PATH="$1"
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Ensure server and remote path are specified
if [ -z "$SERVER" ] || [ -z "$REMOTE_PATH" ]; then
  echo "Error: Server and remote path must be specified."
  show_help
  exit 1
fi

# Ensure action is specified
if [ -z "$ACTION" ]; then
  echo "Error: Missing action (-f or -d)."
  show_help
  exit 1
fi

# Function to deploy a specific file
deploy_file() {
  local FILE=$1

  if [ ! -f "$FILE" ]; then
	echo "Error: File '$FILE' not found."
	exit 1
  fi

  rsync -avz "$FILE" "$SERVER:$REMOTE_PATH"
  echo "Deployed file: $FILE to $SERVER:$REMOTE_PATH"
}

# Function to deploy all files in a directory
deploy_directory() {
  local DIR=$1

  if [ ! -d "$DIR" ]; then
	echo "Error: Directory '$DIR' not found."
	exit 1
  fi

  rsync -avz "$DIR/" "$SERVER:$REMOTE_PATH"
  echo "Deployed directory: $DIR to $SERVER:$REMOTE_PATH"
}

# Check if necessary tools are installed, if not, install them
if ! command -v rsync &> /dev/null || ! command -v ssh &> /dev/null; then
  echo "'rsync' or 'ssh' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  deploy_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  deploy_directory "$DIR_PATH"
fi

# ./deploy-front-end.sh -f index.html -s user@yourserver.com -p /var/www/html
# ./deploy-front-end.sh -d ./build -s user@yourserver.com -p /var/www/html
# ./deploy-front-end.sh -v