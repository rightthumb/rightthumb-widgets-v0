#!/bin/bash

# Function to install necessary tools
install_tools() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing dependencies for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y nginx
	;;
	fedora|centos|rhel)
	echo "Installing dependencies for Fedora/CentOS/RHEL..."
	sudo dnf install -y nginx
	;;
	arch)
	echo "Installing dependencies for Arch Linux..."
	sudo pacman -Syu --noconfirm nginx
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install 'nginx' manually."
	exit 1
	;;
  esac
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options]"
  echo ""
  echo "Options:"
  echo "  -h, --help              Show this help menu"
  echo "  -d, --directory <dir>   Serve a specific directory (default: /var/www/html)"
  echo "  -p, --port <port>       Set the port number (default: 80)"
  echo "  -v, --version           Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -d /var/www/myapp"
  echo "  $0 -p 8080"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
PORT=80
DIRECTORY="/var/www/html"

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-d|--directory)
	shift
	DIRECTORY="$1"
	;;
	-p|--port)
	shift
	PORT="$1"
	;;
	-v|--version)
	echo "setup-nginx.sh version $SCRIPT_VERSION"
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

# Ensure the directory exists
if [ ! -d "$DIRECTORY" ]; then
  echo "Error: Directory '$DIRECTORY' not found."
  exit 1
fi

# Install necessary tools if not installed
if ! command -v nginx &> /dev/null; then
  echo "'nginx' not found. Installing..."
  install_tools
fi

# Create Nginx configuration file
CONF_FILE="/etc/nginx/sites-available/myapp"
echo "Creating Nginx config file at $CONF_FILE"

cat <<EOL > $CONF_FILE
server {
	listen $PORT;
	server_name localhost;

	root $DIRECTORY;
	index index.html index.htm;

	location / {
		try_files \$uri \$uri/ =404;
	}
}
EOL

# Enable the site configuration
ln -s $CONF_FILE /etc/nginx/sites-enabled/

# Test Nginx configuration
echo "Testing Nginx configuration..."
sudo nginx -t

if [ $? -eq 0 ]; then
  # Restart Nginx to apply the changes
  echo "Restarting Nginx..."
  sudo systemctl restart nginx
  echo "Nginx setup completed successfully!"
else
  echo "Error: Nginx configuration test failed."
  exit 1
fi


# ./setup-nginx.sh -d /var/www/myapp -p 8080
# ./setup-nginx.sh -v