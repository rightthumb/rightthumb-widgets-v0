#!/usr/bin/env bash
#
# virsh-stack.sh
#
# Bootstrap script for:
#   - Installing KVM + libvirt + virt-install (virsh stack)
#   - Managing an ISO library (download & list)
#   - Creating new VMs using virt-install
#
# Usage:
#   bash virsh-stack.sh install
#   bash virsh-stack.sh iso-list
#   bash virsh-stack.sh iso-download <ISO_KEY> [DEST_DIR]
#   bash virsh-stack.sh new-vm --name NAME --iso-key ISO_KEY [options...]
#
# Example:
#   bash virsh-stack.sh install
#   bash virsh-stack.sh iso-list
#   bash virsh-stack.sh iso-download ubuntu-24.04-server
#   bash virsh-stack.sh new-vm --name testvm --iso-key ubuntu-24.04-server --ram 4096 --vcpus 2 --disk-size 40
#

set -euo pipefail

DEFAULT_ISO_DIR="$HOME/iso-library"
DEFAULT_VM_DIR="$HOME/vm-images"
SCRIPT_NAME="$(basename "$0")"

# ---------- Color helpers ----------
c_red()   { printf '\033[0;31m%s\033[0m\n' "$*" ; }
c_grn()   { printf '\033[0;32m%s\033[0m\n' "$*" ; }
c_yel()   { printf '\033[0;33m%s\033[0m\n' "$*" ; }
c_cyn()   { printf '\033[0;36m%s\033[0m\n' "$*" ; }
c_bold()  { printf '\033[1m%s\033[0m\n'   "$*" ; }

# ---------- ISO library ----------
# ISO_KEY format suggestion:
#   <distro>-<version>-<kind>
# where kind ~ server|desktop|minimal|light|ext

declare -A ISO_URLS
declare -A ISO_DESC
declare -A ISO_TYPE       # desktop/server
declare -A ISO_FLAVOR     # light/ext/minimal/etc
declare -A ISO_OSVARIANT  # osinfo-query os short name (best-effort, can be blank)

# --- Ubuntu (server / desktop / light) ---
ISO_URLS[ubuntu-24.04-server]="https://releases.ubuntu.com/24.04/ubuntu-24.04-live-server-amd64.iso"
ISO_DESC[ubuntu-24.04-server]="Ubuntu 24.04 LTS (Noble) - Server"
ISO_TYPE[ubuntu-24.04-server]="server"
ISO_FLAVOR[ubuntu-24.04-server]="extensive"
ISO_OSVARIANT[ubuntu-24.04-server]="ubuntu24.04"

ISO_URLS[ubuntu-24.04-desktop]="https://releases.ubuntu.com/24.04/ubuntu-24.04-desktop-amd64.iso"
ISO_DESC[ubuntu-24.04-desktop]="Ubuntu 24.04 LTS (Noble) - Desktop"
ISO_TYPE[ubuntu-24.04-desktop]="desktop"
ISO_FLAVOR[ubuntu-24.04-desktop]="extensive"
ISO_OSVARIANT[ubuntu-24.04-desktop]="ubuntu24.04"

ISO_URLS[ubuntu-22.04-server]="https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso"
ISO_DESC[ubuntu-22.04-server]="Ubuntu 22.04 LTS (Jammy) - Server"
ISO_TYPE[ubuntu-22.04-server]="server"
ISO_FLAVOR[ubuntu-22.04-server]="extensive"
ISO_OSVARIANT[ubuntu-22.04-server]="ubuntu22.04"

ISO_URLS[xubuntu-24.04-desktop]="https://cdimage.ubuntu.com/xubuntu/releases/24.04/release/xubuntu-24.04-desktop-amd64.iso"
ISO_DESC[xubuntu-24.04-desktop]="Xubuntu 24.04 - XFCE lightweight desktop"
ISO_TYPE[xubuntu-24.04-desktop]="desktop"
ISO_FLAVOR[xubuntu-24.04-desktop]="light"
ISO_OSVARIANT[xubuntu-24.04-desktop]="ubuntu24.04"

ISO_URLS[lubuntu-24.04-desktop]="https://cdimage.ubuntu.com/lubuntu/releases/24.04/release/lubuntu-24.04-desktop-amd64.iso"
ISO_DESC[lubuntu-24.04-desktop]="Lubuntu 24.04 - LXQt extra-light desktop"
ISO_TYPE[lubuntu-24.04-desktop]="desktop"
ISO_FLAVOR[lubuntu-24.04-desktop]="light"
ISO_OSVARIANT[lubuntu-24.04-desktop]="ubuntu24.04"

# --- Debian (server/light vs desktop) ---
ISO_URLS[debian-12-netinst]="https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-12.5.0-amd64-netinst.iso"
ISO_DESC[debian-12-netinst]="Debian 12 (Bookworm) netinst (minimal/server)"
ISO_TYPE[debian-12-netinst]="server"
ISO_FLAVOR[debian-12-netinst]="minimal"
ISO_OSVARIANT[debian-12-netinst]="debian12"

ISO_URLS[debian-12-gnome]="https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.5.0-amd64-DVD-1.iso"
ISO_DESC[debian-12-gnome]="Debian 12 (Bookworm) GNOME desktop (DVD)"
ISO_TYPE[debian-12-gnome]="desktop"
ISO_FLAVOR[debian-12-gnome]="extensive"
ISO_OSVARIANT[debian-12-gnome]="debian12"

# --- Fedora (Workstation vs Server) ---
ISO_URLS[fedora-40-workstation]="https://download.fedoraproject.org/pub/fedora/linux/releases/40/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-40-1.14.iso"
ISO_DESC[fedora-40-workstation]="Fedora 40 Workstation (GNOME desktop)"
ISO_TYPE[fedora-40-workstation]="desktop"
ISO_FLAVOR[fedora-40-workstation]="extensive"
ISO_OSVARIANT[fedora-40-workstation]="fedora40"

ISO_URLS[fedora-40-server]="https://download.fedoraproject.org/pub/fedora/linux/releases/40/Server/x86_64/iso/Fedora-Server-dvd-x86_64-40-1.14.iso"
ISO_DESC[fedora-40-server]="Fedora 40 Server"
ISO_TYPE[fedora-40-server]="server"
ISO_FLAVOR[fedora-40-server]="extensive"
ISO_OSVARIANT[fedora-40-server]="fedora40"

# --- Rocky & Alma (server/minimal) ---
ISO_URLS[rocky-9-minimal]="https://download.rockylinux.org/pub/rocky/9/isos/x86_64/Rocky-9-latest-minimal.iso"
ISO_DESC[rocky-9-minimal]="Rocky Linux 9 - Minimal (server/light)"
ISO_TYPE[rocky-9-minimal]="server"
ISO_FLAVOR[rocky-9-minimal]="minimal"
ISO_OSVARIANT[rocky-9-minimal]="rocky9"

ISO_URLS[alma-9-minimal]="https://repo.almalinux.org/almalinux/9/isos/x86_64/AlmaLinux-9-latest-minimal-x86_64.iso"
ISO_DESC[alma-9-minimal]="AlmaLinux 9 - Minimal (server/light)"
ISO_TYPE[alma-9-minimal]="server"
ISO_FLAVOR[alma-9-minimal]="minimal"
ISO_OSVARIANT[alma-9-minimal]="almalinux9"

# --- Arch (rolling, lightweight) ---
ISO_URLS[arch-latest]="https://mirror.rackspace.com/archlinux/iso/latest/archlinux-x86_64.iso"
ISO_DESC[arch-latest]="Arch Linux latest - rolling, minimal"
ISO_TYPE[arch-latest]="server"
ISO_FLAVOR[arch-latest]="minimal"
ISO_OSVARIANT[arch-latest]="archlinux"

# --- openSUSE (Leap & Tumbleweed) ---
ISO_URLS[opensuse-leap-15.5]="https://download.opensuse.org/distribution/leap/15.5/iso/openSUSE-Leap-15.5-DVD-x86_64.iso"
ISO_DESC[opensuse-leap-15.5]="openSUSE Leap 15.5 (desktop/server DVD)"
ISO_TYPE[opensuse-leap-15.5]="desktop"
ISO_FLAVOR[opensuse-leap-15.5]="extensive"
ISO_OSVARIANT[opensuse-leap-15.5]="opensuse15.5"

ISO_URLS[opensuse-tumbleweed]="https://download.opensuse.org/tumbleweed/iso/openSUSE-Tumbleweed-DVD-x86_64-Current.iso"
ISO_DESC[opensuse-tumbleweed]="openSUSE Tumbleweed (rolling desktop/server DVD)"
ISO_TYPE[opensuse-tumbleweed]="desktop"
ISO_FLAVOR[opensuse-tumbleweed]="extensive"
ISO_OSVARIANT[opensuse-tumbleweed]="opensuse-tumbleweed"

# ---------- Helpers ----------

usage() {
	cat <<EOF
$(c_bold "Usage:")
  $SCRIPT_NAME install
	Install KVM + libvirt + virt-install and enable libvirtd

  $SCRIPT_NAME iso-list
	List all known ISO keys (desktop/server, light/extensive)

  $SCRIPT_NAME iso-download <ISO_KEY> [DEST_DIR]
	Download ISO for ISO_KEY into DEST_DIR (default: $DEFAULT_ISO_DIR)

  $SCRIPT_NAME new-vm --name NAME --iso-key ISO_KEY [options...]
	Create a new VM using virt-install and an ISO from the library.

Options for new-vm:
  --name NAME            VM name (required)
  --iso-key ISO_KEY      ISO key from iso-list (or use --iso-path instead)
  --iso-path PATH        Full path to ISO (overrides iso-key download)
  --ram MB               RAM in MB (default: 4096)
  --vcpus N              vCPUs (default: 2)
  --disk-size GB         Disk size in GB (default: 40)
  --disk-path PATH       Disk image path (default: $DEFAULT_VM_DIR/NAME.qcow2)
  --network NET          virt-install --network argument (default: network=default)
  --graphics MODE        virt-install --graphics argument (default: spice)
  --os-variant VARIANT   Override auto OS variant (optional)

Examples:
  $SCRIPT_NAME install
  $SCRIPT_NAME iso-list
  $SCRIPT_NAME iso-download ubuntu-24.04-server
  $SCRIPT_NAME new-vm --name lab-ubuntu --iso-key ubuntu-24.04-server --ram 4096 --vcpus 2 --disk-size 30
EOF
}

detect_pkg_manager() {
	if command -v apt-get >/dev/null 2>&1; then
		echo "apt"
	elif command -v dnf >/dev/null 2>&1; then
		echo "dnf"
	elif command -v yum >/dev/null 2>&1; then
		echo "yum"
	elif command -v pacman >/dev/null 2>&1; then
		echo "pacman"
	elif command -v zypper >/dev/null 2>&1; then
		echo "zypper"
	else
		c_red "Could not detect a supported package manager (apt/dnf/yum/pacman/zypper)."
		exit 1
	fi
}

install_stack() {
	local pm
	pm="$(detect_pkg_manager)"

	c_cyn "Detected package manager: $pm"
	c_cyn "Installing KVM + libvirt + virt-install stack..."

	case "$pm" in
		apt)
			sudo apt-get update
			sudo apt-get install -y \
				qemu-kvm libvirt-daemon-system libvirt-clients bridge-utils \
				virtinst virt-manager
			;;
		dnf)
			sudo dnf install -y \
				qemu-kvm libvirt libvirt-daemon libvirt-daemon-config-network \
				libvirt-daemon-kvm bridge-utils virt-install virt-manager
			;;
		yum)
			sudo yum install -y \
				qemu-kvm libvirt libvirt-daemon libvirt-daemon-config-network \
				libvirt-daemon-kvm bridge-utils virt-install virt-manager
			;;
		pacman)
			sudo pacman -Sy --noconfirm \
				qemu-base libvirt virt-manager dnsmasq iptables-nft edk2-ovmf
			;;
		zypper)
			sudo zypper refresh
			sudo zypper install -y \
				qemu-kvm libvirt virt-install virt-manager bridge-utils
			;;
	esac

	c_cyn "Enabling and starting libvirtd (if available)..."
	if command -v systemctl >/dev/null 2>&1; then
		sudo systemctl enable --now libvirtd || true
	fi

	c_grn "Installation complete."
	c_yel "Remember to add your user to the 'libvirt' or 'kvm' group if needed:"
	echo "  sudo usermod -aG libvirt \$USER"
	echo "  sudo usermod -aG kvm    \$USER"
}

iso_list() {
	c_bold "Known ISO entries:"
	printf "  %-24s  %-8s  %-10s  %s\n" "ISO_KEY" "TYPE" "FLAVOR" "DESCRIPTION"
	printf "  %-24s  %-8s  %-10s  %s\n" "------" "----" "------" "-----------"

	for key in "${!ISO_URLS[@]}"; do
		local t f d
		t="${ISO_TYPE[$key]:-?}"
		f="${ISO_FLAVOR[$key]:-?}"
		d="${ISO_DESC[$key]:-}"
		printf "  %-24s  %-8s  %-10s  %s\n" "$key" "$t" "$f" "$d"
	done | sort
}

iso_download() {
	local key dest url fname
	key="${1:-}"
	dest="${2:-$DEFAULT_ISO_DIR}"

	if [[ -z "$key" ]]; then
		c_red "ISO key is required."
		iso_list
		exit 1
	fi

	if [[ -z "${ISO_URLS[$key]:-}" ]]; then
		c_red "Unknown ISO key: $key"
		iso_list
		exit 1
	fi

	url="${ISO_URLS[$key]}"
	mkdir -p "$dest"

	fname="$(basename "$url")"
	local out_path="$dest/$fname"

	c_cyn "Downloading ISO for key '$key':"
	c_cyn "  URL:  $url"
	c_cyn "  Dest: $out_path"

	if [[ -f "$out_path" ]]; then
		c_yel "File already exists: $out_path"
		c_yel "Skipping download. Remove or rename if you want to re-download."
		echo "$out_path"
		return 0
	fi

	if command -v curl >/dev/null 2>&1; then
		curl -L -o "$out_path" "$url"
	elif command -v wget >/dev/null 2>&1; then
		wget -O "$out_path" "$url"
	else
		c_red "Neither curl nor wget found. Install one of them and try again."
		exit 1
	fi

	c_grn "Downloaded: $out_path"
	echo "$out_path"
}

new_vm() {
	local name="" iso_key="" iso_path="" ram="4096" vcpus="2"
	local disk_size="40" disk_path="" network="network=default"
	local graphics="spice" os_variant=""

	# Parse args
	while [[ $# -gt 0 ]]; do
		case "$1" in
			--name)
				name="$2"; shift 2 ;;
			--iso-key)
				iso_key="$2"; shift 2 ;;
			--iso-path)
				iso_path="$2"; shift 2 ;;
			--ram)
				ram="$2"; shift 2 ;;
			--vcpus)
				vcpus="$2"; shift 2 ;;
			--disk-size)
				disk_size="$2"; shift 2 ;;
			--disk-path)
				disk_path="$2"; shift 2 ;;
			--network)
				network="$2"; shift 2 ;;
			--graphics)
				graphics="$2"; shift 2 ;;
			--os-variant)
				os_variant="$2"; shift 2 ;;
			*)
				c_red "Unknown option for new-vm: $1"
				usage
				exit 1 ;;
		esac
	done

	if [[ -z "$name" ]]; then
		c_red "--name is required."
		exit 1
	fi

	# Resolve ISO path
	if [[ -n "$iso_path" ]]; then
		if [[ ! -f "$iso_path" ]]; then
			c_red "ISO file not found: $iso_path"
			exit 1
		fi
	else
		if [[ -z "$iso_key" ]]; then
			c_red "Either --iso-key or --iso-path must be provided."
			exit 1
		fi
		if [[ -z "${ISO_URLS[$iso_key]:-}" ]]; then
			c_red "Unknown ISO key: $iso_key"
			iso_list
			exit 1
		fi
		c_cyn "No --iso-path provided. Using ISO library key: $iso_key"
		iso_path="$(iso_download "$iso_key" "$DEFAULT_ISO_DIR")"
	fi

	# Disk path
	if [[ -z "$disk_path" ]]; then
		mkdir -p "$DEFAULT_VM_DIR"
		disk_path="$DEFAULT_VM_DIR/${name}.qcow2"
	fi

	if [[ -f "$disk_path" ]]; then
		c_yel "Disk already exists: $disk_path"
	else
		c_cyn "Creating disk image: $disk_path (${disk_size}G)"
		qemu-img create -f qcow2 "$disk_path" "${disk_size}G"
	fi

	# OS variant
	if [[ -z "$os_variant" && -n "$iso_key" ]]; then
		os_variant="${ISO_OSVARIANT[$iso_key]:-}"
	fi

	c_bold "Creating VM with virt-install:"
	echo "  Name:       $name"
	echo "  ISO:        $iso_path"
	echo "  RAM:        ${ram}MB"
	echo "  vCPUs:      $vcpus"
	echo "  Disk:       $disk_path (${disk_size}G)"
	echo "  Network:    $network"
	echo "  Graphics:   $graphics"
	echo "  OS variant: ${os_variant:-<auto>}"

	local cmd=( virt-install
		--name "$name"
		--ram "$ram"
		--vcpus "$vcpus"
		--disk "path=$disk_path,format=qcow2"
		--cdrom "$iso_path"
		--network "$network"
		--graphics "$graphics"
		--noautoconsole
	)

	if [[ -n "$os_variant" ]]; then
		cmd+=( --os-variant "$os_variant" )
	fi

	c_cyn "Running virt-install..."
	"${cmd[@]}"

	c_grn "VM '$name' created. You can connect with:"
	echo "  virsh list --all"
	echo "  virt-manager (GUI) or 'virsh console $name' if configured."
}

# ---------- Main ----------

main() {
	local cmd="${1:-}"

	case "$cmd" in
		install)
			shift
			install_stack
			;;
		iso-list)
			shift
			iso_list
			;;
		iso-download)
			shift
			iso_download "$@"
			;;
		new-vm)
			shift
			new_vm "$@"
			;;
		""|-h|--help|help)
			usage
			;;
		*)
			c_red "Unknown command: $cmd"
			usage
			exit 1
			;;
	esac
}

main "$@"