#!/bin/bash

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Update package index and install Certbot
apt update
apt install certbot python3-certbot-apache -y

# Run Certbot to obtain and install the SSL certificate
certbot --apache --agree-tos --redirect --hsts --staple-ocsp --email your_email@example.com -d your_domain.com

# Restart Apache to apply changes
systemctl restart apache2

echo "SSL certificate setup complete. Your website is now accessible over HTTPS."
