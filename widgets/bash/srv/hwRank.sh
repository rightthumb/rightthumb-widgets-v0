#!/usr/bin/env bash
# hwRank.sh — Server stats + performance score & rank (fixed)
# Usage:
#   bash ./hwRank.sh [--quick] [--no-network] [--no-fio] [--disk DEV|PATH] [--json]

set -euo pipefail

# -----------------------------------
# Config (weights & thresholds)
# -----------------------------------
WEIGHT_CPU=0.35
WEIGHT_RAM=0.20
WEIGHT_DISK=0.30
WEIGHT_NET=0.10
WEIGHT_HEALTH=0.05

RANK_A=85
RANK_B=70
RANK_C=55
RANK_D=40

DISK_TARGET=""
DO_NETWORK=1
DO_FIO=1
QUICK=0
OUTPUT_JSON=0

# -----------------------------------
# CLI
# -----------------------------------
while [[ ${#} -gt 0 ]]; do
	case "$1" in
		--disk) DISK_TARGET="${2:-}"; shift 2 ;;
		--no-network) DO_NETWORK=0; shift ;;
		--no-fio) DO_FIO=0; shift ;;
		--quick) QUICK=1; shift ;;
		--json) OUTPUT_JSON=1; shift ;;
		-h|--help)
			echo "hwRank.sh - server stats + performance score"
			echo "Options:"
			echo "  --disk DEV|PATH   Disk device (/dev/nvme0n1) or mount path (/) to test"
			echo "  --quick           Faster, shorter tests"
			echo "  --no-network      Skip speed test"
			echo "  --no-fio          Skip fio random IOPS test"
			echo "  --json            JSON output"
			exit 0
			;;
		*) echo "Unknown option: $1" >&2; exit 1 ;;
	esac
done

# -----------------------------------
# Helpers
# -----------------------------------
has() { command -v "$1" >/dev/null 2>&1; }
jescape() { sed -E 's/\\/\\\\/g; s/"/\\"/g'; } # naive json escape

WORKDIR="$(mktemp -d)"; trap 'rm -rf "$WORKDIR"' EXIT

resolve_disk_target() { [[ -n "${1:-}" ]] && echo "$1" || echo "/"; }
path_to_device() {
	local p="$1"
	if [[ "$p" == /dev/* ]]; then echo "$p"; return; fi
	df -P "$p" 2>/dev/null | awk 'NR==2{print $1}'
}

# -----------------------------------
# CPU
# -----------------------------------
CPU_MODEL="$(awk -F: '/model name/ {sub(/^ +/,"",$2); print $2; exit}' /proc/cpuinfo 2>/dev/null || echo "Unknown")"
CPU_CORES="$(nproc 2>/dev/null || echo 1)"
CPU_MHZ="$(awk -F: '/cpu MHz/ {sub(/^ +/,"",$2); mhz=$2} END{print (mhz=="")?0:int(mhz)}' /proc/cpuinfo 2>/dev/null || echo 0)"
if [[ "${CPU_MHZ:-0}" -eq 0 ]] && has lscpu; then
	CPU_MHZ="$(lscpu | awk -F: '/CPU max MHz/ {sub(/^ +/,"",$2); print int($2)}')"
fi
[[ -z "${CPU_MHZ:-}" || "${CPU_MHZ:-0}" -eq 0 ]] && CPU_MHZ=2000

CPU_SCORE_RAW=$(awk -v c="$CPU_CORES" -v m="$CPU_MHZ" 'BEGIN{print c*(m/1000.0)}')
CPU_SCORE=$(awk -v s="$CPU_SCORE_RAW" 'BEGIN{max=224.0; n=s/max*100; if(n>100)n=100; if(n<0)n=0; printf "%.1f", n}')

# -----------------------------------
# RAM
# -----------------------------------
MEM_TOTAL_KB="$(awk '/MemTotal/ {print $2}' /proc/meminfo 2>/dev/null || echo 0)"
MEM_TOTAL_GB=$(awk -v k="${MEM_TOTAL_KB:-0}" 'BEGIN{printf "%.2f", k/1024/1024}')
RAM_SCORE=$(awk -v g="$MEM_TOTAL_GB" 'BEGIN{n=(g/128.0)*100; if(n>100)n=100; if(n<0)n=0; printf "%.1f", n}')

# -----------------------------------
# Load & disk usage (health penalties)
# -----------------------------------
LOAD_1="$(awk '{print $1}' /proc/loadavg 2>/dev/null || echo 0)"
LOAD_PER_CORE=$(awk -v l="$LOAD_1" -v c="$CPU_CORES" 'BEGIN{if(c==0)c=1; printf "%.2f", l/c}')
# No awk min(): clamp with if
HEALTH_PENALTY_LOAD=$(awk -v lpc="$LOAD_PER_CORE" 'BEGIN{
	p = (lpc>1.0) ? ((lpc-1.0)*20.0) : 0;
	if (p>20) p=20;
	printf "%.1f", p
}')
ROOT_USE_PCT="$(df -P / | awk 'NR==2{gsub("%","",$5); print $5}')"
HEALTH_PENALTY_DISK=$(awk -v u="${ROOT_USE_PCT:-0}" 'BEGIN{
	p = (u>90) ? (u-90)*1.5 : 0;
	if (p>10) p=10;
	printf "%.1f", p
}')

# -----------------------------------
# DISK throughput & IOPS
# -----------------------------------
TARGET_PATH="$(resolve_disk_target "$DISK_TARGET")"
TARGET_DEV="$(path_to_device "$TARGET_PATH")"

DISK_READ_MBPS=0
DISK_WRITE_MBPS=0
DISK_RAND_IOPS=0

# Prefer hdparm for read if device
if [[ -n "${TARGET_DEV:-}" && "$TARGET_DEV" == /dev/* && $(id -u) -eq 0 && $(has hdparm; echo $?) -eq 0 ]]; then
	HDOUT="$(hdparm -t "$TARGET_DEV" 2>/dev/null || true)"
	# "...= 2355.53 MB/sec"
	HD_MBPS="$(echo "$HDOUT" | awk '/buffered disk reads/ {print $(NF-1)}')"
	if [[ -n "${HD_MBPS:-}" ]]; then DISK_READ_MBPS="$(printf "%.0f" "$HD_MBPS")"; fi
fi

TEST_SIZE_MB=$([[ "$QUICK" -eq 1 ]] && echo 256 || echo 1024)
TESTFILE="$WORKDIR/io_test.bin"

# dd write (try direct I/O)
WRITE_CMD=(dd if=/dev/zero of="$TESTFILE" bs=1M count="$TEST_SIZE_MB" conv=fdatasync)
if dd if=/dev/zero of="$TESTFILE".probe bs=1M count=1 oflag=direct conv=fdatasync >/dev/null 2>&1; then
	WRITE_CMD=(dd if=/dev/zero of="$TESTFILE" bs=1M count="$TEST_SIZE_MB" oflag=direct conv=fdatasync)
fi
DDW="$("${WRITE_CMD[@]}" 2>&1 || true)"
# Parse "... copied, ... s, 123 MB/s" (also handles kB/s, GB/s)
parse_rate_to_MBps() {
	awk -F, '/copied/{
		rate=$NF; gsub(/[[:space:]]/,"",rate)
		if (rate ~ /GB\/s$/){ sub(/GB\/s/,"",rate); printf "%.0f\n", rate*1024; next }
		if (rate ~ /MB\/s$/){ sub(/MB\/s/,"",rate); printf "%.0f\n", rate; next }
		if (rate ~ /kB\/s$/){ sub(/kB\/s/,"",rate); printf "%.0f\n", rate/1024; next }
		print 0
	}'
}
DDW_MBPS="$(echo "$DDW" | parse_rate_to_MBps || echo 0)"
DISK_WRITE_MBPS="${DDW_MBPS:-0}"

# dd read (direct if possible)
DDR="$(dd if="$TESTFILE" of=/dev/null bs=4M iflag=direct 2>&1 || true)"
DDR_MBPS="$(echo "$DDR" | parse_rate_to_MBps || echo 0)"
if [[ ${DDR_MBPS:-0} -gt ${DISK_READ_MBPS:-0} ]]; then
	DISK_READ_MBPS="$DDR_MBPS"
fi

# fio random IOPS
if [[ "$DO_FIO" -eq 1 && $(id -u) -eq 0 && $(has fio; echo $?) -eq 0 ]]; then
	FIO_TIME=$([[ "$QUICK" -eq 1 ]] && echo 4 || echo 8)
	FIO_OUT="$(fio --name=randmix --rw=randrw --rwmixread=50 --bs=4k --iodepth=16 --numjobs=1 \
		--size=$((TEST_SIZE_MB/2))m --time_based=1 --runtime="$FIO_TIME" \
		--filename="$TESTFILE.fio" --direct=1 --group_reporting 2>/dev/null || true)"
	DISK_RAND_IOPS="$(echo "$FIO_OUT" | awk -F'[:, ]+' '
		/IOPS=/ { for(i=1;i<=NF;i++) if ($i ~ /IOPS=/){gsub(/IOPS=/,"",$i); val=$i} }
		END{printf "%d", (val=="")?0:val}
	')"
fi

# Disk score
DISK_TP_AVG=$(awk -v r="${DISK_READ_MBPS:-0}" -v w="${DISK_WRITE_MBPS:-0}" 'BEGIN{print (r+w)/2.0}')
DISK_TP_SCORE=$(awk -v a="$DISK_TP_AVG" 'BEGIN{n=(a/1000.0)*100; if(n>100)n=100; if(n<0)n=0; printf "%.1f", n}')
if [[ ${DISK_RAND_IOPS:-0} -gt 0 ]]; then
	DISK_IOPS_SCORE=$(awk -v i="$DISK_RAND_IOPS" 'BEGIN{n=(i/100000.0)*100; if(n>100)n=100; if(n<0)n=0; printf "%.1f", n}')
	DISK_SCORE=$(awk -v t="$DISK_TP_SCORE" -v io="$DISK_IOPS_SCORE" 'BEGIN{printf "%.1f", (t*0.6 + io*0.4)}')
else
	DISK_SCORE="$DISK_TP_SCORE"
fi

# -----------------------------------
# Network
# -----------------------------------
NET_DOWN_Mbps=0
NET_UP_Mbps=0
NET_LAT_ms=0
if [[ "$DO_NETWORK" -eq 1 ]]; then
	if has speedtest; then
		STOUT="$(speedtest --accept-license --accept-gdpr -f json 2>/dev/null || true)"
		if [[ -n "${STOUT:-}" ]]; then
			bw_down="$(echo "$STOUT" | sed -n 's/.*"download":{[^}]*"bandwidth":[ ]*\([0-9]*\).*/\1/p' | head -n1)"
			bw_up="$(echo "$STOUT"   | sed -n 's/.*"upload":{[^}]*"bandwidth":[ ]*\([0-9]*\).*/\1/p' | head -n1)"
			lat="$(echo "$STOUT"     | sed -n 's/.*"latency":[ ]*{[^}]*"low":[ ]*\([0-9.]*\).*/\1/p' | head -n1)"
			[[ -n "${bw_down:-}" && "${bw_down:-0}" -gt 0 ]] && NET_DOWN_Mbps="$(awk -v b="$bw_down" 'BEGIN{printf "%.0f",(b*8)/1e6}')"
			[[ -n "${bw_up:-}"   && "${bw_up:-0}"   -gt 0 ]] && NET_UP_Mbps="$(awk -v b="$bw_up"   'BEGIN{printf "%.0f",(b*8)/1e6}')"
			NET_LAT_ms="${lat:-0}"
		fi
	elif has speedtest-cli; then
		STOUT="$(speedtest-cli --simple 2>/dev/null || true)"
		NET_DOWN_Mbps="$(echo "$STOUT" | awk '/Download/ {print int($2)}')"
		NET_UP_Mbps="$(echo "$STOUT"   | awk '/Upload/   {print int($2)}')"
		NET_LAT_ms="$(echo "$STOUT"    | awk '/Ping/     {print int($2)}')"
	fi
fi

if [[ ${NET_DOWN_Mbps:-0} -gt 0 ]]; then
	NET_SCORE=$(awk -v d="$NET_DOWN_Mbps" -v u="$NET_UP_Mbps" -v lat="$NET_LAT_ms" 'BEGIN{
		n=(d/1000.0)*80 + (u/1000.0)*20; if(n>100)n=100;
		if(lat>0 && lat<10) n+=5; if(n>100)n=100;
		printf "%.1f", n
	}')
else
	NET_SCORE="0.0"
fi

# -----------------------------------
# Score & Rank
# -----------------------------------
HEALTH_PENALTY=$(awk -v a="$HEALTH_PENALTY_LOAD" -v b="$HEALTH_PENALTY_DISK" 'BEGIN{
	p=a+b; if(p>25)p=25; if(p<0)p=0; printf "%.1f", p
}')
TOTAL_SCORE=$(awk -v cpu="$CPU_SCORE" -v ram="$RAM_SCORE" -v disk="$DISK_SCORE" -v net="$NET_SCORE" \
	-v wcpu="$WEIGHT_CPU" -v wram="$WEIGHT_RAM" -v wdisk="$WEIGHT_DISK" -v wnet="$WEIGHT_NET" -v whealth="$WEIGHT_HEALTH" \
	-v pen="$HEALTH_PENALTY" 'BEGIN{
		base = cpu*wcpu + ram*wram + disk*wdisk + net*wnet;
		total = base - (pen * whealth);
		if(total<0) total=0; if(total>100) total=100;
		printf "%.1f", total
	}')

RANK="F"
sc="$(printf "%.0f" "${TOTAL_SCORE%.*}")"
if   [[ $sc -ge $RANK_A ]]; then RANK="A"
elif [[ $sc -ge $RANK_B ]]; then RANK="B"
elif [[ $sc -ge $RANK_C ]]; then RANK="C"
elif [[ $sc -ge $RANK_D ]]; then RANK="D"
fi

# -----------------------------------
# Output
# -----------------------------------
HOSTNAME_STR="$(hostname 2>/dev/null || echo unknown)"
UPTIME_STR="$(uptime -p 2>/dev/null || true)"
KERNEL_STR="$(uname -r 2>/dev/null || echo unknown)"
ROOT_USED_H="$(df -h / | awk 'NR==2{print $5" used of "$2" on /"}')"

if [[ "$OUTPUT_JSON" -eq 1 ]]; then
	cat <<JSON
{
	"host": "$(echo "$HOSTNAME_STR" | jescape)",
	"kernel": "$(echo "$KERNEL_STR" | jescape)",
	"uptime_pretty": "$(echo "$UPTIME_STR" | jescape)",
	"cpu": {"model":"$(echo "$CPU_MODEL" | jescape)","cores":$CPU_CORES,"mhz":$CPU_MHZ,"score":$CPU_SCORE},
	"memory": {"total_gb":$MEM_TOTAL_GB,"score":$RAM_SCORE},
	"disk": {"target_path":"$(echo "$TARGET_PATH" | jescape)","device":"$(echo "$TARGET_DEV" | jescape)","read_MBps":${DISK_READ_MBPS:-0},"write_MBps":${DISK_WRITE_MBPS:-0},"rand_iops":${DISK_RAND_IOPS:-0},"score":$DISK_SCORE},
	"network": {"download_Mbps":${NET_DOWN_Mbps:-0},"upload_Mbps":${NET_UP_Mbps:-0},"latency_ms":${NET_LAT_ms:-0},"score":$NET_SCORE},
	"health": {"root_usage_pct":${ROOT_USE_PCT:-0},"load_1":$LOAD_1,"load_per_core":$LOAD_PER_CORE,"penalty":$HEALTH_PENALTY},
	"weights": {"cpu":$WEIGHT_CPU,"ram":$WEIGHT_RAM,"disk":$WEIGHT_DISK,"network":$WEIGHT_NET,"health":$WEIGHT_HEALTH},
	"score_total": $TOTAL_SCORE,
	"rank": "$RANK",
	"notes": "Install hdparm/fio/speedtest for richer tests. Use --quick to shorten."
}
JSON
	exit 0
fi

printf "\n== Server Scorecard: %s ==\n" "$HOSTNAME_STR"
printf "Kernel: %s | %s\n" "$KERNEL_STR" "${UPTIME_STR:-uptime N/A}"
printf "Root FS: %s\n\n" "$ROOT_USED_H"

printf "CPU    : %-45s  Cores: %-3d  MHz: %-5d  Score: %5.1f\n" "$CPU_MODEL" "$CPU_CORES" "$CPU_MHZ" "$CPU_SCORE"
printf "Memory : Total: %6.2f GB                                   Score: %5.1f\n" "$MEM_TOTAL_GB" "$RAM_SCORE"
printf "Disk   : Target: %-18s Device: %-14s\n" "$TARGET_PATH" "${TARGET_DEV:-unknown}"
printf "         Read: %5d MB/s   Write: %5d MB/s   Rand IOPS: %7d   Score: %5.1f\n" "${DISK_READ_MBPS:-0}" "${DISK_WRITE_MBPS:-0}" "${DISK_RAND_IOPS:-0}" "$DISK_SCORE"

if [[ "$DO_NETWORK" -eq 1 ]]; then
	if [[ ${NET_DOWN_Mbps:-0} -gt 0 ]]; then
		printf "Network: Down: %5d Mbps   Up: %5d Mbps   Lat: %4d ms       Score: %5.1f\n" "$NET_DOWN_Mbps" "$NET_UP_Mbps" "$NET_LAT_ms" "$NET_SCORE"
	else
		printf "Network: (speedtest not available or skipped)              Score: %5.1f\n" "$NET_SCORE"
	fi
else
	printf "Network: (skipped by --no-network)\n"
fi

printf "Health : Root Used: %2d%%   Load1: %.2f (per-core: %.2f)   Penalty: %4.1f\n" "${ROOT_USE_PCT:-0}" "$LOAD_1" "$LOAD_PER_CORE" "$HEALTH_PENALTY"
printf "\nTOTAL  : %5.1f / 100   Rank: %s\n\n" "$TOTAL_SCORE" "$RANK"
printf "Tips   : Install 'hdparm', 'fio', and 'speedtest' (or 'speedtest-cli'). Use '--disk /dev/nvme0n1'. 'sudo' improves accuracy.\n\n"