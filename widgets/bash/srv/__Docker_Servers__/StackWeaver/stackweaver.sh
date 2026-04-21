#!/usr/bin/env bash
#
# StackWeaver - Per-domain full-stack orchestrator
# - Per-domain YAML configs in /etc/stackweaver/{domain}/config.yml
# - Project roots under /var/www/html/{domain}/...
# - Commands: --encrypt, --decrypt, --domain <domain> -refresh|-start|-stop
# - Uses yq for YAML, openssl for encryption

set -euo pipefail

SCRIPT_NAME="$(basename "$0")"

CONFIG_ROOT="/etc/stackweaver"
WWW_ROOT="/var/www/html"

# -------- Colors --------
if [ -t 1 ]; then
    ESC="$(printf '\033')"

    C_RESET="${ESC}[0m"
    C_BOLD="${ESC}[1m"

    C_RED="${ESC}[31m"
    C_GREEN="${ESC}[32m"
    C_YELLOW="${ESC}[33m"
    C_BLUE="${ESC}[34m"
    C_MAGENTA="${ESC}[35m"
    C_CYAN="${ESC}[36m"

else
    C_RESET=""
    C_BOLD=""
    C_RED=""
    C_GREEN=""
    C_YELLOW=""
    C_BLUE=""
    C_MAGENTA=""
    C_CYAN=""
fi


# -------- Logging helpers --------
die() {
    echo -e "${C_RED}[ERROR]${C_RESET} $*" >&2
    exit 1
}
info() {
    echo -e "${C_BLUE}[INFO]${C_RESET} $*"
}
ok() {
    echo -e "${C_GREEN}[OK]${C_RESET} $*"
}
warn() {
    echo -e "${C_YELLOW}[WARN]${C_RESET} $*"
}

# -------- Help --------
show_help() {
    cat <<EOF
${C_BOLD}${C_CYAN}$SCRIPT_NAME (StackWeaver)${C_RESET} - Per-domain stack orchestrator

${C_BOLD}Config root:${C_RESET}
  Global config directory:     ${C_GREEN}$CONFIG_ROOT${C_RESET}
  Per-domain config directory: ${C_GREEN}$CONFIG_ROOT/{domain-name}/config.yml${C_RESET}
  Per-domain project root:     ${C_GREEN}$WWW_ROOT/{domain-name/${C_RESET}}
  Last-applied snapshot:       ${C_GREEN}$WWW_ROOT/{domain-name}/last.yml${C_RESET}

${C_BOLD}Standalone encryption tools (no domain required):${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --encrypt${C_RESET}
      - Prompts (no echo) for plaintext and key
      - Prints AES-256-CBC + base64 ciphertext
      - Nothing sensitive appears in shell history or arguments

  ${C_GREEN}$SCRIPT_NAME --decrypt${C_RESET}
      - Prompts (no echo) for ciphertext and key
      - Prints decrypted plaintext

${C_BOLD}Domain operations:${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -refresh${C_RESET}
      - Ensure /etc and /var/www structure exists:
            $CONFIG_ROOT/domain-two.top/config.yml
            $WWW_ROOT/domain-two.top/
            $WWW_ROOT/domain-two.top/www
            (and optional service folders based on config)
      - Update last snapshot:
            $WWW_ROOT/domain-two.top/last.yml

  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -start${C_RESET}
      - Read config from:
            $CONFIG_ROOT/domain-two.top/config.yml
      - Ensure directory tree exists
      - ${C_YELLOW}TODO:${C_RESET} Bring up LAMP/Mongo/email/DNS containers for this domain

  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -stop${C_RESET}
      - ${C_YELLOW}TODO:${C_RESET} Stop/remove containers for this domain (without deleting data)

${C_BOLD}Email helpers (YAML-driven, wiring TBD):${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top --email -add user@domain-two.top${C_RESET}
      - Append an email account entry into the domain YAML
      - You may then edit the password and run:
            ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -refresh${C_RESET}
      - ${C_YELLOW}TODO:${C_RESET} Hook into your chosen mail server to create/change mailbox.

${C_BOLD}Typical flows:${C_RESET}
  # New domain from scratch
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -refresh${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -start${C_RESET}

  # Copy an existing config to a new domain
  ${C_GREEN}cp /etc/stackweaver/example.com/config.yml /etc/stackweaver/domain-two.top/config.yml${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -refresh${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -start${C_RESET}

  # Safe config change (e.g., password updated in YAML)
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -stop${C_RESET}
  # edit /etc/stackweaver/domain-two.top/config.yml
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -refresh${C_RESET}
  ${C_GREEN}$SCRIPT_NAME --domain domain-two.top -start${C_RESET}

${C_BOLD}Notes:${C_RESET}
  - StackWeaver does NOT put any secret values on the command line.
  - Passwords should be stored encrypted in YAML using ${C_GREEN}--encrypt${C_RESET} /
    ${C_GREEN}--decrypt${C_RESET}, then applied via -refresh / -start flows.
  - LAMP/Mongo/email/DNS container management is stubbed with TODOs so you can
    plug in your exact Docker (or non-Docker) stack cleanly.
EOF
}

# -------- Package manager detection --------
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
    elif command -v apk >/dev/null 2>&1; then
        echo "apk"
    else
        echo ""
    fi
}

install_yq_if_needed() {
    if command -v yq >/dev/null 2>&1; then
        return
    fi
    warn "yq not found; attempting to install..."
    local pm
    pm="$(detect_pkg_manager)"
    [ -z "$pm" ] && die "Could not detect package manager to install yq. Install it manually."

    if [ "$EUID" -ne 0 ]; then
        die "Installing yq requires root. Run this script as root or install yq manually."
    fi

    case "$pm" in
        apt)    apt-get update -y && apt-get install -y yq ;;
        dnf)    dnf install -y yq ;;
        yum)    yum install -y yq ;;
        pacman) pacman -Sy --noconfirm yq ;;
        zypper) zypper install -y yq ;;
        apk)    apk add --no-cache yq ;;
        *)      die "Unsupported package manager '$pm' for yq installation." ;;
    esac

    command -v yq >/dev/null 2>&1 || die "yq installation failed. Install manually and retry."
    ok "yq installed."
}

install_openssl_if_needed() {
    if command -v openssl >/dev/null 2>&1; then
        return
    fi
    warn "openssl not found; attempting to install..."
    local pm
    pm="$(detect_pkg_manager)"
    [ -z "$pm" ] && die "Could not detect package manager to install openssl. Install it manually."

    if [ "$EUID" -ne 0 ]; then
        die "Installing openssl requires root. Run this script as root or install openssl manually."
    fi

    case "$pm" in
        apt)    apt-get update -y && apt-get install -y openssl ;;
        dnf)    dnf install -y openssl ;;
        yum)    yum install -y openssl ;;
        pacman) pacman -Sy --noconfirm openssl ;;
        zypper) zypper install -y openssl ;;
        apk)    apk add --no-cache openssl ;;
        *)      die "Unsupported package manager '$pm' for openssl installation." ;;
    esac

    command -v openssl >/dev/null 2>&1 || die "openssl installation failed. Install manually and retry."
    ok "openssl installed."
}

# -------- Encryption helpers --------
encrypt_value() {
    install_openssl_if_needed

    echo -ne "${C_CYAN}Enter plaintext to encrypt: ${C_RESET}"
    read -rs PLAINTEXT
    echo
    echo -ne "${C_CYAN}Enter encryption key: ${C_RESET}"
    read -rs KEY
    echo

    if [ -z "$PLAINTEXT" ] || [ -z "$KEY" ]; then
        die "Plaintext or key cannot be empty."
    fi

    local CIPHERTEXT
    CIPHERTEXT="$(printf '%s' "$PLAINTEXT" | openssl enc -aes-256-cbc -a -salt -pbkdf2 -pass stdin <<<"$KEY")" || \
        die "Encryption failed."

    echo
    echo -e "${C_GREEN}Encrypted value (base64):${C_RESET}"
    echo "$CIPHERTEXT"
}

decrypt_value() {
    install_openssl_if_needed

    echo -ne "${C_CYAN}Enter ciphertext (base64): ${C_RESET}"
    read -rs CIPHERTEXT
    echo
    echo -ne "${C_CYAN}Enter decryption key: ${C_RESET}"
    read -rs KEY
    echo

    if [ -z "$CIPHERTEXT" ] || [ -z "$KEY" ]; then
        die "Ciphertext or key cannot be empty."
    fi

    local PLAINTEXT
    PLAINTEXT="$(printf '%s' "$CIPHERTEXT" | openssl enc -d -aes-256-cbc -a -pbkdf2 -pass stdin <<<"$KEY")" || \
        die "Decryption failed. Wrong key or corrupted ciphertext."

    echo
    echo -e "${C_GREEN}Decrypted value:${C_RESET}"
    echo "$PLAINTEXT"
}

# -------- Domain helpers --------
sanitize_domain_id() {
    printf '%s\n' "$1" | tr '.-' '_'
}

domain_config_dir() {
    local domain="$1"
    echo "$CONFIG_ROOT/$domain"
}

domain_config_file() {
    local domain="$1"
    echo "$(domain_config_dir "$domain")/config.yml"
}

domain_root_dir() {
    local domain="$1"
    echo "$WWW_ROOT/$domain"
}

domain_last_file() {
    local domain="$1"
    echo "$(domain_root_dir "$domain")/last.yml"
}

ensure_domain_config_dir() {
    local domain="$1"
    local dir
    dir="$(domain_config_dir "$domain")"
    if [ ! -d "$dir" ]; then
        info "Creating config directory: $dir"
        mkdir -p "$dir"
    fi
}

create_default_config_if_missing() {
    local domain="$1"
    ensure_domain_config_dir "$domain"
    local cfg
    cfg="$(domain_config_file "$domain")"
    if [ -f "$cfg" ]; then
        return
    fi

    info "Creating default config YAML for domain '$domain' at $cfg"
    mkdir -p "$(dirname "$cfg")"
    cat > "$cfg" <<EOF
domain: "$domain"
root: "$(domain_root_dir "$domain")"
docroot: "$(domain_root_dir "$domain")/www"

services:
  apache_php: true
  mysql:
    enabled: false
    database: "${domain//./_}"
    user: "${domain//./_}"
    password_enc: ""
  mongo:
    enabled: false
    database: "${domain//./_}"
    user: "${domain//./_}"
    password_enc: ""
  email:
    enabled: false
    accounts: []
  dns:
    enabled: false

ssl:
  enabled: false
  email: ""
EOF
    ok "Default config created."
}

ensure_domain_dirs() {
    local domain="$1"
    install_yq_if_needed
    local cfg
    cfg="$(domain_config_file "$domain")"

    local root docroot
    root="$(yq e '.root // ""' "$cfg")"
    docroot="$(yq e '.docroot // ""' "$cfg")"

    [ -z "$root" ] && root="$(domain_root_dir "$domain")"
    [ -z "$docroot" ] && docroot="$root/www"

    info "Ensuring directory tree for domain '$domain'..."
    mkdir -p "$root"
    mkdir -p "$docroot"

    local mysql_enabled mongo_enabled email_enabled dns_enabled
    mysql_enabled="$(yq e '.services.mysql.enabled // false' "$cfg")"
    mongo_enabled="$(yq e '.services.mongo.enabled // false' "$cfg")"
    email_enabled="$(yq e '.services.email.enabled // false' "$cfg")"
    dns_enabled="$(yq e '.services.dns.enabled // false' "$cfg")"

    if [ "$mysql_enabled" = "true" ]; then
        mkdir -p "$root/mysql"
    fi
    if [ "$mongo_enabled" = "true" ]; then
        mkdir -p "$root/mongo"
    fi
    if [ "$email_enabled" = "true" ]; then
        mkdir -p "$root/email"
    fi
    if [ "$dns_enabled" = "true" ]; then
        mkdir -p "$root/named"
    fi

    ok "Directory structure ensured for '$domain'."
}

snapshot_last_config() {
    local domain="$1"
    local cfg last
    cfg="$(domain_config_file "$domain")"
    last="$(domain_last_file "$domain")"

    mkdir -p "$(dirname "$last")"
    cp "$cfg" "$last"
    ok "Snapshot of config saved to $last"
}

# -------- Domain operations --------
refresh_domain() {
    local domain="$1"
    install_yq_if_needed
    create_default_config_if_missing "$domain"
    ensure_domain_dirs "$domain"
    snapshot_last_config "$domain"

    ok "Refresh complete for domain '$domain'."
    echo -e "  Config:  ${C_GREEN}$(domain_config_file "$domain")${C_RESET}"
    echo -e "  Root:    ${C_GREEN}$(domain_root_dir "$domain")${C_RESET}"
}

start_domain() {
    local domain="$1"
    install_yq_if_needed
    create_default_config_if_missing "$domain"
    ensure_domain_dirs "$domain"

    local cfg
    cfg="$(domain_config_file "$domain")"
    local id
    id="$(sanitize_domain_id "$domain")"
    local root docroot
    root="$(yq e '.root // ""' "$cfg")"
    docroot="$(yq e '.docroot // ""' "$cfg")"
    [ -z "$root" ] && root="$(domain_root_dir "$domain")"
    [ -z "$docroot" ] && docroot="$root/www"

    info "Starting stack for domain '$domain' (id: $id)..."

    local apache_enabled mysql_enabled mongo_enabled email_enabled dns_enabled
    apache_enabled="$(yq e '.services.apache_php // true' "$cfg")"
    mysql_enabled="$(yq e '.services.mysql.enabled // false' "$cfg")"
    mongo_enabled="$(yq e '.services.mongo.enabled // false' "$cfg")"
    email_enabled="$(yq e '.services.email.enabled // false' "$cfg")"
    dns_enabled="$(yq e '.services.dns.enabled // false' "$cfg")"

    echo
    echo -e "${C_YELLOW}[TODO]${C_RESET} Add Docker (or other) start logic for:"
    [ "$apache_enabled" = "true" ] && echo "  - Apache/PHP web container for $domain (docroot: $docroot)"
    [ "$mysql_enabled" = "true" ] && echo "  - MySQL database for $domain (data: $root/mysql)"
    [ "$mongo_enabled" = "true" ] && echo "  - MongoDB database for $domain (data: $root/mongo)"
    [ "$email_enabled" = "true" ] && echo "  - Email service for $domain (config/data: $root/email)"
    [ "$dns_enabled" = "true" ] && echo "  - DNS/named service for $domain (config/data: $root/named)"

    snapshot_last_config "$domain"
    ok "Start routine complete for '$domain' (infra wiring TODO as noted)."
}

stop_domain() {
    local domain="$1"
    install_yq_if_needed
    create_default_config_if_missing "$domain"
    local id
    id="$(sanitize_domain_id "$domain")"

    info "Stopping stack for domain '$domain' (id: $id)..."

    echo
    echo -e "${C_YELLOW}[TODO]${C_RESET} Add Docker (or other) stop/remove logic for domain '$domain'."
    ok "Stop routine completed for '$domain' (no containers manipulated yet)."
}

# -------- Email YAML helpers --------
add_email_account_to_yaml() {
    local domain="$1"
    local address="$2"
    install_yq_if_needed
    create_default_config_if_missing "$domain"
    local cfg
    cfg="$(domain_config_file "$domain")"

    yq e -i '.services.email.enabled = true' "$cfg"

    local exists
    exists="$(yq e ".services.email.accounts[]?.address == \"$address\"" "$cfg" 2>/dev/null || echo "false")"

    if echo "$exists" | grep -q "true"; then
        warn "Email address '$address' already present in YAML for domain '$domain'."
    else
        info "Adding email account '$address' to YAML for domain '$domain'."
        yq e -i ".services.email.accounts += [{\"address\": \"$address\", \"password_enc\": \"\"}]" "$cfg"
        ok "Email account '$address' added. Edit password_enc and run -refresh/-start."
    fi
}

# -------- CLI parsing --------
if [ "$#" -eq 0 ]; then
    show_help
    exit 0
fi

if [ "$1" = "--encrypt" ]; then
    shift
    if [ "$#" -ne 0 ]; then
        die "--encrypt must be used alone (no extra arguments)."
    fi
    encrypt_value
    exit 0
fi

if [ "$1" = "--decrypt" ]; then
    shift
    if [ "$#" -ne 0 ]; then
        die "--decrypt must be used alone (no extra arguments)."
    fi
    decrypt_value
    exit 0
fi

DOMAIN=""
ACTION=""
EMAIL_OP=""
EMAIL_ADDRESS=""

while [ "$#" -gt 0 ]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        --domain)
            shift
            [ -z "${1:-}" ] && die "Missing domain name after --domain."
            DOMAIN="$1"
            shift
            ;;
        -refresh)
            ACTION="refresh"
            shift
            ;;
        -start)
            ACTION="start"
            shift
            ;;
        -stop)
            ACTION="stop"
            shift
            ;;
        --email)
            EMAIL_OP="manage"
            shift
            ;;
        -add)
            shift
            [ -z "${1:-}" ] && die "Missing email address after -add."
            EMAIL_ADDRESS="$1"
            shift
            ;;
        *)
            die "Unknown argument: $1 (use -h for help)"
            ;;
    esac
done

if [ -z "$DOMAIN" ]; then
    die "Domain-scoped operations require --domain <name>. (Use -h for help.)"
fi

if [ -n "$EMAIL_OP" ] && [ -n "$EMAIL_ADDRESS" ] && [ -z "$ACTION" ]; then
    add_email_account_to_yaml "$DOMAIN" "$EMAIL_ADDRESS"
    exit 0
fi

if [ -z "$ACTION" ]; then
    die "No action specified for domain '$DOMAIN'. Use -refresh, -start, -stop or email ops."
fi

if [ ! -d "$CONFIG_ROOT" ]; then
    info "Creating StackWeaver global config root: $CONFIG_ROOT"
    mkdir -p "$CONFIG_ROOT"
fi

case "$ACTION" in
    refresh) refresh_domain "$DOMAIN" ;;
    start)   start_domain "$DOMAIN" ;;
    stop)    stop_domain "$DOMAIN" ;;
    *)       die "Unknown action '$ACTION' (should not happen)." ;;
esac
