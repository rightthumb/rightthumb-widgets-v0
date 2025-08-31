#!/usr/bin/env bash
# ThreatWeaver: unified runner with profiles, per-knob overrides, and print-only mode
# Save as: /opt/ThreatWeaver/run_all_fw.sh
# Make executable: chmod +x /opt/ThreatWeaver/run_all_fw.sh
# Examples:
#   ./run_all_fw.sh --auth
#   ./run_all_fw.sh --mode aggressive --auth --apache-error
#   ./run_all_fw.sh --print-command --apache-access
#   ./run_all_fw.sh --set WIN_AUTH=600 --set SSH_FAIL_THRESH_AUTH=4 --auth
set -euo pipefail

# --------- GLOBAL DEFAULTS (BALANCED = best-practice) ---------
PY="/bin/python3"
ENGINE="/opt/ThreatWeaver/FirewallEngine.py"
WL="/opt/whitelist_ip.txt"
FW="iptables"
LEDGER_DB="/opt/FirewallEngine_ingest_events.sqlite"

# CSV inputs (used by --win-csv / --procmon-csv)
WIN_EVENTS_CSV="/opt/logs/windows_events.csv"
PROCMON_CSV="/opt/logs/procmon.csv"

# Common toggles
INGEST_SUMMARY=1       # 1=--ingest-summary
LEDGER_SCAN=1          # 1=--ledger-scan
DRY_RUN=0              # 1=--dry appended

# Common ledger thresholds (balanced)
LEDGER_SINCE=0         # minutes; 0 = all-time
LEDGER_MIN_TOTAL=500
LEDGER_MIN_SSH=10

# --------- PER-JOB PATHS ---------
FILE_SYSLOG="/var/log/syslog"               # RHEL: /var/log/messages
FILE_SECURE="/var/log/secure"
FILE_AUTH="/var/log/auth.log"
FILE_SSH="/var/log/sshd/sshd.log"
FILE_DMESG="/var/log/dmesg"
FILE_APACHE_ACCESS="/usr/local/apache/logs/access_log"
FILE_APACHE_ERROR="/usr/local/apache/logs/error_log"
FILE_EXIM="/var/log/exim_mainlog"

# --------- PER-JOB KNOBS (BALANCED DEFAULTS) ---------
# Syslog (generic)
WIN_SYSLOG=3000
SCORE_BLOCK_SYSLOG=8

# Secure/auth/ssh (SSH brute force)
WIN_SECURE=3000
SSH_FAIL_THRESH_SECURE=5
SSH_FAIL_SCORE_SECURE=2
SSH_FAIL_BONUS_SECURE=4
SCORE_BLOCK_SECURE=8

WIN_AUTH=3000
SSH_FAIL_THRESH_AUTH=5
SSH_FAIL_SCORE_AUTH=2
SSH_FAIL_BONUS_AUTH=4
SCORE_BLOCK_AUTH=8

WIN_SSH=3000
SSH_FAIL_THRESH_SSH=5
SSH_FAIL_SCORE_SSH=2
SSH_FAIL_BONUS_SSH=4
SCORE_BLOCK_SSH=8

# Auth strict (its own “job”)
PY_STRICT="/bin/python3.11"
WIN_AUTH_STRICT=120
SSH_FAIL_THRESH_AUTH_STRICT=3
SSH_FAIL_SCORE_AUTH_STRICT=3
SSH_FAIL_BONUS_AUTH_STRICT=8
SCORE_BLOCK_AUTH_STRICT=6
LEDGER_SINCE_AUTH_STRICT=2880
LEDGER_MIN_SSH_AUTH_STRICT=30
LEDGER_MIN_TOTAL_AUTH_STRICT=200
MAX_DECISIONS_AUTH_STRICT=500

# dmesg (ledger-only decisions)
WIN_DMESG=3000
SCORE_BLOCK_DMESG=8

# Apache access
WIN_APACHE_ACCESS=3000
SCORE_BLOCK_APACHE_ACCESS=8
WP_SCORE=5
SUSP_SCORE=4
BURST_404_THRESH=20
BURST_404_BONUS=10

# Apache error
WIN_APACHE_ERROR=3000
SCORE_BLOCK_APACHE_ERROR=8
APACHE_ERR_THRESH=8
APACHE_ERR_BONUS=8

# Exim (ledger-only decisions)
WIN_EXIM=3000
SCORE_BLOCK_EXIM=8

# Windows CSV (ledger-only decisions)
WIN_WINCSV=3000
SCORE_BLOCK_WINCSV=8

# Procmon CSV (ledger-only decisions)
WIN_PROCMON=3000
SCORE_BLOCK_PROCMON=8

# --------- PROFILE MODES ---------
MODE="balanced"       # balanced | aggressive | lenient

apply_mode() {
  case "$MODE" in
	aggressive)
	LEDGER_SINCE=2880          # 2 days
	LEDGER_MIN_TOTAL=200
	LEDGER_MIN_SSH=30
	WIN_SECURE=120;  SSH_FAIL_THRESH_SECURE=3; SSH_FAIL_SCORE_SECURE=3; SSH_FAIL_BONUS_SECURE=8; SCORE_BLOCK_SECURE=6
	WIN_AUTH=120;    SSH_FAIL_THRESH_AUTH=3;   SSH_FAIL_SCORE_AUTH=3;   SSH_FAIL_BONUS_AUTH=8;   SCORE_BLOCK_AUTH=6
	WIN_SSH=120;     SSH_FAIL_THRESH_SSH=3;    SSH_FAIL_SCORE_SSH=3;    SSH_FAIL_BONUS_SSH=8;    SCORE_BLOCK_SSH=6
	WIN_SYSLOG=600;  SCORE_BLOCK_SYSLOG=7
	WIN_APACHE_ACCESS=600; SCORE_BLOCK_APACHE_ACCESS=7; BURST_404_THRESH=15; BURST_404_BONUS=12; WP_SCORE=6; SUSP_SCORE=5
	WIN_APACHE_ERROR=600; SCORE_BLOCK_APACHE_ERROR=7; APACHE_ERR_THRESH=6; APACHE_ERR_BONUS=10
	;;
	lenient)
	LEDGER_SINCE=10080         # 7 days
	LEDGER_MIN_TOTAL=1000
	LEDGER_MIN_SSH=50
	WIN_SECURE=4320;  SSH_FAIL_THRESH_SECURE=7; SSH_FAIL_SCORE_SECURE=2; SSH_FAIL_BONUS_SECURE=4; SCORE_BLOCK_SECURE=10
	WIN_AUTH=4320;    SSH_FAIL_THRESH_AUTH=7;   SSH_FAIL_SCORE_AUTH=2;   SSH_FAIL_BONUS_AUTH=4;   SCORE_BLOCK_AUTH=10
	WIN_SSH=4320;     SSH_FAIL_THRESH_SSH=7;    SSH_FAIL_SCORE_SSH=2;    SSH_FAIL_BONUS_SSH=4;    SCORE_BLOCK_SSH=10
	WIN_SYSLOG=4320;  SCORE_BLOCK_SYSLOG=10
	WIN_APACHE_ACCESS=4320; SCORE_BLOCK_APACHE_ACCESS=10; BURST_404_THRESH=30; BURST_404_BONUS=8; WP_SCORE=4; SUSP_SCORE=3
	WIN_APACHE_ERROR=4320; SCORE_BLOCK_APACHE_ERROR=10; APACHE_ERR_THRESH=12; APACHE_ERR_BONUS=8
	;;
	balanced) ;; # already set by defaults above
	*) echo "Unknown --mode: $MODE" >&2; exit 2 ;;
  esac
}

# --------- HELP ---------
show_help() {
  cat >&2 <<USAGE
NAME
  run_all_fw.sh — Unified ThreatWeaver runner with profiles, per-knob overrides, and print-only mode

SYNOPSIS
  run_all_fw.sh [JOB ...] [--mode MODE] [--print-command] [--dry]
			[--set KEY=VALUE ...]
			[--python PATH] [--python-strict PATH]
			[--engine PATH] [--whitelist PATH] [--firewall NAME]
			[--ledger-db PATH] [--win-csv-path PATH] [--procmon-csv-path PATH]

DESCRIPTION
  Builds and runs (or prints) FirewallEngine.py commands for one or more log sources.
  Defaults (BALANCED profile) are declared as variables in this script.
  Use --mode to switch profiles and --set to override any variable inline.

JOBS
  --syslog         Parse generic syslog (${FILE_SYSLOG})
  --secure         Parse RHEL/Alma/CentOS secure log (${FILE_SECURE})
  --auth           Parse Debian/Ubuntu auth log (${FILE_AUTH})
  --auth-strict    Stricter variant of --auth with tighter windows/thresholds
  --ssh            Parse dedicated sshd log (${FILE_SSH})
  --dmesg          Ingest dmesg snapshot (${FILE_DMESG}) (ledger-only decisions)
  --apache-access  Parse Apache access_log (${FILE_APACHE_ACCESS}) (probes/404 heuristics)
  --apache-error   Parse Apache error_log (${FILE_APACHE_ERROR}) (client_ip error frequency)
  --exim           Parse Exim mainlog (${FILE_EXIM}) (ledger-only decisions)
  --win-csv        Ingest Windows Event CSV export (${WIN_EVENTS_CSV})
  --procmon-csv    Ingest Sysinternals ProcMon CSV export (${PROCMON_CSV})

PROFILES
  --mode balanced     Default best-practice baselines (current: ${MODE})
  --mode aggressive   Tighter windows & lower thresholds (more blocks, faster)
  --mode lenient      Wider windows & higher thresholds (fewer blocks, slower)

GLOBAL OVERRIDES
  --python PATH           Interpreter for standard jobs (default: ${PY})
  --python-strict PATH    Interpreter for strict job (default: ${PY_STRICT:-/bin/python3.11})
  --engine PATH           Path to FirewallEngine.py (default: ${ENGINE})
  --whitelist PATH        IP/CIDR allowlist file (default: ${WL})
  --firewall NAME         Backend (e.g., iptables|iptables|ufw|csf) (default: ${FW})
  --ledger-db PATH        Ingest/ledger SQLite path (default: ${LEDGER_DB})
  --win-csv-path PATH     Windows Events CSV (default: ${WIN_EVENTS_CSV})
  --procmon-csv-path PATH ProcMon CSV (default: ${PROCMON_CSV})

PER-KNOB OVERRIDES
  Use multiple --set KEY=VALUE entries to modify any variable in this script.
  Examples:
	--set WIN_AUTH=600 --set SSH_FAIL_THRESH_AUTH=4
	--set FW=iptables --set FILE_AUTH=/custom/auth.log
  Overrides apply AFTER --mode, so they always win.

PRINTING & DRY RUN
  --print-command    Print the exact FirewallEngine.py command(s) that would run, then exit
  --dry              Add --dry to each command to avoid applying firewall actions

EXAMPLES
  # Balanced auth job (run now)
  run_all_fw.sh --auth

  # Aggressive profile, print auth + apache-error commands (don’t run)
  run_all_fw.sh --mode aggressive --print-command --auth --apache-error

  # Tweak a couple knobs for auth and run
  run_all_fw.sh --auth --set WIN_AUTH=600 --set SSH_FAIL_THRESH_AUTH=4

  # Use plain iptables backend globally for this run
  run_all_fw.sh --auth --apache-access --set FW=iptables

EXIT STATUS
  0  success
  2  incorrect usage or unknown option
USAGE
}

# --------- UTIL: build common flag bundle ---------
USE_SQLITE=0   # set to 1 if you actually want DB

build_common_flags() {
  local -a out=()
  out+=( --whitelist-ip "$WL" )
  out+=( --firewall "$FW" )
  if [[ "$USE_SQLITE" -eq 1 ]]; then
	out+=( --ingest-events-sqlite "$LEDGER_DB" )
  fi
  [[ "$LEDGER_SCAN" -eq 1 ]] && out+=( --ledger-scan )
  out+=( --ledger-since-min "$LEDGER_SINCE" )
  [[ "$INGEST_SUMMARY" -eq 1 ]] && out+=( --ingest-summary )
  [[ "$DRY_RUN" -eq 1 ]] && out+=( --dry )
  echo "${out[@]}"
}


# --------- BUILDERS (echo a full command for print/run) ---------
cmd_syslog()        { echo "$PY $ENGINE --file $FILE_SYSLOG --log-type syslog --window-min $WIN_SYSLOG --score-block $SCORE_BLOCK_SYSLOG $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_secure()        { echo "$PY $ENGINE --file $FILE_SECURE --log-type secure --window-min $WIN_SECURE --ssh-fail-thresh $SSH_FAIL_THRESH_SECURE --ssh-fail-score $SSH_FAIL_SCORE_SECURE --ssh-fail-bonus $SSH_FAIL_BONUS_SECURE --score-block $SCORE_BLOCK_SECURE $(build_common_flags) --ledger-min-ssh $LEDGER_MIN_SSH --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_auth()          { echo "$PY $ENGINE --file $FILE_AUTH --log-type auth --window-min $WIN_AUTH --ssh-fail-thresh $SSH_FAIL_THRESH_AUTH --ssh-fail-score $SSH_FAIL_SCORE_AUTH --ssh-fail-bonus $SSH_FAIL_BONUS_AUTH --score-block $SCORE_BLOCK_AUTH $(build_common_flags) --ledger-min-ssh $LEDGER_MIN_SSH --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_auth_strict()   {
  local ls="${LEDGER_SINCE_AUTH_STRICT:-$LEDGER_SINCE}"
  local lssh="${LEDGER_MIN_SSH_AUTH_STRICT:-$LEDGER_MIN_SSH}"
  local ltot="${LEDGER_MIN_TOTAL_AUTH_STRICT:-$LEDGER_MIN_TOTAL}"
  local maxd="${MAX_DECISIONS_AUTH_STRICT:-500}"
  echo "$PY_STRICT $ENGINE --file $FILE_AUTH --log-type auth --window-min $WIN_AUTH_STRICT --ssh-fail-thresh $SSH_FAIL_THRESH_AUTH_STRICT --ssh-fail-score $SSH_FAIL_SCORE_AUTH_STRICT --ssh-fail-bonus $SSH_FAIL_BONUS_AUTH_STRICT --score-block $SCORE_BLOCK_AUTH_STRICT $(build_common_flags) --ledger-since-min $ls --ledger-min-ssh $lssh --ledger-min-total $ltot --max-decisions $maxd"
}
cmd_ssh()           { echo "$PY $ENGINE --file $FILE_SSH --log-type ssh --window-min $WIN_SSH --ssh-fail-thresh $SSH_FAIL_THRESH_SSH --ssh-fail-score $SSH_FAIL_SCORE_SSH --ssh-fail-bonus $SSH_FAIL_BONUS_SSH --score-block $SCORE_BLOCK_SSH $(build_common_flags) --ledger-min-ssh $LEDGER_MIN_SSH --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_dmesg()         { echo "$PY $ENGINE --file $FILE_DMESG --log-type dmesg --window-min $WIN_DMESG --score-block $SCORE_BLOCK_DMESG $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_apache_access() { echo "$PY $ENGINE --file $FILE_APACHE_ACCESS --log-type apache_access --window-min $WIN_APACHE_ACCESS --score-block $SCORE_BLOCK_APACHE_ACCESS --wp-score $WP_SCORE --susp-score $SUSP_SCORE --burst-404-thresh $BURST_404_THRESH --burst-404-bonus $BURST_404_BONUS $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_apache_error()  { echo "$PY $ENGINE --file $FILE_APACHE_ERROR --log-type apache_error --window-min $WIN_APACHE_ERROR --score-block $SCORE_BLOCK_APACHE_ERROR --apache-err-thresh $APACHE_ERR_THRESH --apache-err-bonus $APACHE_ERR_BONUS $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_exim()          { echo "$PY $ENGINE --file $FILE_EXIM --log-type exim_mail --window-min $WIN_EXIM --score-block $SCORE_BLOCK_EXIM $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_win_csv()       { echo "$PY $ENGINE --file $WIN_EVENTS_CSV --log-type windows_event --window-min $WIN_WINCSV --score-block $SCORE_BLOCK_WINCSV $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }
cmd_procmon_csv()   { echo "$PY $ENGINE --file $PROCMON_CSV --log-type procmon --window-min $WIN_PROCMON --score-block $SCORE_BLOCK_PROCMON $(build_common_flags) --ledger-min-total $LEDGER_MIN_TOTAL"; }

# --------- ARG PARSING ---------
PRINT_ONLY=0
JOBS=()
OVERRIDES=()

while (( "$#" )); do
  case "$1" in
	# Help
	--help|-h) show_help; exit 0 ;;
	# Job selectors (you can pass multiple)
	--syslog|--secure|--auth|--auth-strict|--ssh|--dmesg|--apache-access|--apache-error|--exim|--win-csv|--procmon-csv)
	JOBS+=("$1"); shift ;;
	# Profiles
	--mode) MODE="${2:-}"; shift 2 ;;
	--mode=*) MODE="${1#*=}"; shift ;;
	# Print instead of run
	--print-command) PRINT_ONLY=1; shift ;;
	# Dry-run (passes --dry to FirewallEngine)
	--dry) DRY_RUN=1; shift ;;
	# Generic per-knob overrides: --set KEY=VALUE (repeat as needed)
	--set) OVERRIDES+=("${2:-}"); shift 2 ;;
	--set=*) OVERRIDES+=("${1#*=}"); shift ;;
	# Convenience overrides for common globals
	--python) PY="${2:-}"; shift 2 ;;
	--python=*) PY="${1#*=}"; shift ;;
	--python-strict) PY_STRICT="${2:-}"; shift 2 ;;
	--python-strict=*) PY_STRICT="${1#*=}"; shift ;;
	--engine) ENGINE="${2:-}"; shift 2 ;;
	--engine=*) ENGINE="${1#*=}"; shift ;;
	--whitelist) WL="${2:-}"; shift 2 ;;
	--whitelist=*) WL="${1#*=}"; shift ;;
	--firewall) FW="${2:-}"; shift 2 ;;
	--firewall=*) FW="${1#*=}"; shift ;;
	--ledger-db) LEDGER_DB="${2:-}"; shift 2 ;;
	--ledger-db=*) LEDGER_DB="${1#*=}"; shift ;;
	--win-csv-path) WIN_EVENTS_CSV="${2:-}"; shift 2 ;;
	--win-csv-path=*) WIN_EVENTS_CSV="${1#*=}"; shift ;;
	--procmon-csv-path) PROCMON_CSV="${2:-}"; shift 2 ;;
	--procmon-csv-path=*) PROCMON_CSV="${1#*=}"; shift ;;
	--) shift; break ;;
	-*)
	echo "Unknown option: $1" >&2; exit 2 ;;
	*)
	echo "Unexpected argument: $1" >&2; exit 2 ;;
  esac
done

# Apply profile mode first
apply_mode

# Apply explicit overrides next (only if any were provided)
if ((${#OVERRIDES[@]})); then
  for kv in "${OVERRIDES[@]}"; do
	# Require KEY=VALUE form
	if [[ -z "$kv" || "$kv" != *=* ]]; then
	echo "--set requires KEY=VALUE (got '${kv:-}')" >&2
	exit 2
	fi
	key="${kv%%=*}"
	val="${kv#*=}"

	# Allow only safe variable names
	if [[ ! "$key" =~ ^[A-Za-z_][A-Za-z0-9_]*$ ]]; then
	echo "--set invalid key name: '$key' (use letters, digits, underscore; not starting with a digit)" >&2
	exit 2
	fi

	# Assign without eval
	printf -v "$key" '%s' "$val"
  done
fi


# If no jobs specified, show help
if [[ "${#JOBS[@]}" -eq 0 ]]; then
  show_help
  exit 2
fi

# Dispatch: print or run each selected job
for j in "${JOBS[@]}"; do
  case "$j" in
	--syslog)        cmd=$(cmd_syslog) ;;
	--secure)        cmd=$(cmd_secure) ;;
	--auth)          cmd=$(cmd_auth) ;;
	--auth-strict)   cmd=$(cmd_auth_strict) ;;
	--ssh)           cmd=$(cmd_ssh) ;;
	--dmesg)         cmd=$(cmd_dmesg) ;;
	--apache-access) cmd=$(cmd_apache_access) ;;
	--apache-error)  cmd=$(cmd_apache_error) ;;
	--exim)          cmd=$(cmd_exim) ;;
	--win-csv)       cmd=$(cmd_win_csv) ;;
	--procmon-csv)   cmd=$(cmd_procmon_csv) ;;
  esac

  if [[ "$PRINT_ONLY" -eq 1 ]]; then
	echo "$cmd"
  else
	echo "+ $cmd"
	eval "$cmd"
  fi
done


# # RHEL/Alma/CentOS secure log (every 5m)
# */5 * * * * /opt/ThreatWeaver/run_all_fw.sh --secure

# # Debian/Ubuntu auth.log (every 5m)
# */5 * * * * /opt/ThreatWeaver/run_all_fw.sh --auth

# # Apache access (cPanel) (every 10m)
# */10 * * * * /opt/ThreatWeaver/run_all_fw.sh --apache-access

# # Apache error (cPanel) (every 10m)
# */10 * * * * /opt/ThreatWeaver/run_all_fw.sh --apache-error

# ./run_all_fw.sh     --set USE_SQLITE=0     --python /bin/python3.11     --engine /opt/ThreatWeaver/FirewallEngine.py     --secure