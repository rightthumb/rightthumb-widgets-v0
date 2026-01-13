#!/usr/bin/env bash
# FreePBX 17 Universal Installer (Debian/Ubuntu/RHEL/Alma/Rocky/Arch) + optional Let's Encrypt
# - Debian 12 (bookworm): official Sangoma repo (preferred)
# - Ubuntu 22.04/24.04, RHEL/Rocky/Alma 8/9, Arch: source-based install (opt. Asterisk build)
# - Robust PHP detection (Ubuntu 24.04 prefers native first)
# - Correct Asterisk paths, fwconsole wiring, Apache vhosts, SSL (certbot)
# - Fixes /var/log/asterisk/freepbx.log perms + logrotate (prevents Whoops)
# - No-arg help; strict error handling; detailed logging

set -euo pipefail

AST_VERSION="${AST_VERSION:-21}"
LOG_DIR="/var/log/pbx"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/freepbx-universal-$(date '+%Y.%m.%d-%H.%M.%S').log"
exec > >(tee -a "$LOG_FILE") 2>&1

# ------------------- HELP -------------------
ORIGINAL_ARGC=$#
print_help() {
cat <<'EOF'
FreePBX 17 Universal Installer (Debian/Ubuntu/RHEL/Alma/Rocky/Arch)

USAGE:
  sudo bash freepbx-universal.sh [FLAGS]

FLAGS:
  --build-asterisk        Compile Asterisk from source (uses AST_VERSION env, default 21)
  --no-ioncube            Skip ionCube loader (only needed for commercial modules)
  --fqdn DOMAIN           Public FQDN for HTTPS (Let's Encrypt)
  --le-email EMAIL        Email for Let's Encrypt registration
  --agree-tos             Non-interactive Let's Encrypt (agree to ToS)
  --non-interactive       Non-interactive mode (accept sane defaults)
  --skip-ssl              Do not attempt SSL issuance/configuration
  -h, --help              Show this help

EXAMPLES:
  Debian 12 + SSL:
    sudo bash freepbx-universal.sh --fqdn pbx.example.com --le-email you@example.com --agree-tos
  Ubuntu 24.04 + build Asterisk + SSL:
    sudo bash freepbx-universal.sh --build-asterisk --fqdn pbx.example.com --le-email you@example.com --agree-tos
  No SSL now:
    sudo bash freepbx-universal.sh --skip-ssl

NOTES:
  - Run on a fresh VM as root.
  - Ensure DNS for --fqdn points to this server before attempting Let's Encrypt.
  - Full logs: /var/log/pbx/.
EOF
}
if [[ $ORIGINAL_ARGC -eq 0 ]]; then print_help; exit 0; fi

# ------------------- ARGS -------------------
BUILD_ASTERISK=false
SKIP_IONCUBE=false
FQDN=""
LE_EMAIL=""
LE_AGREE_TOS=false
NONINTERACTIVE=false
SKIP_SSL=false

while [[ $# -gt 0 ]]; do
  case "$1" in
    --build-asterisk) BUILD_ASTERISK=true; shift ;;
    --no-ioncube)     SKIP_IONCUBE=true; shift ;;
    --fqdn)           FQDN="${2:-}"; shift 2 ;;
    --le-email)       LE_EMAIL="${2:-}"; shift 2 ;;
    --agree-tos)      LE_AGREE_TOS=true; shift ;;
    --non-interactive) NONINTERACTIVE=true; shift ;;
    --skip-ssl)       SKIP_SSL=true; shift ;;
    -h|--help)        print_help; exit 0 ;;
    *) echo "Unknown option: $1"; echo; print_help; exit 1 ;;
  esac
done

# ------------------- PRECHECKS -------------------
trap 'echo "ERROR at line $LINENO. See $LOG_FILE"; exit 1' ERR
[[ $EUID -eq 0 ]] || { echo "Run as root."; exit 1; }
command -v systemctl >/dev/null || { echo "systemd required."; exit 1; }

if [[ -r /etc/os-release ]]; then
  . /etc/os-release
  OS_ID="${ID:-unknown}"
  OS_LIKE="${ID_LIKE:-}"
  OS_VERSION_ID="${VERSION_ID:-}"
  OS_CODENAME="${VERSION_CODENAME:-}"
else
  echo "Cannot detect OS via /etc/os-release"; exit 1
fi
echo "Detected OS: ID=$OS_ID LIKE=$OS_LIKE VERSION_ID=$OS_VERSION_ID CODENAME=$OS_CODENAME"

die(){ echo "ERROR: $*" >&2; exit 1; }
is_debian_bookworm(){ [[ "$OS_ID" == "debian" && "$OS_CODENAME" == "bookworm" ]]; }
is_ubuntu(){ [[ "$OS_ID" == "ubuntu" ]]; }
is_rhel_like(){ [[ "$OS_ID" =~ (rhel|rocky|almalinux|centos|ol) || "$OS_LIKE" =~ (rhel|fedora) ]]; }
is_arch(){ [[ "$OS_ID" == "arch" || "$OS_ID" == "endeavouros" ]]; }

# ------------------- USERS & PATHS -------------------
ensure_asterisk_user(){
  getent group asterisk >/dev/null || groupadd -r asterisk
  getent passwd asterisk >/dev/null 2>&1 || useradd -r -g asterisk -d /var/lib/asterisk -s /sbin/nologin asterisk
}
apache_user() {
  if id -u www-data >/dev/null 2>&1; then echo www-data
  elif id -u apache   >/dev/null 2>&1; then echo apache
  else echo ""; fi
}
set_ast_paths_vars(){
  AST_ETC="/etc/asterisk"
  AST_MOD_DIR="/usr/lib/asterisk/modules"
  AST_VAR="/var/lib/asterisk"
  AST_AGI="/usr/share/asterisk/agi-bin"
  AST_SPOOL="/var/spool/asterisk"
  AST_RUN="/var/run/asterisk"
  AST_LOG="/var/log/asterisk"
  [[ -d /usr/lib/x86_64-linux-gnu/asterisk/modules ]] && AST_MOD_DIR="/usr/lib/x86_64-linux-gnu/asterisk/modules"
  mkdir -p "$AST_ETC" "$AST_MOD_DIR" "$AST_VAR" "$AST_AGI" "$AST_SPOOL" "$AST_RUN" "$AST_LOG" /var/lib/asterisk/bin
  chown -R asterisk:asterisk "$AST_ETC" "$AST_VAR" "$AST_AGI" "$AST_SPOOL" "$AST_RUN" "$AST_LOG" || true
}

# Fix /var/log/asterisk/freepbx.log perms + logrotate (prevents GUI Whoops)
fix_freepbx_log_perms() {
  local ap_user; ap_user="$(apache_user)"
  ensure_asterisk_user
  [[ -n "$ap_user" ]] && usermod -aG asterisk "$ap_user" || true
  mkdir -p /var/log/asterisk
  touch /var/log/asterisk/freepbx.log
  chown -R asterisk:asterisk /var/log/asterisk
  chmod 2775 /var/log/asterisk
  chmod 0664 /var/log/asterisk/freepbx.log
}
ensure_logrotate_asterisk() {
  cat >/etc/logrotate.d/freepbx <<'EOF'
/var/log/asterisk/freepbx.log {
    daily
    rotate 14
    missingok
    notifempty
    compress
    delaycompress
    sharedscripts
    create 0664 asterisk asterisk
    postrotate
        /usr/sbin/fwconsole --help >/dev/null 2>&1 && /usr/sbin/fwconsole chown >/dev/null 2>&1 || true
    endscript
}
EOF
}

# ------------------- PHP DETECTION (Deb/Ub) -------------------
has_pkg() { local pkg="$1"; local cand; cand="$(apt-cache policy "$pkg" 2>/dev/null | awk '/Candidate:/{print $2}')"; [[ -n "$cand" && "$cand" != "(none)" ]]; }
PHP_SERIES=""
detect_php_deb() {
  export DEBIAN_FRONTEND=noninteractive
  apt-get update -y
  apt-get install -y lsb-release ca-certificates apt-transport-https software-properties-common gnupg curl wget
  if [[ "${OS_ID}" == "ubuntu" ]]; then
    add-apt-repository -y ppa:ondrej/php || true
  elif [[ "${OS_ID}" == "debian" ]]; then
    wget -qO /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
    add-apt-repository -y -S "deb [arch=$(dpkg --print-architecture)] https://packages.sury.org/php/ $(lsb_release -sc) main"
  fi
  apt-get update -y
  for v in 8.4 8.3 8.2 8.1 8.0; do
    if has_pkg "php${v}-cli"; then PHP_SERIES="$v"; break; fi
  done
  if [[ -z "$PHP_SERIES" ]] && has_pkg php-cli; then PHP_SERIES="native"; fi
  [[ -n "$PHP_SERIES" ]] || die "No PHP series available. Check repos/network."
  echo "Using PHP series: ${PHP_SERIES}"
}
php_pkg_deb(){ local base="$1"; [[ "$PHP_SERIES" == "native" ]] && echo "php-$base" || echo "php${PHP_SERIES}-$base"; }
php_meta_deb(){ [[ "$PHP_SERIES" == "native" ]] && echo "php php-cli" || echo "php${PHP_SERIES} php${PHP_SERIES}-cli"; }
php_apache_mod_pkg(){ [[ "$PHP_SERIES" == "native" ]] && echo "libapache2-mod-php" || echo "libapache2-mod-php${PHP_SERIES}"; }
switch_apache_php_deb(){
  local v="$PHP_SERIES"
  if [[ "$v" == "native" ]]; then a2dismod php* 2>/dev/null || true; a2enmod php || true; return; fi
  a2dismod php* 2>/dev/null || true
  a2enmod "php${v}" || true
  update-alternatives --set php "/usr/bin/php${v}" || true
}

# ------------------- PHP DETECTION (RHEL/Arch) -------------------
PHP_SERIES_RHEL=""
detect_php_rhel() {
  (dnf -y install epel-release || yum -y install epel-release || true)
  dnf -y install "https://rpms.remirepo.net/enterprise/remi-release-${OS_VERSION_ID%%.*}.rpm" || true
  for v in 84 83 82 81 80; do
    dnf -y module reset php || true
    if dnf -y module enable php:$v; then PHP_SERIES_RHEL="8.${v:1}"; break; fi
  done
  [[ -n "$PHP_SERIES_RHEL" ]] || PHP_SERIES_RHEL="native"
}
php_pkg_rhel(){ echo "php-$1"; }
php_meta_rhel(){ echo "php php-cli"; }

# ------------------- CERTBOT -------------------
obtain_le_apache(){
  $SKIP_SSL && { echo "Skipping SSL (--skip-ssl)."; return 0; }
  [[ -n "$FQDN" ]] || { echo "No --fqdn provided; skipping Let's Encrypt."; return 0; }

  local agree=""; $LE_AGREE_TOS && agree="--agree-tos"
  local email_arg=""; [[ -n "$LE_EMAIL" ]] && email_arg="--email $LE_EMAIL" || email_arg="--register-unsafely-without-email"

  if is_debian_bookworm || is_ubuntu; then
    apt-get install -y certbot python3-certbot-apache
    systemctl enable --now apache2
    if certbot plugins 2>/dev/null | grep -qi apache; then
      if $NONINTERACTIVE; then certbot --apache -d "$FQDN" $email_arg $agree --non-interactive --redirect || true
      else certbot --apache -d "$FQDN" $email_arg $agree --redirect || true; fi
    else
      mkdir -p /var/www/html
      if $NONINTERACTIVE; then certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree --non-interactive || true
      else certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree || true; fi
    fi

  elif is_rhel_like; then
    (dnf -y install certbot python3-certbot-apache || yum -y install certbot python3-certbot-apache || true)
    systemctl enable --now httpd
    if certbot plugins 2>/dev/null | grep -qi apache; then
      if $NONINTERACTIVE; then certbot --apache -d "$FQDN" $email_arg $agree --non-interactive --redirect || true
      else certbot --apache -d "$FQDN" $email_arg $agree --redirect || true; fi
    else
      mkdir -p /var/www/html
      if $NONINTERACTIVE; then certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree --non-interactive || true
      else certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree || true; fi
    fi

  elif is_arch; then
    pacman -Sy --noconfirm certbot
    systemctl enable --now httpd || true
    mkdir -p /var/www/html
    if $NONINTERACTIVE; then certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree --non-interactive || true
    else certbot certonly --webroot -w /var/www/html -d "$FQDN" $email_arg $agree || true; fi
    echo "If needed, set SSLCertificateFile/KeyFile in /etc/httpd/conf.d/ssl.conf → /etc/letsencrypt/live/$FQDN/"
  fi
}

# ------------------- COMMON TUNING -------------------
tune_php_ini_paths(){ [[ -d /etc/php ]] && find /etc/php -name php.ini 2>/dev/null || find /etc -maxdepth 3 -name php.ini 2>/dev/null; }
tune_php_ini(){
  for ini in $(tune_php_ini_paths); do
    [[ -f "$ini" ]] || continue
    sed -i 's/^\s*expose_php\s*=.*/expose_php = Off/' "$ini" || true
    sed -i 's/^\s*upload_max_filesize\s*=.*/upload_max_filesize = 128M/' "$ini" || true
    sed -i 's/^\s*post_max_size\s*=.*/post_max_size = 128M/' "$ini" || true
    sed -i 's/^\s*memory_limit\s*=.*/memory_limit = 512M/' "$ini" || true
    sed -i 's/^\s*max_execution_time\s*=.*/max_execution_time = 300/' "$ini" || true
  done
}
apache_root(){ echo "/var/www/html"; }
enable_apache_mods_deb(){ a2enmod rewrite ssl expires headers proxy proxy_http >/dev/null 2>&1 || true; }
write_vhost_deb(){
  local docroot="$1"; mkdir -p "$docroot"
  cat >/etc/apache2/sites-available/freepbx.conf <<EOF
<VirtualHost *:80>
    ServerName ${FQDN:-_default_}
    DocumentRoot ${docroot}
    <Directory "${docroot}">
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog \${APACHE_LOG_DIR}/freepbx_error.log
    CustomLog \${APACHE_LOG_DIR}/freepbx_access.log combined
</VirtualHost>
EOF
  ln -sf ../sites-available/freepbx.conf /etc/apache2/sites-enabled/freepbx.conf
}
write_vhost_rhel(){
  local docroot="$1"; mkdir -p "$docroot"
  cat >/etc/httpd/conf.d/freepbx.conf <<EOF
<VirtualHost *:80>
    ServerName ${FQDN:-_default_}
    DocumentRoot ${docroot}
    <Directory "${docroot}">
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog /var/log/httpd/freepbx_error.log
    CustomLog /var/log/httpd/freepbx_access.log combined
</VirtualHost>
EOF
}

# ------------------- DEBIAN 12 REPO PATH -------------------
install_debian_repo(){
  echo "== Debian 12 repo-based install =="
  export DEBIAN_FRONTEND=noninteractive

  # Pin to bookworm (avoid 'stable' drift)
  sed -i 's@deb \+http[^ ]\+ \+stable@deb http://deb.debian.org/debian bookworm@g' /etc/apt/sources.list || true
  apt-get update -y
  apt-get install -y lsb-release ca-certificates apt-transport-https software-properties-common gnupg curl wget

  # PHP
  detect_php_deb

  # FreePBX repo (Sangoma)
  wget -qO - http://deb.freepbx.org/gpg/aptly-pubkey.asc | gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/freepbx.gpg
  add-apt-repository -y -S "deb [arch=$(dpkg --print-architecture)] http://deb.freepbx.org/freepbx17-prod bookworm main"
  apt-get update -y

  # Core OS bits
  apt-get install -y apache2 mariadb-server mariadb-client redis-server curl wget zip unzip git nodejs npm fail2ban sngrep
  # PHP set (+ proper Apache PHP module)
  PHP_SET="$(php_meta_deb) $(php_pkg_deb mysql) $(php_pkg_deb gd) $(php_pkg_deb mbstring) $(php_pkg_deb xml) $(php_pkg_deb curl) $(php_pkg_deb zip) $(php_pkg_deb intl) $(php_pkg_deb ldap) php-soap php-bz2 php-pear $(php_apache_mod_pkg)"
  apt-get install -y $PHP_SET
  enable_apache_mods_deb
  switch_apache_php_deb
  tune_php_ini

  # Asterisk from repo (best effort)
  apt-get install -y "asterisk${AST_VERSION}" "asterisk${AST_VERSION}-core" "asterisk${AST_VERSION}-addons" "asterisk${AST_VERSION}-voicemail" \
                     "asterisk${AST_VERSION}-odbc" "asterisk${AST_VERSION}-ogg" "asterisk${AST_VERSION}-curl" "asterisk${AST_VERSION}-snmp" || true
  apt-get install -y "asterisk${AST_VERSION}.0-freepbx-asterisk-modules" asterisk-version-switch || true

  # ionCube optional
  $SKIP_IONCUBE || apt-get install -y ioncube-loader-82 || true

  # FreePBX meta packages
  apt-get install -y freepbx17 sangoma-pbx17 ffmpeg

  # Harden Apache
  sed -i 's/^\s*ServerTokens .*/ServerTokens Prod/' /etc/apache2/conf-available/security.conf || true
  sed -i 's/^\s*ServerSignature .*/ServerSignature Off/' /etc/apache2/conf-available/security.conf || true

  systemctl enable --now mariadb
  systemctl enable --now asterisk || true
  systemctl enable --now apache2

  # Ensure logging perms
  fix_freepbx_log_perms
  ensure_logrotate_asterisk

  # First-run touches (if fwconsole already present)
  if command -v fwconsole >/dev/null 2>&1; then
    fwconsole chown || true
    fwconsole ma upgradeall || true
    fwconsole reload || true
    fwconsole restart || true
  fi

  obtain_le_apache

  echo
  echo "== Done (Debian 12) =="
  IP="$(hostname -I | awk '{print $1}')"
  echo "GUI (HTTP):  http://${FQDN:-$IP}/admin"
  [[ -n "$FQDN" ]] && echo "GUI (HTTPS): https://${FQDN}/admin"
}

# ------------------- SOURCE PATH (Ubuntu/RHEL/Arch) -------------------
install_source(){
  echo "== Source install path =="

  if is_ubuntu; then
    detect_php_deb
    apt-get install -y build-essential git wget curl unzip uuid-runtime subversion \
      apache2 mariadb-server mariadb-client \
      $(php_meta_deb) $(php_pkg_deb mysql) $(php_pkg_deb gd) $(php_pkg_deb mbstring) $(php_pkg_deb xml) $(php_pkg_deb curl) $(php_pkg_deb zip) $(php_pkg_deb intl) $(php_pkg_deb ldap) php-soap php-bz2 php-pear $(php_apache_mod_pkg) \
      libxml2-dev libncurses5-dev libsqlite3-dev libssl-dev libcurl4-openssl-dev libjansson-dev libedit-dev pkg-config \
      nodejs npm fail2ban sngrep
    enable_apache_mods_deb
    switch_apache_php_deb
    tune_php_ini
    systemctl enable --now mariadb apache2

  elif is_rhel_like; then
    detect_php_rhel
    (dnf -y groupinstall "Development Tools" || yum -y groupinstall "Development Tools")
    (dnf -y install git wget curl unzip uuid httpd mariadb-server mariadb \
      $(php_meta_rhel) $(php_pkg_rhel mysqlnd) $(php_pkg_rhel gd) $(php_pkg_rhel mbstring) $(php_pkg_rhel xml) $(php_pkg_rhel curl) $(php_pkg_rhel zip) $(php_pkg_rhel intl) $(php_pkg_rhel ldap) $(php_pkg_rhel soap) \
      libxml2-devel ncurses-devel sqlite-devel openssl-devel libcurl-devel jansson-devel libedit-devel \
      nodejs npm fail2ban sngrep || true)
    systemctl enable --now mariadb httpd

  elif is_arch; then
    pacman -Sy --noconfirm base-devel git wget curl unzip apache mariadb \
      php php-apache php-gd php-intl php-ldap php-soap php-curl php-zip php-sqlite php-pgsql php-xml php-mbstring \
      jansson libedit ncurses sqlite openssl nodejs npm fail2ban sngrep || true
    systemctl enable --now mariadb httpd
    # Ensure PHP is loaded in Apache (Arch)
    if ! grep -q "LoadModule php_module" /etc/httpd/conf/httpd.conf; then
      echo "LoadModule php_module modules/libphp.so" >> /etc/httpd/conf/httpd.conf || true
      echo "AddHandler php-script .php" >> /etc/httpd/conf/httpd.conf || true
      echo "Include conf/extra/php_module.conf" >> /etc/httpd/conf/httpd.conf || true
    fi
  else
    die "Unsupported distro in source path."
  fi

  # Users/paths/logs
  ensure_asterisk_user
  set_ast_paths_vars
  fix_freepbx_log_perms
  ensure_logrotate_asterisk

  # ----- Asterisk -----
  if $BUILD_ASTERISK; then
    echo "Building Asterisk ${AST_VERSION}..."
    cd /usr/src
    AST_TGZ="asterisk-${AST_VERSION}-current.tar.gz"
    wget -q https://downloads.asterisk.org/pub/telephony/asterisk/${AST_TGZ}
    tar xzf ${AST_TGZ}
    cd asterisk-${AST_VERSION}.*/
    contrib/scripts/get_mp3_source.sh || true
    ./configure --with-jansson-bundled=no
    make menuselect.makeopts
    menuselect/menuselect --enable format_mp3 menuselect.makeopts || true
    make -j"$(nproc)"
    make install
    make samples
    make config
    ldconfig
    systemctl enable --now asterisk || true
  else
    echo "Skipping Asterisk build (assumes provided by distro or already installed)."
    systemctl enable --now asterisk 2>/dev/null || true
  fi

  # ----- FreePBX (source) -----
  echo "Installing FreePBX 17 (source)..."
  cd /usr/src
  if [[ ! -d freepbx ]]; then
    git clone https://github.com/FreePBX/framework.git freepbx
  fi
  cd freepbx
  git fetch --all
  git checkout release/17.0 2>/dev/null || git checkout master

  # Databases
  mysql -e "CREATE DATABASE IF NOT EXISTS asterisk DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
  mysql -e "CREATE DATABASE IF NOT EXISTS asteriskcdrdb DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
  mysql -e "CREATE USER IF NOT EXISTS 'asterisk'@'localhost' IDENTIFIED BY 'asterisk';"
  mysql -e "GRANT ALL PRIVILEGES ON asterisk.* TO 'asterisk'@'localhost';"
  mysql -e "GRANT ALL PRIVILEGES ON asteriskcdrdb.* TO 'asterisk'@'localhost';"
  mysql -e "FLUSH PRIVILEGES;"

  DOCROOT="$(apache_root)"
  mkdir -p "$DOCROOT"

  ./start_asterisk start || true

  # PASS **ALL** AST paths to avoid ASTLOGDIR errors
  ./install -n \
    --dbuser asterisk --dbpass asterisk \
    --dbname asterisk --cdrdbname asteriskcdrdb \
    --webroot "$DOCROOT" \
    --astetcdir "$AST_ETC" \
    --astmoddir "$AST_MOD_DIR" \
    --astvarlibdir "$AST_VAR" \
    --astagidir "$AST_AGI" \
    --astspooldir "$AST_SPOOL" \
    --astrundir "$AST_RUN" \
    --astlogdir "$AST_LOG" \
    --ampbin /var/lib/asterisk/bin \
    --ampsbin /usr/sbin \
    --ampcgibin /var/www/cgi-bin || true

  # Symlink fwconsole for convenience
  if [[ -x /var/lib/asterisk/bin/fwconsole ]]; then
    ln -sf /var/lib/asterisk/bin/fwconsole /usr/sbin/fwconsole
  fi

  # Web vhost
  if is_ubuntu; then
    write_vhost_deb "$DOCROOT"; systemctl restart apache2
  elif is_rhel_like || is_arch; then
    write_vhost_rhel "$DOCROOT"; systemctl restart httpd
  fi

  # Ownerships
  chown -R asterisk:asterisk "$AST_ETC" "$AST_VAR" "$AST_AGI" "$AST_SPOOL" "$AST_RUN" "$AST_LOG" || true
  chown -R www-data:www-data "$DOCROOT" 2>/dev/null || chown -R apache:apache "$DOCROOT" 2>/dev/null || true
  usermod -aG asterisk www-data 2>/dev/null || usermod -aG asterisk apache 2>/dev/null || true

  # Initialize FreePBX
  if command -v fwconsole >/dev/null 2>&1; then
    fwconsole chown || true
    fwconsole ma upgradeall || true
    fwconsole reload || true
    fwconsole restart || true
  fi

  obtain_le_apache

  echo
  echo "== Done (Source path) =="
  IP="$(hostname -I | awk '{print $1}')"
  echo "GUI (HTTP):  http://${FQDN:-$IP}/admin"
  [[ -n "$FQDN" ]] && echo "GUI (HTTPS): https://${FQDN}/admin"
}

# ------------------- DISPATCH -------------------
if is_debian_bookworm; then
  install_debian_repo
else
  install_source
fi

echo
echo "Log: $LOG_FILE"
echo "If Certbot failed (DNS not ready), retry later, e.g.:"
echo "  certbot --apache -d ${FQDN:-your.domain}   # or certonly --webroot"
