#!/bin/bash

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 example.com"
	exit 1
fi

cd /opt
echo "Install git"
sudo apt-get -y install git
echo "git clone https://github.com/rehmatworks/lamp-pack"
git clone https://github.com/rehmatworks/lamp-pack
chmod 777 -R lamp-pack
cd lamp-pack
echo "Installing..."
./sp-lamp.sh
echo "Creating virtual host"
spvhost create $1
echo "Adding SSL"
spssl main $1
echo "Force SSL: spssl sub $1 force"
echo "Website Root: /var/www"