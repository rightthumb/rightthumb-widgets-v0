#!/bin/bash

# Check if four arguments are provided
if [ "$#" -ne 4 ]; then
	echo "Usage: $0 <root_password> <database_name> <new_user> <new_user_password>"
	exit 1
fi

# Assign arguments to variables
MYSQL_ROOT_PASSWORD=$1
DB_NAME=$2
NEW_USER=$3
NEW_USER_PASSWORD=$4

# Create MySQL commands to create the user and grant privileges
MYSQL_CREATE_USER_COMMAND="CREATE USER IF NOT EXISTS '$NEW_USER'@'localhost' IDENTIFIED BY '$NEW_USER_PASSWORD';"
MYSQL_GRANT_COMMAND="GRANT ALL PRIVILEGES ON $DB_NAME.* TO '$NEW_USER'@'localhost';"
MYSQL_FLUSH_PRIVILEGES="FLUSH PRIVILEGES;"

# Execute MySQL commands
mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$MYSQL_CREATE_USER_COMMAND"
if [ $? -ne 0 ]; then
	echo "Error creating user '$NEW_USER'. Please check your credentials and try again."
	exit 1
fi

mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$MYSQL_GRANT_COMMAND"
if [ $? -ne 0 ]; then
	echo "Error granting privileges to user '$NEW_USER'. Please check your credentials and try again."
	exit 1
fi

mysql -u root -p"$MYSQL_ROOT_PASSWORD" -e "$MYSQL_FLUSH_PRIVILEGES"
if [ $? -ne 0 ]; then
	echo "Error flushing privileges. Please check your credentials and try again."
	exit 1
fi

echo "User '$NEW_USER' created and granted full permissions on database '$DB_NAME' successfully."