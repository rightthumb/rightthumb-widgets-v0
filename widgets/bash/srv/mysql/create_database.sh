#!/bin/bash

# Check if two arguments are provided
if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <root_password> <database_name>"
	exit 1
fi

# Assign arguments to variables
MYSQL_ROOT_PASSWORD=$1
DB_NAME=$2

# MySQL command to create the database
MYSQL_CREATE_DB_COMMAND="CREATE DATABASE IF NOT EXISTS $DB_NAME;"

# Execute MySQL command to create the database and check for errors
mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$MYSQL_CREATE_DB_COMMAND"
if [ $? -ne 0 ]; then
	echo "Error creating MySQL database '$DB_NAME'. Please check your credentials and try again."
	exit 1
fi

echo "MySQL database '$DB_NAME' created successfully."