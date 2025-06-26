#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y npm
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y npm
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm npm
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'npm' manually."
	exit 1
	;;
  esac

  # If npm is not found in package manager, install it using the node.js installation script
  if ! command -v npm &> /dev/null; then
	echo "'npm' not found, installing via Node.js..."
	curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
	sudo apt-get install -y nodejs
  fi

  # Install uglify-js using npm
  if ! command -v uglifyjs &> /dev/null; then
	echo "Installing uglify-js..."
	npm install -g uglify-js
  fi
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options] <path>"
  echo ""
  echo "Options:"
  echo "  -h, --help             Show this help menu"
  echo "  -f, --file <file>      Minify a single JS file"
  echo "  -d, --directory <dir>  Minify all JS files in a directory"
  echo "  -o, --output <file>    Specify output file name (default: <input_file>.min.js)"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f my-script.js"
  echo "  $0 -d ./js-files"
  echo "  $0 -o output.js -f my-script.js"
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
OUTPUT_FILE=""
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
	-o|--output)
	shift
	OUTPUT_FILE="$1"
	;;
	-v|--version)
	echo "minify-js.sh version $SCRIPT_VERSION"
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

# Function to minify a single file
minify_file() {
  local JS_FILE=$1
  if [ -z "$OUTPUT_FILE" ]; then
	OUTPUT_FILE="${JS_FILE%.js}.min.js"
  fi

  # Check if the file exists
  if [ ! -f "$JS_FILE" ]; then
	echo "Error: File '$JS_FILE' not found."
	exit 1
  fi

  # Minify the JS using 'uglifyjs'
  echo "Minifying JS file: $JS_FILE"
  uglifyjs "$JS_FILE" -o "$OUTPUT_FILE"

  echo "Minified JS file saved as: $OUTPUT_FILE"
}

# Function to minify all JS files in a directory
minify_directory() {
  local DIR=$1
  if [ -z "$DIR" ]; then
	echo "Error: No directory specified."
	exit 1
  fi

  if [ ! -d "$DIR" ]; then
	echo "Error: Directory '$DIR' not found."
	exit 1
  fi

  for JS_FILE in "$DIR"/*.js; do
	if [ -f "$JS_FILE" ]; then
	if [ -z "$OUTPUT_FILE" ]; then
		OUTPUT_FILE="${JS_FILE%.js}.min.js"
	fi
	minify_file "$JS_FILE"
	fi
  done
}

# Check if uglifyjs is installed, if not, install it
if ! command -v uglifyjs &> /dev/null; then
  echo "'uglifyjs' is not installed. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  minify_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  minify_directory "$DIR_PATH"
fi

# ./minify-js.sh -f my-script.js
# ./minify-js.sh -d ./js-files
# ./minify-js.sh -f my-script.js -o output.js
# ./minify-js.sh -h