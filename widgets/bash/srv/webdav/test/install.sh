#!/bin/bash

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Update package index and install necessary packages
apt update
apt install apache2 apache2-utils -y

# Enable required Apache modules
a2enmod dav
a2enmod dav_fs
a2enmod auth_digest

# Create directory for WebDAV
mkdir -p /var/www/webdav
chown www-data:www-data /var/www/webdav
chmod 775 /var/www/webdav

# Create a password file for WebDAV users
touch /etc/apache2/webdav.users
chown www-data:www-data /etc/apache2/webdav.users
chmod 640 /etc/apache2/webdav.users

# Configure Apache to use WebDAV
cat << EOF > /etc/apache2/sites-available/webdav.conf
Alias /webdav /var/www/webdav

<Directory /var/www/webdav>
    DAV On
    AuthType Basic
    AuthName "WebDAV"
    AuthUserFile /etc/apache2/webdav.users
    Require valid-user
</Directory>
EOF

# Enable the WebDAV site
a2ensite webdav.conf

# Restart Apache to apply changes
systemctl restart apache2
the_host=$(cat /etc/hostname)
echo "WebDAV setup complete. You can now access your WebDAV server at http://$the_host/webdav"

