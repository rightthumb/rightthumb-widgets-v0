#!/bin/bash

# Check if three arguments are provided
if [ "$#" -ne 3 ]; then
	echo "Usage: $0 <root_password> <username> <password>"
	exit 1
fi

# Assign arguments to variables
MYSQL_ROOT_PASSWORD=$1
DB_USER=$2
DB_PASSWORD=$3

# MySQL command to create user
MYSQL_CREATE_USER_COMMAND="CREATE USER '$DB_USER'@'localhost' IDENTIFIED BY '$DB_PASSWORD';"

# Execute MySQL command
mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$MYSQL_CREATE_USER_COMMAND"

# Check if the command executed successfully
if [ $? -eq 0 ]; then
	echo "MySQL user '$DB_USER' created successfully."
else
	echo "Error creating MySQL user. Please check your credentials and try again."
fi