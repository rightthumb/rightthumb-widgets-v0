#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi

# Variables
DOMAIN=$1
INSTALLER="SPSS_Statistics_Installer.bin"
PROPERTIES_FILE="installer.properties"

# Function to install SPSS
install_spss() {
    echo "Updating package list and installing dependencies for SPSS..."
    sudo apt-get update
    sudo apt-get install -y libc6 libncurses5 libstdc++6 libaio1

    echo "Making SPSS installer executable..."
    chmod +x $INSTALLER

    echo "Running SPSS installer..."
    sudo ./$INSTALLER -i silent -f $PROPERTIES_FILE

    echo "SPSS installation completed."
}

# Create virtual host
echo "Creating virtual host for $DOMAIN..."
spvhost create $DOMAIN

# Install Apache plugin for Let's Encrypt
echo "Installing Apache plugin for Let's Encrypt..."
sudo apt install certbot python3-certbot-apache -y

# Obtain and install SSL certificate
echo "Obtaining and installing SSL certificate for $DOMAIN..."
sudo certbot --apache

# Add SSL
echo "Adding SSL for $DOMAIN..."
spssl main $DOMAIN
echo "spssl sub $DOMAIN force"

# Print web root directory
echo "/var/www"

# Call the SPSS installation function
install_spss


# #!/bin/bash

# # Check if at least one argument is provided
# if [ $# -lt 1 ]; then
# 	echo "Usage: $0 example.com"
# 	exit 1
# fi

# echo "Create virtual host"
# spvhost create $1
# echo "Installing Apache plugin for Lets encrypt"
# sudo apt install certbot python3-certbot-apache -y
# sudo certbot --apache
# echo "Add SSL"
# spssl main $1
# echo "spssl sub $1 force"
# echo "/var/www"