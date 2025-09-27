#!/bin/bash

sudo certbot --apache -d $(cat /etc/hostname)
exit

# Check if script is run as root
if [ "$(id -u)" -ne 0 ]; then
    echo "This script must be run as root" 
    exit 1
fi

# Get server name from /etc/hostname
server_name=$(cat /etc/hostname)

# Enable SSL module
a2enmod ssl

# Update Apache virtual host configuration for SSL
cat <<EOF > /etc/apache2/sites-available/${server_name}_ssl.conf
<VirtualHost *:443>
    ServerName $server_name

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/$server_name/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/$server_name/privkey.pem

    # Redirect HTTP to HTTPS
    Redirect permanent / https://$server_name/
</VirtualHost>
EOF

# Enable the new SSL virtual host
a2ensite ${server_name}_ssl.conf

# Restart Apache to apply changes
systemctl restart apache2

echo "SSL/TLS setup complete. Your website is now accessible over HTTPS."
 
