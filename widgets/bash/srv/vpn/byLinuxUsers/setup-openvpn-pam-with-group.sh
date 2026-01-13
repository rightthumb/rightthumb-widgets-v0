#!/usr/bin/env bash
set -euo pipefail

# =========================================================
# OpenVPN + PAM (Linux users) with certificate auth kept on
# Restrict access to users in the 'openvpn-users' group
#
# Usage examples:
#   sudo bash setup-openvpn-pam-with-group.sh --users alice,bob
#   sudo bash setup-openvpn-pam-with-group.sh --users alice,bob --create-users
#   sudo bash setup-openvpn-pam-with-group.sh --allowed-file /root/vpn_allowed.txt --create-users
#
# Notes:
# - Keeps cert auth. Adds username/password (PAM) as an additional factor.
# - Clients must have 'auth-user-pass' in their .ovpn to be prompted.
# - Script also enables full-tunnel by default (redirect-gateway + DNS) and NAT.
# =========================================================

# ---------------------- Defaults ----------------------
ALLOWED_USERS_CSV=""
ALLOWED_FILE=""
CREATE_USERS=0
VPN_GROUP="openvpn-users"

SERVER_DIR="/etc/openvpn/server"
LEGACY_DIR="/etc/openvpn"
SERVER_CONF=""
SERVICE_NAME=""
INSTANCE_NAME="server"

VPN_SUBNET="10.8.0.0"
VPN_MASK="255.255.255.0"
VPN_CIDR="${VPN_SUBNET}/24"
DEFAULT_PROTO="udp"
DEFAULT_PORT="1194"
TUN_DEV="tun0"   # default device name

# ---------------------- Helpers ----------------------
msg(){ echo -e "$*"; }
die(){ echo "ERROR: $*" >&2; exit 1; }
ensure_root(){ [[ $EUID -eq 0 ]] || die "Run as root (sudo)."; }

detect_pkg_mgr(){
  if command -v apt-get >/dev/null 2>&1; then
	PKG_MGR="apt"; INSTALL="apt-get install -y"; UPDATE="apt-get update -y || true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib/openvpn/openvpn-plugin-auth-pam.so"
	"/usr/lib/x86_64-linux-gnu/openvpn/plugins/openvpn-plugin-auth-pam.so"
	)
  elif command -v dnf >/dev/null 2>&1; then
	PKG_MGR="dnf"; INSTALL="dnf install -y"; UPDATE="dnf makecache -y || true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so"
	"/usr/lib64/openvpn/openvpn-plugin-auth-pam.so"
	)
  elif command -v yum >/dev/null 2>&1; then
	PKG_MGR="yum"; INSTALL="yum install -y"; UPDATE="yum makecache -y || true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so"
	"/usr/lib64/openvpn/openvpn-plugin-auth-pam.so"
	)
  elif command -v pacman >/dev/null 2>&1; then
	PKG_MGR="pacman"; INSTALL="pacman -S --noconfirm"; UPDATE="pacman -Sy --noconfirm || true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib/openvpn/plugins/openvpn-plugin-auth-pam.so"
	"/usr/lib/openvpn/openvpn-plugin-auth-pam.so"
	)
  elif command -v zypper >/dev/null 2>&1; then
	PKG_MGR="zypper"; INSTALL="zypper install -y"; UPDATE="zypper refresh || true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib64/openvpn/plugins/openvpn-plugin-auth-pam.so"
	"/usr/lib64/openvpn/openvpn-plugin-auth-pam.so"
	)
  elif command -v apk >/dev/null 2>&1; then
	PKG_MGR="apk"; INSTALL="apk add --no-cache"; UPDATE="true"
	PAM_SVC_DIR="/etc/pam.d"
	PLUGIN_CANDIDATES=(
	"/usr/lib/openvpn/plugins/openvpn-plugin-auth-pam.so"
	"/usr/lib/openvpn/openvpn-plugin-auth-pam.so"
	)
  else
	die "Unsupported distro (needs apt/dnf/yum/pacman/zypper/apk)"
  fi
}

ensure_packages(){
  bash -c "$UPDATE"
  case "$PKG_MGR" in
	apt)   bash -c "$INSTALL openvpn libpam-modules" ;;
	dnf|yum) bash -c "$INSTALL openvpn pam" || true ;;
	pacman)  bash -c "$INSTALL openvpn pambase" || true ;;
	zypper)  bash -c "$INSTALL openvpn pam" || true ;;
	apk)     bash -c "$INSTALL openvpn linux-pam" || true ;;
  esac
}

detect_active_server_conf(){
  # Prefer new layout; also support legacy. If none, we create it under new layout.
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

ensure_line_in_conf(){
  local key="$1"
  local pattern="$2"
  grep -Eq "$pattern" "$SERVER_CONF" || echo "$key" >> "$SERVER_CONF"
}

create_server_if_missing(){
  mkdir -p "$SERVER_DIR"
  detect_active_server_conf
  if [[ -n "$SERVER_CONF" ]]; then
	return
  fi
  # Create a minimal server with full-tunnel defaults
  SERVER_CONF="${SERVER_DIR}/server.conf"
  SERVICE_NAME="openvpn-server@${INSTANCE_NAME}"

  # Basic PKI via Easy-RSA (quick init)
  local EASYRSA_DIR="/etc/openvpn/easy-rsa"
  mkdir -p "$EASYRSA_DIR"
  if [[ -d /usr/share/easy-rsa ]]; then
	cp -a /usr/share/easy-rsa/* "$EASYRSA_DIR"/
  elif compgen -G "/usr/share/easy-rsa-*/*" >/dev/null; then
	cp -a /usr/share/easy-rsa-*/* "$EASYRSA_DIR"/
  fi
  pushd "$EASYRSA_DIR" >/dev/null
  export EASYRSA_BATCH=1
  ./easyrsa init-pki
  ./easyrsa build-ca nopass
  ./easyrsa gen-dh
  ./easyrsa build-server-full server nopass
  ./easyrsa gen-crl
  popd >/dev/null

  openvpn --genkey secret "${SERVER_DIR}/tc.key"
  cp -f "$EASYRSA_DIR/pki/ca.crt"                 "${SERVER_DIR}/"
  cp -f "$EASYRSA_DIR/pki/dh.pem"                 "${SERVER_DIR}/"
  cp -f "$EASYRSA_DIR/pki/issued/server.crt"      "${SERVER_DIR}/"
  cp -f "$EASYRSA_DIR/pki/private/server.key"     "${SERVER_DIR}/"
  cp -f "$EASYRSA_DIR/pki/crl.pem"                "${SERVER_DIR}/"
  chmod 600 "${SERVER_DIR}/server.key"

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

locate_pam_plugin(){
  PLUGIN_PATH=""
  for p in "${PLUGIN_CANDIDATES[@]}"; do
	[[ -f "$p" ]] && { PLUGIN_PATH="$p"; break; }
  done
  [[ -n "$PLUGIN_PATH" ]] || die "openvpn PAM plugin not found. Tried: ${PLUGIN_CANDIDATES[*]}"
}

enable_pam_with_group(){
  # PAM service policy
  local PAM_FILE="${PAM_SVC_DIR}/openvpn"
  cat > "$PAM_FILE" <<'EOF'
# PAM policy for OpenVPN password auth (with certs kept on server)
# Only allow users who are members of group "openvpn-users".

# Quick fail if not in the group:
auth    requisite   pam_succeed_if.so user ingroup openvpn-users

# Standard UNIX auth:
auth    required    pam_unix.so
account required    pam_unix.so
EOF
  chmod 0644 "$PAM_FILE"

  # Ensure group exists
  getent group "$VPN_GROUP" >/dev/null || groupadd "$VPN_GROUP"

  # Make sure we load the plugin with our 'openvpn' service
  if grep -Eq '^\s*plugin\s+.+openvpn-plugin-auth-pam\.so\b' "$SERVER_CONF"; then
	sed -i -E "s|(plugin\s+.+openvpn-plugin-auth-pam\.so)(\s+\S+)?|\1 openvpn|g" "$SERVER_CONF"
  else
	{
	echo ""
	echo "# Enable username/password via PAM (service: openvpn), keeping cert auth"
	echo "plugin ${PLUGIN_PATH} openvpn"
	} >> "$SERVER_CONF"
  fi

  # Keep certs on: remove any password-only directives if present
  sed -i '/^\s*verify-client-cert\s\+none\s*$/d' "$SERVER_CONF" || true
  sed -i '/^\s*client-cert-not-required\s*$/d' "$SERVER_CONF" || true

  # If a file-based verifier was previously enabled, remove it to avoid double-auth chains
  sed -i -E '/^\s*auth-user-pass-verify\s+/d' "$SERVER_CONF" || true
}

enable_forwarding_and_nat(){
  echo "net.ipv4.ip_forward=1" > /etc/sysctl.d/99-openvpn-forward.conf
  sysctl -p /etc/sysctl.d/99-openvpn-forward.conf >/dev/null || true

  local IFACE
  IFACE="$(ip route get 1.1.1.1 2>/dev/null | awk '/dev/{for(i=1;i<=NF;i++) if($i=="dev"){print $(i+1); exit}}')"
  IFACE="${IFACE:-eth0}"

  # nftables (preferred)
  if command -v nft >/dev/null 2>&1; then
	nft list table ip filter >/dev/null 2>&1 || nft add table ip filter
	nft list chain ip filter FORWARD >/dev/null 2>&1 || nft add chain ip filter FORWARD '{ type filter hook forward priority 0 ; }'

	nft list chain ip filter FORWARD | grep -q "iif \"$TUN_DEV\" oif \"$IFACE\" accept" || \
	nft add rule ip filter FORWARD iif "$TUN_DEV" oif "$IFACE" accept
	nft list chain ip filter FORWARD | grep -q "iif \"$IFACE\" oif \"$TUN_DEV\" ct state related,established accept" || \
	nft add rule ip filter FORWARD iif "$IFACE" oif "$TUN_DEV" ct state related,established accept

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

restart_service(){
  systemctl daemon-reload || true
  if [[ -z "$SERVICE_NAME" ]]; then
	for s in openvpn-server@server openvpn@server openvpn-server openvpn; do
	systemctl list-unit-files | grep -q "^${s}.service" && { SERVICE_NAME="$s"; break; }
	done
  fi
  [[ -n "$SERVICE_NAME" ]] || die "Could not determine OpenVPN systemd unit"
  systemctl enable "$SERVICE_NAME" >/dev/null 2>&1 || true
  systemctl restart "$SERVICE_NAME"
}

# ---------------------- User/group helpers ----------------------
dedupe_users_array(){
  if [[ ${#ALLOWED_USERS[@]} -gt 0 ]]; then
	ALLOWED_USERS=($(printf "%s\n" "${ALLOWED_USERS[@]}" | awk 'NF' | sort -u))
  fi
}

maybe_create_users_and_group(){
  local NOLOGIN_SHELL="/usr/sbin/nologin"
  [[ -x "$NOLOGIN_SHELL" ]] || NOLOGIN_SHELL="/sbin/nologin"

  if [[ $CREATE_USERS -eq 1 && ${#ALLOWED_USERS[@]} -gt 0 ]]; then
	for u in "${ALLOWED_USERS[@]}"; do
	if ! id "$u" >/dev/null 2>&1; then
		useradd -m -s "$NOLOGIN_SHELL" "$u"
		echo "Created user: $u (shell $(basename "$NOLOGIN_SHELL"))"
		echo "Set a password for $u:"
		passwd "$u"
	fi
	usermod -aG "$VPN_GROUP" "$u"
	done
  elif [[ ${#ALLOWED_USERS[@]} -gt 0 ]]; then
	for u in "${ALLOWED_USERS[@]}"; do
	if ! id "$u" >/dev/null 2>&1; then
		echo "User $u does not exist. Create it or re-run with --create-users." >&2
	else
		usermod -aG "$VPN_GROUP" "$u"
	fi
	done
  fi
}

# ---------------------- Commands ----------------------
cmd_install(){
  ensure_root
  detect_pkg_mgr
  ensure_packages

  # Collect allowed users (if provided)
  declare -a ALLOWED_USERS=()
  if [[ -n "$ALLOWED_USERS_CSV" ]]; then
	IFS=',' read -r -a ALLOWED_USERS <<< "$ALLOWED_USERS_CSV"
  fi
  if [[ -n "$ALLOWED_FILE" ]]; then
	[[ -f "$ALLOWED_FILE" ]] || die "allowed-file not found: $ALLOWED_FILE"
	mapfile -t FILE_USERS < <(grep -E '^[a-z_][a-z0-9_-]*[$]?$' "$ALLOWED_FILE" || true)
	ALLOWED_USERS+=("${FILE_USERS[@]}")
  fi
  dedupe_users_array

  create_server_if_missing
  detect_active_server_conf

  # Ensure full-tunnel push + DNS + logging present (idempotent)
  ensure_line_in_conf 'push "redirect-gateway def1 bypass-dhcp"' '^\s*push\s+"redirect-gateway def1 bypass-dhcp"'
  ensure_line_in_conf 'push "dhcp-option DNS 1.1.1.1"' '^\s*push\s+"dhcp-option DNS 1\.1\.1\.1"'
  ensure_line_in_conf 'push "dhcp-option DNS 9.9.9.9"' '^\s*push\s+"dhcp-option DNS 9\.9\.9\.9"'
  ensure_line_in_conf 'log-append /var/log/openvpn.log' '^\s*log-append\s+\/var\/log\/openvpn\.log'
  ensure_line_in_conf 'verb 3' '^\s*verb\s+3\b'

  locate_pam_plugin
  enable_pam_with_group

  maybe_create_users_and_group
  enable_forwarding_and_nat
  restart_service

  echo
  echo "✅ OpenVPN is now configured for CERT + PAM (Linux users)."
  echo "   Allowed group: ${VPN_GROUP}"
  if [[ ${#ALLOWED_USERS[@]} -gt 0 ]]; then
	echo "   Users added to ${VPN_GROUP}: ${ALLOWED_USERS[*]}"
  fi
  echo
  echo "👉 Ensure each client .ovpn contains:  auth-user-pass"
  echo "   (Re-export or edit client profiles as needed.)"
  echo
  echo "Service:"
  echo "   systemctl status ${SERVICE_NAME} --no-pager"
  echo
  echo "Routing/NAT: nftables rules and IP forwarding are enabled for full-tunnel."
  echo "If you prefer split-tunnel, comment out the 'redirect-gateway' push in server.conf."
  echo
}

cmd_help(){
  cat <<'HLP'
setup-openvpn-pam-with-group.sh

Usage:
  setup-openvpn-pam-with-group.sh --users alice,bob [--create-users]
  setup-openvpn-pam-with-group.sh --allowed-file /root/vpn_allowed.txt [--create-users]
  setup-openvpn-pam-with-group.sh --help

What it does:
  - Keeps certificate auth ON.
  - Adds username/password via PAM (Linux users), restricted to 'openvpn-users' group.
  - Creates group and optionally creates users with nologin shell.
  - Enables full-tunnel by default (push redirect-gateway + DNS) and sets nftables FORWARD + NAT.

Notes:
  - Clients must have 'auth-user-pass' in their .ovpn.
  - To switch to split-tunnel, remove the redirect-gateway push and restart OpenVPN.

Examples:
  sudo bash setup-openvpn-pam-with-group.sh --users alice,bob --create-users
  sudo bash setup-openvpn-pam-with-group.sh --allowed-file /root/vpn_allowed.txt

HLP
}

# ---------------------- Arg parse & dispatch ----------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
	--users)        ALLOWED_USERS_CSV="${2:-}"; shift 2 ;;
	--allowed-file) ALLOWED_FILE="${2:-}"; shift 2 ;;
	--create-users) CREATE_USERS=1; shift ;;
	-h|--help)      cmd_help; exit 0 ;;
	*) die "Unknown arg: $1" ;;
  esac
done

cmd_install