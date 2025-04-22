#!/bin/bash

# Check if MySQL is already installed by querying the package status
if ! dpkg-query -W -f='${Status}' mysql-server | grep -q "ok installed"; then
    echo "MySQL is not installed. Proceeding with the installation."

    # Update your package index
    sudo apt-get update

    # Install MySQL Server in a Non-Interactive mode. Default root password will be "root"
    echo "mysql-server mysql-server/root_password password root" | sudo debconf-set-selections
    echo "mysql-server mysql-server/root_password_again password root" | sudo debconf-set-selections

    # Install MySQL
    sudo apt-get install -y mysql-server

    echo "MySQL has been installed."
else
    echo "MySQL is already installed."
fi

# Echo command to secure MySQL installation
echo "Run 'sudo mysql_secure_installation' to secure your MySQL installation."
