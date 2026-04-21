#!/bin/bash

# Function to ensure the virtual environment directory exists
ensure_venv_directory() {
	mkdir -p "$HOME/.pyEnvironment"
}

# Function to check if the package is already installed and working in the virtual environment
is_package_installed() {
	package=$1
	venv_path=$2
	source "$venv_path/bin/activate"
	# Use pip to check if package is installed and can be imported
	if python -c "import $package" &> /dev/null; then
		echo "1"  # Package is installed and importable
	else
		echo "0"  # Package not installed or broken
	fi
	deactivate
}

# Function to attempt pip installation within a virtual environment
install_with_venv() {
	package=$1
	package_name=$(echo $package | cut -d'=' -f1)  # Extract the package name without version
	venv_path="$HOME/.pyEnvironment/venv_$package_name"  # Use package name for venv directory

	ensure_venv_directory

	# Check if the virtual environment already exists
	if [ -d "$venv_path" ]; then
		echo "Checking if $package is correctly installed in the existing virtual environment..."
		if [ $(is_package_installed $package_name $venv_path) -eq 1 ]; then
			echo "$package is already installed and working. Moving on..."
			return 0
		else
			echo "$package installation is broken or not present. Attempting to fix..."
			# Attempt to reinstall the package
			source "$venv_path/bin/activate"
			pip install --force-reinstall $package
			deactivate
			return 0
		fi
	else
		echo "Creating a new virtual environment for $package..."
		python3 -m venv "$venv_path"
	fi

	# Activate the virtual environment and install the package
	source "$venv_path/bin/activate"
	pip install $package
	echo "$package installed successfully in virtual environment $venv_path"
	deactivate
}

# Loop through each line in require.txt and install the package
while IFS= read -r package; do
	echo "Attempting to install $package..."
	install_with_venv "$package"
done < ../require.txt

echo "All packages processed."