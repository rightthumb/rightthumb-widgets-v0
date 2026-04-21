#!/usr/bin/env bash
# log_established.sh
# Continuously log ESTABLISHED TCP connections without duplicates,
# plus an optional extended per-process log.
#
# Usage:
#   sudo bash log_established.sh                  # basic log only
#   sudo bash log_established.sh -x               # also write extended log
#   sudo bash log_established.sh -i 10 -d /var/log/established --extended

set -euo pipefail

# -----------------------------
# Defaults & CLI parsing
# -----------------------------
LOGDIR="/opt/established"
INTERVAL=30
EXTENDED=0

print_help() {
	cat <<'EOF'
Usage: log_established.sh [options]

Options:
  -d, --dir DIR         Log directory (default: /opt/established)
  -i, --interval SEC    Poll interval in seconds (default: 30)
  -x, --extended        Also write extended.log with process details
  -h, --help            Show this help
EOF
}

while [[ $# -gt 0 ]]; do
	case "$1" in
		-d|--dir) LOGDIR="${2:-}"; shift 2 ;;
		-i|--interval) INTERVAL="${2:-}"; shift 2 ;;
		-x|--extended) EXTENDED=1; shift ;;
		-h|--help) print_help; exit 0 ;;
		*) echo "Unknown option: $1" >&2; print_help; exit 1 ;;
	esac
done

# -----------------------------
# Paths & setup
# -----------------------------
mkdir -p "$LOGDIR"
LOGFILE="$LOGDIR/established.log"
TMPFILE="$LOGDIR/_established.tmp"
NEWFILE="$LOGDIR/_established.new"
EXTLOG="$LOGDIR/extended.log"

cleanup() { rm -f "$NEWFILE" 2>/dev/null || true; }
trap cleanup EXIT INT TERM

: > "$LOGFILE"
: > "$TMPFILE"
[[ $EXTENDED -eq 1 ]] && : > "$EXTLOG"

echo "Starting established connections logger..."
echo "  Log dir      : $LOGDIR"
echo "  Base log     : $LOGFILE"
[[ $EXTENDED -eq 1 ]] && echo "  Extended log : $EXTLOG"
echo "  Interval     : ${INTERVAL}s"
echo "Press Ctrl+C to stop."

# -----------------------------
# Helpers
# -----------------------------

# get_established() -> writes normalized lines to $NEWFILE
# Normalized format (tab-delimited):
#   PROTO\tLADDR\tLPORT\tRADDR\tRPORT\tSTATE\tPID\tPROG
get_established() {
	netstat -tulanp 2>/dev/null \
	| awk '$6=="ESTABLISHED" {print}' \
	| awk '
		function splitHostPort(addr, host, port) {
			if (addr ~ /^\[/) {
				host = addr
				gsub(/^\[|\](:[0-9]+)?$/, "", host)
				sub(/^\[[^]]+\]:/, "", addr)
				port = addr
			} else {
				n = split(addr, arr, ":")
				if (n > 1) {
					port = arr[n]
					host = arr[1]
					for (i=2; i<n; i++) host = host ":" arr[i]
				} else {
					host = addr
					port = ""
				}
			}
			return host "\t" port
		}
		{
			proto=$1; l=$4; r=$5; state=$6; pidprog=$7
			pid=""; prog="-"
			if (pidprog ~ /^[0-9]+\//) {
				split(pidprog, pp, "/"); pid=pp[1]; prog=pp[2]
			} else if (pidprog ~ /^[0-9]+$/) {
				pid=pidprog
			} else { pid="-"; prog="-"; }

			lhp = splitHostPort(l, lh, lp)
			rhp = splitHostPort(r, rh, rp)
			split(lhp, la, "\t"); split(rhp, ra, "\t")
			lh = la[1]; lp = la[2]; rh = ra[1]; rp = ra[2]
			if (lp=="") lp="-"; if (rp=="") rp="-"

			print proto "\t" lh "\t" lp "\t" rh "\t" rp "\t" state "\t" pid "\t" prog
		}
	' | sort -u > "$NEWFILE"
}

write_base_log() {
	local ts="$1"; shift
	local rec="$*"
	IFS=$'\t' read -r PROTO LADDR LPORT RADDR RPORT STATE PID PROG <<< "$rec"
	echo "[$ts] $PROTO $LADDR:$LPORT -> $RADDR:$RPORT $STATE pid=$PID prog=$PROG" >> "$LOGFILE"
}

# Extended info collector for a given PID (set -u safe)
write_extended_log() {
	local ts="$1"; shift
	local PROTO="$1" LADDR="$2" LPORT="$3" RADDR="$4" RPORT="$5" STATE="$6" PID_VAL="$7" PROG_VAL="$8"

	# Pre-initialize all vars
	local PROC_USER="" PROC_PPID="" PROC_CPU="" PROC_MEM="" PROC_START="" PROC_CMD=""

	if [[ "$PID_VAL" != "-" && "$PID_VAL" =~ ^[0-9]+$ ]]; then
		PROC_USER="$(ps -o user=    -p "$PID_VAL" 2>/dev/null || true)"
		PROC_PPID="$(ps -o ppid=    -p "$PID_VAL" 2>/dev/null || true)"
		PROC_CPU="$(ps -o %cpu=     -p "$PID_VAL" 2>/dev/null || true)"
		PROC_MEM="$(ps -o %mem=     -p "$PID_VAL" 2>/dev/null || true)"
		PROC_START="$(ps -o lstart= -p "$PID_VAL" 2>/dev/null || true)"
		if [[ -r "/proc/$PID_VAL/cmdline" ]]; then
			PROC_CMD="$(tr '\0' ' ' < "/proc/$PID_VAL/cmdline" 2>/dev/null || true)"
		fi

		[[ -z "${PROC_CMD}"  ]] && PROC_CMD="$PROG_VAL"
		[[ -z "${PROC_USER}" ]] && PROC_USER="-"
		[[ -z "${PROC_PPID}" ]] && PROC_PPID="-"
		[[ -z "${PROC_CPU}"  ]] && PROC_CPU="-"
		[[ -z "${PROC_MEM}"  ]] && PROC_MEM="-"
		[[ -z "${PROC_START}" ]] && PROC_START="-"

		echo "[$ts] $PROTO $LADDR:$LPORT -> $RADDR:$RPORT $STATE pid=$PID_VAL prog=$PROG_VAL user=$PROC_USER ppid=$PROC_PPID cpu=${PROC_CPU}% mem=${PROC_MEM}% start=\"$PROC_START\" cmd=\"$PROC_CMD\"" \
			>> "$EXTLOG"
	else
		echo "[$ts] $PROTO $LADDR:$LPORT -> $RADDR:$RPORT $STATE pid=$PID_VAL prog=$PROG_VAL (no PID info available)" \
			>> "$EXTLOG"
	fi
}

# -----------------------------
# Main loop
# -----------------------------
while true; do
	TIMESTAMP="$(date '+%Y-%m-%d %H:%M:%S')"

	get_established

	if [[ -s "$NEWFILE" ]]; then
		comm -13 "$TMPFILE" "$NEWFILE" | while IFS= read -r rec; do
			write_base_log "$TIMESTAMP" "$rec"
			if [[ $EXTENDED -eq 1 ]]; then
				IFS=$'\t' read -r PROTO LADDR LPORT RADDR RPORT STATE PID PROG <<< "$rec"
				write_extended_log "$TIMESTAMP" "$PROTO" "$LADDR" "$LPORT" "$RADDR" "$RPORT" "$STATE" "$PID" "$PROG"
			fi
		done
	fi

	mv -f "$NEWFILE" "$TMPFILE"
	sleep "$INTERVAL"
done