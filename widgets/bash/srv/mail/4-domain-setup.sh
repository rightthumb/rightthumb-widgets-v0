#!/bin/bash

# Check if the correct number of arguments were passed
if [ "$#" -ne 4 ]; then
	echo "Usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME> <DOMAIN_NAME>"
	exit 1
fi

# Assign arguments to variables
DB_USER="$1"
DB_PASSWORD="$2"
DB_NAME="$3"
DOMAIN_NAME="$4"

# Command to insert the new domain into the virtual_domains table
mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" <<EOF
INSERT INTO virtual_domains (name) VALUES ('$DOMAIN_NAME');
EOF

if [ $? -eq 0 ]; then
	echo "Domain '$DOMAIN_NAME' added successfully."
else
	echo "Failed to add domain '$DOMAIN_NAME'."
fi