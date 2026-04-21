#!/bin/bash

set -e

DISTRO_DIR="/mnt/chroot"
mkdir -p "$DISTRO_DIR"

# === All supported distros with methods ===
declare -A DISTROS

# Debootstrap-based
DISTROS["ubuntu-jammy"]="debootstrap http://archive.ubuntu.com/ubuntu/ jammy"
DISTROS["ubuntu-focal"]="debootstrap http://archive.ubuntu.com/ubuntu/ focal"
DISTROS["debian-bookworm"]="debootstrap http://deb.debian.org/debian bookworm"
DISTROS["debian-bullseye"]="debootstrap http://deb.debian.org/debian bullseye"
DISTROS["devuan-daedalus"]="debootstrap http://deb.devuan.org/merged daedalus"
DISTROS["kali"]="debootstrap http://http.kali.org/kali kali-rolling"
DISTROS["parrot"]="debootstrap http://deb.parrot.sh/parrot parrot"

# Rootfs-based
DISTROS["arch"]="rootfs https://mirror.rackspace.com/archlinux/iso/latest/archlinux-bootstrap-x86_64.tar.gz"
DISTROS["alpine"]="rootfs https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-minirootfs-3.18.4-x86_64.tar.gz"
DISTROS["void"]="rootfs https://repo-default.voidlinux.org/live/current/void-x86_64-ROOTFS-20230628.tar.xz"
DISTROS["gentoo"]="rootfs https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64.tar.xz"
DISTROS["fedora"]="rootfs https://download.fedoraproject.org/pub/fedora/linux/releases/39/Container/x86_64/images/Fedora-Container-Base-39-1.5.x86_64.tar.xz"
DISTROS["opensuse"]="rootfs https://download.opensuse.org/tumbleweed/appliances/openSUSE-Tumbleweed-ContainerHost.x86_64-ContainerHost-rootfs.tar.xz"
DISTROS["chimera"]="rootfs https://github.com/chimera-linux/cports/releases/latest/download/chimera-rootfs.tar.xz"

# === Help ===
show_help() {
	echo "Usage: $0 -distro <name>"
	echo "       $0 -clone <existing> <new>"
	echo "       $0 --help"
	echo
	echo "Available distros:"
	for key in "${!DISTROS[@]}"; do
		echo "  - $key"
	done
	exit 0
}

# === Install dependencies ===
detect_pkg_manager() {
	if command -v apt &>/dev/null; then
		sudo apt update
		sudo apt install -y debootstrap wget tar xz-utils
	elif command -v dnf &>/dev/null; then
		sudo dnf install -y debootstrap wget tar xz
	elif command -v pacman &>/dev/null; then
		sudo pacman -Sy --noconfirm debootstrap wget tar xz
	else
		echo "Unsupported system. Install debootstrap, wget, and tar manually."
		exit 1
	fi
}

# === Create start script ===

make_start_script() {
    local name="$1"
    local path="$DISTRO_DIR/$name"
    local script="$DISTRO_DIR/start-$name.sh"

    cat > "$script" <<'EOF'
#!/bin/bash

CHROOT="__CHROOT_PATH__"

echo "🔧 Mounting system folders into chroot..."

# Mount required filesystems
sudo mount --bind /dev "$CHROOT/dev"
sudo mount --bind /dev/pts "$CHROOT/dev/pts"
sudo mount --bind /proc "$CHROOT/proc"
sudo mount --bind /sys "$CHROOT/sys"

# Mount /dev/shm if not already
if ! mountpoint -q "$CHROOT/dev/shm"; then
    sudo mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs "$CHROOT/dev/shm"
    sudo chmod 1777 "$CHROOT/dev/shm"
fi

# Bind D-Bus socket for system bus (optional, needed for some apps)
if [ -S /run/dbus/system_bus_socket ]; then
    sudo mkdir -p "$CHROOT/run/dbus"
    sudo mount --bind /run/dbus "$CHROOT/run/dbus"
fi

# Optional: ensure DNS resolution inside chroot
if [ ! -f "$CHROOT/etc/resolv.conf" ]; then
    sudo cp /etc/resolv.conf "$CHROOT/etc/resolv.conf"
fi

echo "🚀 Entering chroot: $CHROOT"
sudo chroot "$CHROOT" /bin/bash

echo "🧹 Cleaning up mounts..."
sudo umount -l "$CHROOT/run/dbus" 2>/dev/null
sudo umount -l "$CHROOT/dev/shm" 2>/dev/null
sudo umount -l "$CHROOT/dev/pts" 2>/dev/null
sudo umount -l "$CHROOT/dev" 2>/dev/null
sudo umount -l "$CHROOT/proc" 2>/dev/null
sudo umount -l "$CHROOT/sys" 2>/dev/null

echo "✅ Chroot exited and cleaned."
EOF

    # Now replace __CHROOT_PATH__ with the actual path
    sed -i "s|__CHROOT_PATH__|$path|g" "$script"

    chmod +x "$script"
    echo "🟢 Created start script: $script"

    # Now fix bash.bashrc inside the chroot
    cat >> "$path/etc/bash.bashrc" <<'EOB'
# Auto-mount devpts if not already mounted inside chroot bash sessions
if ! mountpoint -q /dev/pts; then
    mount -t devpts devpts /dev/pts
fi

# Ensure shm is mounted inside chroot
if ! mountpoint -q /dev/shm; then
    mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs /dev/shm
    chmod 1777 /dev/shm
fi

# Optional: ensure D-Bus if needed
if [ -S /run/dbus/system_bus_socket ] && [ ! -S /run/dbus/system_bus_socket ]; then
    mkdir -p /run/dbus
    mount --bind /run/dbus /run/dbus
fi
EOB
}



# === Setup Distro ===
setup_distro() {
	local name="$1"
	local data=( ${DISTROS[$name]} )
	local method="${data[0]}"
	local url="${data[1]}"
	local suite="${data[2]}"
	local path="$DISTRO_DIR/$name"

	mkdir -p "$path"

	if [[ "$method" == "debootstrap" ]]; then
		sudo debootstrap "$suite" "$path" "$url"
	elif [[ "$method" == "rootfs" ]]; then
		local tmp="$path/rootfs.tar"
		wget -O "$tmp" "$url"
		sudo tar -xf "$tmp" -C "$path" --strip-components=1 || sudo tar -xf "$tmp" -C "$path"
		rm "$tmp"
	else
		echo "❌ Unsupported install method for $name."
		exit 1
	fi

	make_start_script "$name"
}

# === Clone ===
clone_distro() {
	local src="$1"
	local dest="$2"
	cp -a "$DISTRO_DIR/$src" "$DISTRO_DIR/$dest"
	make_start_script "$dest"
}

# === Main ===
main() {
	[[ "$1" == "--help" || "$1" == "-h" || -z "$1" ]] && show_help
	detect_pkg_manager

	case "$1" in
		-distro)
			[[ -z "$2" || -z "${DISTROS[$2]}" ]] && show_help
			setup_distro "$2"
			;;
		-clone)
			[[ -z "$2" || -z "$3" ]] && show_help
			clone_distro "$2" "$3"
			;;
		*)
			echo "Unknown command: $1"
			show_help
			;;
	esac
}

main "$@"

# nano /etc/apt/sources.list
# deb http://archive.ubuntu.com/ubuntu jammy main universe multiverse restricted
# deb http://archive.ubuntu.com/ubuntu jammy-updates main universe multiverse restricted
# deb http://archive.ubuntu.com/ubuntu jammy-security main universe multiverse restricted

# apt clean
# rm -rf /var/lib/apt/lists/*
# apt update


