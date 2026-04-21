#!/bin/bash

set -e

echo ''
echo -e "\e[32m🚀 LampPack: Cross-Distro LAMP Web Setup + Firewall Configuration\e[39m"
echo ''

# 🧑‍🔒 Must run as root
if [[ "$EUID" -ne 0 ]]; then
    echo -e "\e[31m❌ Error: Run this script as root.\e[39m"
    exit 1
fi

# 🧪 Detect package manager
if command -v apt &>/dev/null; then
    PM="apt"
    UPDATE="apt update -y"
    INSTALL="apt install -y"
    CERTBOT="certbot python3-certbot-apache"
    PHP_PACKAGES="php libapache2-mod-php php-mbstring php-zip"
    APACHE_SERVICE="apache2"
    ENABLE_MODULES="a2enmod rewrite ssl"
elif command -v dnf &>/dev/null; then
    PM="dnf"
    UPDATE="dnf update -y"
    INSTALL="dnf install -y"
    CERTBOT="certbot python3-certbot-apache"
    PHP_PACKAGES="php php-mbstring php-zip"
    APACHE_SERVICE="httpd"
    ENABLE_MODULES=""
elif command -v yum &>/dev/null; then
    PM="yum"
    UPDATE="yum update -y"
    INSTALL="yum install -y"
    CERTBOT="certbot python3-certbot-apache"
    PHP_PACKAGES="php php-mbstring php-zip"
    APACHE_SERVICE="httpd"
    ENABLE_MODULES=""
elif command -v pacman &>/dev/null; then
    PM="pacman"
    UPDATE="pacman -Sy"
    INSTALL="pacman -S --noconfirm"
    CERTBOT="certbot certbot-apache"
    PHP_PACKAGES="php apache php-apache"
    APACHE_SERVICE="httpd"
    ENABLE_MODULES=""
else
    echo -e "\e[31m❌ Unsupported distro. No known package manager found (apt, yum, dnf, pacman)\e[39m"
    exit 1
fi

echo -e "\e[34m📦 Using package manager: $PM\e[39m"

# 🔄 Update system
echo -e "\e[34m🔄 Updating system packages...\e[39m"
eval "$UPDATE"

# 📥 Install core components
echo -e "\e[34m📥 Installing Apache, PHP, SSL, and core tools...\e[39m"
eval "$INSTALL $APACHE_SERVICE $PHP_PACKAGES zip sendmail $CERTBOT"

# 🔌 Enable Apache modules if needed
if [[ "$PM" == "apt" ]]; then
    echo -e "\e[34m🔌 Enabling Apache modules...\e[39m"
    eval "$ENABLE_MODULES" &>/dev/null
fi

# 🧹 Remove default site configs (optional)
if [[ "$PM" == "apt" ]]; then
    echo -e "\e[34m🧹 Cleaning up Apache defaults...\e[39m"
    rm -f /etc/apache2/sites-{enabled,available}/000-default.conf
fi

# 🌍 Permissions
echo -e "\e[34m🔧 Setting permissions for /var/www...\e[39m"
chmod -R 0755 /var/www
chown -R www-data:www-data /var/www || chown -R apache:apache /var/www

# 🔥 Configure Firewall
echo -e "\e[34m🔥 Checking and configuring firewall rules...\e[39m"

if command -v ufw &>/dev/null; then
    echo -e "\e[36m🛡️ Using ufw\e[39m"
    ufw allow 80/tcp   # HTTP
    ufw allow 443/tcp  # HTTPS
    ufw allow 25/tcp   # SMTP
    ufw allow 465/tcp  # SMTPS
    ufw allow 587/tcp  # Submission
    echo -e "\e[32m✅ Allowed common web/email ports via UFW\e[39m"
elif command -v firewall-cmd &>/dev/null; then
    echo -e "\e[36m🛡️ Using firewalld\e[39m"
    firewall-cmd --permanent --add-service=http
    firewall-cmd --permanent --add-service=https
    firewall-cmd --permanent --add-port=25/tcp
    firewall-cmd --permanent --add-port=465/tcp
    firewall-cmd --permanent --add-port=587/tcp
    firewall-cmd --reload
    echo -e "\e[32m✅ Allowed common web/email ports via firewalld\e[39m"
elif command -v iptables &>/dev/null; then
    echo -e "\e[36m🛡️ Using iptables\e[39m"
    iptables -C INPUT -p tcp --dport 80  -j ACCEPT || iptables -A INPUT -p tcp --dport 80  -j ACCEPT
    iptables -C INPUT -p tcp --dport 443 -j ACCEPT || iptables -A INPUT -p tcp --dport 443 -j ACCEPT
    iptables -C INPUT -p tcp --dport 25  -j ACCEPT || iptables -A INPUT -p tcp --dport 25  -j ACCEPT
    iptables -C INPUT -p tcp --dport 465 -j ACCEPT || iptables -A INPUT -p tcp --dport 465 -j ACCEPT
    iptables -C INPUT -p tcp --dport 587 -j ACCEPT || iptables -A INPUT -p tcp --dport 587 -j ACCEPT
    echo -e "\e[33m⚠️ iptables changes are temporary unless saved manually\e[39m"
    echo -e "\e[32m✅ Allowed common web/email ports via iptables\e[39m"
else
    echo -e "\e[31m⚠️ No supported firewall system detected. Skipping firewall config.\e[39m"
fi

# 🔁 Restart Apache
echo -e "\e[34m🔁 Restarting Apache ($APACHE_SERVICE)...\e[39m"
systemctl reload "$APACHE_SERVICE" || true
systemctl restart "$APACHE_SERVICE"

# ⬆️ Enable auto-upgrades if available
if [[ "$PM" == "apt" ]]; then
    echo -e "\e[34m📅 Enabling unattended upgrades...\e[39m"
    $INSTALL unattended-upgrades &>/dev/null
    dpkg-reconfigure -p critical unattended-upgrades &>/dev/null
fi

echo ''
echo -e "\e[32m✅ LampPack complete! Web server is ready for add-domain.sh\e[39m"
