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
  echo "  -b, --backend <url>     Backend server URL (e.g., http://localhost:5000)"
  echo "  -p, --port <port>       Set the port number for Nginx to listen on (default: 80)"
  echo "  -v, --version           Display script version"
  echo ""
  echo "Examples:"
  echo "  $0 -b http://localhost:5000 -p 8080"
  echo "  $0 -v"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
PORT=80
BACKEND_URL=""

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-b|--backend)
	shift
	BACKEND_URL="$1"
	;;
	-p|--port)
	shift
	PORT="$1"
	;;
	-v|--version)
	echo "deploy-back-end.sh version $SCRIPT_VERSION"
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

# Ensure the backend URL is specified
if [ -z "$BACKEND_URL" ]; then
  echo "Error: Backend URL is required (-b option)."
  show_help
  exit 1
fi

# Install Nginx if it's not already installed
if ! command -v nginx &> /dev/null; then
  echo "'nginx' not found. Installing..."
  install_tools
fi

# Create Nginx configuration file for reverse proxy
CONF_FILE="/etc/nginx/sites-available/backend"
echo "Creating Nginx config file at $CONF_FILE"

cat <<EOL > $CONF_FILE
server {
	listen $PORT;
	server_name localhost;

	location / {
		proxy_pass $BACKEND_URL;
		proxy_set_header Host \$host;
		proxy_set_header X-Real-IP \$remote_addr;
		proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto \$scheme;
	}
}
EOL

# Enable the site configuration by creating a symlink
ln -s $CONF_FILE /etc/nginx/sites-enabled/

# Test Nginx configuration
echo "Testing Nginx configuration..."
sudo nginx -t

if [ $? -eq 0 ]; then
  # Restart Nginx to apply changes
  echo "Restarting Nginx..."
  sudo systemctl restart nginx
  echo "Backend deployment complete, Nginx is now proxying to $BACKEND_URL!"
else
  echo "Error: Nginx configuration test failed."
  exit 1
fi

# ./deploy-back-end.sh -b http://localhost:5000 -p 8080
# ./deploy-back-end.sh -v