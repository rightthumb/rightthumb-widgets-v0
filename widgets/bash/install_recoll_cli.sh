#!/bin/bash

set -e

# Exit if already installed
if command -v recollq >/dev/null 2>&1; then
    echo "✅ recollq is already installed."
    exit 0
fi

# Function to build from source
install_recoll_from_source() {
    echo "🔧 Building recoll CLI from source..."

    sudo mkdir -p /usr/local/src/recoll-cli && cd /usr/local/src/recoll-cli

    # Install dependencies
    if command -v dnf >/dev/null 2>&1; then
        sudo dnf install -y git make gcc xapian-core-devel python3-devel qt5-qttools qt5-qtbase-devel
    fi
    if command -v yum >/dev/null 2>&1; then
        sudo yum install -y git make gcc xapian-core-devel python3-devel qt5-qttools qt5-qtbase-devel
    fi
    if command -v apt >/dev/null 2>&1; then
        sudo apt update && sudo apt install -y git make g++ libxapian-dev python3-dev qttools5-dev qtbase5-dev
    fi
    if command -v pacman >/dev/null 2>&1; then
        sudo pacman -Sy --noconfirm git base-devel xapian-core python qt5-base qt5-tools
    fi

    # Clone and build Recoll
    git clone https://framagit.org/medoc92/recoll.git .
    ./configure --without-gui
    make
    sudo make install

    echo "✅ recoll CLI installed successfully."
}

# Try system package managers first
if command -v apt >/dev/null 2>&1; then
    sudo apt update && sudo apt install -y recoll && exit 0
fi

if command -v pacman >/dev/null 2>&1; then
    sudo pacman -Sy --noconfirm recoll && exit 0
fi

if command -v dnf >/dev/null 2>&1; then
    echo "❌ recoll not found in dnf repos. Building from source..."
    install_recoll_from_source
    exit $?
fi

if command -v yum >/dev/null 2>&1; then
    echo "❌ recoll not found in yum repos. Building from source..."
    install_recoll_from_source
    exit $?
fi

echo "❌ No supported package manager found."
exit 1
