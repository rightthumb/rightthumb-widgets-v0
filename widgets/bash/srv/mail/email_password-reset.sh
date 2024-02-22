#!/bin/bash

# Check if the correct number of arguments were passed
if [ "$#" -ne 4 ]; then
	echo "Usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME> <EMAIL_ADDRESS> <NEW_PASSWORD>"
	exit 1
fi

# Assign arguments to variables
DB_USER="$1"
DB_PASSWORD="$2"
DB_NAME="$3"
EMAIL_ADDRESS="$4"
NEW_PASSWORD="$5"
# Encrypt the new password using Dovecot's doveadm utility
ENCRYPTED_PASSWORD=$(doveadm pw -s SHA512-CRYPT -p "$NEW_PASSWORD")

# Connect to the database and update the user's password
mysql -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e \
"UPDATE virtual_users SET password='$ENCRYPTED_PASSWORD' WHERE email='$EMAIL_ADDRESS';"

if [ $? -eq 0 ]; then
	echo "Password for $EMAIL_ADDRESS updated successfully."
else
	echo "Failed to update password for $EMAIL_ADDRESS."
fi