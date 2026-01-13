#!/bin/bash

set -e

CONFIG=""
MODE=""

function show_help() {
	echo ""
	echo "Usage:"
	echo "  $0 --help                     Show this help menu"
	echo "  $0 --generate-config          Generate a sample YAML config"
	echo "  $0 --install --config FILE    Install PostgreSQL securely using config file"
	echo "  $0 --firewall --config FILE   Print firewall commands only (safe copy/paste)"
	echo ""
}

function generate_config() {
	cat <<EOF > pg-config.sample.yml
postgres:
  username: myuser
  password: strongpassword
  database: mydb
  allow_remote: true
  allowed_ips:
    - 123.45.67.89
    - 10.0.0.5
ssl:
  enable: true
  self_signed: true
  cert_days: 365
firewall:
  enable: true

EOF
	echo "Sample config written to pg-config.sample.yml"
}

function detect_distro() {
	if [ -f /etc/os-release ]; then
		. /etc/os-release
		DISTRO=$ID
	else
		DISTRO=$(uname -s)
	fi
}

function install_yq() {
	if ! command -v yq >/dev/null 2>&1; then
		echo "[+] Installing yq..."
		detect_distro
		if command -v apt >/dev/null; then
			sudo apt update
			sudo apt install -y yq
		elif command -v dnf >/dev/null; then
			sudo dnf install -y epel-release
			sudo dnf install -y yq
		elif command -v yum >/dev/null; then
			sudo yum install -y epel-release
			sudo yum install -y yq
		elif command -v pacman >/dev/null; then
			sudo pacman -Sy --noconfirm yq
		else
			echo "Installing yq via GitHub binary..."
			curl -L https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -o /usr/local/bin/yq
			chmod +x /usr/local/bin/yq
		fi
	fi
}

function parse_config() {
	USERNAME=$(yq e '.postgres.username' "$CONFIG")
	PASSWORD=$(yq e '.postgres.password' "$CONFIG")
	DBNAME=$(yq e '.postgres.database' "$CONFIG")
	IPS=$(yq e '.postgres.allowed_ips[]' "$CONFIG")
	ENABLE_SSL=$(yq e '.ssl.enable' "$CONFIG")
	SELF_SIGNED=$(yq e '.ssl.self_signed' "$CONFIG")
	CERT_DAYS=$(yq e '.ssl.cert_days' "$CONFIG")
	FIREWALL=$(yq e '.firewall.enable' "$CONFIG")
}

function install_postgres() {
	echo "[+] Installing PostgreSQL..."
	detect_distro
	if command -v apt >/dev/null; then
		sudo apt update
		sudo apt install -y postgresql postgresql-contrib
	elif command -v dnf >/dev/null; then
		sudo dnf install -y postgresql-server postgresql-contrib
		sudo postgresql-setup --initdb
	elif command -v yum >/dev/null; then
		sudo yum install -y postgresql-server postgresql-contrib
		sudo postgresql-setup initdb
	elif command -v pacman >/dev/null; then
		sudo pacman -Sy --noconfirm postgresql
		sudo -iu postgres initdb --locale $LANG -D /var/lib/postgres/data
	else
		echo "Unsupported distro"
		exit 1
	fi
	sudo systemctl enable postgresql
	sudo systemctl start postgresql
}

function create_user_db() {
	echo "[+] Creating user and database..."
	sudo -u postgres psql <<EOF
DO
\$do\$
BEGIN
   IF NOT EXISTS (
	SELECT FROM pg_catalog.pg_roles WHERE rolname = '${USERNAME}'
   ) THEN
	CREATE ROLE ${USERNAME} LOGIN PASSWORD '${PASSWORD}';
   END IF;
END
\$do\$;

CREATE DATABASE ${DBNAME} OWNER ${USERNAME};
GRANT ALL PRIVILEGES ON DATABASE ${DBNAME} TO ${USERNAME};
EOF
}

function configure_postgres() {
	echo "[+] Configuring PostgreSQL..."
	CONF_FILE=$(find /etc -name postgresql.conf | head -n 1)
	HBA_FILE=$(find /etc -name pg_hba.conf | head -n 1)
	sudo sed -i "s/#*listen_addresses =.*/listen_addresses = '*'/'" "$CONF_FILE"
	for ip in $IPS; do
		echo "host    $DBNAME    $USERNAME    $ip/32    md5" | sudo tee -a "$HBA_FILE" >/dev/null
	done
	if [ "$ENABLE_SSL" = "true" ]; then
		sudo sed -i "s/#*ssl = .*/ssl = on/" "$CONF_FILE"
		sudo sed -i "s|#*ssl_cert_file = .*|ssl_cert_file = '/etc/ssl/private/server.crt'|" "$CONF_FILE"
		sudo sed -i "s|#*ssl_key_file = .*|ssl_key_file = '/etc/ssl/private/server.key'|" "$CONF_FILE"
	fi
	sudo systemctl restart postgresql
}

function generate_ssl() {
	if [ "$ENABLE_SSL" = "true" ] && [ "$SELF_SIGNED" = "true" ]; then
		echo "[+] Generating self-signed SSL cert..."
		sudo openssl req -new -x509 -days "$CERT_DAYS" -nodes \
			-out /etc/ssl/private/server.crt -keyout /etc/ssl/private/server.key \
			-subj "/C=US/ST=State/L=City/O=Org/OU=Dev/CN=$(hostname)"
		sudo chown postgres:postgres /etc/ssl/private/server.*
		sudo chmod 600 /etc/ssl/private/server.key
	fi
}

function firewall_commands() {
	echo ""
	echo "[*] Recommended firewall commands to allow PostgreSQL access:"
	if command -v ufw >/dev/null; then
		for ip in $IPS; do
			echo "sudo ufw allow from $ip to any port 5432 proto tcp"
		done
	elif command -v firewall-cmd >/dev/null; then
		for ip in $IPS; do
			echo "sudo firewall-cmd --permanent --add-rich-rule='rule family=\"ipv4\" source address=\"$ip\" port protocol=\"tcp\" port=\"5432\" accept'"
		done
		echo "sudo firewall-cmd --reload"
	else
		echo "⚠️ No known firewall system detected. Install ufw or firewalld."
	fi
}

# Argument parsing
while [[ "$#" -gt 0 ]]; do
	case "$1" in
		--help) show_help; exit 0 ;;
		--generate-config) generate_config; exit 0 ;;
		--install) MODE="install"; shift ;;
		--firewall) MODE="firewall"; shift ;;
		--config) CONFIG="$2"; shift 2 ;;
		*) echo "Unknown argument: $1"; show_help; exit 1 ;;
	esac
done

if [[ -z "$MODE" ]]; then
	show_help
	exit 1
fi

install_yq

if [[ ! -f "$CONFIG" ]]; then
	echo "❌ Config file not found: $CONFIG"
	exit 1
fi

parse_config

if [[ "$MODE" == "install" ]]; then
	install_postgres
	create_user_db
	configure_postgres
	generate_ssl
	echo "[✔] PostgreSQL installation and config complete."
	firewall_commands
elif [[ "$MODE" == "firewall" ]]; then
	firewall_commands
fi
