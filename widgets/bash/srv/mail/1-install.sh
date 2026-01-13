#!/bin/bash

# Update package lists
sudo apt-get update

sudo apt-get install dovecot-core

# Install Postfix, Dovecot (IMAP and POP3 server)
# For Postfix, select 'Internet Site' when prompted
echo "postfix postfix/mailname string your_domain.com" | sudo debconf-set-selections
echo "postfix postfix/main_mailer_type string 'Internet Site'" | sudo debconf-set-selections
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y postfix dovecot-core dovecot-imapd dovecot-pop3d

# Basic Postfix configuration for local only delivery
sudo postconf -e 'inet_interfaces = loopback-only'
sudo postconf -e 'mydestination = localhost'

# Basic Dovecot configuration to enable IMAP and POP3
sudo sed -i 's/#mail_location = /mail_location = mbox:~\/mail:INBOX=\/var\/mail\/%u/' /etc/dovecot/conf.d/10-mail.conf
sudo sed -i 's/#disable_plaintext_auth = yes/disable_plaintext_auth = no/' /etc/dovecot/conf.d/10-auth.conf
sudo sed -i 's/ssl = required/ssl = no/' /etc/dovecot/conf.d/10-ssl.conf

# Restart services to apply changes
sudo systemctl restart postfix
sudo systemctl restart dovecot

echo "Postfix and Dovecot installation completed."