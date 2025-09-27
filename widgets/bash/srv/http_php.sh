#!/bin/bash

# 📌 HTTP-only PHP Web Server Setup
# Usage: ./setup_http_php.sh yourdomain.com

# Exit on errors
set -e

DOMAIN="$1"
if [[ -z "$DOMAIN" ]]; then
	echo -e "\nUsage: $0 <domain>\nExample: $0 domain.com\n"
	exit 1
fi

FIRST_RUN=false

# 🔍 Detect OS and setup env
if which apt &>/dev/null; then
	PM_INSTALL="apt install -y"
	UPDATE_CMD="apt update -y"
	APACHE_USER="www-data"
	CONF_DIR="/etc/apache2/sites-available"
	ENABLE_SITE="a2ensite"
	RELOAD_CMD="systemctl reload apache2"
	APACHE_BIN="apache2"
elif which dnf &>/dev/null || which yum &>/dev/null; then
	PM_INSTALL="dnf install -y"
	UPDATE_CMD="dnf update -y"
	APACHE_USER="apache"
	CONF_DIR="/etc/httpd/conf.d"
	ENABLE_SITE="echo"  # no-op
	RELOAD_CMD="systemctl reload httpd"
	APACHE_BIN="httpd"
else
	echo "❌ Unsupported package manager"
	exit 1
fi

# 📦 Install missing dependencies
function ensure_installed() {
	local bin="$1"
	local pkg="$2"
	local name="$3"
	if ! which "$bin" &>/dev/null; then
		echo "📦 Installing $name..."
		eval "$PM_INSTALL $pkg"
		FIRST_RUN=true
	else
		echo "✅ $name already installed."
	fi
}

echo "🔄 Updating..."
eval "$UPDATE_CMD"

ensure_installed "$APACHE_BIN" "apache2 httpd" "Apache"
ensure_installed "php" "php" "PHP"

# 📁 Web root & vhost
DOCROOT="/var/www/$DOMAIN"
VHOST_CONF="$CONF_DIR/$DOMAIN.conf"

# 🔁 Handle existing vhost
if [[ -f "$VHOST_CONF" ]]; then
	echo "⚠️  Virtual host for $DOMAIN already exists."
	read -p "Do you want to remove and rebuild it? (y/N): " yn
	if [[ "$yn" =~ ^[Yy]$ ]]; then
		echo "🗑️  Removing old vhost and web root"
		sudo rm -f "$VHOST_CONF"
		sudo rm -rf "$DOCROOT"
	else
		echo "❌ Aborting."
		exit 0
	fi
fi

# 📂 Create root + index
mkdir -p "$DOCROOT"
echo "<?php phpinfo(); ?>" > "$DOCROOT/index.php"
chown -R $APACHE_USER:$APACHE_USER "$DOCROOT"

# 🌐 Build vhost
echo "🌐 Creating vhost config"
cat <<EOF | sudo tee "$VHOST_CONF" > /dev/null
<VirtualHost *:80>
	ServerName $DOMAIN
	DocumentRoot $DOCROOT
	<Directory $DOCROOT>
		AllowOverride All
		Require all granted
	</Directory>
	ErrorLog /var/log/apache2/${DOMAIN}-error.log
	CustomLog /var/log/apache2/${DOMAIN}-access.log combined
</VirtualHost>
EOF

# ✅ Enable site (Debian)
if [[ "$ENABLE_SITE" != "echo" ]]; then
	$ENABLE_SITE "$DOMAIN"
fi

# 🧠 Add to /etc/hosts
if ! grep -q "$DOMAIN" /etc/hosts; then
	echo "🧠 Mapping $DOMAIN to 127.0.0.1"
	echo "127.0.0.1 $DOMAIN" | sudo tee -a /etc/hosts > /dev/null
fi

# 🔁 Reload Apache
echo "🔁 Reloading Apache..."
if apachectl configtest | grep -q "Syntax OK"; then
	if $RELOAD_CMD; then
		echo "✅ Apache reloaded"
	else
		echo "❌ Apache reload failed. Check status with:"
		echo "   systemctl status $APACHE_BIN"
		exit 1
	fi
else
	echo "❌ Apache config syntax error. Run: apachectl configtest"
	exit 1
fi

# 🎉 Done
echo -e "\n✅ Domain ready: http://$DOMAIN"