#!/bin/bash

# Function to install MongoDB
install_mongo() {
  DISTRO=$(cat /etc/os-release | grep -i '^ID=' | cut -d= -f2)

  case $DISTRO in
	debian|ubuntu)
	echo "Installing MongoDB for Debian/Ubuntu..."
	sudo apt update
	sudo apt install -y mongodb
	;;
	fedora|centos|rhel)
	echo "Installing MongoDB for Fedora/CentOS/RHEL..."
	sudo dnf install -y mongodb
	;;
	arch)
	echo "Installing MongoDB for Arch Linux..."
	sudo pacman -Syu --noconfirm mongodb
	;;
	*)
	echo "Unknown distribution: $DISTRO. Please install MongoDB manually."
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
  echo "  -v, --version           Display script version"
  echo "  -u, --username <name>    MongoDB admin username"
  echo "  -p, --password <pass>    MongoDB admin password"
  echo "  -d, --database <name>    Name of the MongoDB database"
  echo ""
  echo "Examples:"
  echo "  $0 -u admin -p securepass -d mydatabase"
  echo "  $0 -v"
  echo ""
}

# Script version
SCRIPT_VERSION="1.0.0"
MONGO_USERNAME=""
MONGO_PASSWORD=""
MONGO_DATABASE=""

# Parse command line options
while [[ "$1" =~ ^- ]]; do
  case "$1" in
	-h|--help)
	show_help
	exit 0
	;;
	-v|--version)
	echo "setup-mongo.sh version $SCRIPT_VERSION"
	exit 0
	;;
	-u|--username)
	shift
	MONGO_USERNAME="$1"
	;;
	-p|--password)
	shift
	MONGO_PASSWORD="$1"
	;;
	-d|--database)
	shift
	MONGO_DATABASE="$1"
	;;
	*)
	echo "Invalid option: $1"
	show_help
	exit 1
	;;
  esac
  shift
done

# Check if MongoDB username and password are set
if [ -z "$MONGO_USERNAME" ] || [ -z "$MONGO_PASSWORD" ] || [ -z "$MONGO_DATABASE" ]; then
  echo "Error: MongoDB username, password, and database name are required."
  show_help
  exit 1
fi

# Install MongoDB if it is not installed
if ! command -v mongod &> /dev/null; then
  echo "'mongod' not found. Installing MongoDB..."
  install_mongo
fi

# Start MongoDB service
echo "Starting MongoDB service..."
sudo systemctl start mongodb
sudo systemctl enable mongodb

# Check MongoDB service status
echo "Checking MongoDB service status..."
sudo systemctl status mongodb

# Secure MongoDB (create admin user if not already created)
echo "Securing MongoDB with admin user..."
mongo <<EOF
use admin
db.createUser({
  user: "$MONGO_USERNAME",
  pwd: "$MONGO_PASSWORD",
  roles: [{ role: "root", db: "admin" }]
})
EOF

# Create the specified database if it doesn't already exist
echo "Creating MongoDB database '$MONGO_DATABASE'..."
mongo <<EOF
use $MONGO_DATABASE
EOF

echo "MongoDB setup completed!"


# ./setup-mongo.sh -u admin -p securepass -d mydatabase
# ./setup-mongo.sh -v
# sudo systemctl status mongodb