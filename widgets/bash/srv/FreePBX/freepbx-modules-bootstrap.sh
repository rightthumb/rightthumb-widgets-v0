#!/usr/bin/env bash
# FreePBX 17 Module Bootstrapper
# - Enables repos (standard, extended; optional commercial)
# - Installs a reliable baseline set so the GUI works after first login
# - Optional --all to grab every module from enabled repos
# - Refreshes signatures, upgrades, fixes ownerships, reloads dialplan

set -euo pipefail

LOG_DIR="/var/log/pbx"
mkdir -p "$LOG_DIR"
LOG_FILE="${LOG_DIR}/freepbx-modules-$(date '+%Y.%m.%d-%H.%M.%S').log"
exec > >(tee -a "$LOG_FILE") 2>&1

INCLUDE_COMMERCIAL=false
INSTALL_ALL=false

usage() {
  cat <<'EOF'
Usage:
  sudo bash freepbx-modules-bootstrap.sh [--all] [--include-commercial]

Options:
  --all                Install ALL modules from the enabled repos (standard + extended).
  --include-commercial Enable 'commercial' repo too (requires ionCube + proper licensing).
  -h, --help           Show this help and exit.

Notes:
  - Requires a working FreePBX 17 install with /usr/sbin/fwconsole available.
  - Safe to rerun; idempotent where possible.
  - Logs: /var/log/pbx/
EOF
}

# ----- args -----
while [[ $# -gt 0 ]]; do
  case "$1" in
    --all)                INSTALL_ALL=true; shift ;;
    --include-commercial) INCLUDE_COMMERCIAL=true; shift ;;
    -h|--help)            usage; exit 0 ;;
    *) echo "Unknown option: $1"; usage; exit 1 ;;
  esac
done

die(){ echo "ERROR: $*" >&2; exit 1; }
need(){ command -v "$1" >/dev/null 2>&1 || die "Missing required command: $1"; }

echo "== FreePBX 17 Module Bootstrapper =="
need fwconsole

# Quick environment sanity
PHPV="$(php -r 'echo PHP_MAJOR_VERSION.".".PHP_MINOR_VERSION;' 2>/dev/null || echo 'unknown')"
echo "Detected PHP: $PHPV"
if [[ "$PHPV" != 8.2* ]]; then
  echo "WARNING: FreePBX 17 targets PHP 8.2. If you see vendor/Carbon errors, switch Apache/CLI to PHP 8.2."
fi

# Ensure log path is writable (prevents Whoops and repo/module UI issues)
fix_log_perms(){
  getent group asterisk >/dev/null || groupadd -r asterisk
  getent passwd asterisk >/dev/null 2>&1 || useradd -r -g asterisk -d /var/lib/asterisk -s /sbin/nologin asterisk
  if id -u www-data >/dev/null 2>&1; then usermod -aG asterisk www-data || true; fi
  if id -u apache   >/dev/null 2>&1; then usermod -aG asterisk apache   || true; fi
  mkdir -p /var/log/asterisk
  touch /var/log/asterisk/freepbx.log
  chown -R asterisk:asterisk /var/log/asterisk
  chmod 2775 /var/log/asterisk
  chmod 0664 /var/log/asterisk/freepbx.log
}
fix_log_perms

# Asterisk status (non-fatal)
systemctl is-active --quiet asterisk && echo "Asterisk: active" || echo "WARNING: Asterisk not running (continuing)."

echo "== Repos =="
fwconsole ma listrepos || true
fwconsole ma enablerepo standard || true
fwconsole ma enablerepo extended || true

if $INCLUDE_COMMERCIAL; then
  echo "Enabling commercial repo (requires ionCube)…"
  if php -m | grep -qi ioncube; then
    fwconsole ma enablerepo commercial || true
  else
    echo "WARNING: ionCube not loaded in PHP; skipping commercial repo."
  fi
fi

echo "== Refresh signatures, show online modules =="
fwconsole ma refreshsignatures || true
fwconsole ma listonline || true

# Baseline set (minimal but complete to eliminate "Module Not Found" on first login)
BASELINE=(
  framework core sipsettings voicemail
  userman featurecodeadmin infoservices logfiles
  recordings callrecording dashboard pm2
  ucp cel cdr
)

# Some extras that are commonly needed (best effort; harmless if missing)
NICE_TO_HAVE=(
  extensionroutes bulkhandler firewall
  restapi contactmanager
)

echo "== Installing baseline modules =="
for mod in "${BASELINE[@]}"; do
  echo "--> $mod"
  fwconsole ma downloadinstall "$mod" || true
done

echo "== Installing common extras (best effort) =="
ONLINE_LIST="$(fwconsole ma listonline 2>/dev/null | awk '/Online/ {print $2}' | sort -u || true)"
for mod in "${NICE_TO_HAVE[@]}"; do
  if echo "$ONLINE_LIST" | grep -qx "$mod"; then
    echo "--> $mod"
    fwconsole ma downloadinstall "$mod" || true
  fi
done

if $INSTALL_ALL; then
  echo "== Installing ALL modules from enabled repos (this can take a while) =="
  for mod in $ONLINE_LIST; do
    case "$mod" in
      sysadmin|zulu|ucpnode|pms|endpoint|callaccounting|propertymanagement|webrtc)
        if ! $INCLUDE_COMMERCIAL; then
          echo "Skipping likely commercial module without ionCube: $mod"
          continue
        fi
      ;;
    esac
    echo "--> $mod"
    fwconsole ma downloadinstall "$mod" || true
  done
fi

echo "== Upgrading all modules, fixing ownerships =="
fwconsole ma upgradeall || true
fwconsole chown || true

echo "== Reloading and restarting FreePBX =="
fwconsole reload || true
fwconsole restart || true

echo
echo "Done. If the GUI showed 'Module Not Found', refresh (Ctrl+F5)."
echo "Log: $LOG_FILE"
