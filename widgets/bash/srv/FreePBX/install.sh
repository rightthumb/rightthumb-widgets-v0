#!/bin/bash

# Function to display error and exit
display_error() {
    echo "Error: $1"
    exit 1
}

# Check if the script is run with root privileges
if [[ $EUID -ne 0 ]]; then
   display_error "This script must be run as root"
fi

# Update the system
apt update || display_error "Failed to update the system"
apt upgrade -y || display_error "Failed to upgrade the system"

# Install dependencies
apt install -y wget mariadb-server apache2 build-essential php php-{cli,pear,opcache,mbstring,xml,xmlrpc,curl,gd,intl,ldap,imap,json,pgsql,snmp,sqlite,xmlrpc,mysql,mongodb} || display_error "Failed to install required packages"

# Start and enable services
systemctl start mariadb apache2 || display_error "Failed to start services"
systemctl enable mariadb apache2 || display_error "Failed to enable services"

# Download and install FreePBX
cd /usr/src || display_error "Failed to change directory to /usr/src"
wget http://mirror.freepbx.org/modules/packages/freepbx/freepbx-15.0-latest.tgz || display_error "Failed to download FreePBX"
tar xf freepbx-15.0-latest.tgz || display_error "Failed to extract FreePBX"
cd freepbx || display_error "FreePBX directory not found"

# Set permissions
chown -R asterisk:asterisk /var/www/html
chmod -R 775 /var/www/html
fwconsole chown || display_error "Failed to set permissions"

# Run FreePBX installation script
./start_asterisk start || display_error "Failed to start Asterisk"
./install -n || display_error "Failed to install FreePBX"

echo "FreePBX installation completed successfully"
echo "You can access FreePBX web interface by visiting http://your_server_ip/admin"

exit 0
