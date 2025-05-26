#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y inotify-tools uglifyjs
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y inotify-tools uglify-js
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm inotify-tools uglifyjs
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'inotify-tools' and 'uglifyjs' manually."
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
  echo "  -f, --file <file>      Watch a specific JavaScript file"
  echo "  -d, --directory <dir>  Watch all JavaScript files in a directory"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f script.js"
  echo "  $0 -d ./js-directory"
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
	echo "watch-js.sh version $SCRIPT_VERSION"
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

# Function to minify and update the JavaScript file
minify_js() {
  local JS_FILE=$1
  local OUTPUT_FILE="${JS_FILE%.js}.min.js"

  if [ ! -f "$JS_FILE" ]; then
	echo "Error: File '$JS_FILE' not found."
	exit 1
  fi

  # Minify the JavaScript file using uglifyjs
  uglifyjs "$JS_FILE" -o "$OUTPUT_FILE" --compress --mangle

  echo "Minified JavaScript saved to: $OUTPUT_FILE"
}

# Function to watch a specific JavaScript file for changes
watch_js_file() {
  local JS_FILE=$1

  # Watch for changes in the JavaScript file and minify when changed
  echo "Watching for changes in $JS_FILE..."
  while inotifywait -e modify "$JS_FILE"; do
	minify_js "$JS_FILE"
  done
}

# Function to watch all JavaScript files in a directory for changes
watch_js_directory() {
  local DIR=$1

  # Watch for changes in JavaScript files in the directory and minify when changed
  echo "Watching for changes in JavaScript files in $DIR..."
  while inotifywait -e modify "$DIR"/*.js; do
	for JS_FILE in "$DIR"/*.js; do
	minify_js "$JS_FILE"
	done
  done
}

# Check if inotify-tools and uglifyjs are installed, if not, install them
if ! command -v inotifywait &> /dev/null || ! command -v uglifyjs &> /dev/null; then
  echo "'inotifywait' or 'uglifyjs' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  watch_js_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  watch_js_directory "$DIR_PATH"
fi

# ./watch-js.sh -f script.js
# ./watch-js.sh -d ./js-directory
# ./watch-js.sh -v