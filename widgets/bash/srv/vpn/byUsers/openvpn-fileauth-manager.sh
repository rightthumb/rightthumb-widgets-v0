#!/usr/bin/env bash
set -euo pipefail

# ======================================================================
# OpenVPN File-Auth Manager
#  - Auto-installs OpenVPN + Easy-RSA + htpasswd tools
#  - Creates server (if missing), enables CERTS + file-based passwords
#  - Manages auth users in /etc/openvpn/auth/users.htpasswd (bcrypt)
#  - Creates client certs and generates embedded .ovpn files
#
# Commands:
#   install                           Install deps, create/patch server, enable NAT+FORWARD (nft/iptables)
#   add-user   USER [--password P]    Add/update auth user in users.htpasswd
#   del-user   USER                   Remove auth user
#   client-ovpn USER [--out PATH]     Create certs if missing + generate embedded .ovpn
#   list                              Show users and clients present
#   status                            Show service + key paths
#   help                              This help
#
# Notes:
#   - Clients MUST have 'auth-user-pass' in profile (this script sets it).
#   - Certs remain REQUIRED (2FA-ish: cert + password).
#   - Full-tunnel by default (redirect-gateway). Change in server.conf if you want split-tunnel.
# ======================================================================

# ---------------------- Globals ----------------------
PM=""; INSTALL=""; UPDATE="true"
EASYRSA_PKG="easy-rsa"
HTPASSWD_BIN=""

SERVER_DIR="/etc/openvpn/server"
LEGACY_DIR="/etc/openvpn"
EASYRSA_DIR="/etc/openvpn/easy-rsa"
AUTH_DIR="/etc/openvpn/auth"
USERS_FILE="${AUTH_DIR}/users.htpasswd"
VERIFY_SCRIPT="${AUTH_DIR}/file-auth.sh"

SERVER_CONF=""
SERVICE_NAME=""
INSTANCE_NAME="server"
VPN_SUBNET="10.8.0.0"
VPN_MASK="255.255.255.0"
VPN_CIDR="${VPN_SUBNET}/24"
DEFAULT_PROTO="udp"
DEFAULT_PORT="1194"
TUN_DEV="tun0"   # default device name OpenVPN will use for 'dev tun'

# ---------------------- Helpers ----------------------
msg() { echo -e "$*"; }
die() { echo "ERROR: $*" >&2; exit 1; }
ensure_root() { [[ $EUID -eq 0 ]] || die "Run as root (sudo)."; }

resolve_htpasswd() {
	HTPASSWD_BIN="$(command -v htpasswd || true)"
	[[ -n "$HTPASSWD_BIN" ]] || die "htpasswd not found. Install apache2-utils (Debian/Ubuntu) or httpd-tools (RHEL/Fedora)."
}

detect_pkg_mgr() {
	if command -v apt-get >/dev/null 2>&1; then
		PM="apt"; INSTALL="apt-get install -y"; UPDATE="apt-get update -y || true"
	elif command -v dnf >/dev/null 2>&1; then
		PM="dnf"; INSTALL="dnf install -y"; UPDATE="dnf makecache -y || true"
	elif command -v yum >/dev/null 2>&1; then
		PM="yum"; INSTALL="yum install -y"; UPDATE="yum makecache -y || true"
	elif command -v pacman >/dev/null 2>&1; then
		PM="pacman"; INSTALL="pacman -S --noconfirm"; UPDATE="pacman -Sy --noconfirm || true"
	elif command -v zypper >/dev/null 2>&1; then
		PM="zypper"; INSTALL="zypper install -y"; UPDATE="zypper refresh || true"
	elif command -v apk >/dev/null 2>&1; then
		PM="apk"; INSTALL="apk add --no-cache"; UPDATE="true"
	else
		die "Unsupported distro (needs apt/dnf/yum/pacman/zypper/apk)"
	fi
}

ensure_packages() {
	bash -c "$UPDATE"
	case "$PM" in
		apt)     bash -c "$INSTALL openvpn apache2-utils $EASYRSA_PKG" ;;
		dnf|yum) bash -c "$INSTALL openvpn httpd-tools $EASYRSA_PKG" ;;
		pacman)  bash -c "$INSTALL openvpn apache easy-rsa" ;;
		zypper)  bash -c "$INSTALL openvpn apache2-utils $EASYRSA_PKG" ;;
		apk)     bash -c "$INSTALL openvpn apache2-utils easy-rsa" ;;
	esac
	resolve_htpasswd
}

detect_active_server_conf() {
	# Prefer new layout if service WorkingDirectory is /etc/openvpn/server
	# but also support legacy /etc/openvpn/*.conf
	if [[ -f "${SERVER_DIR}/server.conf" ]]; then
		SERVER_CONF="${SERVER_DIR}/server.conf"
		SERVICE_NAME="openvpn-server@${INSTANCE_NAME}"
		return
	fi
	if ls "${SERVER_DIR}"/*.conf >/dev/null 2>&1; then
		SERVER_CONF="$(ls -1 "${SERVER_DIR}"/*.conf | head -n1)"
		local base; base="$(basename "$SERVER_CONF" .conf)"
		SERVICE_NAME="openvpn-server@${base}"
		return
	fi
	if ls "${LEGACY_DIR}"/*.conf >/dev/null 2>&1; then
		SERVER_CONF="$(ls -1 "${LEGACY_DIR}"/*.conf | head -n1)"
		local base; base="$(basename "$SERVER_CONF" .conf)"
		if systemctl list-unit-files | grep -q '^openvpn@.service'; then
			SERVICE_NAME="openvpn@${base}"
		else
			SERVICE_NAME="openvpn"
		fi
		return
	fi
}

find_or_create_server_conf() {
	mkdir -p "$SERVER_DIR" "$AUTH_DIR"
	chmod 750 "$AUTH_DIR"

	detect_active_server_conf
	if [[ -n "$SERVER_CONF" ]]; then
		return
	fi

	# Create brand new config under new layout
	SERVER_CONF="${SERVER_DIR}/server.conf"
	SERVICE_NAME="openvpn-server@${INSTANCE_NAME}"

	# Copy Easy-RSA skeleton
	mkdir -p "$EASYRSA_DIR"
	if [[ -d /usr/share/easy-rsa ]]; then
		cp -a /usr/share/easy-rsa/* "$EASYRSA_DIR"/
	elif compgen -G "/usr/share/easy-rsa-*/*" >/dev/null; then
		cp -a /usr/share/easy-rsa-*/* "$EASYRSA_DIR"/
	fi

	# Build PKI
	pushd "$EASYRSA_DIR" >/dev/null
	export EASYRSA_BATCH=1
	./easyrsa init-pki
	./easyrsa build-ca nopass
	./easyrsa gen-dh
	./easyrsa build-server-full server nopass
	./easyrsa gen-crl
	popd >/dev/null

	# tls-crypt key
	openvpn --genkey secret "${SERVER_DIR}/tc.key"

	# Copy server artifacts
	cp -f "$EASYRSA_DIR/pki/ca.crt"                 "${SERVER_DIR}/"
	cp -f "$EASYRSA_DIR/pki/dh.pem"                 "${SERVER_DIR}/"
	cp -f "$EASYRSA_DIR/pki/issued/server.crt"      "${SERVER_DIR}/"
	cp -f "$EASYRSA_DIR/pki/private/server.key"     "${SERVER_DIR}/"
	cp -f "$EASYRSA_DIR/pki/crl.pem"                "${SERVER_DIR}/"
	chmod 600 "${SERVER_DIR}/server.key"

	# Write server.conf (full-tunnel by default)
	cat > "${SERVER_CONF}" <<EOF
port ${DEFAULT_PORT}
proto ${DEFAULT_PROTO}
dev tun

user nobody
group nogroup
persist-key
persist-tun
topology subnet

server ${VPN_SUBNET} ${VPN_MASK}
ifconfig-pool-persist ipp.txt

push "redirect-gateway def1 bypass-dhcp"
push "dhcp-option DNS 1.1.1.1"
push "dhcp-option DNS 9.9.9.9"

keepalive 10 60
explicit-exit-notify 1

ca ${SERVER_DIR}/ca.crt
cert ${SERVER_DIR}/server.crt
key ${SERVER_DIR}/server.key
dh ${SERVER_DIR}/dh.pem
crl-verify ${SERVER_DIR}/crl.pem
tls-crypt ${SERVER_DIR}/tc.key
tls-version-min 1.2

data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305
data-ciphers-fallback AES-256-GCM
auth SHA256

# Logging
verb 3
log-append /var/log/openvpn.log
EOF
}

ensure_line_in_conf() {
	local key="$1"
	local pattern="$2"
	grep -Eq "$pattern" "$SERVER_CONF" || echo "$key" >> "$SERVER_CONF"
}

enable_file_auth() {
	# Write verifier
	cat > "$VERIFY_SCRIPT" <<'EOF'
#!/usr/bin/env bash
set -euo pipefail
CRED_FILE="$1"
AUTH_DIR="/etc/openvpn/auth"
USER_DB="${AUTH_DIR}/users.htpasswd"
HTPASSWD_BIN="$(command -v htpasswd || true)"
if [[ -z "${HTPASSWD_BIN}" ]]; then
  for p in /usr/bin/htpasswd /bin/htpasswd; do [[ -x "$p" ]] && HTPASSWD_BIN="$p"; done
fi

# Debug (optional): write who runs me (comment out in production)
# echo "==== $(date) ====" >> /var/log/openvpn-auth.log
# echo "UID=$(id -u) USER=$(id -un) GID=$(id -g)" >> /var/log/openvpn-auth.log
# echo "ARGV: $@" >> /var/log/openvpn-auth.log

[[ -f "$CRED_FILE" && -s "$CRED_FILE" ]] || exit 1
U="$(sed -n '1p' "$CRED_FILE" | tr -d '\r\n')"
P="$(sed -n '2p' "$CRED_FILE" | tr -d '\r\n')"
[[ -n "$U" && -n "$P" ]] || exit 1
grep -qE "^${U}:" "$USER_DB" 2>/dev/null || exit 1
"$HTPASSWD_BIN" -vb "$USER_DB" "$U" "$P" >/dev/null 2>&1 && exit 0 || exit 1
EOF

	# Perms: script exec by root+nogroup; db readable by root+nogroup
	chown root:nogroup "$VERIFY_SCRIPT" || true
	chmod 750 "$VERIFY_SCRIPT"
	mkdir -p "$AUTH_DIR"
	touch "$USERS_FILE"
	chown root:nogroup "$USERS_FILE" || true
	chmod 640 "$USERS_FILE"

	# Ensure directives present (idempotent)
	sed -i '/^\s*client-cert-not-required\s*$/d' "$SERVER_CONF" || true
	sed -i '/^\s*verify-client-cert\s\+none\s*$/d' "$SERVER_CONF" || true
	ensure_line_in_conf "script-security 3" '^\s*script-security\s+3\b'
	if grep -Eq '^\s*auth-user-pass-verify\b' "$SERVER_CONF"; then
		sed -i -E "s|^\s*auth-user-pass-verify\s+.*|auth-user-pass-verify ${VERIFY_SCRIPT} via-file|g" "$SERVER_CONF"
	else
		echo "auth-user-pass-verify ${VERIFY_SCRIPT} via-file" >> "$SERVER_CONF"
	fi

	# Prepare auth debug log (owned by nobody so script can append if you enable debug)
	touch /var/log/openvpn-auth.log || true
	chown nobody:nogroup /var/log/openvpn-auth.log || true
	chmod 664 /var/log/openvpn-auth.log || true
}

enable_forwarding_and_nat() {
	# sysctl
	echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/99-openvpn-forward.conf
	sysctl -p /etc/sysctl.d/99-openvpn-forward.conf >/dev/null || true

	# Detect external iface
	local IFACE
	IFACE="$(ip route get 1.1.1.1 2>/dev/null | awk '/dev/{for(i=1;i<=NF;i++) if($i=="dev"){print $(i+1); exit}}')"
	IFACE="${IFACE:-eth0}"

	# nftables rules (preferred)
	if command -v nft >/dev/null 2>&1; then
		# Allow forward between tun and WAN (idempotent adds)
		nft list table ip filter >/dev/null 2>&1 || nft add table ip filter
		nft list chain ip filter FORWARD >/dev/null 2>&1 || nft add chain ip filter FORWARD '{ type filter hook forward priority 0 ; }'

		nft list chain ip filter FORWARD | grep -q "iif \"$TUN_DEV\" oif \"$IFACE\" accept" || \
			nft add rule ip filter FORWARD iif "$TUN_DEV" oif "$IFACE" accept
		nft list chain ip filter FORWARD | grep -q "iif \"$IFACE\" oif \"$TUN_DEV\" ct state related,established accept" || \
			nft add rule ip filter FORWARD iif "$IFACE" oif "$TUN_DEV" ct state related,established accept

		# NAT table/chain
		nft list table ip nat >/dev/null 2>&1 || nft add table ip nat
		nft list chain ip nat POSTROUTING >/dev/null 2>&1 || \
			nft 'add chain ip nat POSTROUTING { type nat hook postrouting priority 100 ; }'

		nft list chain ip nat POSTROUTING | grep -q "ip saddr ${VPN_CIDR} oif \"$IFACE\" masquerade" || \
			nft add rule ip nat POSTROUTING ip saddr ${VPN_CIDR} oif "$IFACE" masquerade

	# iptables fallback
	elif command -v iptables >/dev/null 2>&1; then
		iptables -C FORWARD -i "$TUN_DEV" -o "$IFACE" -j ACCEPT 2>/dev/null || \
			iptables -A FORWARD -i "$TUN_DEV" -o "$IFACE" -j ACCEPT
		iptables -C FORWARD -i "$IFACE" -o "$TUN_DEV" -m state --state RELATED,ESTABLISHED -j ACCEPT 2>/dev/null || \
			iptables -A FORWARD -i "$IFACE" -o "$TUN_DEV" -m state --state RELATED,ESTABLISHED -j ACCEPT
		iptables -t nat -C POSTROUTING -s "${VPN_CIDR}" -o "$IFACE" -j MASQUERADE 2>/dev/null || \
			iptables -t nat -A POSTROUTING -s "${VPN_CIDR}" -o "$IFACE" -j MASQUERADE
	fi
}

restart_service() {
	systemctl daemon-reload || true
	if [[ -z "$SERVICE_NAME" ]]; then
		for s in openvpn-server@server openvpn@server openvpn-server openvpn; do
			systemctl list-unit-files | grep -q "^${s}.service" && { SERVICE_NAME="$s"; break; }
		done
	fi
	[[ -n "$SERVICE_NAME" ]] || die "Could not determine OpenVPN systemd unit"
	systemctl enable "$SERVICE_NAME" >/dev/null 2&> /dev/null || true
	systemctl restart "$SERVICE_NAME"
}

ensure_easyrsa_ready() {
	[[ -d "$EASYRSA_DIR" ]] || die "Easy-RSA dir not found: $EASYRSA_DIR (run '$0 install')"
	[[ -x "$EASYRSA_DIR/easyrsa" ]] || die "easyrsa not executable in $EASYRSA_DIR"
}

generate_client_cert_if_missing() {
	local name="$1"
	ensure_easyrsa_ready
	local crt="$EASYRSA_DIR/pki/issued/${name}.crt"
	local key="$EASYRSA_DIR/pki/private/${name}.key"
	if [[ -f "$crt" && -f "$key" ]]; then
		return 0
	fi
	msg "No cert/key for $name, generating..."
	pushd "$EASYRSA_DIR" >/dev/null
	export EASYRSA_BATCH=1
	./easyrsa build-client-full "$name" nopass
	popd >/dev/null
}

# ---------------------- Commands ----------------------
cmd_install() {
	ensure_root
	detect_pkg_mgr
	ensure_packages
	find_or_create_server_conf

	# Ensure full-tunnel push and logging exist (idempotent)
	ensure_line_in_conf 'push "redirect-gateway def1 bypass-dhcp"' '^\s*push\s+"redirect-gateway def1 bypass-dhcp"'
	ensure_line_in_conf 'push "dhcp-option DNS 1.1.1.1"' '^\s*push\s+"dhcp-option DNS 1\.1\.1\.1"'
	ensure_line_in_conf 'push "dhcp-option DNS 9.9.9.9"' '^\s*push\s+"dhcp-option DNS 9\.9\.9\.9"'
	ensure_line_in_conf 'log-append /var/log/openvpn.log' '^\s*log-append\s+\/var\/log\/openvpn\.log'

	enable_file_auth
	enable_forwarding_and_nat
	restart_service

	# Summary
	msg "\n✅ Install/Setup complete."
	msg "   Server config : $SERVER_CONF"
	msg "   Service       : $SERVICE_NAME"
	msg "   Auth DB       : $USERS_FILE"
	msg "   Verifier      : $VERIFY_SCRIPT"
	msg "   NAT           : enabled (nft/iptables)"
	msg "\nTip: Use a separate client device for testing full-tunnel, or add 'route-nopull' if testing from the server itself."
}

cmd_add_user() {
	ensure_root; resolve_htpasswd
	local user="${1:-}"; shift || true
	[[ -n "$user" ]] || die "Usage: $0 add-user USER [--password P]"
	local pass=""
	while [[ $# -gt 0 ]]; do
		case "$1" in
			--password) pass="${2:-}"; shift 2 ;;
			*) die "Unknown flag $1" ;;
		esac
	done
	mkdir -p "$AUTH_DIR"; touch "$USERS_FILE"
	chown root:nogroup "$USERS_FILE" || true
	if [[ -z "$pass" ]]; then
		msg "Set password for $user (prompted twice):"
		"$HTPASSWD_BIN" -B "$USERS_FILE" "$user"
	else
		"$HTPASSWD_BIN" -B -b "$USERS_FILE" "$user" "$pass"
	fi
	chmod 640 "$USERS_FILE"
	msg "✅ user '$user' added/updated in $USERS_FILE"
}

cmd_del_user() {
	ensure_root; resolve_htpasswd
	local user="${1:-}"; [[ -n "$user" ]] || die "Usage: $0 del-user USER"
	[[ -f "$USERS_FILE" ]] || die "No users file at $USERS_FILE"
	if "$HTPASSWD_BIN" -h 2>&1 | grep -q -- "-D"; then
		"$HTPASSWD_BIN" -D "$USERS_FILE" "$user" || true
	else
		tmp="$(mktemp)"; grep -vE "^${user}:" "$USERS_FILE" > "$tmp" || true; mv "$tmp" "$USERS_FILE"
	fi
	chmod 640 "$USERS_FILE"
	msg "✅ user '$user' removed (if present)"
}

cmd_client_ovpn() {
	ensure_root
	local name="${1:-}"; shift || true
	[[ -n "$name" ]] || die "Usage: $0 client-ovpn NAME [--out PATH]"
	local out=""
	while [[ $# -gt 0 ]]; do
		case "$1" in
			--out) out="${2:-}"; shift 2 ;;
			*) die "Unknown flag $1" ;;
		esac
	done

	find_or_create_server_conf
	generate_client_cert_if_missing "$name"

	# Parse from server.conf
	local ca_path tc_path ta_path port proto remote_host
	ca_path="$(awk '/^[ \t]*ca[ \t]+/{print $2; exit}' "$SERVER_CONF")"
	tc_path="$(awk '/^[ \t]*tls-crypt[ \t]+/{print $2; exit}' "$SERVER_CONF")"
	ta_path="$(awk '/^[ \t]*tls-auth[ \t]+/{print $2; exit}' "$SERVER_CONF")"
	port="$(awk '/^[ \t]*port[ \t]+/{print $2; exit}' "$SERVER_CONF")"; port="${port:-$DEFAULT_PORT}"
	proto="$(awk '/^[ \t]*proto[ \t]+/{print $2; exit}' "$SERVER_CONF")"; proto="${proto:-$DEFAULT_PROTO}"

	[[ -n "$ca_path" ]] || ca_path="${SERVER_DIR}/ca.crt"
	local use_tlscrypt=1
	if [[ -n "$tc_path" && -f "$tc_path" ]]; then
		:
	elif [[ -n "$ta_path" && -f "$ta_path" ]]; then
		use_tlscrypt=0
	else
		if [[ -f "${SERVER_DIR}/tc.key" ]]; then
			tc_path="${SERVER_DIR}/tc.key"
		elif [[ -f "${SERVER_DIR}/ta.key" ]]; then
			ta_path="${SERVER_DIR}/ta.key"; use_tlscrypt=0
		fi
	fi

	# Best-effort remote (replace with public IP/DNS if you have one)
	remote_host="$(hostname -I 2>/dev/null | awk '{print $1}')"
	remote_host="${remote_host:-YOUR_SERVER_IP_OR_DNS}"

	local crt="$EASYRSA_DIR/pki/issued/${name}.crt"
	local key="$EASYRSA_DIR/pki/private/${name}.key"

	local tmp; tmp="$(mktemp)"
	{
		echo "client"
		echo "dev tun"
		echo "proto ${proto}"
		echo "remote ${remote_host} ${port}"
		echo "resolv-retry infinite"
		echo "nobind"
		echo "persist-key"
		echo "persist-tun"
		echo "remote-cert-tls server"
		echo "auth SHA256"
		echo "verb 3"
		echo "auth-user-pass"
		echo "auth-nocache"
		echo "data-ciphers AES-256-GCM:AES-128-GCM:CHACHA20-POLY1305"
		echo "data-ciphers-fallback AES-256-GCM"

		echo "<ca>";        sed 's/\r$//' "$ca_path";  echo "</ca>"
		echo "<cert>";      sed 's/\r$//' "$crt";      echo "</cert>"
		echo "<key>";       sed 's/\r$//' "$key";      echo "</key>"

		if [[ $use_tlscrypt -eq 1 ]]; then
			echo "<tls-crypt>"; sed 's/\r$//' "$tc_path"; echo "</tls-crypt>"
		else
			echo "key-direction 1"
			echo "<tls-auth>"; sed 's/\r$//' "$ta_path"; echo "</tls-auth>"
		fi
	} > "$tmp"

	out="${out:-/root/${name}.ovpn}"
	mv "$tmp" "$out"
	chmod 600 "$out"
	msg "✅ .ovpn written: $out"
}

cmd_list() {
	msg "== Users in ${USERS_FILE} =="
	if [[ -f "$USERS_FILE" ]]; then
		cut -d: -f1 "$USERS_FILE" || true
	else
		msg "(no users file)"
	fi
	msg ""
	msg "== Clients in ${EASYRSA_DIR}/pki/issued =="
	if compgen -G "${EASYRSA_DIR}/pki/issued/*.crt" >/dev/null; then
		ls -1 "${EASYRSA_DIR}/pki/issued/"*.crt | sed 's#.*/##; s#\.crt$##'
	else
		msg "(no client certs)"
	fi
}

cmd_status() {
	find_or_create_server_conf
	msg "Server config : $SERVER_CONF"
	msg "Service       : $SERVICE_NAME"
	msg "Auth DB       : $USERS_FILE"
	msg "Verifier      : $VERIFY_SCRIPT"
	systemctl status "$SERVICE_NAME" --no-pager || true
}

cmd_help() {
	cat <<'HLP'
OpenVPN File-Auth Manager

Usage:
  openvpn-fileauth-manager.sh install
  openvpn-fileauth-manager.sh add-user USER [--password PASS]
  openvpn-fileauth-manager.sh del-user USER
  openvpn-fileauth-manager.sh client-ovpn USER [--out /path/client.ovpn]
  openvpn-fileauth-manager.sh list
  openvpn-fileauth-manager.sh status
  openvpn-fileauth-manager.sh help

Flow:
  1) install
  2) add-user alice --password 'S3cret!'
  3) client-ovpn alice --out /root/alice.ovpn

Defaults:
  - Full-tunnel (push redirect-gateway) + DNS (1.1.1.1, 9.9.9.9)
  - nftables FORWARD + NAT rules for 10.8.0.0/24
  - /etc/openvpn/auth/file-auth.sh (bcrypt users in users.htpasswd)

Logging:
  verb 3
  log-append /var/log/openvpn.log
  # Optional auth debug: /var/log/openvpn-auth.log (owned by nobody)

Notes:
  - If you ever test a client on the same VPS, use 'route-nopull' in the client to avoid hairpinning the default route.
HLP
}

# ---------------------- Router ----------------------
cmd="${1:-help}"; shift || true
case "$cmd" in
  install)     cmd_install "$@" ;;
  add-user)    cmd_add_user "$@" ;;
  del-user)    cmd_del_user "$@" ;;
  client-ovpn) cmd_client_ovpn "$@" ;;
  list)        cmd_list "$@" ;;
  status)      cmd_status "$@" ;;
  help|--help|-h) cmd_help ;;
  *) die "Unknown command '$cmd'. Run: $0 help" ;;
esac