#!/usr/bin/env bash
#
# auto_brain_install.sh
# Multi-distro installer for your autonomous project-brain stack.
#
# Safe-by-design: installs packages, creates venv, no deletes, no config nukes.
#

set -euo pipefail

# -----------------------------
# Color helpers
# -----------------------------
RED="$(printf '\033[0;31m')"
GRN="$(printf '\033[0;32m')"
YEL="$(printf '\033[0;33m')"
BLU="$(printf '\033[0;34m')"
CYN="$(printf '\033[0;36m')"
BOLD="$(printf '\033[1m')"
RESET="$(printf '\033[0m')"

log_info()  { printf "%s[INFO]%s  %s\n"  "$CYN" "$RESET" "$*"; }
log_warn()  { printf "%s[WARN]%s  %s\n"  "$YEL" "$RESET" "$*"; }
log_error() { printf "%s[ERROR]%s %s\n" "$RED" "$RESET" "$*" >&2; }
log_ok()    { printf "%s[OK]%s    %s\n" "$GRN" "$RESET" "$*"; }

# -----------------------------
# Distro detection
# -----------------------------
if [[ -r /etc/os-release ]]; then
    # shellcheck disable=SC1091
    . /etc/os-release
    DISTRO_ID="${ID:-unknown}"
    DISTRO_LIKE="${ID_LIKE:-}"
else
    DISTRO_ID="unknown"
    DISTRO_LIKE=""
fi

PKG_UPDATE=""
PKG_INSTALL=""
PKG_GROUP_DEV="" # dev tools group (if applicable)

case "$DISTRO_ID" in
    ubuntu|debian|linuxmint|pop)
        PKG_UPDATE="sudo apt-get update -y"
        PKG_INSTALL="sudo apt-get install -y"
        PKG_GROUP_DEV=""
        ;;

    almalinux|rocky|centos|rhel|fedora)
        if command -v dnf >/dev/null 2>&1; then
            PKG_UPDATE="sudo dnf -y update"
            PKG_INSTALL="sudo dnf -y install"
            PKG_GROUP_DEV="sudo dnf -y groupinstall 'Development Tools'"
        else
            PKG_UPDATE="sudo yum -y update"
            PKG_INSTALL="sudo yum -y install"
            PKG_GROUP_DEV="sudo yum -y groupinstall 'Development Tools'"
        fi
        ;;

    arch|manjaro|endeavouros)
        PKG_UPDATE="sudo pacman -Syu --noconfirm"
        PKG_INSTALL="sudo pacman -S --noconfirm"
        PKG_GROUP_DEV="$PKG_INSTALL base-devel"
        ;;

    opensuse*|sles)
        PKG_UPDATE="sudo zypper refresh"
        PKG_INSTALL="sudo zypper install -y"
        PKG_GROUP_DEV="sudo zypper install -y -t pattern devel_C_C++"
        ;;

    *)
        log_warn "Unrecognized distro ID: $DISTRO_ID"
        log_warn "Script will try Debian/Ubuntu-style commands; adjust manually if needed."
        PKG_UPDATE="sudo apt-get update -y || true"
        PKG_INSTALL="sudo apt-get install -y"
        ;;
esac

# -----------------------------
# Usage
# -----------------------------
usage() {
    cat <<EOF
${BOLD}auto_brain_install.sh${RESET}

Sets up core dependencies for your autonomous project manager / meta-brain.

${BOLD}Supported components:${RESET}
  - Base tools: git, curl, wget, tmux, jq, build tools
  - Python: python3, venv, pip
  - Databases: PostgreSQL, Redis
  - Python venv: /opt/auto_brain/venv with core libraries preinstalled

${BOLD}Usage:${RESET}
  $0 --all          Install everything (recommended on new brain server)
  $0 --base         Base tools only
  $0 --python       Python + venv only
  $0 --db           PostgreSQL + Redis
  $0 --venv         Create /opt/auto_brain/venv and install Python libs
  $0 --help         Show this help

You can combine flags, e.g.:
  $0 --base --python --db --venv

EOF
}

if [[ "${1:-}" == "--help" || $# -eq 0 ]]; then
    usage
    exit 0
fi

DO_BASE=0
DO_PYTHON=0
DO_DB=0
DO_VENV=0

for arg in "$@"; do
    case "$arg" in
        --all)
            DO_BASE=1
            DO_PYTHON=1
            DO_DB=1
            DO_VENV=1
            ;;
        --base)   DO_BASE=1 ;;
        --python) DO_PYTHON=1 ;;
        --db)     DO_DB=1 ;;
        --venv)   DO_VENV=1 ;;
        *)
            log_error "Unknown argument: $arg"
            usage
            exit 1
            ;;
    esac
done

log_info "Detected distro: ${BOLD}${DISTRO_ID}${RESET} (like: ${DISTRO_LIKE})"
log_info "Using package manager: ${PKG_INSTALL}"

# -----------------------------
# Install base tools
# -----------------------------
install_base() {
    log_info "Installing base tools..."

    eval "$PKG_UPDATE" || log_warn "Package index update failed, continuing anyway."

    if [[ -n "$PKG_GROUP_DEV" ]]; then
        log_info "Installing development tools group..."
        eval "$PKG_GROUP_DEV" || log_warn "Dev group install failed (may be non-fatal)."
    fi

    case "$DISTRO_ID" in
        ubuntu|debian|linuxmint|pop)
            $PKG_INSTALL \
                build-essential \
                git curl wget tmux jq \
                ca-certificates
            ;;
        almalinux|rocky|centos|rhel|fedora)
            $PKG_INSTALL \
                git curl wget tmux jq \
                ca-certificates \
                gcc gcc-c++ make
            ;;
        arch|manjaro|endeavouros)
            $PKG_INSTALL \
                git curl wget tmux jq \
                base-devel
            ;;
        opensuse*|sles)
            $PKG_INSTALL \
                git curl wget tmux jq \
                ca-certificates \
                gcc gcc-c++ make
            ;;
        *)
            $PKG_INSTALL \
                build-essential \
                git curl wget tmux jq \
                ca-certificates || true
            ;;
    esac

    log_ok "Base tools installed."
}

# -----------------------------
# Install Python stack
# -----------------------------
install_python_stack() {
    log_info "Installing Python 3 + venv + pip..."

    case "$DISTRO_ID" in
        ubuntu|debian|linuxmint|pop)
            $PKG_INSTALL python3 python3-venv python3-pip python3-dev libpq-dev
            ;;
        almalinux|rocky|centos|rhel|fedora)
            $PKG_INSTALL python3 python3-pip python3-devel postgresql-devel
            ;;
        arch|manjaro|endeavouros)
            $PKG_INSTALL python python-pip python-virtualenv postgresql-libs
            ;;
        opensuse*|sles)
            $PKG_INSTALL python3 python3-pip python3-virtualenv python3-devel libpq-devel
            ;;
        *)
            $PKG_INSTALL python3 python3-venv python3-pip python3-dev libpq-dev || true
            ;;
    esac

    log_ok "Python stack installed."
}

# -----------------------------
# Install PostgreSQL + Redis
# -----------------------------
install_databases() {
    log_info "Installing PostgreSQL + Redis..."

    case "$DISTRO_ID" in
        ubuntu|debian|linuxmint|pop)
            $PKG_INSTALL postgresql postgresql-contrib redis-server
            ;;
        almalinux|rocky|centos|rhel|fedora)
            $PKG_INSTALL postgresql-server postgresql-contrib redis
            ;;
        arch|manjaro|endeavouros)
            $PKG_INSTALL postgresql redis
            ;;
        opensuse*|sles)
            $PKG_INSTALL postgresql-server postgresql-contrib redis
            ;;
        *)
            $PKG_INSTALL postgresql postgresql-contrib redis-server || true
            ;;
    esac

    # Initialize Postgres DB where needed (safe no-op if already initialized)
    if command -v postgresql-setup >/dev/null 2>&1; then
        log_info "Initializing PostgreSQL (if not already)..."
        sudo postgresql-setup initdb || true
    fi

    # Enable + start services (best effort)
    for svc in postgresql postgres redis redis-server; do
        if systemctl list-unit-files | grep -q "^${svc}"; then
            log_info "Enabling + starting service: ${svc}"
            sudo systemctl enable "$svc" || true
            sudo systemctl start "$svc" || true
        fi
    done

    log_ok "PostgreSQL + Redis installation step completed."
    log_warn "PostgreSQL is installed with distro defaults; configure users/passwords manually."
}

# -----------------------------
# Set up /opt/auto_brain venv
# -----------------------------
setup_venv() {
    log_info "Setting up Python venv under /opt/auto_brain..."

    sudo mkdir -p /opt/auto_brain
    sudo chown "$(id -u)":"$(id -g)" /opt/auto_brain

    if [[ ! -d /opt/auto_brain/venv ]]; then
        python3 -m venv /opt/auto_brain/venv
        log_ok "Created venv at /opt/auto_brain/venv."
    else
        log_warn "Venv already exists at /opt/auto_brain/venv; reusing."
    fi

    # shellcheck disable=SC1091
    source /opt/auto_brain/venv/bin/activate

    log_info "Installing core Python libraries into venv..."
    pip install --upgrade pip wheel

    # Core libraries for your learning / meta-brain stack:
    pip install \
        openai \
        psycopg[binary] \
        redis \
        pymongo \
        sqlalchemy \
        pydantic \
        tenacity \
        uvloop \
        python-dotenv

    log_ok "Core Python libraries installed into /opt/auto_brain/venv."
    log_info "You can activate it with:"
    printf "  %s\n" "source /opt/auto_brain/venv/bin/activate"
}

# -----------------------------
# Execute requested sections
# -----------------------------
if [[ "$DO_BASE" -eq 1 ]];   then install_base;          fi
if [[ "$DO_PYTHON" -eq 1 ]]; then install_python_stack;  fi
if [[ "$DO_DB" -eq 1 ]];     then install_databases;     fi
if [[ "$DO_VENV" -eq 1 ]];   then setup_venv;            fi

log_ok "auto_brain_install.sh finished."
