#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi

sudo apt install certbot python3-certbot-apache -y
sudo certbot --apache

#   sudo certbot delete --cert-name "$DOMAIN"


echo "/var/www"