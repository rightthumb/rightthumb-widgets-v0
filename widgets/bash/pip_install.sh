#!/bin/bash

# Get hostname from /etc/hostname
hostname=$(cat /etc/hostname)

# Check if arguments are provided
if [ $# -eq 0 ]; then
	echo "No package(s) specified for installation."
	exit 1
fi

# Function to install package using pip and fallback to apt
install_package() {
	local package=$1

	echo "Starting installation of $package using pip on $hostname..."
	if python3 -m pip install "$package"; then
		echo "Installation of $package successful using pip on $hostname."
		curl -X POST -d "hostname=$hostname&pip=$package" https://sds.sh/pip/
	else
		echo "pip installation failed for $package. Trying sudo apt install -y python3-$package..."
		sudo apt-get update -y
		if sudo apt-get install -y "python3-$package"; then
			echo "Installation of $package successful using apt on $hostname."
			curl -X POST -d "hostname=$hostname&apt=python3-$package" https://sds.sh/apt/
		else
			echo "Failed to install $package using apt on $hostname. Trying pip3 install --upgrade --no-cache-dir --break-system-packages..."
			if python3 -m pip install --upgrade --no-cache-dir --break-system-packages "$package"; then
				echo "Installation of $package successful using pip3 install --upgrade --no-cache-dir --break-system-packages on $hostname."
				curl -X POST -d "hostname=$hostname&pip_upgrade=$package" https://sds.sh/pip/
			else
				echo "Failed to install $package using all methods on $hostname."
			fi
		fi
	fi
}

# Install each package provided as an argument
for package in "$@"; do
	install_package "$package"
done