#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew &> /dev/null
then
    echo "Homebrew not installed. Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Update Homebrew
echo "Updating Homebrew..."
brew update

# Install PowerShell
echo "Installing PowerShell..."
brew install --cask powershell

# Check if PowerShell is installed successfully
if command -v pwsh &> /dev/null
then
    echo "PowerShell installation was successful."
else
    echo "PowerShell installation failed."
fi
