#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y inotify-tools cssmin
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y inotify-tools cssmin
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm inotify-tools cssmin
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'inotify-tools' and 'cssmin' manually."
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
  echo "  -f, --file <file>      Watch a specific CSS file"
  echo "  -d, --directory <dir>  Watch all CSS files in a directory"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f style.css"
  echo "  $0 -d ./css-directory"
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
	echo "watch-css.sh version $SCRIPT_VERSION"
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

# Function to minify and update the CSS file
minify_css() {
  local CSS_FILE=$1
  local OUTPUT_FILE="${CSS_FILE%.css}.min.css"

  if [ ! -f "$CSS_FILE" ]; then
	echo "Error: File '$CSS_FILE' not found."
	exit 1
  fi

  # Minify the CSS file
  cssmin < "$CSS_FILE" > "$OUTPUT_FILE"

  echo "Minified CSS saved to: $OUTPUT_FILE"
}

# Function to watch a specific CSS file for changes
watch_css_file() {
  local CSS_FILE=$1

  # Watch for changes in the CSS file and minify when changed
  echo "Watching for changes in $CSS_FILE..."
  while inotifywait -e modify "$CSS_FILE"; do
	minify_css "$CSS_FILE"
  done
}

# Function to watch all CSS files in a directory for changes
watch_css_directory() {
  local DIR=$1

  # Watch for changes in CSS files in the directory and minify when changed
  echo "Watching for changes in CSS files in $DIR..."
  while inotifywait -e modify "$DIR"/*.css; do
	for CSS_FILE in "$DIR"/*.css; do
	minify_css "$CSS_FILE"
	done
  done
}

# Check if inotify-tools and cssmin are installed, if not, install them
if ! command -v inotifywait &> /dev/null || ! command -v cssmin &> /dev/null; then
  echo "'inotifywait' or 'cssmin' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  watch_css_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  watch_css_directory "$DIR_PATH"
fi

# ./watch-css.sh -f style.css
# ./watch-css.sh -d ./css-directory
# ./watch-css.sh -v