#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Variables
REPO_DIR="/var/www/myrepo"
HOSTNAME=$(hostname -f)
APACHE_CONFIG="/etc/apache2/sites-available/myrepo.conf"
GPG_KEY_NAME=""
GPG_KEY_EMAIL=""
GPG_PASSPHRASE=""
CODENAMES=""
ARCHITECTURES=""
PACKAGE_DIR=$(mktemp -d)

# Functions
echo_info() {
	echo -e "\e[34m[INFO]\e[0m $1"
}

echo_success() {
	echo -e "\e[32m[SUCCESS]\e[0m $1"
}

echo_error() {
	echo -e "\e[31m[ERROR]\e[0m $1"
}

install_repo() {
	echo_info "Starting repository installation..."

	# Prompt for repository configuration
	read -p "Enter your repository domain (e.g., repo.example.com) or IP address: " REPO_DOMAIN
	read -p "Enter your name for the GPG key: " GPG_KEY_NAME
	read -p "Enter your email for the GPG key: " GPG_KEY_EMAIL
	read -s -p "Enter a passphrase for the GPG key (leave empty for no passphrase): " GPG_PASSPHRASE
	echo
	read -p "Enter the distribution codename(s) you want to support (separated by space, e.g., focal bionic): " CODENAMES
	read -p "Enter the architectures you want to support (e.g., amd64 i386): " ARCHITECTURES

	# Update package lists
	echo_info "Updating package lists..."
	sudo apt-get update

	# Install required packages
	echo_info "Installing required packages: reprepro, gnupg, apache2..."
	sudo apt-get install -y reprepro gnupg apache2 wget curl dpkg-dev

	# Set up the repository structure
	echo_info "Creating repository directory structure at $REPO_DIR..."
	sudo mkdir -p $REPO_DIR/{conf,dists,pool,logs}

	# Configure reprepro
	echo_info "Configuring reprepro..."
	sudo tee $REPO_DIR/conf/distributions > /dev/null <<EOL
Origin: $GPG_KEY_NAME
Label: $REPO_DOMAIN
Suite: stable
Codename: $(echo $CODENAMES | awk '{print $1}')  # Using the first codename for initial setup
Version: 1.0
Architectures: $ARCHITECTURES
Components: main
Description: Personal APT Repository
SignWith: yes
EOL

	# Generate GPG key
	echo_info "Generating GPG key..."
	GPG_BATCH=$(mktemp)
	sudo tee "$GPG_BATCH" > /dev/null <<EOF
	%echo Generating a GPG key
	Key-Type: RSA
	Key-Length: 4096
	Name-Real: $GPG_KEY_NAME
	Name-Email: $GPG_KEY_EMAIL
	Expire-Date: 0
	Passphrase: $GPG_PASSPHRASE
	%commit
	%echo Done
EOF

	sudo gpg --batch --generate-key "$GPG_BATCH"
	rm "$GPG_BATCH"

	# Get the GPG key ID
	GPG_KEY_ID=$(sudo gpg --list-keys --with-colons "$GPG_KEY_EMAIL" | awk -F: '/^pub/ {print $5}')
	echo_success "Generated GPG key with ID: $GPG_KEY_ID"

	# Export the public key
	echo_info "Exporting public GPG key..."
	sudo gpg --export -a "$GPG_KEY_EMAIL" | sudo tee $REPO_DIR/conf/public.key > /dev/null
	echo_success "Exported public GPG key to $REPO_DIR/conf/public.key"

	# Set permissions
	sudo chown -R www-data:www-data $REPO_DIR

	# Configure Apache to serve the repository
	echo_info "Configuring Apache web server..."
	sudo tee $APACHE_CONFIG > /dev/null <<EOL
<VirtualHost *:80>
	ServerAdmin admin@$HOSTNAME
	ServerName $REPO_DOMAIN
	DocumentRoot $REPO_DIR

	<Directory $REPO_DIR>
		Options Indexes FollowSymLinks
		AllowOverride None
		Require all granted
	</Directory>

	ErrorLog \${APACHE_LOG_DIR}/myrepo_error.log
	CustomLog \${APACHE_LOG_DIR}/myrepo_access.log combined
</VirtualHost>
EOL

	# Enable the new site and disable the default
	echo_info "Enabling Apache site configuration..."
	sudo a2dissite 000-default.conf
	sudo a2ensite myrepo.conf

	# Reload Apache to apply changes
	echo_info "Reloading Apache..."
	sudo systemctl reload apache2
	echo_success "Apache configured and reloaded."

	# Import GPG key into reprepro
	echo_info "Importing GPG key into reprepro..."
	sudo cp $REPO_DIR/conf/public.key $REPO_DIR/conf/repo-key.gpg

	# Provide repository access instructions
	echo_success "Repository setup complete."
	echo_info "To add packages to your repository, use the following command:"
	echo "reprepro -b $REPO_DIR includedeb <codename> /path/to/your-package.deb"

	# Provide client setup instructions
	echo_info "Setup Instructions for Client Servers:"
	echo "---------------------------------------"
	echo "1. Import the GPG key:"
	echo "   wget -O /usr/share/keyrings/myrepo.gpg http://$REPO_DOMAIN/conf/public.key"
	echo
	echo "2. Add the repository to your sources list:"
	echo "   echo 'deb [signed-by=/usr/share/keyrings/myrepo.gpg] http://$REPO_DOMAIN/ $(echo $CODENAMES | awk '{print $1}') main' | sudo tee /etc/apt/sources.list.d/myrepo.list"
	echo
	echo "3. Update package lists and install your package:"
	echo "   sudo apt update"
	echo "   sudo apt install <your-package>"

	# Create a client setup script
	echo_info "Creating a client setup script at /usr/local/bin/add-myrepo.sh..."
	CLIENT_SCRIPT="/usr/local/bin/add-myrepo.sh"

	sudo tee $CLIENT_SCRIPT > /dev/null <<EOF
#!/bin/bash

echo "Adding APT repository from $REPO_DOMAIN..."

# Import the GPG key
wget -O /usr/share/keyrings/myrepo.gpg http://$REPO_DOMAIN/conf/public.key

# Add the repository to sources.list
echo "deb [signed-by=/usr/share/keyrings/myrepo.gpg] http://$REPO_DOMAIN/ $(echo $CODENAMES | awk '{print $1}') main" | sudo tee /etc/apt/sources.list.d/myrepo.list

# Update package lists
sudo apt update

echo "Repository added successfully. You can now install packages from the repository."
EOF

	sudo chmod +x $CLIENT_SCRIPT
	echo_success "Client setup script created at $CLIENT_SCRIPT."
	echo_info "You can run this script on client servers to automatically add the repository."
}

start_repo() {
	echo_info "Starting Apache web server..."
	sudo systemctl start apache2
	echo_success "Apache started."
}

stop_repo() {
	echo_info "Stopping Apache web server..."
	sudo systemctl stop apache2
	echo_success "Apache stopped."
}

restart_repo() {
	echo_info "Restarting Apache web server..."
	sudo systemctl restart apache2
	echo_success "Apache restarted."
}

add_package() {
	local package_path=$1
	local codename=$2

	if [[ -z "$package_path" || -z "$codename" ]]; then
		echo_error "Usage: -a|--add /path/to/package.deb <codename>"
		exit 1
	fi

	echo_info "Adding package $package_path to codename $codename..."
	sudo reprepro -b $REPO_DIR includedeb $codename $package_path
	echo_success "Package added successfully."
}

add_folder() {
	local folder_path=$1
	local codename=$2

	if [[ -z "$folder_path" || -z "$codename" ]]; then
		echo_error "Usage: -af|--add-folder /path/to/folder <codename>"
		exit 1
	fi

	echo_info "Creating package from folder $folder_path for codename $codename..."

	mkdir -p $PACKAGE_DIR/$folder_path/DEBIAN
	cp -r $folder_path/* $PACKAGE_DIR/
	dpkg-deb --build $PACKAGE_DIR $REPO_DIR/pool/main/$(basename $folder_path)_1.0_all.deb

	sudo reprepro -b $REPO_DIR includedeb $codename $REPO_DIR/pool/main/$(basename $folder_path)_1.0_all.deb
	echo_success "Package created from folder and added to repository."
}

create_template() {
	local package_name=$1

	if [[ -z "$package_name" ]]; then
		echo_error "Usage: --create <package_name>"
		exit 1
	fi

	echo_info "Creating package template for $package_name..."
	mkdir -p $PACKAGE_DIR/$package_name/usr/local/bin

	cat <<EOL > $PACKAGE_DIR/$package_name/usr/local/bin/$package_name.py
#!/usr/bin/env python3

def main():
	print("Hello, World!")

if __name__ == "__main__":
	main()
EOL

	chmod +x $PACKAGE_DIR/$package_name/usr/local/bin/$package_name.py

	mkdir -p $PACKAGE_DIR/$package_name/DEBIAN

	cat <<EOL > $PACKAGE_DIR/$package_name/DEBIAN/control
Package: $package_name
Version: 1.0
Section: base
Priority: optional
Architecture: all
Maintainer: Your Name <you@example.com>
Description: A simple Hello, World! Python app
EOL

	dpkg-deb --build $PACKAGE_DIR/$package_name $REPO_DIR/pool/main/${package_name}_1.0_all.deb
	echo_success "Template package created at $REPO_DIR/pool/main/${package_name}_1.0_all.deb"
}

# Main Script
if [[ "$EUID" -ne 0 ]]; then
	echo_error "Please run as root or use sudo."
	exit 1
fi

if [[ $# -eq 0 ]]; then
	echo "Usage: $0 {--install|-i|--start|-start|--stop|-stop|--restart|-restart|--add|-a|--add-folder|-af|--create}"
	exit 1
fi

while [[ "$#" -gt 0 ]]; do
	case $1 in
		-i|--install)
			install_repo
			shift
			;;
		-start)
			start_repo
			shift
			;;
		-stop)
			stop_repo
			shift
			;;
		-restart)
			restart_repo
			shift
			;;
		-a|--add)
			add_package "$2" "$3"
			shift 3
			;;
		-af|--add-folder)
			add_folder "$2" "$3"
			shift 3
			;;
		--create)
			create_template "$2"
			shift 2
			;;
		*)
			echo_error "Unknown parameter passed: $1"
			echo "Usage: $0 {--install|-i|--start|-start|--stop|-stop|--restart|-restart|--add|-a|--add-folder|-af|--create}"
			exit 1
			;;
	esac
done