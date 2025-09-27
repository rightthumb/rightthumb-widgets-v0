#!/bin/bash

# Check if the script is run as root
if [ "$(id -u)" -ne "0" ]; then
  echo "This script must be run as root" 1>&2
  exit 1
fi

# Assign arguments to variables
POSTFIX_USER=$1
POSTFIX_PASSWORD=$2
HOSTS=$3
DBNAME=$4

# Check if all arguments are provided
if [ -z "$POSTFIX_USER" ] || [ -z "$POSTFIX_PASSWORD" ] || [ -z "$HOSTS" ] || [ -z "$DBNAME" ]; then
  echo "Usage: $0 <postfix_user> <postfix_password> <hosts> <dbname>"
  exit 1
fi

# Create mysql-virtual-alias-maps.cf
cat << EOF > /etc/postfix/mysql-virtual-alias-maps.cf
# MySQL connection parameters
user = $POSTFIX_USER
password = $POSTFIX_PASSWORD
hosts = $HOSTS
dbname = $DBNAME

# Query to retrieve alias mappings
query = SELECT destination FROM virtual_aliases WHERE source='%s'
EOF
echo "Created: /etc/postfix/mysql-virtual-alias-maps.cf"

# Create mysql-virtual-mailbox-domains.cf
cat << EOF > /etc/postfix/mysql-virtual-mailbox-domains.cf
# MySQL connection parameters
user = $POSTFIX_USER
password = $POSTFIX_PASSWORD
hosts = $HOSTS
dbname = $DBNAME

# Query to retrieve alias mappings
query = SELECT domain FROM virtual_domains WHERE domain='%s'
EOF
echo "Created: /etc/postfix/mysql-virtual-mailbox-domains.cf"

# Create mysql-virtual-mailbox-maps.cf
cat << EOF > /etc/postfix/mysql-virtual-mailbox-maps.cf
# MySQL connection parameters
user = $POSTFIX_USER
password = $POSTFIX_PASSWORD
hosts = $HOSTS
dbname = $DBNAME

# Query to retrieve alias mappings
query = SELECT mailbox FROM virtual_mailboxes WHERE email='%s'
EOF
echo "Created: /etc/postfix/mysql-virtual-mailbox-maps.cf"

cat /opt/rightthumb-widgets-v0/widgets/bash/srv/mail/config/main.cf >> /etc/postfix/main.cf