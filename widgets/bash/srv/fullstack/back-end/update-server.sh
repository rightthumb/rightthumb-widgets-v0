#!/bin/bash

# Default configuration values
DISTRO=""
DRY_RUN=false
FORCE_UPDATE=false

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help            Show this help menu"
  echo "  -v, --version         Show script version"
  echo "  -d, --distro <distro> Specify the distribution to update (e.g., ubuntu, centos)"
  echo "  -n, --dry-run         Perform a dry run without actually updating the server"
  echo "  -f, --force-update    Force update even if the system is up-to-date"
  echo ""
  echo "Examples:"
  echo "  $0 -d ubuntu           Update Ubuntu system"
  echo "  $0 -n                  Perform a dry run"
  echo "  $0 -f                  Force update"
}

# Script version
SCRIPT_VERSION="1.0.0"

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "update-server.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-d|--distro)
	shift
	DISTRO=$1
	;;
	-n|--dry-run)
	DRY_RUN=true
	;;
	-f|--force-update)
	FORCE_UPDATE=true
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Function to check if running as root
check_root() {
  if [ "$(id -u)" -ne 0 ]; then
	echo "You must run this script as root or with sudo privileges."
	exit 1
  fi
}

# Function to update Ubuntu/Debian-based systems
update_ubuntu() {
  echo "Updating Ubuntu/Debian-based system..."
  if [ "$DRY_RUN" = true ]; then
	echo "[Dry Run] sudo apt update && sudo apt upgrade"
  else
	sudo apt update -y
	sudo apt upgrade -y
	sudo apt dist-upgrade -y
	sudo apt autoremove -y
  fi
}

# Function to update CentOS/RHEL-based systems
update_centos() {
  echo "Updating CentOS/RHEL-based system..."
  if [ "$DRY_RUN" = true ]; then
	echo "[Dry Run] sudo yum update"
  else
	sudo yum update -y
  fi
}

# Function to update Arch-based systems
update_arch() {
  echo "Updating Arch-based system..."
  if [ "$DRY_RUN" = true ]; then
	echo "[Dry Run] sudo pacman -Syu"
  else
	sudo pacman -Syu --noconfirm
  fi
}

# Function to handle updating based on distro
update_system() {
  case "$DISTRO" in
	ubuntu|debian)
	update_ubuntu
	;;
	centos|rhel|fedora)
	update_centos
	;;
	arch)
	update_arch
	;;
	*)
	echo "Unsupported distribution: $DISTRO"
	exit 1
	;;
  esac
}

# Ensure script is run as root
check_root

# If no distro specified, prompt user
if [ -z "$DISTRO" ]; then
  echo "Please specify a distribution with the -d option (e.g., ubuntu, centos)."
  show_help
  exit 1
fi

# Force update if specified
if [ "$FORCE_UPDATE" = true ]; then
  echo "Forcing update, even if system is up-to-date..."
fi

# Run the update
update_system


# ./update-server.sh -d ubuntu
# ./update-server.sh -d ubuntu -n
# ./update-server.sh -d ubuntu -f
# ./update-server.sh -v