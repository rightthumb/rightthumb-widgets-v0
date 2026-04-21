#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y imagemagick optipng pngcrush gifsicle jpegoptim
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y imagemagick optipng pngcrush gifsicle jpegoptim
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm imagemagick optipng pngcrush gifsicle jpegoptim
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'imagemagick', 'optipng', 'pngcrush', 'gifsicle', and 'jpegoptim' manually."
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
  echo "  -f, --file <file>      Optimize a specific image file"
  echo "  -d, --directory <dir>  Optimize all image files in a directory"
  echo "  -v, --version          Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -f image.png"
  echo "  $0 -d ./images"
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
	echo "optimize-images.sh version $SCRIPT_VERSION"
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

# Function to optimize an image file
optimize_image() {
  local IMAGE_FILE=$1

  if [ ! -f "$IMAGE_FILE" ]; then
	echo "Error: File '$IMAGE_FILE' not found."
	exit 1
  fi

  EXT="${IMAGE_FILE##*.}"
  EXT=${EXT,,}  # Convert to lowercase for consistent handling

  case "$EXT" in
	jpg|jpeg)
	jpegoptim --max=85 "$IMAGE_FILE"
	;;
	png)
	optipng -o7 "$IMAGE_FILE"
	pngcrush -brute "$IMAGE_FILE" "$IMAGE_FILE"
	;;
	gif)
	gifsicle -O3 "$IMAGE_FILE" -o "$IMAGE_FILE"
	;;
	*)
	echo "Unsupported image format: $EXT"
	exit 1
	;;
  esac

  echo "Optimized image: $IMAGE_FILE"
}

# Function to optimize all images in a directory
optimize_images_in_directory() {
  local DIR=$1

  # Loop through all image files in the directory
  for IMAGE_FILE in "$DIR"/*.{jpg,jpeg,png,gif}; do
	if [ -f "$IMAGE_FILE" ]; then
	optimize_image "$IMAGE_FILE"
	fi
  done
}

# Check if necessary tools are installed, if not, install them
if ! command -v imagemagick &> /dev/null || ! command -v optipng &> /dev/null || ! command -v pngcrush &> /dev/null || ! command -v gifsicle &> /dev/null || ! command -v jpegoptim &> /dev/null; then
  echo "'imagemagick', 'optipng', 'pngcrush', 'gifsicle', or 'jpegoptim' not found. Installing dependencies..."
  install_tools
fi

# Execute based on the action (file or directory)
if [ "$ACTION" == "file" ]; then
  optimize_image "$FILE_PATH"
elif [ "$ACTION" == "directory" ]; then
  optimize_images_in_directory "$DIR_PATH"
fi

# ./optimize-images.sh -d ./images
# ./optimize-images.sh -f image.png
# ./optimize-images.sh -v