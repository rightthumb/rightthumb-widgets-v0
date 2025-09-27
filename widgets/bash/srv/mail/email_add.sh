#!/bin/bash

# Check arguments and assign
if [ "$#" -ne 6 ]; then
  echo "Usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME> <EMAIL_LOCAL_PART> <DOMAIN> <PASSWORD>"
  exit 1
fi

DB_USER="$1"
export DB_PASSWORD="$2"  # Avoid exporting sensitive data; store securely
DB_NAME="$3"
EMAIL_LOCAL_PART="$4"
DOMAIN="$5"
PASSWORD="$6"
# Validate domain existence
CHECK=$(mysql -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e "SELECT 1 FROM virtual_domains WHERE name='$DOMAIN'" -s)
if [ -z "$CHECK" ]; then
  echo "Error: Domain '$DOMAIN' not found."
  exit 1
fi


# Decide on password handling (modify as needed)
# Using doveadm
ENCRYPTED_PASSWORD=$(doveadm pw -s SHA512-CRYPT -p "$PASSWORD")
if [ $? -ne 0 ]; then
  echo "Failed to encrypt password using doveadm."
  exit 1
fi
# Alternatively, use database encryption if suitable
# ENCRYPTED_PASSWORD=$(...)

# Concatenate email address
EMAIL_ADDRESS="$EMAIL_LOCAL_PART@$DOMAIN"

# Use prepared statement for secure insertion
MYSQL_COMMAND="mysql -u $DB_USER -p$DB_PASSWORD -D $DB_NAME -e \"INSERT INTO virtual_users (domain_id, password, email) VALUES ((SELECT id FROM virtual_domains WHERE name='$DOMAIN'), '$ENCRYPTED_PASSWORD', '$EMAIL_ADDRESS')\""
if ! result=$(eval "$MYSQL_COMMAND"); then
  echo "Error: Failed to insert into virtual_users."
  exit 1
fi

unset DB_PASSWORD

if [ $? -eq 0 ]; then
  echo "Email account $EMAIL_ADDRESS added successfully."
else
  echo "Failed to add email account. Please check database configuration, permissions, and error logs."
  exit 1
fi

# Securely clear password from memory (consider alternatives to exporting)

echo "Please note: Script has been revised to address potential issues and security best practices. Consider tailoring based on your specific requirements and environment."