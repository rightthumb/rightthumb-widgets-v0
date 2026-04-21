#!/bin/bash

# Define the base directory for Python virtual environments
base_venv_dir="$HOME/.pyEnvironment"

# Function to attempt pip installation within a virtual environment
install_with_venv() {
	package=$1
	venv_path="$base_venv_dir/venv_$package"

	# Ensure the base directory exists
	mkdir -p "$base_venv_dir"

	# Check if python3-full is installed; if not, attempt to install
	if ! dpkg -l | grep -qw python3-full; then
			echo "python3-full is not installed. Attempting to install..."
			sudo apt-get install -y python3-full || { echo "Failed to install python3-full. Exiting."; return 1; }
	fi

	# Create a virtual environment for the package
	python3 -m venv "$venv_path"
	source "$venv_path/bin/activate"

	# Attempt to install the package within the virtual environment
	pip install "$package" && echo "$package installed successfully in virtual environment $venv_path" && return 0

	echo "Failed to install $package in virtual environment."
	deactivate
	return 1
}

# Check if at least one argument is provided
if [ $# -lt 1 ]; then
	echo "Usage: $0 <package_name>"
	exit 1
fi

package=$1
echo "Attempting to install $package with pip3"
if ! pip3 install "$package" 2>&1 | grep -q 'externally-managed-environment'; then
	echo "$package installed successfully with pip3"
else
	echo "Encountered an externally-managed-environment error with $package"
	# Attempt to install using a virtual environment
	if ! install_with_venv "$package"; then
		# If virtual environment installation fails, attempt apt-get
		package_name="${package%%=*}"
		if ! sudo apt-get install -y "python3-$package_name"; then
				echo "apt-get install failed for $package_name. Consider manual installation or review the package name."
		fi
	fi
fi