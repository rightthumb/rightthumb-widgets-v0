#!/usr/bin/env bash
# _chroot.sh - bad ass chroot manager
# Manages Debian/Ubuntu/Kali chroots under /mnt/chroot/<name>
#
# Features:
#   - _chroot.sh -install              # install prereqs
#   - _chroot.sh -new                  # pick distro preset, name it, bootstrap
#   - _chroot.sh -start <name>         # mount & chroot
#   - _chroot.sh -stop  <name>         # unmount
#   - _chroot.sh -clone <src> <dst>    # rsync clone (offline, then start dst)
#
# All chroots live under: /mnt/chroot/<name>
# ISOs cached under:       /mnt/chroot/_isos

set -u

CHROOT_BASE="/mnt/chroot"
ISO_DIR="${CHROOT_BASE}/_isos"

# --------- logging helpers ---------
log() {
    printf '[*] %s\n' "$*" >&2
}
info() {
    printf '[+] %s\n' "$*" >&2
}
warn() {
    printf '[!] %s\n' "$*" >&2
}
err() {
    printf '[ERROR] %s\n' "$*" >&2
    exit 1
}

# --------- root / deps ---------
ensure_root() {
    if [ "$(id -u)" -ne 0 ]; then
        err "Run this script as root (sudo _chroot.sh ...)."
    fi
}

ensure_tools() {
    local tools=("debootstrap" "wget" "rsync" "mount" "umount")
    local missing=()
    for t in "${tools[@]}"; do
        if ! command -v "$t" >/dev/null 2>&1; then
            missing+=("$t")
        fi
    done

    if [ "${#missing[@]}" -gt 0 ]; then
        warn "Missing tools: ${missing[*]}"
        if command -v apt-get >/dev/null 2>&1; then
            info "Installing prerequisites via apt-get..."
            apt-get update
            apt-get install -y "${missing[@]}"
        else
            err "Please install these manually: ${missing[*]}"
        fi
    fi
}

# --------- usage / help ---------
usage() {
    cat <<EOF
Usage:
  _chroot.sh -install
      Install required tools (debootstrap, wget, rsync, …).

  _chroot.sh -new
      Interactive wizard:
        - Show distro presets
        - Let you choose one
        - Download ISO if needed
        - Ask for chroot name
        - Bootstrap into /mnt/chroot/<name>

  _chroot.sh -start <name>
      Bind-mount /dev, /proc, /sys, /run and chroot into /mnt/chroot/<name>.

  _chroot.sh -stop <name>
      Unmount bind mounts for /mnt/chroot/<name>.

  _chroot.sh -clone <src> <dst>
      Clone an existing chroot:
        /mnt/chroot/<src> -> /mnt/chroot/<dst>

Notes:
  - All chroots live under: ${CHROOT_BASE}/<name>
  - ISOs cached under:       ${ISO_DIR}
  - Example:
        _chroot.sh -new
        _chroot.sh -start ubuntu24
        _chroot.sh -stop  ubuntu24
        _chroot.sh -clone ubuntu22 ubuntu22b
EOF
}

# ========= DISTRO PRESETS =========
# These are tuned for debootstrap (Debian/Ubuntu/Kali based).

ISO_KEYS=(
    "ubuntu18"
    "ubuntu20"
    "ubuntu22"
    "ubuntu24"
    "debian12"
    "debian13"
    "kali2024"
)

ISO_LABELS=(
    "Ubuntu 18.04.6 LTS (Bionic, server)"
    "Ubuntu 20.04.6 LTS (Focal, server)"
    "Ubuntu 22.04.5 LTS (Jammy, server)"
    "Ubuntu 24.04.1 LTS (Noble, server)"
    "Debian 12.x (Bookworm, netinst)"
    "Debian 13.x (Trixie, netinst)"
    "Kali Linux 2024.x (kali-rolling)"
)

# Direct ISO URLs (amd64) – these are the files wget will pull.
ISO_URLS=(
    "https://releases.ubuntu.com/18.04/ubuntu-18.04.6-live-server-amd64.iso"
    "https://releases.ubuntu.com/focal/ubuntu-20.04.6-live-server-amd64.iso"
    "https://releases.ubuntu.com/jammy/ubuntu-22.04.5-live-server-amd64.iso"
    "https://releases.ubuntu.com/noble/ubuntu-24.04.1-live-server-amd64.iso"
    "https://cdimage.debian.org/cdimage/archive/latest-oldstable/amd64/iso-cd/debian-12.12.0-amd64-netinst.iso"
    "https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-13.2.0-amd64-netinst.iso"
    "https://old.kali.org/kali-images/kali-2024.2/kali-linux-2024.2-installer-amd64.iso"
)

# Suites passed to debootstrap
ISO_SUITES=(
    "bionic"
    "focal"
    "jammy"
    "noble"
    "bookworm"
    "trixie"
    "kali-rolling"
)

# Mirrors passed to debootstrap
ISO_MIRRORS=(
    "http://archive.ubuntu.com/ubuntu"
    "http://archive.ubuntu.com/ubuntu"
    "http://archive.ubuntu.com/ubuntu"
    "http://archive.ubuntu.com/ubuntu"
    "http://deb.debian.org/debian"
    "http://deb.debian.org/debian"
    "http://http.kali.org/kali"
)

print_iso_menu() {
    mkdir -p "${ISO_DIR}"
    echo "Available distro presets:"
    echo
    local idx
    local iso_file
    for idx in "${!ISO_KEYS[@]}"; do
        iso_file="${ISO_DIR}/$(basename "${ISO_URLS[$idx]}")"
        if [ -f "$iso_file" ]; then
            printf "  [%2d] * %-10s - %s\n" "$((idx+1))" "${ISO_KEYS[$idx]}" "${ISO_LABELS[$idx]}"
        else
            printf "  [%2d]   %-10s - %s\n" "$((idx+1))" "${ISO_KEYS[$idx]}" "${ISO_LABELS[$idx]}"
        fi
    done
    echo
    echo "Legend: * = ISO already downloaded into ${ISO_DIR}"
}

ensure_base_dirs() {
    mkdir -p "${CHROOT_BASE}" "${ISO_DIR}"
}

distro_from_key() {
    # given key, return index or -1
    local key="$1"
    local i
    for i in "${!ISO_KEYS[@]}"; do
        if [ "${ISO_KEYS[$i]}" = "$key" ]; then
            echo "$i"
            return 0
        fi
    done
    echo "-1"
}

download_iso() {
    local idx="$1"
    local url="${ISO_URLS[$idx]}"
    local iso_file="${ISO_DIR}/$(basename "$url")"

    if [ -f "$iso_file" ]; then
        info "ISO already present: $iso_file"
        echo "$iso_file"
        return 0
    fi

    info "Downloading ISO:"
    info "  URL: $url"
    info "  ->  $iso_file"
    (
        cd "${ISO_DIR}"
        if ! wget -c "$url"; then
            err "ISO download failed for $url"
        fi
    )
    echo "$iso_file"
}

create_chroot_rootfs() {
    local key="$1"
    local name="$2"

    local idx
    idx="$(distro_from_key "$key")"
    if [ "$idx" -lt 0 ]; then
        err "Unknown distro key: $key"
    fi

    local suite="${ISO_SUITES[$idx]}"
    local mirror="${ISO_MIRRORS[$idx]}"
    local target="${CHROOT_BASE}/${name}"

    if [ -d "$target" ]; then
        err "Chroot already exists: $target"
    fi

    info "Bootstrapping $key -> $target"
    info "  suite:  $suite"
    info "  mirror: $mirror"

    mkdir -p "$target"
    debootstrap --arch=amd64 "$suite" "$target" "$mirror"
    info "Base system installed."

    # Basic QoL tweaks
    echo "proc /proc proc defaults 0 0" >> "${target}/etc/fstab"

    # minimal resolv.conf (host's DNS will be bind-mounted too, but belt & suspenders)
    if [ ! -f "${target}/etc/resolv.conf" ]; then
        echo "nameserver 1.1.1.1" > "${target}/etc/resolv.conf"
    fi

    info "Chroot $name created."
}

mount_bind() {
    local name="$1"
    local root="${CHROOT_BASE}/${name}"

    [ -d "$root" ] || err "Chroot does not exist: $root"

    for d in dev proc sys run; do
        if mountpoint -q "${root}/${d}"; then
            continue
        fi
        case "$d" in
            dev)
                mount --bind /dev "${root}/dev"
                ;;
            proc)
                mount -t proc /proc "${root}/proc"
                ;;
            sys)
                mount --bind /sys "${root}/sys"
                ;;
            run)
                mount --bind /run "${root}/run"
                ;;
        esac
    done
}

umount_bind() {
    local name="$1"
    local root="${CHROOT_BASE}/${name}"

    [ -d "$root" ] || err "Chroot does not exist: $root"

    # unmount in reverse order
    for d in run sys proc dev; do
        if mountpoint -q "${root}/${d}"; then
            umount "${root}/${d}" || warn "Failed to unmount ${root}/${d}"
        fi
    done
}

start_chroot() {
    local name="$1"
    local root="${CHROOT_BASE}/${name}"

    [ -d "$root" ] || err "Chroot does not exist: $root"

    mount_bind "$name"

    info "Entering chroot $name (root: $root)"
    info "Type 'exit' or Ctrl+D to leave."
    chroot "$root" /bin/bash --login
}

stop_chroot() {
    local name="$1"
    umount_bind "$name"
    info "Chroot $name unmounted."
}

clone_chroot() {
    local src="$1"
    local dst="$2"

    local src_root="${CHROOT_BASE}/${src}"
    local dst_root="${CHROOT_BASE}/${dst}"

    [ -d "$src_root" ] || err "Source chroot does not exist: $src_root"
    [ ! -d "$dst_root" ] || err "Destination already exists: $dst_root"

    info "Cloning chroot:"
    info "  from: $src_root"
    info "  to:   $dst_root"

    # Safety: refuse if src has bind mounts still attached
    local m
    while read -r m; do
        if echo "$m" | grep -q "^${src_root}/"; then
            err "Source chroot appears to have mounts still active. Run: _chroot.sh -stop ${src}"
        fi
    done < <(mount)

    mkdir -p "$dst_root"
    rsync -aHAX --numeric-ids "${src_root}/" "${dst_root}/"
    info "Clone complete."
}

handle_install() {
    ensure_root
    ensure_tools
    ensure_base_dirs
    info "Install complete. You are ready to create chroots."
}

handle_new() {
    ensure_root
    ensure_tools
    ensure_base_dirs

    print_iso_menu

    local choice
    while true; do
        read -rp "Choose distro number: " choice
        if [[ "$choice" =~ ^[0-9]+$ ]] && [ "$choice" -ge 1 ] && [ "$choice" -le "${#ISO_KEYS[@]}" ]; then
            break
        fi
        echo "Invalid choice. Please enter a number between 1 and ${#ISO_KEYS[@]}."
    done

    local idx=$((choice-1))
    local key="${ISO_KEYS[$idx]}"

    info "You chose: $key - ${ISO_LABELS[$idx]}"

    # Try to download / ensure ISO exists (even though we don't auto-use it yet)
    local iso_file
    iso_file="$(download_iso "$idx")"
    info "ISO cached at: $iso_file"

    local name=""
    while true; do
        read -rp "Enter chroot name (e.g. ubuntu24, debian12-lab): " name
        if [ -z "$name" ]; then
            echo "Name cannot be empty."
            continue
        fi
        if [[ "$name" =~ [^a-zA-Z0-9._-] ]]; then
            echo "Use only letters, digits, dot, underscore, dash."
            continue
        fi
        if [ -d "${CHROOT_BASE}/${name}" ]; then
            echo "Chroot ${CHROOT_BASE}/${name} already exists. Choose another name."
            continue
        fi
        break
    done

    create_chroot_rootfs "$key" "$name"
    info "You can now start it with:"
    info "  _chroot.sh -start ${name}"
}

# --------- main ---------
main() {
    if [ "$#" -lt 1 ]; then
        usage
        echo
        echo "No arguments given. Here’s the distro menu to get you going:"
        echo "========================================================="
        print_iso_menu
        exit 1
    fi

    case "$1" in
        -install)
            shift
            handle_install
            ;;
        -new)
            shift
            handle_new
            ;;
        -start)
            shift
            [ "$#" -ge 1 ] || err "Usage: _chroot.sh -start <name>"
            ensure_root
            ensure_tools
            start_chroot "$1"
            ;;
        -stop)
            shift
            [ "$#" -ge 1 ] || err "Usage: _chroot.sh -stop <name>"
            ensure_root
            stop_chroot "$1"
            ;;
        -clone)
            shift
            [ "$#" -ge 2 ] || err "Usage: _chroot.sh -clone <src> <dst>"
            ensure_root
            clone_chroot "$1" "$2"
            ;;
        -h|--help|help)
            usage
            ;;
        *)
            err "Unknown option: $1"
            ;;
    esac
}

main "$@"
