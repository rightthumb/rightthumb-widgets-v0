#!/usr/bin/env bash
set -euo pipefail

# ======================================================================
# vm.sh  - simple KVM/virsh VM helper
# ----------------------------------------------------------------------
# Usage:
#   ./vm.sh -setup NAME   # interactive VM creation
#   ./vm.sh -start NAME   # virsh start
#   ./vm.sh -stop  NAME   # virsh shutdown (then destroy if needed)
# ======================================================================

SCRIPT_PATH="$(readlink -f "$0")"
SCRIPT_DIR="$(dirname "$SCRIPT_PATH")"
BAD_URL_LOG="${SCRIPT_PATH}__bad-iso-URLs.log"

ISO_DIR="${SCRIPT_DIR}/isos"
DISK_DIR="${SCRIPT_DIR}/disks"
VM_META_DIR="${SCRIPT_DIR}/vm-meta"

mkdir -p "${ISO_DIR}" "${DISK_DIR}" "${VM_META_DIR}"

# ----------------------------------------------------------------------
# ISO LIBRARY
#   - Add/modify entries here if you want more distros
#   - We validate ALL URLs with curl before showing integer menus
# ----------------------------------------------------------------------

BASES=("ubuntu" "almalinux" "debian")
BASE_LABELS=("Ubuntu" "AlmaLinux" "Debian")

# Ubuntu
UBUNTU_VERSIONS=("22.04 LTS" "24.04 LTS")
UBUNTU_URLS=(
	"https://releases.ubuntu.com/22.04/ubuntu-22.04.5-live-server-amd64.iso"
	"https://releases.ubuntu.com/24.04/ubuntu-24.04.1-live-server-amd64.iso"
)

# AlmaLinux
ALMALINUX_VERSIONS=("8.10" "9.4")
ALMALINUX_URLS=(
	"https://repo.almalinux.org/almalinux/8.10/isos/x86_64/AlmaLinux-8.10-x86_64-dvd.iso"
	"https://repo.almalinux.org/almalinux/9.4/isos/x86_64/AlmaLinux-9.4-x86_64-dvd.iso"
)

# Debian
DEBIAN_VERSIONS=("12.7.0")
DEBIAN_URLS=(
	"https://cdimage.debian.org/debian-cd/current/amd64/iso-dvd/debian-12.7.0-amd64-DVD-1.iso"
)

# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

usage() {
	cat <<EOF
Usage:
  $0 -setup NAME   # interactively create a VM
  $0 -start NAME   # virsh start NAME (prints command)
  $0 -stop  NAME   # virsh shutdown/destroy NAME (prints commands)
EOF
	exit 1
}

run_cmd_print() {
	# Run a command, printing it exactly as executed (with safe quoting)
	local cmd=("$@")
	printf "Executing:"
	printf ' %q' "${cmd[@]}"
	echo
	"${cmd[@]}"
}

validate_one_iso() {
	local label="$1"
	local url="$2"
	local -n bad_ref="$3"

	# -I: HEAD request, -s: silent, we only care about HTTP code
	local http_code
	http_code="$(curl -o /dev/null -s -w '%{http_code}' -I "$url" || echo "000")"

	if [[ ! "$http_code" =~ ^2[0-9][0-9]$ ]]; then
		bad_ref+=("$label | $url | HTTP $http_code")
	fi
}

validate_iso_urls() {
	echo "Validating ISO URLs with curl (HEAD)..."
	local bad_urls=()

	# Ubuntu
	validate_one_iso "Ubuntu ${UBUNTU_VERSIONS[0]}" "${UBUNTU_URLS[0]}" bad_urls
	validate_one_iso "Ubuntu ${UBUNTU_VERSIONS[1]}" "${UBUNTU_URLS[1]}" bad_urls

	# AlmaLinux
	validate_one_iso "AlmaLinux ${ALMALINUX_VERSIONS[0]}" "${ALMALINUX_URLS[0]}" bad_urls
	validate_one_iso "AlmaLinux ${ALMALINUX_VERSIONS[1]}" "${ALMALINUX_URLS[1]}" bad_urls

	# Debian
	validate_one_iso "Debian ${DEBIAN_VERSIONS[0]}" "${DEBIAN_URLS[0]}" bad_urls

	if ((${#bad_urls[@]} > 0)); then
		echo "Some ISO URLs appear bad. Logging to:"
		echo "  ${BAD_URL_LOG}"
		: > "${BAD_URL_LOG}"
		for line in "${bad_urls[@]}"; do
			echo "${line}" >> "${BAD_URL_LOG}"
		done
	else
		# Do NOT create the log file if everything is good
		echo "All ISO URLs look OK."
	fi
}

normalize_ram_to_mb() {
	# RAM: if <3 digits assume GB; >=3 digits assume MB
	# Also accept suffixes like 4G, 4096M
	local input="$1"
	input="${input,,}"  # lower-case

	local num unit
	if [[ "$input" =~ ^([0-9]+)([gm])$ ]]; then
		num="${BASH_REMATCH[1]}"
		unit="${BASH_REMATCH[2]}"
		if [[ "$unit" == "g" ]]; then
			echo $((num * 1024))
		else
			echo "${num}"
		fi
	elif [[ "$input" =~ ^[0-9]+$ ]]; then
		num="$input"
		if ((${#num} < 3)); then
			# Fewer than 3 digits => assume GB
			echo $((num * 1024))
		else
			# 3 or more digits => assume MB
			echo "${num}"
		fi
	else
		echo "ERROR"  # caller should handle
	fi
}

normalize_disk_to_gb() {
	# Disk: similar logic but returns GB (integer, rounded up if needed)
	# - "<3 digits" => GB
	# - ">=3 digits" => MB, then converted to GB (ceil)
	# - Supports suffix G/M too.
	local input="$1"
	input="${input,,}"

	local num unit
	if [[ "$input" =~ ^([0-9]+)([gm])$ ]]; then
		num="${BASH_REMATCH[1]}"
		unit="${BASH_REMATCH[2]}"
		if [[ "$unit" == "g" ]]; then
			echo "${num}"
		else
			# MB -> GB (ceil)
			echo $(((num + 1023) / 1024))
		fi
	elif [[ "$input" =~ ^[0-9]+$ ]]; then
		num="$input"
		if ((${#num} < 3)); then
			# Fewer than 3 digits => GB
			echo "${num}"
		else
			# 3 or more digits => MB -> GB (ceil)
			echo $(((num + 1023) / 1024))
		fi
	else
		echo "ERROR"
	fi
}

select_distro_base() {
	echo
	echo "Select distro base:"
	local i idx
	for i in "${!BASES[@]}"; do
		idx=$((i + 1))
		printf "  %d) %s\n" "${idx}" "${BASE_LABELS[$i]}"
	done

	local choice
	while true; do
		read -rp "Base choice (1-${#BASES[@]}): " choice
		if [[ "$choice" =~ ^[0-9]+$ ]] && ((choice >= 1 && choice <= ${#BASES[@]})); then
			break
		fi
		echo "Invalid choice, try again."
	done

	local base_index=$((choice - 1))
	echo "${BASES[$base_index]}"
}

select_distro_version() {
	local base="$1"

	local -a versions=()
	local -a urls=()

	case "$base" in
		ubuntu)
			versions=("${UBUNTU_VERSIONS[@]}")
			urls=("${UBUNTU_URLS[@]}")
			;;
		almalinux)
			versions=("${ALMALINUX_VERSIONS[@]}")
			urls=("${ALMALINUX_URLS[@]}")
			;;
		debian)
			versions=("${DEBIAN_VERSIONS[@]}")
			urls=("${DEBIAN_URLS[@]}")
			;;
		*)
			echo "Unknown base '$base'" >&2
			exit 1
			;;
	esac

	echo
	echo "Select ${base} version:"
	local i idx
	for i in "${!versions[@]}"; do
		idx=$((i + 1))
		printf "  %d) %s\n" "${idx}" "${versions[$i]}"
	done

	local choice
	while true; do
		read -rp "Version choice (1-${#versions[@]}): " choice
		if [[ "$choice" =~ ^[0-9]+$ ]] && ((choice >= 1 && choice <= ${#versions[@]})); then
			break
		fi
		echo "Invalid choice, try again."
	done

	local ver_index=$((choice - 1))
	# Return "version|url" via echo
	echo "${versions[$ver_index]}|${urls[$ver_index]}"
}

get_host_ip() {
	# Try to grab first non-loopback IP
	local ip
	ip="$(hostname -I 2>/dev/null | awk '{print $1}')"
	if [[ -z "${ip}" ]]; then
		# Fallback
		ip="$(ip route get 1.1.1.1 2>/dev/null | awk '/src/ {print $7; exit}')"
	fi
	echo "${ip:-127.0.0.1}"
}

setup_vm() {
	local vm_name="$1"

	# Validate ISO URLs before we present any integer options
	validate_iso_urls

	echo
	echo "=== VM Setup for '${vm_name}' ==="

	# Ask ALL questions before taking actions (downloads, disk create, etc.)

	local vcpus ram_input ram_mb disk_input disk_gb vm_ip

	read -rp "vCPUs (e.g. 2): " vcpus
	if [[ ! "$vcpus" =~ ^[0-9]+$ ]] || (( vcpus < 1 )); then
		echo "Invalid vCPU count." >&2
		exit 1
	fi

	read -rp "RAM size (GB or MB, e.g. 4 or 4096 or 4G): " ram_input
	ram_mb="$(normalize_ram_to_mb "$ram_input")"
	if [[ "$ram_mb" == "ERROR" ]]; then
		echo "Invalid RAM value." >&2
		exit 1
	fi
	echo "RAM normalized to: ${ram_mb} MB"

	read -rp "Disk size (GB or MB, e.g. 20 or 20480 or 20G): " disk_input
	disk_gb="$(normalize_disk_to_gb "$disk_input")"
	if [[ "$disk_gb" == "ERROR" ]]; then
		echo "Invalid disk size." >&2
		exit 1
	fi
	echo "Disk normalized to: ${disk_gb} GB"

	read -rp "Static IP for VM (blank to use host IP): " vm_ip
	if [[ -z "$vm_ip" ]]; then
		vm_ip="$(get_host_ip)"
		echo "Using host IP: ${vm_ip}"
	fi

	# Distro base & version (integer menus)
	local base ver_and_url version iso_url
	base="$(select_distro_base)"
	ver_and_url="$(select_distro_version "$base")"
	version="${ver_and_url%%|*}"
	iso_url="${ver_and_url##*|}"

	echo
	echo "Summary:"
	echo "  VM Name : ${vm_name}"
	echo "  vCPUs   : ${vcpus}"
	echo "  RAM     : ${ram_mb} MB"
	echo "  Disk    : ${disk_gb} GB"
	echo "  Base    : ${base}"
	echo "  Version : ${version}"
	echo "  ISO URL : ${iso_url}"
	echo "  VM IP   : ${vm_ip}"
	echo

	read -rp "Proceed with VM creation? [y/N]: " confirm
	confirm="${confirm,,}"
	if [[ "$confirm" != "y" && "$confirm" != "yes" ]]; then
		echo "Aborted."
		exit 0
	fi

	# ------------------------------------------------------------------
	# Actions START here: ISO download, disk, virt-install.
	# ------------------------------------------------------------------

	local iso_file iso_path disk_path
	iso_file="$(basename "$iso_url")"
	iso_path="${ISO_DIR}/${iso_file}"
	disk_path="${DISK_DIR}/${vm_name}.qcow2"

	if [[ -f "$iso_path" ]]; then
		echo "ISO already exists, not downloading again:"
		echo "  ${iso_path}"
	else
		echo "Downloading ISO to ${iso_path}"
		run_cmd_print curl -L -o "${iso_path}" "${iso_url}"
	fi

	if [[ -f "$disk_path" ]]; then
		echo "Disk image already exists:"
		echo "  ${disk_path}"
	else
		echo "Creating qcow2 disk: ${disk_path} (${disk_gb}G)"
		run_cmd_print qemu-img create -f qcow2 "${disk_path}" "${disk_gb}G"
	fi

	# Save simple metadata
	local meta_file="${VM_META_DIR}/${vm_name}.conf"
	cat > "${meta_file}" <<EOF
NAME="${vm_name}"
VCPUS="${vcpus}"
RAM_MB="${ram_mb}"
DISK_GB="${disk_gb}"
DISK_PATH="${disk_path}"
ISO_PATH="${iso_path}"
BASE="${base}"
VERSION="${version}"
VM_IP="${vm_ip}"
EOF
	echo "Saved VM metadata to ${meta_file}"

	# virt-install command
	# NOTE: Adjust network/bridge as needed for your environment.
	local net_arg="network=default"
	local virt_install_cmd=(
		virt-install
		--name "${vm_name}"
		--memory "${ram_mb}"
		--vcpus "${vcpus}"
		--disk "path=${disk_path},format=qcow2"
		--cdrom "${iso_path}"
		--os-variant "generic"
		--network "${net_arg}"
		--graphics vnc
		--noautoconsole
	)

	run_cmd_print "${virt_install_cmd[@]}"

	echo "VM '${vm_name}' setup complete."
}

start_vm() {
	local vm_name="$1"
	local cmd=(virsh start "${vm_name}")
	run_cmd_print "${cmd[@]}"
}

stop_vm() {
	local vm_name="$1"

	# Graceful shutdown first
	local shutdown_cmd=(virsh shutdown "${vm_name}")
	run_cmd_print "${shutdown_cmd[@]}"

	echo "Waiting a few seconds for VM to shut down..."
	sleep 5

	# If still running, force stop
	if virsh list --state-running | awk '{print $2}' | grep -qx "${vm_name}"; then
		local destroy_cmd=(virsh destroy "${vm_name}")
		run_cmd_print "${destroy_cmd[@]}"
	else
		echo "VM '${vm_name}' appears to be stopped."
	fi
}

# ----------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------

if (( $# < 2 )); then
	usage
fi

action="$1"
vm_name="$2"

case "$action" in
	-setup)
		setup_vm "${vm_name}"
		;;
	-start)
		start_vm "${vm_name}"
		;;
	-stop)
		stop_vm "${vm_name}"
		;;
	*)
		usage
		;;
esac