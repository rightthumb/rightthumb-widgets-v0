#!/bin/bash

# Run Homebrew installation script
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

# Prompt for enabling root
read -p "Enable Root (y/N): " enable_root

# Default to 'N' if input is empty
enable_root=${enable_root:-N}

if [[ "$enable_root" =~ ^[Yy]$ ]]; then
    # Set root password
    sudo dscl . -passwd /Users/root

    # Enable root user
    sudo dscl . -create /Users/root UserShell /bin/bash
else
    echo "Root not enabled."
fi
