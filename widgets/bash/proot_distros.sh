#!/bin/bash

set -e

DISTRO_DIR="$HOME/proot-distros"
mkdir -p "$DISTRO_DIR"

declare -A DISTROS
DISTROS["ubuntu"]="https://partner-images.canonical.com/core/focal/current/ubuntu-focal-core-cloudimg-amd64-root.tar.gz"
DISTROS["debian"]="https://cdimage.debian.org/cdimage/archive/10.13.0/debian-10.13.0-amd64-netinst.iso"  # swap with proper rootfs if needed
DISTROS["alpine"]="https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-minirootfs-3.18.4-x86_64.tar.gz"
DISTROS["arch"]="https://mirror.rackspace.com/archlinux/iso/latest/archlinux-bootstrap-x86_64.tar.gz"
DISTROS["fedora"]="https://download.fedoraproject.org/pub/fedora/linux/releases/39/Container/x86_64/images/Fedora-Container-Base-39-1.5.x86_64.tar.xz"
DISTROS["kali"]="https://kali.download/nethunter-images/current/rootfs/kalifs-arm64-full.tar.xz"
DISTROS["void"]="https://repo-default.voidlinux.org/live/current/void-x86_64-ROOTFS-20230628.tar.xz"

# === Help Menu ===
show_help() {
	echo "Usage: $0 [--help]"
	echo
	echo "This script installs PRoot-based Linux distributions."
	echo
	echo "Available Distros:"
	for distro in "${!DISTROS[@]}"; do
		printf "  - %s\n" "$distro"
	done
	echo
	echo "After install, launch a distro with:"
	echo "  ./start-<distro>.sh (e.g., ./start-ubuntu.sh)"
	echo
	exit 0
}

# === Detect Package Manager ===
detect_pkg_manager() {
	if command -v apt &>/dev/null; then
		PKG_INSTALL="sudo apt update && sudo apt install -y"
	elif command -v dnf &>/dev/null; then
		PKG_INSTALL="sudo dnf install -y"
	elif command -v yum &>/dev/null; then
		PKG_INSTALL="sudo yum install -y"
	elif command -v pacman &>/dev/null; then
		PKG_INSTALL="sudo pacman -Sy --noconfirm"
	else
		echo "Unsupported package manager."
		exit 1
	fi
}

# === Install Dependencies ===
install_dependencies() {
	echo "[+] Installing dependencies..."
	$PKG_INSTALL proot wget tar curl
}

# === Setup Distro ===
setup_distro() {
	local name="$1"
	local url="$2"
	local file_name=$(basename "$url")
	local d_path="$DISTRO_DIR/$name"

	echo "[+] Setting up $name"
	mkdir -p "$d_path"

	wget -nc -O "$d_path/$file_name" "$url"
	tar_opts="xf"
	[[ "$file_name" == *.tar.gz ]] && tar_opts="xzf"
	[[ "$file_name" == *.tar.xz ]] && tar_opts="xJf"

	tar $tar_opts "$d_path/$file_name" -C "$d_path" --strip-components=1 || tar $tar_opts "$d_path/$file_name" -C "$d_path"

	cat > "$DISTRO_DIR/start-$name.sh" <<EOF
#!/bin/bash
proot -R $d_path /bin/sh
EOF
	chmod +x "$DISTRO_DIR/start-$name.sh"
}

# === Main ===
main() {
	[[ "$1" == "--help" || "$1" == "-h" ]] && show_help
	detect_pkg_manager
	install_dependencies

	for distro in "${!DISTROS[@]}"; do
		setup_distro "$distro" "${DISTROS[$distro]}"
	done

	echo
	echo "✔️ All distros installed in $DISTRO_DIR"
	echo "Launch with: ./start-<distro>.sh"
}

main "$@"