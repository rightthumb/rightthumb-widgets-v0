#!/usr/bin/env bash
#
# www.sh - Simple secure PHP+Apache Docker launcher with optional Let's Encrypt SSL
# - Installs Docker if missing (apt/dnf/yum/pacman/zypper/apk)
# - Builds a hardened php:8.2-apache image (HTTP + HTTPS support)
# - Serves a single folder or multiple domains from one container
# - SSL switches: -ssl/--ssl, -no-ssl/--no-ssl
#   * If no SSL switches are used: show help and exit
#   * If -ssl/--ssl is used: prompt "force? Y/n" at the beginning

set -e

SCRIPT_NAME="$(basename "$0")"
IMAGE_NAME="secure-php-apache"
DEFAULT_PORT="8080"

# -------- Colors --------
if [ -t 1 ]; then
    C_RESET="\033[0m"
    C_BOLD="\033[1m"
    C_RED="\033[31m"
    C_GREEN="\033[32m"
    C_YELLOW="\033[33m"
    C_BLUE="\033[34m"
    C_CYAN="\033[36m"
else
    C_RESET=""
    C_BOLD=""
    C_RED=""
    C_GREEN=""
    C_YELLOW=""
    C_BLUE=""
    C_CYAN=""
fi

# -------- Help --------
show_help() {
    cat <<EOF
${C_BOLD}${C_CYAN}$SCRIPT_NAME${C_RESET} - Secure PHP+Apache Docker server launcher (HTTP + optional HTTPS)

${C_BOLD}You MUST choose SSL mode:${C_RESET}
  ${C_GREEN}-ssl${CRESET}, ${C_GREEN}--ssl${CRESET}       Enable HTTPS (Let's Encrypt, multi-domain only)
  ${C_GREEN}-no-ssl${CRESET}, ${C_GREEN}--no-ssl${CRESET} Disable HTTPS (HTTP only)

If no SSL switches are used, this help is shown and the script exits.

${C_BOLD}HTTP-only mode (no SSL):${C_RESET}
  ${C_GREEN}$SCRIPT_NAME -no-ssl -single /var/www/html/public${CRESET}
      Serve a single folder as the default site (all hostnames) on port ${DEFAULT_PORT}.

  ${C_GREEN}$SCRIPT_NAME -no-ssl -domain domain-one.top /var/www/html/domain-one.top${CRESET}
      Serve a single domain from its own document root (HTTP only).

  ${C_GREEN}$SCRIPT_NAME -no-ssl -port 8080 \\${CRESET}
  ${C_GREEN}        -domain domain-one.top /var/www/html/domain-one.top \\${CRESET}
  ${C_GREEN}        -domain domain-two.top /var/www/html/domain-two.top${CRESET}
      Serve ${C_BOLD}multiple domains${C_RESET} from one container (HTTP only).

  ${C_GREEN}-port 8080${CRESET}
      Listen on a specific host port for HTTP (default: ${DEFAULT_PORT}).

${C_BOLD}HTTPS mode (Let's Encrypt):${C_RESET}
  ${C_GREEN}sudo $SCRIPT_NAME -ssl --email you@example.com \\${CRESET}
  ${C_GREEN}      -domain domain-one.top /var/www/html/domain-one.top \\${CRESET}
  ${C_GREEN}      -domain domain-two.top /var/www/html/domain-two.top${CRESET}

  - Requires:
      - Real DNS A/AAAA records for each domain pointing to this server.
      - Ports ${C_BOLD}80 and 443${C_RESET} open to the internet (HTTP + HTTPS).
      - Root/sudo to run certbot and bind to port 80.
  - The script will:
      ${C_YELLOW}1.${C_RESET} Ask "force? Y/n" when -ssl/--ssl is used.
      ${C_YELLOW}2.${C_RESET} Install certbot if missing.
      ${C_YELLOW}3.${C_RESET} Request or reuse a Let's Encrypt cert for all domains.
      ${C_YELLOW}4.${C_RESET} Start Docker container on host ports 80 (HTTP redirect) and 443 (HTTPS).

${C_BOLD}Examples:${C_RESET}
  # Single site on http://localhost:${DEFAULT_PORT}/ (HTTP only)
  ${C_GREEN}$SCRIPT_NAME -no-ssl -single /var/www/html/public${CRESET}

  # Multiple domains, HTTP only, port 8080
  ${C_GREEN}$SCRIPT_NAME -no-ssl -port 8080 \\
      -domain domain-one.top /var/www/html/domain-one.top \\
      -domain domain-two.top /var/www/html/domain-two.top${CRESET}

  # Multiple domains with SSL (Let's Encrypt), ports 80+443
  ${C_GREEN}sudo $SCRIPT_NAME -ssl --email you@example.com \\
      -domain domain-one.top /var/www/html/domain-one.top \\
      -domain domain-two.top /var/www/html/domain-two.top${CRESET}

${C_BOLD}What this script does:${CRESET}
  ${C_YELLOW}1.${C_RESET} Checks for Docker, installs it if missing.
  ${C_YELLOW}2.${C_RESET} Builds a hardened image: ${C_BOLD}$IMAGE_NAME${C_RESET} (php:8.2-apache).
  ${C_YELLOW}3.${C_RESET} Generates Apache vhost config based on your arguments.
  ${C_YELLOW}4.${C_RESET} Starts a Docker container:
        - HTTP only: ${C_BOLD}php-www-<port>${C_RESET}
        - HTTPS:     ${C_BOLD}php-www-ssl${C_RESET}
        - Your code mounted ${C_BOLD}read-only${C_RESET}
        - Basic Apache/PHP security hardening enabled.

${C_BOLD}Notes:${C_RESET}
  - SSL mode works only with ${C_BOLD}-domain${C_RESET}, not with -single.
  - In SSL mode, host ports ${C_BOLD}80 and 443${C_RESET} are used (ignoring -port).
  - Stop/remove manually if needed:
        ${C_GREEN}docker stop php-www-<name> && docker rm php-www-<name>${CRESET}
EOF
}

# -------- Logging helpers --------
die() {
    echo -e "${C_RED}[ERROR]${C_RESET} $*" >&2
    exit 1
}

info() {
    echo -e "${C_BLUE}[INFO]${C_RESET} $*"
}

ok() {
    echo -e "${C_GREEN}[OK]${CRESET} $*"
}

warn() {
    echo -e "${C_YELLOW}[WARN]${CRESET} $*"
}

# -------- Detect package manager --------
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

# -------- Install Docker if missing --------
install_docker_if_needed() {
    if command -v docker >/dev/null 2>&1; then
        ok "Docker is already installed."
        return
    fi

    warn "Docker is not installed. Attempting to install..."

    local pm
    pm="$(detect_pkg_manager)"
    [ -z "$pm" ] && die "Unsupported or undetected package manager. Please install Docker manually."

    if [ "$EUID" -ne 0 ]; then
        die "Docker is missing. Please run this script as root (or with sudo) to install Docker."
    fi

    case "$pm" in
        apt)
            info "Using apt-get to install docker.io..."
            apt-get update -y
            apt-get install -y docker.io
            ;;
        dnf)
            info "Using dnf to install docker..."
            dnf install -y docker
            ;;
        yum)
            info "Using yum to install docker..."
            yum install -y docker
            ;;
        pacman)
            info "Using pacman to install docker..."
            pacman -Sy --noconfirm docker
            ;;
        zypper)
            info "Using zypper to install docker..."
            zypper install -y docker
            ;;
        apk)
            info "Using apk to install docker..."
            apk add --no-cache docker
            ;;
        *)
            die "Unsupported package manager '$pm'. Install Docker manually."
            ;;
    esac

    if command -v systemctl >/dev/null 2>&1; then
        info "Enabling and starting docker service..."
        systemctl enable docker || true
        systemctl start docker || true
    else
        warn "Could not find systemctl; please ensure Docker daemon is running."
    fi

    if command -v docker >/dev/null 2>&1; then
        ok "Docker installed."
    else
        die "Docker installation appears to have failed."
    fi
}

# -------- Ensure Docker daemon is reachable --------
ensure_docker_running() {
    if ! docker info >/dev/null 2>&1; then
        warn "Docker daemon does not seem to be running."
        echo "Try: ${C_GREEN}sudo systemctl start docker${CRESET} (or equivalent for your distro)."
        die "Docker is not ready."
    fi
}

# -------- Build secure PHP+Apache image if missing (HTTP + HTTPS capable) --------
build_image_if_needed() {
    if docker image inspect "$IMAGE_NAME:latest" >/dev/null 2>&1; then
        ok "Docker image '$IMAGE_NAME' already exists."
        return
    fi

    info "Building Docker image '$IMAGE_NAME' (php:8.2-apache, hardened, SSL-capable)..."

    local build_dir
    build_dir="$(mktemp -d /tmp/www-php-apache.XXXXXX)"

    cat > "$build_dir/Dockerfile" <<'EOF'
FROM php:8.2-apache

# Basic PHP security hardening
RUN { \
    echo "expose_php = Off"; \
    echo "display_errors = Off"; \
    echo "log_errors = On"; \
    echo "session.use_strict_mode = 1"; \
    echo "session.cookie_httponly = 1"; \
    echo "session.cookie_secure = 1"; \
    echo "disable_functions = exec,passthru,shell_exec,system,proc_open,popen,curl_multi_exec,parse_ini_file,show_source"; \
} > /usr/local/etc/php/conf.d/security.ini

# Apache security hardening: hide version, disable signature
RUN { \
    echo "ServerTokens Prod"; \
    echo "ServerSignature Off"; \
} > /etc/apache2/conf-available/security-hardening.conf && \
    a2enconf security-hardening

# Enable modules: rewrite + ssl + headers
RUN apt-get update && apt-get install -y --no-install-recommends openssl && rm -rf /var/lib/apt/lists/* && \
    a2enmod rewrite ssl headers

# Ensure run as www-data
RUN sed -i 's/^User .*/User www-data/' /etc/apache2/apache2.conf || true && \
    sed -i 's/^Group .*/Group www-data/' /etc/apache2/apache2.conf || true

EXPOSE 80 443

CMD ["apache2-foreground"]
EOF

    docker build -t "$IMAGE_NAME:latest" "$build_dir"
    rm -rf "$build_dir"
    ok "Image '$IMAGE_NAME:latest' built successfully."
}

# -------- Install certbot if missing --------
install_certbot_if_needed() {
    if command -v certbot >/dev/null 2>&1; then
        ok "certbot is already installed."
        return
    fi

    warn "certbot is not installed. Attempting to install..."

    local pm
    pm="$(detect_pkg_manager)"
    [ -z "$pm" ] && die "Unsupported or undetected package manager. Please install certbot manually."

    if [ "$EUID" -ne 0 ]; then
        die "certbot installation requires root. Run this script with sudo for SSL mode."
    fi

    case "$pm" in
        apt)
            info "Using apt-get to install certbot..."
            apt-get update -y
            apt-get install -y certbot
            ;;
        dnf)
            info "Using dnf to install certbot..."
            dnf install -y certbot
            ;;
        yum)
            info "Using yum to install certbot..."
            yum install -y certbot
            ;;
        pacman)
            info "Using pacman to install certbot..."
            pacman -Sy --noconfirm certbot
            ;;
        zypper)
            info "Using zypper to install certbot..."
            zypper install -y certbot
            ;;
        apk)
            info "Using apk to install certbot..."
            apk add --no-cache certbot
            ;;
        *)
            die "Unsupported package manager '$pm'. Install certbot manually."
            ;;
    esac

    if ! command -v certbot >/dev/null 2>&1; then
        die "certbot installation appears to have failed."
    fi

    ok "certbot installed."
}

# -------- Obtain Let's Encrypt cert if needed --------
obtain_cert_if_needed() {
    local primary_domain="$1"
    local email="$2"
    shift 2
    local all_domains=("$@")

    local live_dir="/etc/letsencrypt/live/$primary_domain"
    local cert_file="$live_dir/fullchain.pem"
    local key_file="$live_dir/privkey.pem"

    if [ -f "$cert_file" ] && [ -f "$key_file" ]; then
        ok "Existing Let's Encrypt certificate found for $primary_domain. Reusing."
        return
    fi

    if [ "$EUID" -ne 0 ]; then
        die "Obtaining Let's Encrypt certificates requires root. Run with sudo."
    fi

    info "Requesting new Let's Encrypt certificate for: ${all_domains[*]}"

    local cmd=(certbot certonly --standalone --non-interactive --agree-tos --http-01-port 80)

    if [ -n "$email" ]; then
        cmd+=(-m "$email")
    else
        warn "No email provided for Let's Encrypt; using --register-unsafely-without-email."
        cmd+=(--register-unsafely-without-email)
    fi

    local d
    for d in "${all_domains[@]}"; do
        cmd+=(-d "$d")
    done

    echo -e "${C_BLUE}[INFO]${C_RESET} Running: ${C_GREEN}${cmd[*]}${CRESET}"
    "${cmd[@]}"

    if [ ! -f "$cert_file" ] || [ ! -f "$key_file" ]; then
        die "Let's Encrypt certificate not found after certbot run. Check certbot output."
    fi

    ok "Let's Encrypt certificate obtained for $primary_domain."
}

# -------- Generate Apache vhost config (HTTP only) --------
generate_vhost_conf_http() {
    local mode="$1"
    local outfile="$2"
    shift 2

    {
        echo "# Autogenerated by $SCRIPT_NAME (HTTP only)"
        echo "NameVirtualHost *:80"
        echo ""
        echo "<FilesMatch \"^\\.git|\\.env|composer\\.(json|lock)$\">"
        echo "    Require all denied"
        echo "</FilesMatch>"
        echo ""
    } > "$outfile"

    if [ "$mode" = "single" ]; then
        cat >> "$outfile" <<'EOF'
<VirtualHost *:80>
    DocumentRoot /var/www/html

    <Directory "/var/www/html">
        Options -Indexes -Includes -ExecCGI
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOF
    else
        while [ "$#" -gt 1 ]; do
            local domain="$1"
            local docroot="$2"
            shift 2
            cat >> "$outfile" <<EOF

<VirtualHost *:80>
    ServerName $domain
    DocumentRoot $docroot

    <Directory "$docroot">
        Options -Indexes -Includes -ExecCGI
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOF
        done
    fi
}

# -------- Generate Apache vhost config (HTTPS + redirect) --------
generate_vhost_conf_ssl() {
    local outfile="$1"
    local primary_domain="$2"
    shift 2

    local cert_base="/etc/letsencrypt/live/$primary_domain"
    local cert_file="$cert_base/fullchain.pem"
    local key_file="$cert_base/privkey.pem"

    {
        echo "# Autogenerated by $SCRIPT_NAME (HTTPS with Let's Encrypt)"
        echo ""
        echo "Listen 80"
        echo "Listen 443"
        echo ""
        echo "<FilesMatch \"^\\.git|\\.env|composer\\.(json|lock)$\">"
        echo "    Require all denied"
        echo "</FilesMatch>"
        echo ""
    } > "$outfile"

    local args=("$@")
    local domains=()
    local roots=()
    while [ "${#args[@]}" -gt 1 ]; do
        domains+=("${args[0]}")
        roots+=("${args[1]}")
        args=("${args[@]:2}")
    done

    local i
    for i in "${!domains[@]}"; do
        local d="${domains[$i]}"
        cat >> "$outfile" <<EOF

<VirtualHost *:80>
    ServerName $d
    Redirect permanent / https://$d/
</VirtualHost>
EOF
    done

    for i in "${!domains[@]}"; do
        local d="${domains[$i]}"
        local docroot="${roots[$i]}"

        cat >> "$outfile" <<EOF

<VirtualHost *:443>
    ServerName $d
    DocumentRoot $docroot

    SSLEngine on
    SSLCertificateFile "$cert_file"
    SSLCertificateKeyFile "$key_file"

    SSLProtocol all -SSLv2 -SSLv3
    SSLCipherSuite HIGH:!aNULL:!MD5
    SSLHonorCipherOrder on

    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains" env=HTTPS

    <Directory "$docroot">
        Options -Indexes -Includes -ExecCGI
        AllowOverride All
        Require all granted
    </Directory>
</VirtualHost>
EOF
    done
}

# -------- Main argument parsing --------
MODE=""
SINGLE_PATH=""
PORT="$DEFAULT_PORT"
DOMAINS=()
DOMAIN_PATHS=()

SSL_FLAG=0
NO_SSL_FLAG=0
SSL_ENABLED=0
SSL_MODE="none"
SSL_EMAIL=""

if [ "$#" -eq 0 ]; then
    show_help
    exit 0
fi

while [ "$#" -gt 0 ]; do
    case "$1" in
        -h|--help)
            show_help
            exit 0
            ;;
        -single)
            [ -n "$MODE" ] && die "You cannot mix -single with -domain in the same command."
            MODE="single"
            shift
            [ -z "$1" ] && die "Missing path after -single."
            SINGLE_PATH="$1"
            shift
            ;;
        -domain)
            [ "$MODE" = "single" ] && die "You cannot mix -single with -domain in the same command."
            MODE="multi"
            shift
            [ -z "$1" ] && die "Missing domain after -domain."
            DOMAINS+=("$1")
            shift
            [ -z "$1" ] && die "Missing path after domain '${DOMAINS[-1]}'."
            DOMAIN_PATHS+=("$1")
            shift
            ;;
        -port)
            shift
            [ -z "$1" ] && die "Missing value after -port."
            PORT="$1"
            shift
            ;;
        -ssl|--ssl)
            SSL_FLAG=1
            shift
            ;;
        -no-ssl|--no-ssl)
            NO_SSL_FLAG=1
            shift
            ;;
        --email|-email)
            shift
            [ -z "$1" ] && die "Missing value after --email."
            SSL_EMAIL="$1"
            shift
            ;;
        *)
            die "Unknown argument: $1  (use -h for help)"
            ;;
    esac
done

# Decide SSL mode
if [ "$SSL_FLAG" -eq 1 ] && [ "$NO_SSL_FLAG" -eq 1 ]; then
    die "You cannot use both -ssl/--ssl and -no-ssl/--no-ssl."
fi

if [ "$SSL_FLAG" -eq 1 ]; then
    SSL_MODE="ssl"
elif [ "$NO_SSL_FLAG" -eq 1 ]; then
    SSL_MODE="no_ssl"
else
    # No SSL switches: show help and exit
    show_help
    exit 0
fi

# Prompt for force when SSL is requested - EARLY
if [ "$SSL_MODE" = "ssl" ]; then
    echo -ne "${C_YELLOW}SSL mode requested. force? Y/n ${C_RESET}"
    read -r answer
    answer="${answer:-Y}"
    # lowercase
    answer_lc=$(printf '%s' "$answer" | tr '[:upper:]' '[:lower:]')
    case "$answer_lc" in
        y|yes)
            SSL_ENABLED=1
            ;;
        n|no)
            SSL_ENABLED=0
            SSL_MODE="no_ssl"
            ok "SSL force declined; proceeding in HTTP-only mode."
            ;;
        *)
            SSL_ENABLED=1
            ;;
    esac
fi

# -------- Validate modes and paths --------
if [ -z "$MODE" ]; then
    die "No mode specified. Use -single or -domain. (See -h for help.)"
fi

# SSL constraints
if [ "$SSL_ENABLED" -eq 1 ]; then
    [ "$MODE" = "single" ] && die "SSL mode requires -domain (real FQDN). -single + -ssl is not supported."
    if [ "${#DOMAINS[@]}" -eq 0 ]; then
        die "SSL mode requires at least one -domain <name> <path> pair."
    fi
    if [ "$PORT" != "80" ]; then
        warn "SSL mode forces host HTTP port to 80 (and HTTPS 443). Ignoring -port $PORT."
    fi
    PORT="80"
fi

# Validate paths
if [ "$MODE" = "single" ]; then
    [ ! -d "$SINGLE_PATH" ] && die "Path '$SINGLE_PATH' does not exist or is not a directory."
else
    if [ "${#DOMAINS[@]}" -eq 0 ]; then
        die "At least one -domain <name> <path> pair is required."
    fi
    for i in "${!DOMAINS[@]}"; do
        p="${DOMAIN_PATHS[$i]}"
        [ ! -d "$p" ] && die "Path '$p' for domain '${DOMAINS[$i]}' does not exist or is not a directory."
    done
fi

# -------- Ensure Docker & image --------
install_docker_if_needed
ensure_docker_running
build_image_if_needed

# -------- SSL: ensure certbot + cert if requested --------
PRIMARY_DOMAIN=""
if [ "$SSL_ENABLED" -eq 1 ]; then
    PRIMARY_DOMAIN="${DOMAINS[0]}"
    install_certbot_if_needed

    info "Stopping any existing container that might be listening on ports 80/443..."
    docker rm -f php-www-ssl >/dev/null 2>&1 || true
    docker rm -f "php-www-${PORT}" >/dev/null 2>&1 || true

    obtain_cert_if_needed "$PRIMARY_DOMAIN" "$SSL_EMAIL" "${DOMAINS[@]}"
fi

# -------- Generate config & run container --------
CONF_FILE="$(mktemp /tmp/www-php-vhost.XXXX.conf)"

if [ "$SSL_ENABLED" -eq 1 ]; then
    info "Generating Apache HTTPS config for multiple domains..."
    multi_args=()
    for i in "${!DOMAINS[@]}"; do
        d="${DOMAINS[$i]}"
        multi_args+=("$d" "/srv/sites/$d")
    done
    generate_vhost_conf_ssl "$CONF_FILE" "$PRIMARY_DOMAIN" "${multi_args[@]}"
else
    if [ "$MODE" = "single" ]; then
        info "Generating Apache HTTP config for single site..."
        generate_vhost_conf_http "single" "$CONF_FILE"
    else
        info "Generating Apache HTTP config for multiple domains..."
        multi_args=()
        for i in "${!DOMAINS[@]}"; do
            d="${DOMAINS[$i]}"
            multi_args+=("$d" "/srv/sites/$d")
        done
        generate_vhost_conf_http "multi" "$CONF_FILE" "${multi_args[@]}"
    fi
fi

CONTAINER_NAME=""
DOCKER_RUN_ARGS=(
    -d
    -v "$CONF_FILE:/etc/apache2/sites-enabled/000-default.conf:ro"
)

if [ "$SSL_ENABLED" -eq 1 ]; then
    CONTAINER_NAME="php-www-ssl"
    DOCKER_RUN_ARGS+=( -p "80:80" -p "443:443" )
    DOCKER_RUN_ARGS+=( -v "/etc/letsencrypt:/etc/letsencrypt:ro" )

    for i in "${!DOMAINS[@]}"; do
        d="${DOMAINS[$i]}"
        p="${DOMAIN_PATHS[$i]}"
        DOCKER_RUN_ARGS+=( -v "${p}:/srv/sites/${d}:ro" )
    done
else
    CONTAINER_NAME="php-www-${PORT}"
    DOCKER_RUN_ARGS+=( -p "${PORT}:80" )

    if [ "$MODE" = "single" ]; then
        DOCKER_RUN_ARGS+=( -v "${SINGLE_PATH}:/var/www/html:ro" )
    else
        for i in "${!DOMAINS[@]}"; do
            d="${DOMAINS[$i]}"
            p="${DOMAIN_PATHS[$i]}"
            DOCKER_RUN_ARGS+=( -v "${p}:/srv/sites/${d}:ro" )
        done
    fi
fi

info "Stopping/removing any existing container named '$CONTAINER_NAME'..."
docker rm -f "$CONTAINER_NAME" >/dev/null 2>&1 || true

info "Launching container '$CONTAINER_NAME'..."
docker run --name "$CONTAINER_NAME" "${DOCKER_RUN_ARGS[@]}" "$IMAGE_NAME:latest"

ok "Container '$CONTAINER_NAME' is running."

if [ "$SSL_ENABLED" -eq 1 ]; then
    echo -e "  Domains (HTTPS enabled via Let's Encrypt, cert for ${C_BOLD}$PRIMARY_DOMAIN${CRESET}):"
    for i in "${!DOMAINS[@]}"; do
        echo -e "    - ${C_BOLD}${DOMAINS[$i]}${CRESET}  =>  ${C_BOLD}${DOMAIN_PATHS[$i]}${CRESET}"
    done
    echo
    echo -e "  Test in browser (after DNS propagation):"
    for d in "${DOMAINS[@]}"; do
        echo -e "    ${C_GREEN}https://$d/${CRESET}"
    done
else
    if [ "$MODE" = "single" ]; then
        echo -e "  Single site mounted from: ${C_BOLD}$SINGLE_PATH${CRESET}"
        echo -e "  URL: ${C_GREEN}http://localhost:${PORT}/${CRESET}"
    else
        echo -e "  Domains (HTTP only):"
        for i in "${!DOMAINS[@]}"; do
            echo -e "    - ${C_BOLD}${DOMAINS[$i]}${CRESET}  =>  ${C_BOLD}${DOMAIN_PATHS[$i]}${CRESET}"
        done
        echo -e "  Test locally via /etc/hosts pointing domains to this server, then:"
        for d in "${DOMAINS[@]}"; do
            echo -e "    ${C_GREEN}http://$d:${PORT}/${CRESET}"
        done
    fi
fi

echo
echo -e "${C_BOLD}Docker quick commands:${CRESET}"
echo -e "  ${C_GREEN}docker logs -f $CONTAINER_NAME${CRESET}   # follow logs"
echo -e "  ${C_GREEN}docker stop $CONTAINER_NAME${CRESET}      # stop container"
echo -e "  ${C_GREEN}docker rm $CONTAINER_NAME${CRESET}        # remove container"
