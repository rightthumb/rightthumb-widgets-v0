#!/bin/bash

# Variables
REPO_DIR="/var/www/myrepo"
HOSTNAME=$(cat /etc/hostname)
APACHE_CONFIG="/etc/apache2/sites-available/myrepo.conf"
PACKAGE_DIR=$(mktemp -d)

# Functions
install_repo() {
	# Set up the repository structure
	mkdir -p $REPO_DIR/{dists,binary}

	# Install required tools
	sudo apt-get update
	sudo apt-get install -y dpkg-dev apache2

	# Configure the web server
	sudo tee $APACHE_CONFIG > /dev/null <<EOL
<VirtualHost *:80>
	ServerAdmin admin@$HOSTNAME
	DocumentRoot $REPO_DIR
	ServerName $HOSTNAME

	<Directory $REPO_DIR>
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>

	ErrorLog \${APACHE_LOG_DIR}/error.log
	CustomLog \${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
EOL

	# Enable the site and reload Apache
	sudo a2ensite myrepo.conf
	sudo systemctl reload apache2

	echo "Repository setup complete. Add the following line to your /etc/apt/sources.list on the client machine:"
	echo "deb http://$HOSTNAME binary/"
}

start_repo() {
	sudo systemctl start apache2
	echo "Apache started."
}

stop_repo() {
	sudo systemctl stop apache2
	echo "Apache stopped."
}

restart_repo() {
	sudo systemctl restart apache2
	echo "Apache restarted."
}

add_package() {
	local package_name=$1
	local package_path=$2

	cp $package_path $REPO_DIR/binary/
	cd $REPO_DIR
	dpkg-scanpackages binary /dev/null | gzip -9c > binary/Packages.gz
	echo "Package $package_name added and Packages.gz updated."
}

add_folder() {
	local package_name=$1
	local folder_path=$2

	cd $PACKAGE_DIR
	mkdir -p DEBIAN
	echo "Package: $package_name" > DEBIAN/control
	echo "Version: 1.0" >> DEBIAN/control
	echo "Section: base" >> DEBIAN/control
	echo "Priority: optional" >> DEBIAN/control
	echo "Architecture: all" >> DEBIAN/control
	echo "Maintainer: Your Name <you@example.com>" >> DEBIAN/control
	echo "Description: $package_name package" >> DEBIAN/control

	cp -r $folder_path/* $PACKAGE_DIR/
	dpkg-deb --build . $REPO_DIR/binary/${package_name}_1.0_all.deb

	cd $REPO_DIR
	dpkg-scanpackages binary /dev/null | gzip -9c > binary/Packages.gz
	echo "Package $package_name created from folder and Packages.gz updated."
}

create_template() {
	local folder_path=$1

	mkdir -p $folder_path/usr/local/bin

	cat <<EOL > $folder_path/usr/local/bin/hello.py
#!/usr/bin/env python3

def main():
	print("Hello, World!")

if __name__ == "__main__":
	main()
EOL

	chmod +x $folder_path/usr/local/bin/hello.py

	mkdir -p $folder_path/DEBIAN

	cat <<EOL > $folder_path/DEBIAN/control
Package: mypythonapp
Version: 1.0
Section: base
Priority: optional
Architecture: all
Maintainer: Your Name <you@example.com>
Description: A simple Hello, World! Python app
EOL

	echo "Template created in $folder_path"
}

show_cmd() {
	echo "To add the repository and update the package list on a client machine, run:"
	echo "echo 'deb http://$HOSTNAME binary/' | sudo tee /etc/apt/sources.list.d/myrepo.list"
	echo "sudo apt-get update"
}

# Main Script
while [[ "$#" -gt 0 ]]; do
	case $1 in
		-i|--install) install_repo; shift ;;
		-start) start_repo; shift ;;
		-stop) stop_repo; shift ;;
		-restart) restart_repo; shift ;;
		-a|--add) add_package "$2" "$3"; shift 3 ;;
		-af|--add-folder) add_folder "$2" "$3"; shift 3 ;;
		--create) create_template "$2"; shift 2 ;;
		--cmd) show_cmd; shift ;;
		*) echo "Unknown parameter passed: $1"; exit 1 ;;
	esac
done

# sudo ./repo_manager.sh --install  # To install the repository
# sudo ./repo_manager.sh --start    # To start Apache
# sudo ./repo_manager.sh --stop     # To stop Apache
# sudo ./repo_manager.sh --restart  # To restart Apache
# sudo ./repo_manager.sh --add my-package /path/to/package.deb  # To add a package
# sudo ./repo_manager.sh --add-folder my-package /path/to/folder  # To add a folder as a package
# sudo ./repo_manager.sh --create /path/to/newfolder  # To create a template Python app
# sudo ./repo_manager.sh --cmd  # To get the repository installation command and update apt