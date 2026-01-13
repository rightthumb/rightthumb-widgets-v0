#!/usr/bin/env bash
# chroot_master.sh - master bad ass chroot manager
# Combines:
#  - debootstrap + rootfs distros
#  - interactive numbered menu (1 ubuntu, 22; 2 ubuntu, 24; etc.)
#  - cache downloads
#  - start scripts per chroot with shm/devpts/dbus/resolv.conf mounts
#  - start/stop/clone/install

set -euo pipefail

# ========= Config =========
CHROOT_BASE="${CHROOT_BASE:-/mnt/chroot}"
CACHE_DIR="${CHROOT_BASE}/_cache"

# ========= Logging =========
log(){  printf '[*] %s\n' "$*" >&2; }
info(){ printf '[+] %s\n' "$*" >&2; }
warn(){ printf '[!] %s\n' "$*" >&2; }
err(){  printf '[ERROR] %s\n' "$*" >&2; exit 1; }

# ========= Root / deps =========
ensure_root() {
  if [[ "$(id -u)" -ne 0 ]]; then
    err "Run as root: sudo $0 ..."
  fi
}

have(){ command -v "$1" >/dev/null 2>&1; }

install_deps() {
  # Keep it broad; install what we might use.
  # debootstrap only needed for Debian-family, but it’s fine.
  local pkgs_deb=(debootstrap wget curl rsync tar xz-utils gzip bzip2 unzip util-linux)
  local pkgs_rpm=(debootstrap wget curl rsync tar xz gzip bzip2 unzip util-linux)
  local pkgs_pac=(debootstrap wget curl rsync tar xz gzip bzip2 unzip util-linux)

  if have apt-get; then
    info "Installing deps via apt-get..."
    apt-get update
    apt-get install -y "${pkgs_deb[@]}"
  elif have dnf; then
    info "Installing deps via dnf..."
    dnf install -y "${pkgs_rpm[@]}" || dnf install -y wget curl rsync tar xz gzip bzip2 unzip util-linux
  elif have pacman; then
    info "Installing deps via pacman..."
    pacman -Sy --noconfirm "${pkgs_pac[@]}" || pacman -Sy --noconfirm wget curl rsync tar xz gzip bzip2 unzip util-linux
  else
    err "Unsupported package manager. Install manually: debootstrap wget/curl rsync tar xz gzip bzip2 unzip util-linux"
  fi
}

ensure_dirs() {
  mkdir -p "$CHROOT_BASE" "$CACHE_DIR"
}

# ========= Distro database =========
# We keep:
#  - method: debootstrap|rootfs
#  - for debootstrap: suite + mirror
#  - for rootfs: url only (archive)
#
# Also: menu entries are separate so we can show "ubuntu, 22" style prompts.

declare -A DISTRO_METHOD
declare -A DISTRO_OS
declare -A DISTRO_VER
declare -A DISTRO_SUITE
declare -A DISTRO_MIRROR
declare -A DISTRO_URL

# ---- Debian-family (debootstrap) ----
add_debootstrap() {
  local key="$1" os="$2" ver="$3" suite="$4" mirror="$5"
  DISTRO_METHOD["$key"]="debootstrap"
  DISTRO_OS["$key"]="$os"
  DISTRO_VER["$key"]="$ver"
  DISTRO_SUITE["$key"]="$suite"
  DISTRO_MIRROR["$key"]="$mirror"
}

# ---- Rootfs tarball ----
add_rootfs() {
  local key="$1" os="$2" ver="$3" url="$4"
  DISTRO_METHOD["$key"]="rootfs"
  DISTRO_OS["$key"]="$os"
  DISTRO_VER["$key"]="$ver"
  DISTRO_URL["$key"]="$url"
}

# Populate presets (mix of your two scripts + your big list)
# Ubuntu
add_debootstrap "ubuntu:18" "ubuntu" "18" "bionic" "http://archive.ubuntu.com/ubuntu"
add_debootstrap "ubuntu:20" "ubuntu" "20" "focal"  "http://archive.ubuntu.com/ubuntu"
add_debootstrap "ubuntu:22" "ubuntu" "22" "jammy"  "http://archive.ubuntu.com/ubuntu"
add_debootstrap "ubuntu:24" "ubuntu" "24" "noble"  "http://archive.ubuntu.com/ubuntu"

# Debian
add_debootstrap "debian:12" "debian" "12" "bookworm" "http://deb.debian.org/debian"
add_debootstrap "debian:13" "debian" "13" "trixie"   "http://deb.debian.org/debian"
add_debootstrap "debian:11" "debian" "11" "bullseye" "http://deb.debian.org/debian"

# Kali/Devuan/Parrot
add_debootstrap "kali:rolling"   "kali"   "rolling" "kali-rolling" "http://http.kali.org/kali"
add_debootstrap "devuan:daedalus" "devuan" "daedalus" "daedalus" "http://deb.devuan.org/merged"
add_debootstrap "parrot:stable"  "parrot" "stable"  "parrot" "http://deb.parrot.sh/parrot"

# Rootfs distros (tarballs)
add_rootfs "arch:latest"     "arch"     "latest" "https://mirror.rackspace.com/archlinux/iso/latest/archlinux-bootstrap-x86_64.tar.gz"
add_rootfs "alpine:3.18"     "alpine"   "3.18"   "https://dl-cdn.alpinelinux.org/alpine/v3.18/releases/x86_64/alpine-minirootfs-3.18.4-x86_64.tar.gz"
add_rootfs "void:current"    "void"     "current" "https://repo-default.voidlinux.org/live/current/void-x86_64-ROOTFS-20230628.tar.xz"
add_rootfs "gentoo:stage3"   "gentoo"   "stage3"  "https://distfiles.gentoo.org/releases/amd64/autobuilds/current-stage3-amd64/stage3-amd64.tar.xz"
add_rootfs "fedora:39"       "fedora"   "39"      "https://download.fedoraproject.org/pub/fedora/linux/releases/39/Container/x86_64/images/Fedora-Container-Base-39-1.5.x86_64.tar.xz"
add_rootfs "opensuse:tumbleweed" "opensuse" "tumbleweed" "https://download.opensuse.org/tumbleweed/appliances/openSUSE-Tumbleweed-ContainerHost.x86_64-ContainerHost-rootfs.tar.xz"
add_rootfs "chimera:latest"  "chimera"  "latest"  "https://github.com/chimera-linux/cports/releases/latest/download/chimera-rootfs.tar.xz"

# Menu order (curated; add/remove as you like)
MENU_KEYS=(
  "ubuntu:22"
  "ubuntu:24"
  "debian:12"
  "debian:13"
  "kali:rolling"
  "devuan:daedalus"
  "parrot:stable"
  "arch:latest"
  "alpine:3.18"
  "void:current"
  "gentoo:stage3"
  "fedora:39"
  "opensuse:tumbleweed"
  "chimera:latest"
)

# ========= Helpers =========
usage() {
  cat <<EOF
Usage:
  $0 -install
  $0 -new
  $0 -start <name>
  $0 -stop  <name>
  $0 -clone <src> <dst>
  $0 -list
  $0 -h|--help

Notes:
  - Chroots live under: $CHROOT_BASE/<name>
  - Cache lives under:  $CACHE_DIR
  - Start scripts:      $CHROOT_BASE/start-<name>.sh
EOF
}

list_distros() {
  echo "Available distros:"
  local i=1 k os ver method
  for k in "${MENU_KEYS[@]}"; do
    os="${DISTRO_OS[$k]}"
    ver="${DISTRO_VER[$k]}"
    method="${DISTRO_METHOD[$k]}"
    printf "  %2d) %-8s, %-10s  (%s)\n" "$i" "$os" "$ver" "$method"
    ((i++))
  done
}

prompt_menu_choice() {
  list_distros
  local choice
  while true; do
    read -rp "Choose distro number (1-${#MENU_KEYS[@]}): " choice
    [[ "$choice" =~ ^[0-9]+$ ]] || { echo "Enter a number."; continue; }
    (( choice >= 1 && choice <= ${#MENU_KEYS[@]} )) || { echo "Out of range."; continue; }
    echo "${MENU_KEYS[$((choice-1))]}"
    return 0
  done
}

download_to_cache() {
  local url="$1"
  local file="$CACHE_DIR/$(basename "$url")"

  if [[ -f "$file" ]]; then
    info "Cache hit: $file"
    echo "$file"
    return 0
  fi

  info "Downloading to cache: $url"
  if have curl; then
    curl -L --fail --retry 3 -o "$file" "$url"
  elif have wget; then
    wget -O "$file" "$url"
  else
    err "Need curl or wget."
  fi

  echo "$file"
}

extract_rootfs_into() {
  local archive="$1"
  local dest="$2"

  mkdir -p "$dest"

  info "Extracting $(basename "$archive") -> $dest"

  case "$archive" in
    *.tar.gz|*.tgz)   tar -xzf "$archive" -C "$dest" ;;
    *.tar.xz)         tar -xJf "$archive" -C "$dest" ;;
    *.tar.bz2|*.tbz2) tar -xjf "$archive" -C "$dest" ;;
    *.zip)            unzip -o "$archive" -d "$dest" ;;
    *.gz)
      local out="${archive%.gz}"
      gunzip -kf "$archive"
      mv -f "$out" "$dest/" ;;
    *.xz)
      local out="${archive%.xz}"
      xz -dkf "$archive"
      mv -f "$out" "$dest/" ;;
    *.bz2)
      local out="${archive%.bz2}"
      bunzip2 -kf "$archive"
      mv -f "$out" "$dest/" ;;
    *)
      err "Don't know how to extract: $archive"
      ;;
  esac

  # Some rootfs tarballs have top-level folder; your old script tried both.
  # We handle that more safely: if dest has exactly one subdir and looks like a rootfs, optionally flatten.
  if [[ -d "$dest" ]]; then
    local subdirs
    subdirs="$(find "$dest" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
    local has_etc=0
    [[ -d "$dest/etc" ]] && has_etc=1
    if [[ "$has_etc" -eq 0 && "$subdirs" -eq 1 ]]; then
      local onlydir
      onlydir="$(find "$dest" -mindepth 1 -maxdepth 1 -type d | head -n1)"
      if [[ -d "$onlydir/etc" ]]; then
        info "Flattening one-level rootfs directory: $(basename "$onlydir")"
        shopt -s dotglob
        mv "$onlydir"/* "$dest/"
        rmdir "$onlydir" || true
        shopt -u dotglob
      fi
    fi
  fi
}

# ========= Start script generator (your fancy one) =========
make_start_script() {
  local name="$1"
  local path="$CHROOT_BASE/$name"
  local script="$CHROOT_BASE/start-$name.sh"

  cat > "$script" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

CHROOT="__CHROOT_PATH__"

mount_bind() {
  sudo mount --bind /dev "$CHROOT/dev"
  sudo mount --bind /dev/pts "$CHROOT/dev/pts" 2>/dev/null || true
  sudo mount -t proc /proc "$CHROOT/proc"
  sudo mount --bind /sys "$CHROOT/sys"

  # /dev/shm
  if ! mountpoint -q "$CHROOT/dev/shm"; then
    sudo mkdir -p "$CHROOT/dev/shm"
    sudo mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs "$CHROOT/dev/shm"
    sudo chmod 1777 "$CHROOT/dev/shm"
  fi

  # DNS
  if [[ ! -f "$CHROOT/etc/resolv.conf" ]]; then
    sudo mkdir -p "$CHROOT/etc"
    sudo cp /etc/resolv.conf "$CHROOT/etc/resolv.conf" || true
  fi

  # Optional: D-Bus system socket bind
  if [[ -S /run/dbus/system_bus_socket ]]; then
    sudo mkdir -p "$CHROOT/run/dbus"
    sudo mount --bind /run/dbus "$CHROOT/run/dbus"
  fi
}

umount_bind() {
  sudo umount -l "$CHROOT/run/dbus" 2>/dev/null || true
  sudo umount -l "$CHROOT/dev/shm" 2>/dev/null || true
  sudo umount -l "$CHROOT/dev/pts" 2>/dev/null || true
  sudo umount -l "$CHROOT/dev" 2>/dev/null || true
  sudo umount -l "$CHROOT/proc" 2>/dev/null || true
  sudo umount -l "$CHROOT/sys" 2>/dev/null || true
}

trap umount_bind EXIT

mount_bind
sudo chroot "$CHROOT" /bin/bash --login
EOF

  # inject path
  sed -i "s|__CHROOT_PATH__|$path|g" "$script"
  chmod +x "$script"

  # QoL inside chroot sessions
  if [[ -f "$path/etc/bash.bashrc" ]]; then
    cat >> "$path/etc/bash.bashrc" <<'EOB'

# --- chroot QoL mounts ---
if command -v mountpoint >/dev/null 2>&1; then
  if ! mountpoint -q /dev/pts; then
    mount -t devpts devpts /dev/pts 2>/dev/null || true
  fi
  if ! mountpoint -q /dev/shm; then
    mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs /dev/shm 2>/dev/null || true
    chmod 1777 /dev/shm 2>/dev/null || true
  fi
fi
EOB
  fi

  info "Start script created: $script"
}

# ========= Core operations =========
setup_chroot() {
  local key="$1"
  local name="$2"
  local method="${DISTRO_METHOD[$key]:-}"

  [[ -n "$method" ]] || err "Unknown distro key: $key"

  local target="$CHROOT_BASE/$name"
  [[ ! -d "$target" ]] || err "Chroot exists already: $target"
  mkdir -p "$target"

  info "Creating chroot: $name"
  info "  Distro: ${DISTRO_OS[$key]}, ${DISTRO_VER[$key]}"
  info "  Method: $method"

  if [[ "$method" == "debootstrap" ]]; then
    have debootstrap || err "debootstrap not found. Run: $0 -install"
    local suite="${DISTRO_SUITE[$key]}"
    local mirror="${DISTRO_MIRROR[$key]}"
    debootstrap --arch=amd64 "$suite" "$target" "$mirror"
    echo "proc /proc proc defaults 0 0" >> "$target/etc/fstab" || true
    [[ -f "$target/etc/resolv.conf" ]] || cp /etc/resolv.conf "$target/etc/resolv.conf" 2>/dev/null || true
  elif [[ "$method" == "rootfs" ]]; then
    local url="${DISTRO_URL[$key]}"
    local archive
    archive="$(download_to_cache "$url")"
    extract_rootfs_into "$archive" "$target"
    [[ -f "$target/etc/resolv.conf" ]] || cp /etc/resolv.conf "$target/etc/resolv.conf" 2>/dev/null || true
  else
    err "Unsupported method: $method"
  fi

  make_start_script "$name"
  info "Chroot ready: $target"
}

mount_bind() {
  local name="$1"
  local root="$CHROOT_BASE/$name"
  [[ -d "$root" ]] || err "No such chroot: $root"

  mkdir -p "$root/dev" "$root/proc" "$root/sys" "$root/run" "$root/dev/pts" "$root/dev/shm"

  mountpoint -q "$root/dev"      || mount --bind /dev "$root/dev"
  mountpoint -q "$root/dev/pts"  || mount --bind /dev/pts "$root/dev/pts"
  mountpoint -q "$root/proc"     || mount -t proc /proc "$root/proc"
  mountpoint -q "$root/sys"      || mount --bind /sys "$root/sys"
  mountpoint -q "$root/run"      || mount --bind /run "$root/run"

  if ! mountpoint -q "$root/dev/shm"; then
    mount -t tmpfs -o rw,nosuid,nodev,noexec,relatime,size=512M tmpfs "$root/dev/shm"
    chmod 1777 "$root/dev/shm"
  fi

  # Optional: D-Bus
  if [[ -S /run/dbus/system_bus_socket ]]; then
    mkdir -p "$root/run/dbus"
    mountpoint -q "$root/run/dbus" || mount --bind /run/dbus "$root/run/dbus"
  fi

  # DNS
  [[ -f "$root/etc/resolv.conf" ]] || cp /etc/resolv.conf "$root/etc/resolv.conf" 2>/dev/null || true
}

umount_bind() {
  local name="$1"
  local root="$CHROOT_BASE/$name"
  [[ -d "$root" ]] || err "No such chroot: $root"

  for p in "$root/run/dbus" "$root/dev/shm" "$root/run" "$root/sys" "$root/proc" "$root/dev/pts" "$root/dev"; do
    if mountpoint -q "$p"; then
      umount -l "$p" || warn "Failed to unmount $p"
    fi
  done
}

start_chroot() {
  local name="$1"
  mount_bind "$name"
  info "Entering chroot: $name"
  chroot "$CHROOT_BASE/$name" /bin/bash --login
}

stop_chroot() {
  local name="$1"
  umount_bind "$name"
  info "Stopped: $name"
}

clone_chroot() {
  local src="$1" dst="$2"
  local src_root="$CHROOT_BASE/$src"
  local dst_root="$CHROOT_BASE/$dst"

  [[ -d "$src_root" ]] || err "Source doesn't exist: $src_root"
  [[ ! -d "$dst_root" ]] || err "Destination exists: $dst_root"

  # Refuse if source has active mounts
  while read -r line; do
    if echo "$line" | grep -q "^$src_root/"; then
      err "Source has active mounts. Stop it first: $0 -stop $src"
    fi
  done < <(mount)

  info "Cloning $src -> $dst (rsync -aHAX)"
  mkdir -p "$dst_root"
  rsync -aHAX --numeric-ids "$src_root/" "$dst_root/"

  make_start_script "$dst"
  info "Clone complete: $dst_root"
}

handle_new() {
  ensure_root
  ensure_dirs

  local key
  key="$(prompt_menu_choice)"

  local name
  while true; do
    read -rp "Enter chroot name (e.g. ubuntu24, debian12-lab): " name
    [[ -n "$name" ]] || { echo "Name cannot be empty."; continue; }
    [[ "$name" =~ ^[a-zA-Z0-9._-]+$ ]] || { echo "Use only letters/digits/dot/underscore/dash."; continue; }
    [[ ! -d "$CHROOT_BASE/$name" ]] || { echo "Already exists: $CHROOT_BASE/$name"; continue; }
    break
  done

  setup_chroot "$key" "$name"
  info "Start it with:"
  info "  $CHROOT_BASE/start-$name.sh"
  info "or:"
  info "  sudo $0 -start $name"
}

# ========= Main =========
main() {
  if [[ $# -lt 1 ]]; then
    usage
    echo
    list_distros
    exit 1
  fi

  case "$1" in
    -install)
      ensure_root
      ensure_dirs
      install_deps
      info "Install complete."
      ;;
    -list)
      list_distros
      ;;
    -new)
      handle_new
      ;;
    -start)
      ensure_root
      [[ $# -ge 2 ]] || err "Usage: $0 -start <name>"
      start_chroot "$2"
      ;;
    -stop)
      ensure_root
      [[ $# -ge 2 ]] || err "Usage: $0 -stop <name>"
      stop_chroot "$2"
      ;;
    -clone)
      ensure_root
      [[ $# -ge 3 ]] || err "Usage: $0 -clone <src> <dst>"
      clone_chroot "$2" "$3"
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
