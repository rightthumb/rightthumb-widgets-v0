#!/bin/bash

set -e

echo ''
echo -e "\e[32m📨 LampPack: Full Mail Server + Webmail Setup (Auto Config)\e[39m"
echo ''

# 🧑‍🔒 Root check
if [[ "$EUID" -ne 0 ]]; then
    echo -e "\e[31m❌ Error: Run this script as root.\e[39m"
    exit 1
fi

# 🌐 Ask for mail domain
read -rp $'\e[36m🌍 Enter the domain/subdomain for webmail (e.g., webmail.example.com): \e[39m' MAIL_DOMAIN
if [[ -z "$MAIL_DOMAIN" ]]; then
    echo -e "\e[31m❌ Domain name is required. Exiting.\e[39m"
    exit 1
fi

ADMIN_EMAIL="admin@$MAIL_DOMAIN"

# 🔍 Detect package manager
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

# ✉️ Install mail stack
echo -e "\e[34m📬 Installing Postfix + Dovecot...\e[39m"
eval "$INSTALL postfix dovecot-core dovecot-imapd dovecot-pop3d dovecot-lmtpd dovecot-mysql mailutils"

systemctl enable postfix dovecot
systemctl restart postfix dovecot

# 🌐 Install RainLoop Webmail
echo -e "\e[34m🌐 Installing RainLoop Webmail...\e[39m"
mkdir -p /var/www/$MAIL_DOMAIN
cd /var/www/$MAIL_DOMAIN
curl -sL https://www.rainloop.net/repository/webmail/rainloop-community-latest.zip -o rainloop.zip
unzip -oq rainloop.zip
rm rainloop.zip
chown -R www-data:www-data . || chown -R apache:apache .

# 🌍 Apache config
APACHE_CONF="/etc/apache2/sites-available/$MAIL_DOMAIN.conf"
cat <<EOF > "$APACHE_CONF"
<VirtualHost *:80>
    ServerName $MAIL_DOMAIN
    DocumentRoot /var/www/$MAIL_DOMAIN

    <Directory /var/www/$MAIL_DOMAIN>
        AllowOverride All
        Require all granted
    </Directory>

    ErrorLog \${APACHE_LOG_DIR}/$MAIL_DOMAIN-error.log
    CustomLog \${APACHE_LOG_DIR}/$MAIL_DOMAIN-access.log combined
</VirtualHost>
EOF

a2ensite "$MAIL_DOMAIN.conf"
systemctl reload apache2

# 🔐 Certbot SSL
echo -e "\e[34m🔐 Securing $MAIL_DOMAIN with Certbot...\e[39m"
certbot --apache -d "$MAIL_DOMAIN" --non-interactive --agree-tos -m "$ADMIN_EMAIL" --redirect

# 🔥 Firewall config
echo -e "\e[34m🔥 Opening required ports for mail and webmail...\e[39m"
if command -v ufw &>/dev/null; then
    ufw allow 25,465,587,993,995,143,110,80,443/tcp
elif command -v firewall-cmd &>/dev/null; then
    firewall-cmd --permanent --add-port=25/tcp
    firewall-cmd --permanent --add-port=465/tcp
    firewall-cmd --permanent --add-port=587/tcp
    firewall-cmd --permanent --add-port=993/tcp
    firewall-cmd --permanent --add-port=995/tcp
    firewall-cmd --permanent --add-port=143/tcp
    firewall-cmd --permanent --add-port=110/tcp
    firewall-cmd --permanent --add-port=80/tcp
    firewall-cmd --permanent --add-port=443/tcp
    firewall-cmd --reload
elif command -v iptables &>/dev/null; then
    iptables -C INPUT -p tcp --dport 25  -j ACCEPT || iptables -A INPUT -p tcp --dport 25 -j ACCEPT
    iptables -C INPUT -p tcp --dport 465 -j ACCEPT || iptables -A INPUT -p tcp --dport 465 -j ACCEPT
    iptables -C INPUT -p tcp --dport 587 -j ACCEPT || iptables -A INPUT -p tcp --dport 587 -j ACCEPT
    iptables -C INPUT -p tcp --dport 993 -j ACCEPT || iptables -A INPUT -p tcp --dport 993 -j ACCEPT
    iptables -C INPUT -p tcp --dport 995 -j ACCEPT || iptables -A INPUT -p tcp --dport 995 -j ACCEPT
    iptables -C INPUT -p tcp --dport 143 -j ACCEPT || iptables -A INPUT -p tcp --dport 143 -j ACCEPT
    iptables -C INPUT -p tcp --dport 110 -j ACCEPT || iptables -A INPUT -p tcp --dport 110 -j ACCEPT
    iptables -C INPUT -p tcp --dport 80  -j ACCEPT || iptables -A INPUT -p tcp --dport 80  -j ACCEPT
    iptables -C INPUT -p tcp --dport 443 -j ACCEPT || iptables -A INPUT -p tcp --dport 443 -j ACCEPT
    echo -e "\e[33m⚠️ Remember to save your iptables rules manually!\e[39m"
else
    echo -e "\e[33m⚠️ No known firewall tool found. Skipping firewall config.\e[39m"
fi

# ✅ Done
echo ''
echo -e "\e[32m✅ Mail server + RainLoop webmail is ready!\e[39m"
echo -e "\e[36m📬 Access your email at: https://$MAIL_DOMAIN\e[39m"
echo -e "\e[90mℹ️ You can log into RainLoop with any system mailbox or virtual mail user you create.\e[39m"
