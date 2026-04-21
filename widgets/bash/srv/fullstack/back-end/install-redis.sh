#!/bin/bash

# Function to install Redis
install_redis() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing Redis for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y redis-server
	;;
	fedora|centos|rhel)
	echo "Installing Redis for Fedora/CentOS/RHEL..."
	sudo dnf install -y redis
	;;
	arch)
	echo "Installing Redis for Arch Linux..."
	sudo pacman -Syu --noconfirm redis
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install Redis manually."
	exit 1
	;;
  esac
}

# Function to enable and start Redis service
start_redis() {
  echo "Enabling and starting Redis service..."
  sudo systemctl enable redis
  sudo systemctl start redis
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help            Show this help menu"
  echo "  -v, --version         Display script version"
  echo "  -s, --start           Start the Redis service after installation"
  echo ""
  echo "Examples:"
  echo "  $0 -s"
  echo "  $0 -v"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
START_SERVICE=false

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "install-redis.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-s|--start)
	START_SERVICE=true
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Install Redis
install_redis

# Start Redis service if requested
if [ "$START_SERVICE" = true ]; then
  start_redis
  echo "Redis service has been started."
else
  echo "Redis installation complete. You can start the Redis service manually with 'sudo systemctl start redis'."
fi

echo "Redis installation completed successfully!"

# sudo ./install-redis.sh
# sudo ./install-redis.sh -s
# ./install-redis.sh -v
# ./install-redis.sh -h