#!/bin/bash

# Rust installer script for any Linux distro (handles noexec /tmp)
set -e

echo "[+] Checking dependencies..."

# Ensure curl is available
if ! command -v curl &>/dev/null; then
	echo "[-] curl not found. Installing..."
	if command -v dnf &>/dev/null; then
		sudo dnf install curl -y
	elif command -v apt &>/dev/null; then
		sudo apt update
		sudo apt install -y curl pkg-config libssl-dev
	elif command -v pacman &>/dev/null; then
		sudo pacman -Sy curl --noconfirm
	else
		echo "[-] Package manager not detected. Please install curl manually."
		exit 1
	fi
fi


# Make a safe temp directory to bypass noexec issues
export TMPDIR="$HOME/tmp_rust_installer"
mkdir -p "$TMPDIR"

echo "[+] Downloading and running rustup-init with TMPDIR=$TMPDIR..."

# Download and install Rust
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

# Source environment to use Rust immediately
if [[ -f "$HOME/.cargo/env" ]]; then
	source "$HOME/.cargo/env"
fi

# Confirm installation
if command -v rustc &>/dev/null; then
	echo "[✓] Rust installed successfully! Version: $(rustc --version)"
else
	echo "[-] Rust installation failed or not in PATH."
	exit 1
fi

echo 'source "$HOME/.cargo/env.fish"' >> $HOME/.bashrc.
echo 'source "$HOME/.cargo/env.nu"' >> $HOME/.bashrc.