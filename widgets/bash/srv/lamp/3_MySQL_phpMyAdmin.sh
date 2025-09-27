#!/bin/bash

set -e

echo ''
echo -e "\e[32m🔐 LampPack: MySQL + phpMyAdmin Installer with Auto Domain Config\e[39m"
echo ''

# 🧑‍🔒 Root check
if [[ "$EUID" -ne 0 ]]; then
    echo -e "\e[31m❌ Error: Run this script as root.\e[39m"
    exit 1
fi

# Ask for phpMyAdmin domain
read -rp $'\e[36m🌐 Enter subdomain for phpMyAdmin (e.g., db.example.com): \e[39m' DB_DOMAIN
if [[ -z "$DB_DOMAIN" ]]; then
    echo -e "\e[31m❌ Domain name is required. Exiting.\e[39m"
    exit 1
fi
ADMIN_EMAIL="admin@$DB_DOMAIN"

# Detect Package Manager
if command -v apt &>/dev/null; then
    PM="apt"
    UPDATE="apt update -y"
    INSTALL="apt install -y"
    OS_FAMILY="debian"
elif command -v dnf &>/dev/null; then
    PM="dnf"
    UPDATE="dnf update -y"
    INSTALL="dnf install -y"
    OS_FAMILY="rhel"
elif command -v yum &>/dev/null; then
    PM="yum"
    UPDATE="yum update -y"
    INSTALL="yum install -y"
    OS_FAMILY="rhel"
elif command -v pacman &>/dev/null; then
    PM="pacman"
    UPDATE="pacman -Sy"
    INSTALL="pacman -S --noconfirm"
    OS_FAMILY="arch"
else
    echo -e "\e[31m❌ Unsupported distro. No apt/dnf/yum/pacman found.\e[39m"
    exit 1
fi

echo -e "\e[34m📦 Using package manager: $PM\e[39m"
eval "$UPDATE"

# 🧪 Generate passwords
ROOT_PASS=$(openssl rand -base64 12)
APP_PASS=$(openssl rand -base64 12)
PMA_PASS=$(openssl rand -base64 12)

# 🧩 Install MySQL/MariaDB
echo -e "\e[34m🧩 Installing MySQL Server...\e[39m"
if [[ "$OS_FAMILY" == "debian" ]]; then
    echo "mysql-server mysql-server/root_password password $ROOT_PASS" | sudo debconf-set-selections
    echo "mysql-server mysql-server/root_password_again password $ROOT_PASS" | sudo debconf-set-selections
    eval "$INSTALL mysql-server"
else
    eval "$INSTALL mariadb mariadb-server"
    systemctl enable mariadb || systemctl enable mysqld
    systemctl start mariadb || systemctl start mysqld
fi

# 🔐 Secure MySQL manually
echo -e "\e[34m🔐 Securing MySQL...\e[39m"
mysql --user=root <<EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY '$ROOT_PASS';
DELETE FROM mysql.user WHERE User='';
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';
FLUSH PRIVILEGES;
EOF

# 💾 Save MySQL credentials
echo -e "\e[34m💾 Saving root credentials to /root/.my.cnf...\e[39m"
cat <<EOF > /root/.my.cnf
[client]
user=root
password=$ROOT_PASS
EOF
chmod 600 /root/.my.cnf

# Install phpMyAdmin
if [[ "$OS_FAMILY" == "debian" ]]; then
    echo -e "\e[34m📦 Installing phpMyAdmin...\e[39m"
    echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | sudo debconf-set-selections
    echo "phpmyadmin phpmyadmin/app-password-confirm password $PMA_PASS" | sudo debconf-set-selections
    echo "phpmyadmin phpmyadmin/mysql/admin-pass password $ROOT_PASS" | sudo debconf-set-selections
    echo "phpmyadmin phpmyadmin/mysql/app-pass password $APP_PASS" | sudo debconf-set-selections
    echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" | sudo debconf-set-selections
    eval "$INSTALL phpmyadmin"
else
    echo -e "\e[33m⚠️ Auto-install of phpMyAdmin not supported on $PM. Please install manually.\e[39m"
    exit 1
fi

# 🌐 Apache VirtualHost for phpMyAdmin
echo -e "\e[34m🌍 Creating Apache config for $DB_DOMAIN...\e[39m"
cat <<EOF > "/etc/apache2/sites-available/$DB_DOMAIN.conf"
<VirtualHost *:80>
    ServerName $DB_DOMAIN
    DocumentRoot /usr/share/phpmyadmin

    <Directory /usr/share/phpmyadmin>
        Options FollowSymLinks
        DirectoryIndex index.php
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog \${APACHE_LOG_DIR}/$DB_DOMAIN-error.log
    CustomLog \${APACHE_LOG_DIR}/$DB_DOMAIN-access.log combined
</VirtualHost>
EOF

a2ensite "$DB_DOMAIN.conf"
systemctl reload apache2

# 🔐 Certbot SSL for phpMyAdmin subdomain
echo -e "\e[34m🔐 Setting up HTTPS with Certbot...\e[39m"
certbot --apache -d "$DB_DOMAIN" --non-interactive --agree-tos -m "$ADMIN_EMAIL" --redirect

# 🔁 Restart Apache
echo -e "\e[34m🔁 Restarting Apache...\e[39m"
systemctl restart apache2 || systemctl restart httpd

# ✅ Summary
echo ''
echo -e "\e[32m✅ MySQL is installed and secured.\e[39m"
echo -e "\e[32m🔑 Root credentials saved to /root/.my.cnf\e[39m"
echo -e "\e[32m🌐 phpMyAdmin secured at: https://$DB_DOMAIN\e[39m"
