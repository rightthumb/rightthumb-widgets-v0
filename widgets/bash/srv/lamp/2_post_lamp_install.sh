#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi

echo "Create virtual host"
spvhost create $1
echo "Installing Apache plugin for Lets encrypt"
sudo apt install certbot python3-certbot-apache -y
sudo certbot --apache
echo "Add SSL"
spssl main $1
echo "spssl sub $1 force"
echo "/var/www"