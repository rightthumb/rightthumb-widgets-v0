#!/bin/bash

# Script to create tables for an email system in a MySQL database

# Ensure the correct number of arguments were passed
if [ "$#" -ne 3 ]; then
	echo "Correct usage: $0 <DB_USER> <DB_PASSWORD> <DB_NAME>"
	exit 1
fi

# Assign arguments to variables for better readability
DB_USER="$1"
DB_PASSWORD="$2"
DB_NAME="$3"

# Create the tables within the database
# Note: Using -p without the password for security reasons; it's better to use .my.cnf or an environment variable for passwords
if mysql -u "$DB_USER" -p"$DB_PASSWORD" "$DB_NAME" <<EOF
CREATE TABLE IF NOT EXISTS virtual_domains (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS virtual_users (
	id INT NOT NULL AUTO_INCREMENT,
	domain_id INT NOT NULL,
	password VARCHAR(200) NOT NULL,
	email VARCHAR(100) NOT NULL,
	PRIMARY KEY (id),
	UNIQUE KEY email (email),
	FOREIGN KEY (domain_id) REFERENCES virtual_domains(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS virtual_aliases (
	id INT NOT NULL AUTO_INCREMENT,
	domain_id INT NOT NULL,
	source VARCHAR(100) NOT NULL,
	destination VARCHAR(100) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (domain_id) REFERENCES virtual_domains(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
EOF
then
	echo "Database tables created successfully."
else
	echo "Failed to create database tables. Please check your MySQL credentials and database name."
	exit 1
fi