#!/usr/bin/env bash
# Configure log retention & archiving for compliance audits
# - Journald size/retention limits
# - Logrotate with maxage + compression
# - Daily archive with SHA256 manifests (optional GPG encryption)
# - Permissions hardened; simple reporting

set -euo pipefail

### ---- Configurable settings ----
RETENTION_DAYS="${RETENTION_DAYS:-180}"         # how long to keep logs (days)
ARCHIVE_DIR="${ARCHIVE_DIR:-/var/log/archive}"  # where rotated logs get archived
MIN_FREE_GB="${MIN_FREE_GB:-2}"                 # pause archiving if free space < this
ENCRYPT="${ENCRYPT:-false}"                      # "true" to GPG-encrypt archives
GPG_RECIPIENT="${GPG_RECIPIENT:-}"              # e.g., "audit@example.com"
OWNER="${OWNER:-root}"                           # owner of archive dir
GROUP="${GROUP:-adm}"                            # group for read access ("adm" on Debian; "root" on RHEL)
JOURNAL_MAX_USE="${JOURNAL_MAX_USE:-1G}"         # journal disk cap
JOURNAL_MAX_FILE="${JOURNAL_MAX_FILE:-50M}"      # per-journal file cap
### --------------------------------

require_root() {
  if [[ $EUID -ne 0 ]]; then echo "Please run as root."; exit 1; fi
}
pkg_present() { command -v "$1" >/dev/null 2>&1; }
ensure_pkg() {
  local p="$1"
  if ! pkg_present "$p"; then
	if pkg_present apt-get; then apt-get update -y && apt-get install -y "$p"
	elif pkg_present dnf; then dnf install -y "$p"
	elif pkg_present yum; then yum install -y "$p"
	else echo "Can't install $p automatically; install it and rerun." ; exit 1
	fi
  fi
}

require_root
ensure_pkg logrotate
ensure_pkg coreutils
ensure_pkg gzip
ensure_pkg findutils
ensure_pkg systemd || true  # journald may be present even if this fails

if [[ "$ENCRYPT" == "true" ]]; then
  ensure_pkg gpg
  [[ -n "$GPG_RECIPIENT" ]] || { echo "Set GPG_RECIPIENT when ENCRYPT=true"; exit 1; }
fi

echo "[1/5] Hardening archive directory..."
mkdir -p "$ARCHIVE_DIR"
chown "${OWNER}:${GROUP}" "$ARCHIVE_DIR"
chmod 0750 "$ARCHIVE_DIR"

# Optional: keep archive files append-only (can be disabled by auditors if needed)
# Requires chattr (e2fsprogs)
if pkg_present chattr; then
  # we won't set +a on the directory itself (can hinder rotation); apply on files when created
  :
fi

echo "[2/5] Configuring systemd-journald retention..."
JOURNALD_CONF="/etc/systemd/journald.conf"
cp -a "$JOURNALD_CONF" "${JOURNALD_CONF}.bak.$(date +%s)" || true
# Set/replace keys
sed -ri "s/^#?\s*SystemMaxUse=.*/SystemMaxUse=${JOURNAL_MAX_USE}/" "$JOURNALD_CONF" || echo "SystemMaxUse=${JOURNAL_MAX_USE}" >> "$JOURNALD_CONF"
sed -ri "s/^#?\s*SystemMaxFileSize=.*/SystemMaxFileSize=${JOURNAL_MAX_FILE}/" "$JOURNALD_CONF" || echo "SystemMaxFileSize=${JOURNAL_MAX_FILE}" >> "$JOURNALD_CONF"
# MaxRetentionSec in seconds
RET_SEC=$(( RETENTION_DAYS * 24 * 3600 ))
grep -qE '^#?\s*MaxRetentionSec=' "$JOURNALD_CONF" \
  && sed -ri "s/^#?\s*MaxRetentionSec=.*/MaxRetentionSec=${RET_SEC}/" "$JOURNALD_CONF" \
  || echo "MaxRetentionSec=${RET_SEC}" >> "$JOURNALD_CONF"
systemctl restart systemd-journald || true

echo "[3/5] Installing logrotate policy..."
LR_FILE="/etc/logrotate.d/99-compliance-retention"
cat > "$LR_FILE" <<EOF
# Generic retention/compression for most logs; relies on system defaults + maxage
/var/log/*.log
/var/log/*/*.log
/var/log/**/*.log
{
	daily
	rotate 365
	maxage ${RETENTION_DAYS}
	missingok
	notifempty
	compress
	delaycompress
	dateext
	dateformat -%Y%m%d
	sharedscripts
	create 0640 root ${GROUP}
	postrotate
		# Reload rsyslog if present (Debian/Ubuntu)
		if command -v systemctl >/dev/null 2>&1 && systemctl is-active --quiet rsyslog; then
			systemctl reload rsyslog || true
		fi
		# RHEL variants may use systemd-journald primarily; nothing to reload
	endscript
}
EOF

chmod 0644 "$LR_FILE"

echo "[4/5] Creating daily archive + manifest job..."
ARCHIVER="/usr/local/sbin/log-archive.sh"
cat > "$ARCHIVER" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail

ARCHIVE_DIR="${ARCHIVE_DIR:-/var/log/archive}"
GROUP="${GROUP:-adm}"
ENCRYPT="${ENCRYPT:-false}"
GPG_RECIPIENT="${GPG_RECIPIENT:-}"
MIN_FREE_GB="${MIN_FREE_GB:-2}"

log() { echo "[$(date -Is)] $*"; }

# check free space on partition hosting ARCHIVE_DIR
avail_gb=$(df -Pk "$ARCHIVE_DIR" | awk 'NR==2{printf "%.0f", $4/1024/1024}')
if (( avail_gb < MIN_FREE_GB )); then
  log "Free space ${avail_gb}GB < ${MIN_FREE_GB}GB; skipping run."
  exit 0
fi

mkdir -p "$ARCHIVE_DIR"
# Move yesterday+ rotated logs (*.gz, *.1, *.2.gz etc.) into ARCHIVE_DIR
# Exclude already-archived files
shopt -s nullglob
mapfile -t FILES < <(find /var/log -type f \( -name "*.gz" -o -name "*.1" -o -name "*.2.gz" -o -name "*.log-20*" \) -mtime +0 ! -path "$ARCHIVE_DIR/*")
count=0

MANIFEST="${ARCHIVE_DIR}/manifest-$(date +%Y%m).csv"
touch "$MANIFEST"
chmod 0640 "$MANIFEST"
chgrp "$GROUP" "$MANIFEST"

for f in "${FILES[@]}"; do
  base=$(basename "$f")
  dest="${ARCHIVE_DIR}/${base}"
  # unique-ify if name exists
  if [[ -e "$dest" ]]; then
	dest="${ARCHIVE_DIR}/$(date +%Y%m%d%H%M%S)-${base}"
  end_if_marker=1
  fi
  mv "$f" "$dest"
  chmod 0640 "$dest"
  chgrp "$GROUP" "$dest"

  # Integrity: sha256 and size/mtime into manifest
  sha=$(sha256sum "$dest" | awk '{print $1}')
  size=$(stat -c%s "$dest")
  mtime=$(date -r "$dest" -Is)
  echo "${dest},${sha},${size},${mtime}" >> "$MANIFEST"

  # Optional GPG encryption (keeps both .gpg and removes plaintext)
  if [[ "${ENCRYPT}" == "true" ]]; then
	[[ -n "${GPG_RECIPIENT}" ]] || { log "GPG_RECIPIENT not set; skipping encryption."; }
	if [[ -n "${GPG_RECIPIENT}" ]]; then
	gpg --batch --yes --trust-model always -r "${GPG_RECIPIENT}" --output "${dest}.gpg" --encrypt "${dest}"
	shred -u "${dest}"
	dest="${dest}.gpg"
	chmod 0640 "$dest"
	chgrp "$GROUP" "$dest"
	fi
  fi

  # If chattr exists, mark file append-only (+a) for tamper evidence
  if command -v chattr >/dev/null 2>&1; then
	chattr +a "$dest" || true
  fi

  ((count++)) || true
done

# Enforce retention inside archive (delete older than RETENTION_DAYS)
RETENTION_DAYS="${RETENTION_DAYS:-180}"
find "$ARCHIVE_DIR" -type f -mtime +$RETENTION_DAYS -not -name "manifest-*.csv" -print -delete

# Report
REPORT="${ARCHIVE_DIR}/last_run.txt"
{
  echo "Run: $(date -Is)"
  echo "Moved files: $count"
  echo "Archive dir: $ARCHIVE_DIR"
  echo "Encrypt: $ENCRYPT"
  echo "Free GB now: $(df -Pk "$ARCHIVE_DIR" | awk 'NR==2{printf "%.0f", $4/1024/1024}')"
} > "$REPORT"
chmod 0640 "$REPORT"
chgrp "$GROUP" "$REPORT"

exit 0
EOS
chmod 0750 "$ARCHIVER"

# Drop environment defaults for the archiver
ENV_FILE="/etc/default/log-archive"
cat > "$ENV_FILE" <<EOF
ARCHIVE_DIR="$ARCHIVE_DIR"
GROUP="$GROUP"
ENCRYPT="$ENCRYPT"
GPG_RECIPIENT="$GPG_RECIPIENT"
RETENTION_DAYS="$RETENTION_DAYS"
MIN_FREE_GB="$MIN_FREE_GB"
EOF
chmod 0644 "$ENV_FILE"

# Wrapper so cron has the env
CRON_WRAPPER="/etc/cron.daily/log-archive"
cat > "$CRON_WRAPPER" <<EOF
#!/usr/bin/env bash
set -euo pipefail
source "$ENV_FILE"
export ARCHIVE_DIR GROUP ENCRYPT GPG_RECIPIENT RETENTION_DAYS MIN_FREE_GB
"$ARCHIVER"
EOF
chmod 0755 "$CRON_WRAPPER"

echo "[5/5] Testing logrotate once (dry-ish run)..."
logrotate -d /etc/logrotate.conf >/dev/null || true

echo "Done.

What was configured:
- journald capped at ${JOURNAL_MAX_USE}, files ${JOURNAL_MAX_FILE}, retention ${RETENTION_DAYS}d
- logrotate policy with compression + maxage ${RETENTION_DAYS}d
- daily archiver moves rotated logs to ${ARCHIVE_DIR}, writes SHA256 to monthly manifest, optional GPG encryption
- archive retention also ${RETENTION_DAYS}d
Verification:
  journalctl --disk-usage
  grep -E 'MaxRetentionSec|SystemMaxUse' /etc/systemd/journald.conf
  sudo logrotate -f /etc/logrotate.conf   # force a rotation
  sudo /etc/cron.daily/log-archive        # run the archiver now
  ls -l ${ARCHIVE_DIR} && cat ${ARCHIVE_DIR}/last_run.txt

Optional remote offload (add later):
  # rsync -a --delete ${ARCHIVE_DIR}/ backup@vault:/srv/log-archive/\$(hostname)/

"