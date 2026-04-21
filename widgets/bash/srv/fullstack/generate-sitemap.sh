#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y wget curl
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y wget curl
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm wget curl
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'wget' and 'curl' manually."
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
  echo "  -f, --file <file>      Generate a sitemap for a single HTML file"
  echo "  -d, --directory <dir>  Generate a sitemap for all HTML files in a directory"
  echo "  -o, --output <file>    Specify output file name (default: sitemap.xml)"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f index.html"
  echo "  $0 -d ./html-files"
  echo "  $0 -o custom-sitemap.xml -f index.html"
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
OUTPUT_FILE="sitemap.xml"
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
	echo "generate-sitemap.sh version $SCRIPT_VERSION"
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

# Function to generate a sitemap for a single file
generate_sitemap_file() {
  local HTML_FILE=$1
  if [ ! -f "$HTML_FILE" ]; then
	echo "Error: File '$HTML_FILE' not found."
	exit 1
  fi

  # Extract the base URL (assuming local file URLs for simplicity)
  BASE_URL="http://localhost/$(basename "$HTML_FILE")"
  echo "Generating sitemap for: $HTML_FILE"

  # Start sitemap
  echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" > "$OUTPUT_FILE"
  echo "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" >> "$OUTPUT_FILE"

  # Add entry for the HTML file
  echo "<url>" >> "$OUTPUT_FILE"
  echo "  <loc>$BASE_URL</loc>" >> "$OUTPUT_FILE"
  echo "</url>" >> "$OUTPUT_FILE"

  # End sitemap
  echo "</urlset>" >> "$OUTPUT_FILE"

  echo "Sitemap generated and saved as: $OUTPUT_FILE"
}

# Function to generate a sitemap for all HTML files in a directory
generate_sitemap_directory() {
  local DIR=$1
  if [ ! -d "$DIR" ]; then
	echo "Error: Directory '$DIR' not found."
	exit 1
  fi

  # Start sitemap
  echo "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" > "$OUTPUT_FILE"
  echo "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" >> "$OUTPUT_FILE"

  for HTML_FILE in "$DIR"/*.html; do
	if [ -f "$HTML_FILE" ]; then
	# Extract the base URL (assuming local file URLs for simplicity)
	BASE_URL="http://localhost/$(basename "$HTML_FILE")"
	echo "Adding $HTML_FILE to sitemap"

	# Add entry for the HTML file
	echo "<url>" >> "$OUTPUT_FILE"
	echo "  <loc>$BASE_URL</loc>" >> "$OUTPUT_FILE"
	echo "</url>" >> "$OUTPUT_FILE"
	fi
  done

  # End sitemap
  echo "</urlset>" >> "$OUTPUT_FILE"

  echo "Sitemap generated and saved as: $OUTPUT_FILE"
}

# Check if wget and curl are installed, if not, install them
if ! command -v wget &> /dev/null || ! command -v curl &> /dev/null; then
  echo "'wget' or 'curl' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  generate_sitemap_file "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  generate_sitemap_directory "$DIR_PATH"
fi

# ./generate-sitemap.sh -f index.html
# ./generate-sitemap.sh -d ./html-files
# ./generate-sitemap.sh -o custom-sitemap.xml -f index.html
# ./generate-sitemap.sh -h