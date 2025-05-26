#!/bin/bash

# Check for curl
if ! command -v curl &> /dev/null
then
	echo "curl could not be found, installing curl..."
	sudo apt-get update
	sudo apt-get install -y curl
fi

# Install Homebrew
echo "Installing Homebrew..."
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Add Homebrew to PATH
echo "Adding Homebrew to PATH..."
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"

# For zsh users, also add to .zshrc
if [ -n "$ZSH_VERSION" ]; then
	echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> ~/.zshrc
	source ~/.zshrc
else
	source ~/.bashrc
fi

echo "Homebrew installation complete."