#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y tar zip gzip
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y tar zip gzip
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm tar zip gzip
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'tar', 'zip', and 'gzip' manually."
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
  echo "  -f, --file <file>      Bundle a specific file"
  echo "  -d, --directory <dir>  Bundle all files in a directory"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f style.css"
  echo "  $0 -d ./assets"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
ACTION=""
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
	echo "bundle-assets.sh version $SCRIPT_VERSION"
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

# If no action was specified, show help
if [ -z "$ACTION" ]; then
  echo "Error: Missing action (-f or -d)."
  show_help
  exit 1
fi

# Function to bundle a specific file
bundle_file() {
  local FILE=$1

  if [ ! -f "$FILE" ]; then
	echo "Error: File '$FILE' not found."
	exit 1
  fi

  EXT="${FILE##*.}"
  EXT=${EXT,,}  # Convert to lowercase for consistent handling

  BUNDLE_NAME="${FILE%.*}-bundle.$EXT.tar.gz"
  tar -czf "$BUNDLE_NAME" "$FILE"

  echo "Bundled file: $BUNDLE_NAME"
}

# Function to bundle all files in a directory
bundle_directory() {
  local DIR=$1

  if [ ! -d "$DIR" ]; then
	echo "Error: Directory '$DIR' not found."
	exit 1
  fi

  BUNDLE_NAME="$(basename "$DIR")-bundle.tar.gz"
  tar -czf "$BUNDLE_NAME" -C "$DIR" .

  echo "Bundled directory: $BUNDLE_NAME"
}

# Check if necessary tools are installed, if not, install them
if ! command -v tar &> /dev/null || ! command -v zip &> /dev/null || ! command -v gzip &> /dev/null; then
  echo "'tar', 'zip', or 'gzip' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  bundle_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  bundle_directory "$DIR_PATH"
fi

# ./bundle-assets.sh -d ./assets
# ./bundle-assets.sh -f style.css
# ./bundle-assets.sh -v