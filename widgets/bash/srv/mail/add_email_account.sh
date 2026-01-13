#!/bin/bash

# Check if the correct number of arguments were passed
if [ "$#" -ne 5 ]; then
	echo "Usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME> <EMAIL_LOCAL_PART> <DOMAIN> <PASSWORD>"
	exit 1
fi

# Assign arguments to variables
DB_USER="$1"
DB_PASSWORD="$2"
DB_NAME="$3"
EMAIL_LOCAL_PART="$4"
DOMAIN="$5"
PASSWORD="$6"
# For password encryption, consider using a stronger method in production
ENCRYPTED_PASSWORD=$(doveadm pw -s SHA512-CRYPT -p "$PASSWORD")

# MySQL/MariaDB command to insert the new email account
mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" <<EOF
INSERT INTO virtual_users (domain_id, password , email)
SELECT domain_id, '$ENCRYPTED_PASSWORD', CONCAT('$EMAIL_LOCAL_PART', '@', '$DOMAIN') FROM virtual_domains WHERE name='$DOMAIN';
EOF

echo "Email account $EMAIL_LOCAL_PART@$DOMAIN added successfully."