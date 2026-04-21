#!/bin/bash

set -e

# Help
if [[ -z "$1" || "$1" == "--help" || "$1" == "-h" ]]; then
	echo "Usage: $0 <domain>"
	echo "Example: $0 example.com"
	exit 1
fi

DOMAIN="$1"
WEBROOT="/var/www/$DOMAIN"
APACHE_CONF="/etc/apache2/sites-available/$DOMAIN.conf"

# Create web root
if [ ! -d "$WEBROOT" ]; then
	echo "[+] Creating web root at $WEBROOT"
	sudo mkdir -p "$WEBROOT"
	echo "<html><body><h1>Welcome to $DOMAIN</h1></body></html>" | sudo tee "$WEBROOT/index.html" > /dev/null
	sudo chown -R www-data:www-data "$WEBROOT"
else
	echo "[!] Web root already exists: $WEBROOT"
fi

# Create Apache config
if [ ! -f "$APACHE_CONF" ]; then
	echo "[+] Creating Apache config at $APACHE_CONF"
	sudo bash -c "cat > $APACHE_CONF" <<EOF
<VirtualHost *:80>
	ServerName $DOMAIN
	ServerAlias $DOMAIN
	DocumentRoot $WEBROOT
	ErrorLog \${APACHE_LOG_DIR}/$DOMAIN-error.log
	CustomLog \${APACHE_LOG_DIR}/$DOMAIN-access.log combined
</VirtualHost>
EOF
else
	echo "[!] Apache config already exists: $APACHE_CONF"
fi

# Enable site
echo "[+] Enabling site $DOMAIN"
sudo a2ensite "$DOMAIN.conf"

# Reload Apache to recognize the new site
echo "[+] Reloading Apache"
sudo systemctl reload apache2

# Request SSL cert and auto-enable HTTPS
echo "[+] Running Certbot for $DOMAIN"
sudo certbot --apache -d "$DOMAIN" -d "$DOMAIN" --non-interactive --agree-tos -m admin@$DOMAIN --redirect

echo "[✅] Done! Visit http://$DOMAIN or https://$DOMAIN"