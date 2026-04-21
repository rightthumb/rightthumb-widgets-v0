#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y eslint stylelint
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y eslint stylelint
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm eslint stylelint
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'eslint' and 'stylelint' manually."
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
  echo "  -f, --file <file>      Lint a specific file"
  echo "  -d, --directory <dir>  Lint all files in a directory"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f index.js"
  echo "  $0 -d ./src"
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
	echo "test-linting.sh version $SCRIPT_VERSION"
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

# Ensure action is specified
if [ -z "$ACTION" ]; then
  echo "Error: Missing action (-f or -d)."
  show_help
  exit 1
fi

# Function to lint a specific file
lint_file() {
  local FILE=$1

  if [ ! -f "$FILE" ]; then
	echo "Error: File '$FILE' not found."
	exit 1
  fi

  if [[ "$FILE" == *.js ]]; then
	eslint "$FILE"
  elif [[ "$FILE" == *.css ]]; then
	stylelint "$FILE"
  else
	echo "Error: Unsupported file type. Only .js and .css files are supported."
	exit 1
  fi
}

# Function to lint all files in a directory
lint_directory() {
  local DIR=$1

  if [ ! -d "$DIR" ]; then
	echo "Error: Directory '$DIR' not found."
	exit 1
  fi

  for file in "$DIR"/*; do
	if [[ "$file" == *.js ]]; then
	eslint "$file"
	elif [[ "$file" == *.css ]]; then
	stylelint "$file"
	fi
  done
}

# Check if necessary tools are installed, if not, install them
if ! command -v eslint &> /dev/null || ! command -v stylelint &> /dev/null; then
  echo "'eslint' or 'stylelint' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  lint_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  lint_directory "$DIR_PATH"
fi

# ./test-linting.sh -f index.js
# ./test-linting.sh -d ./src
# ./test-linting.sh -v