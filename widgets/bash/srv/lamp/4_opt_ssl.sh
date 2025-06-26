#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi

DOMAIN=$1
DOCUMENT_ROOT="/var/www/$DOMAIN"

# Update package list and install Certbot and the Apache plugin
echo "Updating package list..."
sudo apt update

echo "Installing Certbot and the Apache plugin..."
sudo apt install -y certbot python3-certbot-apache

# Obtain an SSL certificate
echo "Obtaining SSL certificate for $DOMAIN..."
sudo certbot --apache -d $DOMAIN

# Check if Certbot ran successfully
if [ $? -ne 0 ]; then
	echo "Certbot failed to obtain SSL certificate for $DOMAIN."
	exit 1
fi

# Enable the SSL module in Apache
echo "Enabling SSL module in Apache..."
sudo a2enmod ssl

# Create the document root directory if it doesn't exist
if [ ! -d "$DOCUMENT_ROOT" ]; then
	sudo mkdir -p $DOCUMENT_ROOT
	sudo chown -R $USER:$USER $DOCUMENT_ROOT
fi

# Add SSL configuration to the virtual host file
VHOST_FILE="/etc/apache2/sites-available/${DOMAIN}.conf"

if [ ! -f "$VHOST_FILE" ]; then
	echo "Virtual host file $VHOST_FILE not found. Creating a new one..."
	sudo bash -c "cat > $VHOST_FILE" <<EOL
<VirtualHost *:80>
	ServerName $DOMAIN
	DocumentRoot $DOCUMENT_ROOT

	<Directory $DOCUMENT_ROOT>
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	ErrorLog \${APACHE_LOG_DIR}/error.log
	CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

<VirtualHost *:443>
	ServerName $DOMAIN
	DocumentRoot $DOCUMENT_ROOT

	<Directory $DOCUMENT_ROOT>
		Options Indexes FollowSymLinks
		AllowOverride All
		Require all granted
	</Directory>

	ErrorLog \${APACHE_LOG_DIR}/error.log
	CustomLog \${APACHE_LOG_DIR}/access.log combined

	SSLEngine on
	SSLCertificateFile /etc/letsencrypt/live/$DOMAIN/fullchain.pem
	SSLCertificateKeyFile /etc/letsencrypt/live/$DOMAIN/privkey.pem
	Include /etc/letsencrypt/options-ssl-apache.conf
</VirtualHost>
EOL
fi

# Enable the new virtual host configuration
echo "Enabling virtual host configuration..."
sudo a2ensite ${DOMAIN}.conf

# Reload Apache to apply changes
echo "Reloading Apache..."
sudo systemctl reload apache2

echo "SSL installation and configuration for $DOMAIN is complete."