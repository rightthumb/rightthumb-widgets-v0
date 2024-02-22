#!/bin/bash

# Check if the correct number of arguments were passed
if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME>"
	exit 1
fi

# Assign arguments to variables
DB_USER="$1"
DB_PASSWORD="$2"
DB_NAME="$3"
TABLE_NAME="virtual_users"

# Command to list all email addresses from the specified table
mysql -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e "SELECT email FROM $TABLE_NAME;"