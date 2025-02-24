#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y cleancss
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y cleancss
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm cleancss
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'cleancss' manually."
	exit 1
	;;
  esac

  # If cleancss isn't found in package manager, try npm install
  if ! command -v cleancss &> /dev/null; then
	echo "'cleancss' not found in the package manager, installing via npm..."
	npm install -g clean-css-cli
  fi
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options] <path>"
  echo ""
  echo "Options:"
  echo "  -h, --help             Show this help menu"
  echo "  -f, --file <file>      Minify a single CSS file"
  echo "  -d, --directory <dir>  Minify all CSS files in a directory"
  echo "  -o, --output <file>    Specify output file name (default: <input_file>.min.css)"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f my-style.css"
  echo "  $0 -d ./css-files"
  echo "  $0 -o output.css -f my-style.css"
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
	echo "minify-css.sh version $SCRIPT_VERSION"
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
  local CSS_FILE=$1
  if [ -z "$OUTPUT_FILE" ]; then
	OUTPUT_FILE="${CSS_FILE%.css}.min.css"
  fi

  # Check if the file exists
  if [ ! -f "$CSS_FILE" ]; then
	echo "Error: File '$CSS_FILE' not found."
	exit 1
  fi

  # Minify the CSS using 'cleancss'
  echo "Minifying CSS file: $CSS_FILE"
  cleancss -o "$OUTPUT_FILE" "$CSS_FILE"

  echo "Minified CSS file saved as: $OUTPUT_FILE"
}

# Function to minify all CSS files in a directory
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

  for CSS_FILE in "$DIR"/*.css; do
	if [ -f "$CSS_FILE" ]; then
	if [ -z "$OUTPUT_FILE" ]; then
		OUTPUT_FILE="${CSS_FILE%.css}.min.css"
	fi
	minify_file "$CSS_FILE"
	fi
  done
}

# Check if cleancss is installed, if not, install it
if ! command -v cleancss &> /dev/null; then
  echo "'cleancss' is not installed. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  minify_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  minify_directory "$DIR_PATH"
fi

# ./minify-css.sh -f my-style.css
# ./minify-css.sh -d ./css-files
# ./minify-css.sh -f my-style.css -o output.css
# ./minify-css.sh -h