#!/bin/bash

# Check if the correct number of arguments were passed
if [ "$#" -ne 4 ]; then
	echo "Usage: $0 <DB_ROOT_PASSWORD> <DB_NAME> <DB_USER> <DB_PASSWORD>"
	exit 1
fi

# Assign arguments to variables
DB_ROOT_PASSWORD="$1"
DB_NAME="$2"
DB_USER="$3"
DB_PASSWORD="$4"

# Install MariaDB
sudo apt-get update
sudo apt-get install -y mariadb-server

# Wait for user to manually secure MariaDB installation
echo "Please secure your MariaDB installation manually by running 'sudo mysql_secure_installation' before proceeding."

# Creating database and user, then setting permissions
sudo mysql -u root -p"$DB_ROOT_PASSWORD" <<EOF
CREATE DATABASE IF NOT EXISTS $DB_NAME;
CREATE USER IF NOT EXISTS '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';
GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$DB_USER'@'localhost';
FLUSH PRIVILEGES;
EOF

echo "Database and user setup completed."