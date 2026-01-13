#!/bin/bash

# Function to install Let's Encrypt (Certbot) and dependencies
install_certbot() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing Certbot for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y certbot python3-certbot-nginx
	;;
	fedora|centos|rhel)
	echo "Installing Certbot for Fedora/CentOS/RHEL..."
	sudo dnf install -y certbot python3-certbot-nginx
	;;
	arch)
	echo "Installing Certbot for Arch Linux..."
	sudo pacman -Syu --noconfirm certbot python-certbot-nginx
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install Certbot manually."
	exit 1
	;;
  esac
}

# Function to request an SSL certificate from Let's Encrypt
request_ssl_certificate() {
  DOMAIN=$1

  echo "Requesting SSL certificate for $DOMAIN..."
  sudo certbot --nginx -d $DOMAIN --non-interactive --agree-tos -m admin@$DOMAIN
}

# Function to auto-renew SSL certificates
setup_auto_renewal() {
  echo "Setting up automatic SSL certificate renewal..."
  sudo systemctl enable --now certbot.timer
}

# Function to display help menu
show_help() {
  echo "Usage: $0 [options] <domain>"
  echo ""
  echo "Options:"
  echo "  -h, --help              Show this help menu"
  echo "  -v, --version           Display script version"
  echo "  -r, --renew             Renew the SSL certificate"
  echo "  -d, --domain            Specify the domain for SSL setup (required)"
  echo ""
  echo "Examples:"
  echo "  $0 -d example.com"
  echo "  $0 -r"
  echo "  $0 -v"
}

# Script version
SCRIPT_VERSION="1.0.0"
DOMAIN=""

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "setup-ssl.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-r|--renew)
	echo "Renewing SSL certificates..."
	sudo certbot renew
	exit 0
	;;
	-d|--domain)
	shift
	DOMAIN=$1
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Validate domain input
if [ -z "$DOMAIN" ]; then
  echo "Error: Domain is required."
  show_help
  exit 1
fi

# Install Certbot
install_certbot

# Request SSL certificate
request_ssl_certificate $DOMAIN

# Set up auto-renewal
setup_auto_renewal

echo "SSL certificate for $DOMAIN has been successfully installed and auto-renewal has been set up."


# sudo ./setup-ssl.sh -d example.com
# sudo ./setup-ssl.sh -r
# ./setup-ssl.sh -v
# ./setup-ssl.sh -h