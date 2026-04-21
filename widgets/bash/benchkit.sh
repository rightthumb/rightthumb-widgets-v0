#!/usr/bin/env bash
set -euo pipefail



################################################################################
#
#  BenchKit (Linux) - Modular benchmark runner you can scavenge from later
#
#  Goals:
#   - incredibly modular
#   - registries for installers + git repos
#   - JSON output
#   - HTML report with charts (Chart.js)
#   - safe defaults (no raw /dev writes, only file-based tests)
#
#
#  Examples:
#
#    ./benchkit.sh --all
#
#    sudo ./benchkit.sh --install --all
#
#    sudo ./benchkit.sh --install --usb /media/usb
#
#    ./benchkit.sh --only cpu,memory,nics
#
#    ./benchkit.sh --skip internet
#
#    ./benchkit.sh --git-setup        # clones tools into ./tools/git/
#
################################################################################






################################################################################
#
#  Parent Section: Globals / Paths
#
################################################################################

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

RUN_ID="$(date +%F_%H%M%S)"
OUT_DIR="${ROOT_DIR}/out/runs/${RUN_ID}"

TOOLS_DIR="${ROOT_DIR}/tools"
TOOLS_GIT_DIR="${TOOLS_DIR}/git"

mkdir -p "${OUT_DIR}"
mkdir -p "${OUT_DIR}/graphs"
mkdir -p "${TOOLS_GIT_DIR}"



SIZE_MB_DEFAULT=1024
SIZE_MB="${SIZE_MB_DEFAULT}"

USB_PATH=""




################################################################################
#
#  Parent Section: CLI Switches
#
################################################################################

DO_INSTALL=0
DO_GIT_SETUP=0

DO_ALL=0

DO_INVENTORY=0
DO_CPU=0
DO_MEMORY=0
DO_DISKS=0
DO_USB=0
DO_NICS=0
DO_INTERNET=0
DO_SMART=0
DO_STRESS=0
DO_GRAPHS=1



ONLY_LIST=""
SKIP_LIST=""



usage() {

	cat <<EOF

BenchKit (Linux)

  --install               Install missing tools using distro package manager
  --git-setup             Clone useful benchmark repos into ./tools/git/

  --all                   Run the common suite

  --only cpu,memory,...   Run only these modules
  --skip internet,...     Skip these modules

  --inventory             System inventory
  --cpu                   CPU info + sysbench CPU test
  --memory                Memory info + sysbench memory test
  --disks                 Filesystem benchmarks (fio preferred, dd fallback)
  --usb /path             USB read/write test (file-based)
  --nics                  NIC link speeds (ethtool preferred)
  --internet              Internet speed test (librespeed-cli or speedtest-cli)
  --smart                 SMART health (smartctl)
  --stress                stress-ng quick run

  --size-mb N             Test file size for some modules (default: ${SIZE_MB_DEFAULT})
  --no-graphs             Skip HTML+Chart report

EOF
}



while [[ $# -gt 0 ]]; do
	case "$1" in
		--install) DO_INSTALL=1; shift ;;
		--git-setup) DO_GIT_SETUP=1; shift ;;

		--all) DO_ALL=1; shift ;;

		--only) ONLY_LIST="${2:-}"; shift 2 ;;
		--skip) SKIP_LIST="${2:-}"; shift 2 ;;

		--inventory) DO_INVENTORY=1; shift ;;
		--cpu) DO_CPU=1; shift ;;
		--memory) DO_MEMORY=1; shift ;;
		--disks) DO_DISKS=1; shift ;;
		--usb) DO_USB=1; USB_PATH="${2:-}"; shift 2 ;;
		--nics) DO_NICS=1; shift ;;
		--internet) DO_INTERNET=1; shift ;;
		--smart) DO_SMART=1; shift ;;
		--stress) DO_STRESS=1; shift ;;

		--size-mb) SIZE_MB="${2:-$SIZE_MB_DEFAULT}"; shift 2 ;;
		--no-graphs) DO_GRAPHS=0; shift ;;

		-h|--help) usage; exit 0 ;;
		*) echo "Unknown arg: $1"; usage; exit 1 ;;
	esac
done



if [[ $DO_ALL -eq 1 ]]; then

	DO_INVENTORY=1

	DO_CPU=1
	DO_MEMORY=1
	DO_DISKS=1
	DO_NICS=1
	DO_INTERNET=1

	# USB needs an explicit path; keep it “optional-by-safety”
	DO_USB=1

	DO_SMART=1
	DO_STRESS=0
fi






################################################################################
#
#  Parent Section: Helpers
#
################################################################################

section() {

	echo
	echo
	echo "=============================================================================="
	echo "$1"
	echo "=============================================================================="
	echo
}



have() { command -v "$1" >/dev/null 2>&1; }



csv_escape() {

	# minimal escape helper
	echo "$1" | sed 's/"/""/g'
}



should_run() {

	local key="$1"


	if [[ -n "$ONLY_LIST" ]]; then
		[[ ",$ONLY_LIST," == *",$key,"* ]] || return 1
	fi


	if [[ -n "$SKIP_LIST" ]]; then
		[[ ",$SKIP_LIST," == *",$key,"* ]] && return 1
	fi


	return 0
}



json_init() {

	cat > "${OUT_DIR}/results.json" <<EOF
{
  "run_id": "$(date -Is)",
  "host": "$(hostname)",
  "results": {
EOF
}



json_close() {

	# close JSON object
	# note: we will remove trailing comma safely in json_finalize()
	cat >> "${OUT_DIR}/results.json" <<EOF
  }
}
EOF
}



json_add_raw_object() {

	# Adds: "key": { ... },
	local key="$1"
	local raw="$2"

	cat >> "${OUT_DIR}/results.json" <<EOF
	"$key": $raw,
EOF
}



json_finalize() {

	# Remove the last trailing comma in the "results" object.
	# Doing it carefully without “clever” tools so it’s scavenge-friendly.
	#
	# We:
	#   - create a temp file
	#   - remove the last line ending with "},"
	#   - replace it with "}"
	#
	# Simpler approach: just delete the last comma before closing braces.

	local f="${OUT_DIR}/results.json"
	local tmp="${OUT_DIR}/results.json.tmp"

	awk '
	{ lines[NR]=$0 }
	END {
		for (i=1; i<=NR; i++) {
		print lines[i]
		}
	}
	' "$f" > "$tmp"

	# Remove the last comma on the last "results" entry line (line that ends with "},")
	# This is intentionally simple, not bulletproof for all JSON shapes, but works for our output.
	tac "$tmp" | awk '
	BEGIN { fixed=0 }
	{
		if (fixed==0 && $0 ~ /},[[:space:]]*$/) {
		sub(/},[[:space:]]*$/, "}", $0)
		fixed=1
		}
		print
	}
	' | tac > "$f"

	rm -f "$tmp"
}






################################################################################
#
#  Parent Section: Installer System (Apps)
#
#  - Separate from git system
#  - Registry mapping command -> package name per installer
#
################################################################################

detect_pm() {

	if have apt-get; then echo "apt"; return; fi
	if have dnf; then echo "dnf"; return; fi
	if have yum; then echo "yum"; return; fi
	if have pacman; then echo "pacman"; return; fi
	if have zypper; then echo "zypper"; return; fi

	# snap isn't a full system package manager, but we support it as an installer channel
	if have snap; then echo "snap"; return; fi

	echo ""
}



ensure_snap_ready() {

	# snap may not exist; if not, try to install snapd with the system package manager
	if have snap; then
		return 0
	fi

	local pm
	pm="$(detect_pm)"
	if [[ "$pm" == "snap" || -z "$pm" ]]; then
		return 1
	fi

	section "Snap not found -> attempting snapd install via $pm"

	case "$pm" in
		apt)
			sudo apt-get update -y
			sudo apt-get install -y snapd
			;;
		dnf)
			sudo dnf install -y snapd
			;;
		yum)
			sudo yum install -y snapd
			;;
		pacman)
			echo "snapd on Arch may require extra steps (AUR). Skipping auto-install here."
			return 1
			;;
		zypper)
			sudo zypper --non-interactive install snapd
			;;
	esac

	have snap
}



# ---------------------------
# Child Section: App Registry
# ---------------------------
#
# Map “logical command we check for” -> package name per package manager.
#
# You can add entries quickly, or override per distro.

declare -A PKG_APT=()
declare -A PKG_DNF=()
declare -A PKG_YUM=()
declare -A PKG_PACMAN=()
declare -A PKG_ZYPPER=()
declare -A PKG_SNAP=()



# Common benchmark tools
PKG_APT[fio]="fio"
PKG_DNF[fio]="fio"
PKG_YUM[fio]="fio"
PKG_PACMAN[fio]="fio"
PKG_ZYPPER[fio]="fio"

PKG_APT[sysbench]="sysbench"
PKG_DNF[sysbench]="sysbench"
PKG_YUM[sysbench]="sysbench"
PKG_PACMAN[sysbench]="sysbench"
PKG_ZYPPER[sysbench]="sysbench"

PKG_APT[ethtool]="ethtool"
PKG_DNF[ethtool]="ethtool"
PKG_YUM[ethtool]="ethtool"
PKG_PACMAN[ethtool]="ethtool"
PKG_ZYPPER[ethtool]="ethtool"

PKG_APT[dmidecode]="dmidecode"
PKG_DNF[dmidecode]="dmidecode"
PKG_YUM[dmidecode]="dmidecode"
PKG_PACMAN[dmidecode]="dmidecode"
PKG_ZYPPER[dmidecode]="dmidecode"

PKG_APT[smartctl]="smartmontools"
PKG_DNF[smartctl]="smartmontools"
PKG_YUM[smartctl]="smartmontools"
PKG_PACMAN[smartmontools]="smartmontools"
PKG_ZYPPER[smartctl]="smartmontools"

PKG_APT[stress-ng]="stress-ng"
PKG_DNF[stress-ng]="stress-ng"
PKG_YUM[stress-ng]="stress-ng"
PKG_PACMAN[stress-ng]="stress-ng"
PKG_ZYPPER[stress-ng]="stress-ng"


# Internet speed test options:
# - librespeed-cli (Go client from LibreSpeed project) :contentReference[oaicite:7]{index=7}
# - speedtest-cli (python-based; common package name)
PKG_APT[speedtest-cli]="speedtest-cli"
PKG_DNF[speedtest-cli]="speedtest-cli"
PKG_YUM[speedtest-cli]="speedtest-cli"
PKG_PACMAN[speedtest-cli]="speedtest-cli"
PKG_ZYPPER[speedtest-cli]="speedtest-cli"



# Graph / report tools:
# - We generate HTML with Chart.js, so no OS package is required.
# - If you later want PNG graphs, add gnuplot, python3, etc.
PKG_APT[gnuplot]="gnuplot"
PKG_DNF[gnuplot]="gnuplot"
PKG_YUM[gnuplot]="gnuplot"
PKG_PACMAN[gnuplot]="gnuplot"
PKG_ZYPPER[gnuplot]="gnuplot"



pkg_for_cmd() {

	local pm="$1"
	local cmd="$2"

	case "$pm" in
		apt) echo "${PKG_APT[$cmd]:-}";;
		dnf) echo "${PKG_DNF[$cmd]:-}";;
		yum) echo "${PKG_YUM[$cmd]:-}";;
		pacman) echo "${PKG_PACMAN[$cmd]:-}";;
		zypper) echo "${PKG_ZYPPER[$cmd]:-}";;
		snap) echo "${PKG_SNAP[$cmd]:-}";;
		*) echo "";;
	esac
}



install_pkg() {

	local pm="$1"
	local pkg="$2"

	if [[ -z "$pkg" ]]; then
		return 1
	fi

	case "$pm" in
		apt)
			sudo apt-get update -y
			sudo apt-get install -y "$pkg"
			;;
		dnf)
			sudo dnf install -y "$pkg"
			;;
		yum)
			sudo yum install -y "$pkg"
			;;
		pacman)
			sudo pacman -Sy --noconfirm "$pkg"
			;;
		zypper)
			sudo zypper --non-interactive install "$pkg"
			;;
		snap)
			ensure_snap_ready
			sudo snap install "$pkg"
			;;
		*)
			return 1
			;;
	esac
}



require_cmds() {

	# Installs missing commands if DO_INSTALL=1
	# Otherwise, just warns.

	local pm
	pm="$(detect_pm)"

	local missing=0

	for cmd in "$@"; do

		if have "$cmd"; then
			continue
		fi

		missing=1

		if [[ $DO_INSTALL -eq 0 ]]; then
			echo "WARN: missing command '$cmd' (run with --install to attempt install)"
			continue
		fi

		local pkg
		pkg="$(pkg_for_cmd "$pm" "$cmd")"

		if [[ -z "$pkg" ]]; then
			echo "WARN: no package mapping for command '$cmd' under installer '$pm'"
			continue
		fi

		echo "Installing for '$cmd' -> package '$pkg' via $pm"
		install_pkg "$pm" "$pkg" || true
	done

	return $missing
}






################################################################################
#
#  Parent Section: Git System (Repos)
#
#  - Separate from package installs
#  - Registry lists useful repos you can clone for “alternate approaches”
#
################################################################################

declare -A GIT_REPOS=()

# Framework suite
GIT_REPOS[pts]="https://github.com/phoronix-test-suite/phoronix-test-suite"       # :contentReference[oaicite:8]{index=8}

# Core benchmark tools
GIT_REPOS[fio]="https://github.com/axboe/fio"                                    # :contentReference[oaicite:9]{index=9}
GIT_REPOS[iperf3]="https://github.com/esnet/iperf"                               # :contentReference[oaicite:10]{index=10}

# Speedtest options
GIT_REPOS[librespeed]="https://github.com/librespeed/speedtest"                 # :contentReference[oaicite:11]{index=11}
GIT_REPOS[librespeed-cli]="https://github.com/librespeed/speedtest-cli"         # :contentReference[oaicite:12]{index=12}

# Extras
GIT_REPOS[stress-ng]="https://github.com/ColinIanKing/stress-ng"                 # :contentReference[oaicite:13]{index=13}
GIT_REPOS[smartmontools]="https://github.com/smartmontools/smartmontools"        # :contentReference[oaicite:14]{index=14}

# Report graphics
GIT_REPOS[chartjs]="https://github.com/chartjs/Chart.js"                         # :contentReference[oaicite:15]{index=15}



git_setup() {

	section "Git setup: cloning registered repos into ${TOOLS_GIT_DIR}"

	require_cmds git || true

	if ! have git; then
		echo "ERROR: git not available; cannot clone repos."
		return 1
	fi


	for key in "${!GIT_REPOS[@]}"; do

		local url="${GIT_REPOS[$key]}"
		local dst="${TOOLS_GIT_DIR}/${key}"

		echo "Repo: $key"
		echo "  URL: $url"
		echo "  DST: $dst"

		if [[ -d "$dst/.git" ]]; then
			echo "  -> already cloned"
		else
			git clone "$url" "$dst" || true
		fi

		echo
	done
}






################################################################################
#
#  Parent Section: Modules
#
#  Each module:
#    - calls require_cmds for its dependencies
#    - returns a JSON object string
#
################################################################################

mod_inventory() {

	section "Module: inventory (system info)"

	# Dependencies
	require_cmds uname lscpu lsblk free || true


	local os
	os="$(uname -a | sed 's/"/\\"/g')"

	local cpu
	cpu="$(lscpu 2>/dev/null | sed 's/"/\\"/g')"

	local mem
	mem="$(free -h 2>/dev/null | sed 's/"/\\"/g')"

	local disks
	disks="$(lsblk -o NAME,TYPE,SIZE,MODEL,TRAN,ROTA,MOUNTPOINT,FSTYPE -e7 2>/dev/null | sed 's/"/\\"/g')"


	cat <<EOF
{"os":"$os","cpu":"$cpu","memory":"$mem","disks":"$disks"}
EOF
}



mod_cpu() {

	section "Module: cpu (sysbench cpu)"

	require_cmds lscpu sysbench || true


	local cpu_info
	cpu_info="$(lscpu 2>/dev/null | sed 's/"/\\"/g')"

	local cpu_bench=""
	if have sysbench; then
		cpu_bench="$(sysbench cpu --cpu-max-prime=50000 run 2>/dev/null | sed 's/"/\\"/g')"
	fi


	cat <<EOF
{"info":"$cpu_info","sysbench":"$cpu_bench"}
EOF
}



mod_memory() {

	section "Module: memory (dmidecode + sysbench memory)"

	require_cmds free dmidecode sysbench || true


	local mem_total
	mem_total="$(free -h 2>/dev/null | sed 's/"/\\"/g')"


	local dimm=""
	if have dmidecode; then
		# dmidecode usually needs sudo for full data; if sudo fails, we still proceed
		dimm="$(sudo dmidecode -t memory 2>/dev/null | sed 's/"/\\"/g' | head -n 200)"
	fi


	local mem_bench=""
	if have sysbench; then
		mem_bench="$(sysbench memory --memory-block-size=1M --memory-total-size=5G run 2>/dev/null | sed 's/"/\\"/g')"
	fi


	cat <<EOF
{"free":"$mem_total","dimm":"$dimm","sysbench":"$mem_bench"}
EOF
}



mod_disks() {

	section "Module: disks (fio preferred; dd fallback)"

	require_cmds lsblk fio || true



	# Parent idea:
	#   - benchmark safe, writable mountpoints
	#   - never benchmark raw /dev/sdX
	#
	# Child idea:
	#   - for each writable mountpoint:
	#       write 512MB
	#       read  512MB
	#
	# You can change the job size or add random IO later.

	local mounts=()
	while IFS= read -r mp; do
		mounts+=("$mp")
	done < <(findmnt -rn -o TARGET | grep -vE '^/(proc|sys|dev|run)($|/)' || true)



	local results="["

	local first=1



	for mp in "${mounts[@]}"; do

		if [[ ! -w "$mp" ]]; then
			continue
		fi

		local testfile="$mp/.bench_fio_test.bin"

		local write_out=""
		local read_out=""

		if have fio; then

			write_out="$(fio --name=write --filename="$testfile" --size=512M --rw=write --bs=1M --iodepth=16 --numjobs=1 --direct=1 2>/dev/null | sed 's/"/\\"/g')"
			read_out="$(fio --name=read  --filename="$testfile" --size=512M --rw=read  --bs=1M --iodepth=16 --numjobs=1 --direct=1 2>/dev/null | sed 's/"/\\"/g')"

		else

			# fallback
			write_out="fio_missing_dd_fallback"
			dd if=/dev/zero of="$testfile" bs=1M count=512 conv=fdatasync status=none || true
			dd if="$testfile" of=/dev/null bs=1M status=none || true
			read_out="dd_completed"

		fi

		rm -f "$testfile" || true



		local entry
		entry="{\"mount\":\"$(echo "$mp" | sed 's/"/\\"/g')\",\"write\":\"$write_out\",\"read\":\"$read_out\"}"

		if [[ $first -eq 1 ]]; then
			results+="$entry"
			first=0
		else
			results+=",$entry"
		fi
	done



	results+="]"



	cat <<EOF
{"mount_tests": $results}
EOF
}



mod_usb() {

	section "Module: usb (file-based read/write)"

	# This module is “optional by path”
	if [[ -z "$USB_PATH" ]]; then
		echo "No USB path provided; skipping USB test."
		cat <<EOF
{"skipped": true, "reason": "no_usb_path"}
EOF
		return 0
	fi

	if [[ ! -d "$USB_PATH" || ! -w "$USB_PATH" ]]; then
		echo "USB path invalid/not writable: $USB_PATH"
		cat <<EOF
{"skipped": true, "reason": "usb_path_not_writable"}
EOF
		return 0
	fi

	require_cmds fio || true



	local testfile="${USB_PATH}/bench_usb_test.bin"

	local write_out=""
	local read_out=""

	if have fio; then

		write_out="$(fio --name=usb_write --filename="$testfile" --size="${SIZE_MB}M" --rw=write --bs=1M --iodepth=16 --numjobs=1 --direct=1 2>/dev/null | sed 's/"/\\"/g')"
		read_out="$(fio --name=usb_read  --filename="$testfile" --size="${SIZE_MB}M" --rw=read  --bs=1M --iodepth=16 --numjobs=1 --direct=1 2>/dev/null | sed 's/"/\\"/g')"

	else

		write_out="fio_missing"
		read_out="fio_missing"

	fi

	rm -f "$testfile" || true



	cat <<EOF
{"path":"$(echo "$USB_PATH" | sed 's/"/\\"/g')","write":"$write_out","read":"$read_out"}
EOF
}



mod_nics() {

	section "Module: nics (link speeds)"

	require_cmds ip ethtool || true



	local nics="["

	local first=1



	for dev in $(ls /sys/class/net 2>/dev/null | grep -vE '^(lo)$'); do

		local speed="unknown"
		local duplex="unknown"
		local link="unknown"

		if have ethtool; then

			speed="$(ethtool "$dev" 2>/dev/null | awk -F': ' '/Speed:/{print $2}' | head -n1 | sed 's/"/\\"/g')"
			duplex="$(ethtool "$dev" 2>/dev/null | awk -F': ' '/Duplex:/{print $2}' | head -n1 | sed 's/"/\\"/g')"
			link="$(ethtool "$dev" 2>/dev/null | awk -F': ' '/Link detected:/{print $2}' | head -n1 | sed 's/"/\\"/g')"

		else

			[[ -f "/sys/class/net/$dev/speed" ]] && speed="$(cat "/sys/class/net/$dev/speed" 2>/dev/null) Mb/s"

		fi

		local entry
		entry="{\"dev\":\"$dev\",\"speed\":\"$speed\",\"duplex\":\"$duplex\",\"link\":\"$link\"}"

		if [[ $first -eq 1 ]]; then
			nics+="$entry"; first=0
		else
			nics+=",$entry"
		fi
	done



	nics+="]"



	cat <<EOF
{"interfaces": $nics}
EOF
}



mod_internet() {

	section "Module: internet (speedtest)"

	# Two approaches:
	#   - librespeed-cli (targets your own LibreSpeed server) :contentReference[oaicite:16]{index=16}
	#   - speedtest-cli (common package)
	#
	# You can extend this to Ookla speedtest too, if you prefer.

	require_cmds speedtest-cli || true



	local out=""

	if have librespeed-cli; then
		out="$(librespeed-cli 2>/dev/null | sed 's/"/\\"/g')"
		cat <<EOF
{"tool":"librespeed-cli","output":"$out"}
EOF
		return 0
	fi

	if have speedtest-cli; then
		out="$(speedtest-cli 2>/dev/null | sed 's/"/\\"/g')"
		cat <<EOF
{"tool":"speedtest-cli","output":"$out"}
EOF
		return 0
	fi



	cat <<EOF
{"skipped": true, "reason": "no_speedtest_tool_found"}
EOF
}



mod_smart() {

	section "Module: smart (smartctl health)"

	require_cmds smartctl lsblk || true



	if ! have smartctl; then
		cat <<EOF
{"skipped": true, "reason": "smartctl_missing"}
EOF
		return 0
	fi



	# This is intentionally “summary-ish”.
	# You can expand per device (sata/nvme) later.

	local devices=()
	while IFS= read -r d; do devices+=("$d"); done < <(lsblk -dn -o NAME,TYPE | awk '$2=="disk"{print "/dev/"$1}' || true)



	local arr="["
	local first=1

	for d in "${devices[@]}"; do

		local info
		info="$(smartctl -H "$d" 2>/dev/null | sed 's/"/\\"/g' | head -n 60)"

		local entry="{\"dev\":\"$d\",\"health\":\"$info\"}"

		if [[ $first -eq 1 ]]; then
			arr+="$entry"; first=0
		else
			arr+=",$entry"
		fi
	done

	arr+="]"



	cat <<EOF
{"devices": $arr}
EOF
}



mod_stress() {

	section "Module: stress (stress-ng quick)"

	require_cmds stress-ng || true



	if ! have stress-ng; then
		cat <<EOF
{"skipped": true, "reason": "stress-ng_missing"}
EOF
		return 0
	fi



	local out
	out="$(stress-ng --cpu 0 --timeout 10s --metrics-brief 2>/dev/null | sed 's/"/\\"/g')"

	cat <<EOF
{"output":"$out"}
EOF
}






################################################################################
#
#  Parent Section: HTML Report + Charts
#
################################################################################

build_report_html() {

	section "Report: HTML + Chart.js"


	local json_path="${OUT_DIR}/results.json"
	local html_path="${OUT_DIR}/report.html"


	# We use Chart.js because it’s lightweight and ubiquitous :contentReference[oaicite:17]{index=17}
	# This HTML is meant to be “easy to scavenge”, not perfect.

	cat > "$html_path" <<'EOF'
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>BenchKit Report</title>

  <style>
	body { font-family: system-ui, sans-serif; margin: 24px; }
	pre  { background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: 12px; overflow:auto; }
	.card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; margin-bottom: 16px; }
	canvas { max-width: 900px; }
  </style>

  <!-- Chart.js CDN (easy). If you prefer offline, swap this to a local copy. -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>

<body>

  <h1>BenchKit Report</h1>

  <div class="card">
	<h2>Raw JSON</h2>
	<pre id="raw"></pre>
  </div>

  <div class="card">
	<h2>Charts</h2>
	<p>
	These charts are “starter scaffolding”.
	As you add numeric fields into modules, extend the JS extraction below.
	</p>

	<canvas id="chartNics"></canvas>
  </div>

<script>
(async function () {

  const resp = await fetch('results.json');
  const data = await resp.json();

  document.getElementById('raw').textContent = JSON.stringify(data, null, 2);



  // ---------------------------------------------------------------------------
  // NIC chart example:
  // - parses results.nics.interfaces[]
  // - extracts Mbps number from "1000Mb/s" etc (best effort)
  // ---------------------------------------------------------------------------

  const nics = (data.results.nics && data.results.nics.interfaces) ? data.results.nics.interfaces : [];

  const labels = nics.map(x => x.dev);

  const speeds = nics.map(x => {
	const s = (x.speed || '').toString();
	const m = s.match(/(\d+)\s*Mb\/s/i) || s.match(/(\d+)\s*Mb/i) || s.match(/(\d+)/);
	return m ? parseInt(m[1], 10) : 0;
  });

  const ctx = document.getElementById('chartNics').getContext('2d');

  new Chart(ctx, {
	type: 'bar',
	data: {
	labels,
	datasets: [{
		label: 'NIC Link Speed (Mb/s)',
		data: speeds
	}]
	},
	options: {
	responsive: true
	}
  });

})();
</script>

</body>
</html>
EOF

	# Copy results.json next to report so relative fetch works
	cp -f "$json_path" "${OUT_DIR}/results.json"

	echo "Report written: $html_path"
}






################################################################################
#
#  Parent Section: Main Runner
#
################################################################################

main() {

	section "BenchKit starting"

	echo "ROOT_DIR: $ROOT_DIR"
	echo "OUT_DIR : $OUT_DIR"
	echo



	if [[ $DO_GIT_SETUP -eq 1 ]]; then
		git_setup || true
	fi



	json_init



	# -----------------------
	# Child Section: Dispatch
	# -----------------------

	if should_run "inventory" && [[ $DO_INVENTORY -eq 1 ]]; then
		json_add_raw_object "inventory" "$(mod_inventory)"
	fi


	if should_run "cpu" && [[ $DO_CPU -eq 1 ]]; then
		json_add_raw_object "cpu" "$(mod_cpu)"
	fi


	if should_run "memory" && [[ $DO_MEMORY -eq 1 ]]; then
		json_add_raw_object "memory" "$(mod_memory)"
	fi


	if should_run "disks" && [[ $DO_DISKS -eq 1 ]]; then
		json_add_raw_object "disks" "$(mod_disks)"
	fi


	if should_run "usb" && [[ $DO_USB -eq 1 ]]; then
		json_add_raw_object "usb" "$(mod_usb)"
	fi


	if should_run "nics" && [[ $DO_NICS -eq 1 ]]; then
		json_add_raw_object "nics" "$(mod_nics)"
	fi


	if should_run "internet" && [[ $DO_INTERNET -eq 1 ]]; then
		json_add_raw_object "internet" "$(mod_internet)"
	fi


	if should_run "smart" && [[ $DO_SMART -eq 1 ]]; then
		json_add_raw_object "smart" "$(mod_smart)"
	fi


	if should_run "stress" && [[ $DO_STRESS -eq 1 ]]; then
		json_add_raw_object "stress" "$(mod_stress)"
	fi



	json_close
	json_finalize



	if [[ $DO_GRAPHS -eq 1 ]]; then
		build_report_html || true
	fi



	section "Done"
	echo "Results: ${OUT_DIR}/results.json"
	echo "Report : ${OUT_DIR}/report.html"
	echo
}

main