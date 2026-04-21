<#
BenchKit (PowerShell) - Modular benchmark runner you can scavenge from later

Fixes / Improvements:
  - WinSAT now runs through a safe wrapper:
      - detects missing elevation and records it in JSON (no red errors)
      - catches failures and records error text
  - Optional -Elevate switch to relaunch as Administrator automatically
  - HTML report works offline (no fetch/file:// issues) by embedding results.json into report.html
  - Adds readable number formats in JSON + HTML as *additional* fields (does not replace raw values)

Examples:
  .\benchkit.ps1 -All
  .\benchkit.ps1 -Only "cpu,memory,nics"
  .\benchkit.ps1 -Usb -UsbPath "E:\"
  .\benchkit.ps1 -GitSetup
  .\benchkit.ps1 -Elevate -All
  .\benchkit.ps1 -Install -All   # uses choco/winget if available
#>

[CmdletBinding()]
param(

    [switch]$Install,
    [switch]$GitSetup,

    [switch]$All,

    [string]$Only = "",
    [string]$Skip = "",

    [switch]$Inventory,
    [switch]$CPU,
    [switch]$Memory,
    [switch]$Disks,
    [switch]$USB,
    [string]$UsbPath = "",
    [switch]$NICs,
    [switch]$Internet,
    [switch]$GPU,                # placeholder module hook
    [switch]$Smart,              # placeholder module hook

    [int]$SizeMB = 1024,

    [switch]$NoGraphs,

    [switch]$Elevate
)

################################################################################
#
#  Parent Section: Globals / Paths
#
################################################################################

$Root = Split-Path -Parent $PSCommandPath

$RunId  = Get-Date -Format "yyyy-MM-dd_HHmmss"
$OutDir = Join-Path $Root ("out\runs\" + $RunId)

$ToolsDir    = Join-Path $Root "tools"
$ToolsGitDir = Join-Path $ToolsDir "git"

New-Item -ItemType Directory -Force -Path $OutDir, (Join-Path $OutDir "graphs"), $ToolsGitDir | Out-Null

function Section($t) {
    Write-Host ""
    Write-Host ""
    Write-Host ("=" * 78)
    Write-Host $t
    Write-Host ("=" * 78)
    Write-Host ""
}

function Have($cmd) {
    return [bool](Get-Command $cmd -ErrorAction SilentlyContinue)
}

function Should-Run([string]$Key) {

    if ($Only) {
        # normalize spaces; allow "cpu, memory" etc
        $onlyNorm = ($Only -replace '\s+', '')
        if (",$onlyNorm," -notlike "*,$Key,*") { return $false }
    }

    if ($Skip) {
        $skipNorm = ($Skip -replace '\s+', '')
        if (",$skipNorm," -like "*,$Key,*") { return $false }
    }

    return $true
}

################################################################################
#
#  Parent Section: Formatting Helpers (adds *_fmt fields, keeps raw)
#
################################################################################

function Format-Number {
    param([Parameter(Mandatory=$true)]$Value)
    try {
        if ($null -eq $Value) { return "" }
        if ($Value -is [string]) { return $Value }
        return ([double]$Value).ToString("N0")
    } catch {
        return "$Value"
    }
}

function Format-Bytes {
    param([Parameter(Mandatory=$true)]$Bytes)

    try {
        if ($null -eq $Bytes) { return "" }

        $b = [double]$Bytes
        if ($b -lt 1024) { return ("{0:N0} B" -f $b) }
        if ($b -lt 1024KB) { return ("{0:N2} KB" -f ($b/1KB)) }
        if ($b -lt 1024MB) { return ("{0:N2} MB" -f ($b/1MB)) }
        if ($b -lt 1024GB) { return ("{0:N2} GB" -f ($b/1GB)) }
        if ($b -lt 1024TB) { return ("{0:N2} TB" -f ($b/1TB)) }
        return ("{0:N2} PB" -f ($b/1PB))
    } catch {
        return "$Bytes"
    }
}

function Format-Rate {
    param(
        [Parameter(Mandatory=$true)]$Value,
        [Parameter(Mandatory=$true)][string]$Unit
    )
    try {
        if ($null -eq $Value) { return "" }
        return ("{0:N2} {1}" -f ([double]$Value), $Unit)
    } catch {
        return "$Value $Unit"
    }
}

################################################################################
#
#  Parent Section: Elevation Helpers
#
################################################################################

function Test-IsAdmin {
    $p = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
    return $p.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Invoke-WinSAT {

    <#
      Safe wrapper:
        - If not elevated -> returns object noting that elevation is required
        - If WinSAT missing -> returns object noting missing
        - If WinSAT throws -> captures error text
    #>

    param(
        [Parameter(Mandatory=$true)][string[]]$Args
    )

    $winsatPath = Join-Path $env:WINDIR "System32\winsat.exe"

    if (-not (Test-Path $winsatPath)) {
        return [ordered]@{
            ok = $false
            reason = "winsat_missing"
            path = $winsatPath
            args = $Args
        }
    }

    if (-not (Test-IsAdmin)) {
        return [ordered]@{
            ok = $false
            reason = "requires_elevation"
            path = $winsatPath
            args = $Args
        }
    }

    try {
        $out = & $winsatPath @Args 2>&1 | Out-String

        return [ordered]@{
            ok = $true
            path = $winsatPath
            args = $Args
            output = $out
        }

    } catch {
        return [ordered]@{
            ok = $false
            reason = "winsat_failed"
            path = $winsatPath
            args = $Args
            error = ($_ | Out-String)
        }
    }
}

################################################################################
#
#  Parent Section: Optional Self-Elevation
#
################################################################################

if ($Elevate -and -not (Test-IsAdmin)) {

    Section "Elevation requested - relaunching as Administrator"

    $argList = @()

    # Rebuild args from bound parameters (simple + scavenge-friendly)
    foreach ($k in $PSBoundParameters.Keys) {

        if ($k -eq "Elevate") { continue }

        $v = $PSBoundParameters[$k]

        if ($v -is [bool] -and $v) {
            $argList += "-$k"
        } elseif ($v -isnot [bool]) {
            $argList += "-$k"
            $argList += "`"$v`""
        }
    }

    $argString = $argList -join " "

    Start-Process -FilePath "powershell.exe" -Verb RunAs -ArgumentList "-NoProfile -ExecutionPolicy Bypass -File `"$PSCommandPath`" $argString"
    exit
}

################################################################################
#
#  Parent Section: Defaults for -All
#
################################################################################

if ($All) {

    $Inventory = $true

    $CPU    = $true
    $Memory = $true
    $Disks  = $true
    $NICs   = $true
    $Internet = $true

    # USB needs explicit path -> keep it “optional”
    $USB = $true
}

################################################################################
#
#  Parent Section: Installer System (Apps)
#
################################################################################

$PkgChoco  = @{}
$PkgWinget = @{}

$PkgChoco["speedtest"]  = "speedtest"              # Ookla
$PkgWinget["speedtest"] = "Ookla.Speedtest"        # winget ID

$PkgChoco["iperf3"]  = "iperf3"
$PkgWinget["iperf3"] = "ESnet.iperf3"              # may vary; editable

$PkgChoco["git"]  = "git"
$PkgWinget["git"] = "Git.Git"

$PkgChoco["smartctl"]  = "smartmontools"
$PkgWinget["smartctl"] = "smartmontools.smartmontools"   # may vary; keep editable

function Try-InstallCommand([string]$CmdName) {

    if (Have $CmdName) { return }

    if (-not $Install) {
        Write-Warning "Missing '$CmdName' (run with -Install to attempt install)"
        return
    }

    $hasChoco  = Have "choco"
    $hasWinget = Have "winget"

    if ($hasChoco -and $PkgChoco.ContainsKey($CmdName)) {

        $pkg = $PkgChoco[$CmdName]
        Section "Installing via Chocolatey: $CmdName -> $pkg"

        & choco install $pkg -y | Out-Host
        return
    }

    if ($hasWinget -and $PkgWinget.ContainsKey($CmdName)) {

        $pkg = $PkgWinget[$CmdName]
        Section "Installing via winget: $CmdName -> $pkg"

        & winget install --id $pkg --silent --accept-package-agreements --accept-source-agreements | Out-Host
        return
    }

    Write-Warning "No installer mapping found for '$CmdName' (or installer not available)."
}

################################################################################
#
#  Parent Section: Git System (Repos)
#
################################################################################

$GitRepos = [ordered]@{
    "pts"           = "https://github.com/phoronix-test-suite/phoronix-test-suite"
    "fio"           = "https://github.com/axboe/fio"
    "iperf3"        = "https://github.com/esnet/iperf"
    "librespeed"    = "https://github.com/librespeed/speedtest"
    "librespeedcli" = "https://github.com/librespeed/speedtest-cli"
    "stress-ng"     = "https://github.com/ColinIanKing/stress-ng"
    "smartmontools" = "https://github.com/smartmontools/smartmontools"
    "chartjs"       = "https://github.com/chartjs/Chart.js"
}

function Git-Setup {

    Section "Git setup: cloning repos into .\tools\git\"

    if (-not (Have "git")) {
        Try-InstallCommand "git"
    }

    if (-not (Have "git")) {
        Write-Warning "git not available; cannot clone repos."
        return
    }

    foreach ($k in $GitRepos.Keys) {

        $url = $GitRepos[$k]
        $dst = Join-Path $ToolsGitDir $k

        Write-Host "Repo: $k"
        Write-Host "  URL: $url"
        Write-Host "  DST: $dst"

        if (Test-Path (Join-Path $dst ".git")) {
            Write-Host "  -> already cloned"
        } else {
            & git clone $url $dst | Out-Host
        }

        Write-Host ""
    }
}

if ($GitSetup) { Git-Setup }

################################################################################
#
#  Parent Section: Modules
#
################################################################################

function Mod-Inventory {

    Section "Module: inventory"

    $cpuObj = Get-CimInstance Win32_Processor | Select-Object -First 1 Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed
    $osObj  = Get-CimInstance Win32_OperatingSystem | Select-Object -First 1 Caption, Version, BuildNumber
    $csObj  = Get-CimInstance Win32_ComputerSystem | Select-Object -First 1 TotalPhysicalMemory, Manufacturer, Model

    $memBytes = [int64]$csObj.TotalPhysicalMemory
    $memGB = [math]::Round($memBytes / 1GB, 2)

    return [ordered]@{
        os = [ordered]@{
            caption = $osObj.Caption
            version = $osObj.Version
            build_number = $osObj.BuildNumber
        }
        cpu = [ordered]@{
            name = $cpuObj.Name
            cores = [int]$cpuObj.NumberOfCores
            threads = [int]$cpuObj.NumberOfLogicalProcessors
            max_clock_mhz = [int]$cpuObj.MaxClockSpeed

            cores_fmt = (Format-Number $cpuObj.NumberOfCores)
            threads_fmt = (Format-Number $cpuObj.NumberOfLogicalProcessors)
            max_clock_mhz_fmt = ("{0:N0} MHz" -f ([int]$cpuObj.MaxClockSpeed))
        }
        system = [ordered]@{
            manufacturer = $csObj.Manufacturer
            model = $csObj.Model
            total_physical_memory_bytes = $memBytes
            total_physical_memory_bytes_fmt = (Format-Bytes $memBytes)
            total_physical_memory_gb = $memGB
            total_physical_memory_gb_fmt = (Format-Rate $memGB "GB")
        }
    }
}

function Mod-CPU {

    Section "Module: cpu (WinSAT cpuformal if available)"

    $cpuObj = Get-CimInstance Win32_Processor | Select-Object -First 1 Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed

    $winsat = Invoke-WinSAT -Args @("cpuformal")

    return [ordered]@{
        info = [ordered]@{
            name = $cpuObj.Name
            cores = [int]$cpuObj.NumberOfCores
            threads = [int]$cpuObj.NumberOfLogicalProcessors
            max_clock_mhz = [int]$cpuObj.MaxClockSpeed

            cores_fmt = (Format-Number $cpuObj.NumberOfCores)
            threads_fmt = (Format-Number $cpuObj.NumberOfLogicalProcessors)
            max_clock_mhz_fmt = ("{0:N0} MHz" -f ([int]$cpuObj.MaxClockSpeed))
        }
        winsat = $winsat
    }
}

# function Mod-Memory {

#     Section "Module: memory (DIMM + WinSAT mem if available)"

#     $cs = Get-CimInstance Win32_ComputerSystem | Select-Object -First 1 TotalPhysicalMemory
#     $memBytes = [int64]$cs.TotalPhysicalMemory
#     $memTotalGB = [math]::Round($memBytes / 1GB, 2)

#     $dimmsRaw = Get-CimInstance Win32_PhysicalMemory |
#         Select-Object BankLabel, Manufacturer, PartNumber, Capacity, Speed, ConfiguredClockSpeed

#     $dimms = @()
#     foreach ($d in $dimmsRaw) {
#         $capBytes = [int64]$d.Capacity
#         $capGB = [math]::Round($capBytes / 1GB, 2)
#         $dimms += [ordered]@{
#             bank = $d.BankLabel
#             manufacturer = $d.Manufacturer
#             part_number = ($d.PartNumber -as [string]).Trim()
#             capacity_bytes = $capBytes
#             capacity_bytes_fmt = (Format-Bytes $capBytes)
#             capacity_gb = $capGB
#             capacity_gb_fmt = (Format-Rate $capGB "GB")
#             speed_mhz = $d.Speed

            


#             $speedFmt = ""
#             if ($d.Speed) { $speedFmt = ("{0:N0} MHz" -f ([int]$d.Speed)) }

#             $cfgFmt = ""
#             if ($d.ConfiguredClockSpeed) { $cfgFmt = ("{0:N0} MHz" -f ([int]$d.ConfiguredClockSpeed)) }

#             $dimms += [ordered]@{
#                 bank = $d.BankLabel
#                 manufacturer = $d.Manufacturer
#                 part_number = ($d.PartNumber -as [string]).Trim()
#                 capacity_bytes = $capBytes
#                 capacity_bytes_fmt = (Format-Bytes $capBytes)
#                 capacity_gb = $capGB
#                 capacity_gb_fmt = (Format-Rate $capGB "GB")
#                 speed_mhz = $d.Speed
#                 speed_mhz_fmt = $speedFmt
#                 configured_clock_mhz = $d.ConfiguredClockSpeed
#                 configured_clock_mhz_fmt = $cfgFmt
#             }



#             configured_clock_mhz_fmt = (if ($d.ConfiguredClockSpeed) { ("{0:N0} MHz" -f ([int]$d.ConfiguredClockSpeed)) } else { "" })
#         }
#     }

#     $winsat = Invoke-WinSAT -Args @("mem")

#     return [ordered]@{
#         total_bytes = $memBytes
#         total_bytes_fmt = (Format-Bytes $memBytes)
#         total_gb = $memTotalGB
#         total_gb_fmt = (Format-Rate $memTotalGB "GB")
#         dimms = $dimms
#         winsat = $winsat
#     }
# }



function Mod-Memory {

    Section "Module: memory (DIMM + WinSAT mem if available)"

    $cs = Get-CimInstance Win32_ComputerSystem | Select-Object -First 1 TotalPhysicalMemory
    $memBytes = [int64]$cs.TotalPhysicalMemory
    $memTotalGB = [math]::Round($memBytes / 1GB, 2)

    $dimms = @()

    $rawDimms = Get-CimInstance Win32_PhysicalMemory |
        Select-Object BankLabel, Manufacturer, PartNumber, Capacity, Speed, ConfiguredClockSpeed

    foreach ($d in $rawDimms) {

        $capBytes = [int64]$d.Capacity
        $capGB = [math]::Round($capBytes / 1GB, 2)

        # ---- FORMATTERS MUST COME FIRST (NOT INSIDE HASH) ----
        $speedFmt = ""
        if ($d.Speed) {
            $speedFmt = ("{0:N0} MHz" -f ([int]$d.Speed))
        }

        $cfgFmt = ""
        if ($d.ConfiguredClockSpeed) {
            $cfgFmt = ("{0:N0} MHz" -f ([int]$d.ConfiguredClockSpeed))
        }

        # ---- NOW BUILD THE OBJECT ----
        $dimms += [ordered]@{
            bank = $d.BankLabel
            manufacturer = $d.Manufacturer
            part_number = ($d.PartNumber -as [string]).Trim()

            capacity_bytes = $capBytes
            capacity_bytes_fmt = (Format-Bytes $capBytes)

            capacity_gb = $capGB
            capacity_gb_fmt = (Format-Rate $capGB "GB")

            speed_mhz = $d.Speed
            speed_mhz_fmt = $speedFmt

            configured_clock_mhz = $d.ConfiguredClockSpeed
            configured_clock_mhz_fmt = $cfgFmt
        }
    }

    $winsat = Invoke-WinSAT -Args @("mem")

    return [ordered]@{
        total_bytes = $memBytes
        total_bytes_fmt = (Format-Bytes $memBytes)

        total_gb = $memTotalGB
        total_gb_fmt = (Format-Rate $memTotalGB "GB")

        dimms = $dimms
        winsat = $winsat
    }
}



function Mod-Disks {

    Section "Module: disks (WinSAT disk + PhysicalDisk info)"

    $pd = @()
    $raw = @(Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size, HealthStatus, OperationalStatus)
    foreach ($d in $raw) {
        $sz = [int64]$d.Size
        $pd += [ordered]@{
            name = $d.FriendlyName
            media_type = $d.MediaType
            size_bytes = $sz
            size_bytes_fmt = (Format-Bytes $sz)
            health = $d.HealthStatus
            status = ($d.OperationalStatus -join ",")
        }
    }

    $seqRead  = Invoke-WinSAT -Args @("disk","-seq","-read")
    $seqWrite = Invoke-WinSAT -Args @("disk","-seq","-write")

    return [ordered]@{
        physical = $pd
        winsat_seq_read = $seqRead
        winsat_seq_write = $seqWrite
    }
}

function Mod-USB {

    Section "Module: usb (file copy timing)"

    if (-not $UsbPath) {
        return [ordered]@{ skipped = $true; reason = "no_usb_path" }
    }

    if (-not (Test-Path $UsbPath)) {
        return [ordered]@{ skipped = $true; reason = "usb_path_missing" }
    }

    $targetDir = Join-Path $UsbPath "bench_tmp"
    New-Item -ItemType Directory -Force -Path $targetDir | Out-Null

    $src = Join-Path $env:TEMP "bench_usb_test.bin"
    $dst = Join-Path $targetDir "bench_usb_test.bin"

    # Create file
    $fs = [System.IO.File]::Open($src, [System.IO.FileMode]::Create, [System.IO.FileAccess]::Write)
    try {
        $buf = New-Object byte[] (1024*1024)
        for ($i=0; $i -lt $SizeMB; $i++) { $fs.Write($buf, 0, $buf.Length) }
    } finally { $fs.Close() }

    # Write (PC -> USB)
    $sw = [Diagnostics.Stopwatch]::StartNew()
    Copy-Item -Force $src $dst
    $sw.Stop()
    $writeMBps = [math]::Round($SizeMB / [math]::Max($sw.Elapsed.TotalSeconds, 0.0001), 2)

    # Read (USB -> PC)
    $back = Join-Path $env:TEMP "bench_usb_test_back.bin"
    $sw = [Diagnostics.Stopwatch]::StartNew()
    Copy-Item -Force $dst $back
    $sw.Stop()
    $readMBps = [math]::Round($SizeMB / [math]::Max($sw.Elapsed.TotalSeconds, 0.0001), 2)

    # Cleanup only what we created
    Remove-Item -Force -ErrorAction SilentlyContinue $src, $back, $dst
    Remove-Item -Force -ErrorAction SilentlyContinue $targetDir

    return [ordered]@{
        path = $UsbPath
        size_mb = $SizeMB
        size_mb_fmt = (Format-Number $SizeMB) + " MB"
        write_mb_s = $writeMBps
        write_mb_s_fmt = (Format-Rate $writeMBps "MB/s")
        read_mb_s = $readMBps
        read_mb_s_fmt = (Format-Rate $readMBps "MB/s")
    }
}

function Mod-NICs {

    Section "Module: nics (link speed)"

    $raw = @(Get-NetAdapter | Select-Object Name, InterfaceDescription, Status, LinkSpeed, MacAddress)

    $nics = @()
    foreach ($n in $raw) {
        $nics += [ordered]@{
            name = $n.Name
            description = $n.InterfaceDescription
            status = $n.Status
            link_speed = $n.LinkSpeed
            mac = $n.MacAddress
        }
    }

    return [ordered]@{
        adapters = $nics
        adapters_count = $nics.Count
        adapters_count_fmt = (Format-Number $nics.Count)
    }
}

function Mod-Internet {

    Section "Module: internet (speedtest if available)"

    Try-InstallCommand "speedtest"

    if (Have "speedtest") {
        $out = & speedtest --accept-license --accept-gdpr 2>&1 | Out-String
        return [ordered]@{ tool="ookla_speedtest"; output=$out }
    }

    return [ordered]@{ skipped=$true; reason="speedtest_not_found" }
}

################################################################################
#
#  Parent Section: HTML Report + Charts (Offline-safe)
#
################################################################################

function Build-ReportHtml {

    param(
        [Parameter(Mandatory=$true)][string]$ResultsJsonPath,
        [Parameter(Mandatory=$true)][string]$OutHtmlPath
    )

    if ($NoGraphs) { return }

    Section "Report: HTML + Chart.js (offline-safe)"

    $jsonText = Get-Content -Raw -Encoding UTF8 $ResultsJsonPath

    $html = @"
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <title>BenchKit Report</title>
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <style>
    body { font-family: system-ui, sans-serif; margin: 24px; line-height: 1.35; }
    pre  { background: #0f172a; color: #e2e8f0; padding: 16px; border-radius: 12px; overflow:auto; }
    .card { border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px; margin-bottom: 16px; }
    .row { display:flex; gap:16px; flex-wrap:wrap; }
    .k { color:#334155; font-weight:600; min-width: 180px; }
    .v { color:#0f172a; }
    .kv { display:flex; gap:10px; }
    canvas { max-width: 900px; }
    .muted { color:#64748b; }
    code.inline { background:#f1f5f9; padding:2px 6px; border-radius:8px; }
  </style>

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>

  <h1>BenchKit Report</h1>
  <div class="muted">Offline-safe report (no <code class="inline">fetch()</code>).</div>

  <!-- Embed JSON directly so file:// works -->
  <script id="resultsJson" type="application/json">
$jsonText
  </script>

  <div class="card">
    <h2>Summary (Readable)</h2>
    <div id="summary"></div>
  </div>

  <div class="card">
    <h2>Raw JSON</h2>
    <pre id="raw"></pre>
  </div>

  <div class="card">
    <h2>USB Example Chart</h2>
    <p class="muted">If you ran USB test, it charts read/write MB/s.</p>
    <canvas id="chartUsb"></canvas>
  </div>

<script>
(function () {

  const jsonEl = document.getElementById('resultsJson');
  const data = JSON.parse(jsonEl.textContent);

  document.getElementById('raw').textContent = JSON.stringify(data, null, 2);

  // Build a simple readable summary using *_fmt fields (still keeps raw in JSON)
  function kv(k, v) {
    const d = document.createElement('div');
    d.className = 'kv';
    d.innerHTML = '<div class="k">' + k + '</div><div class="v">' + (v ?? '') + '</div>';
    return d;
  }

  const sum = document.getElementById('summary');
  const r = (data && data.results) ? data.results : {};

  // Inventory
  if (r.inventory) {
    const inv = r.inventory;
    const wrap = document.createElement('div');
    wrap.className = 'row';

    const a = document.createElement('div');
    a.style.minWidth = '420px';
    a.appendChild(kv('OS', (inv.os?.caption || '') + ' (Build ' + (inv.os?.build_number || '') + ')'));
    a.appendChild(kv('CPU', inv.cpu?.name || ''));
    a.appendChild(kv('Cores / Threads', (inv.cpu?.cores_fmt || inv.cpu?.cores || '') + ' / ' + (inv.cpu?.threads_fmt || inv.cpu?.threads || '')));
    a.appendChild(kv('Max Clock', inv.cpu?.max_clock_mhz_fmt || (inv.cpu?.max_clock_mhz || '') + ' MHz'));
    a.appendChild(kv('RAM', inv.system?.total_physical_memory_bytes_fmt || ''));

    const b = document.createElement('div');
    b.style.minWidth = '420px';
    b.appendChild(kv('System', (inv.system?.manufacturer || '') + ' ' + (inv.system?.model || '')));
    wrap.appendChild(a);
    wrap.appendChild(b);

    sum.appendChild(wrap);
  }

  // USB chart
  const usb = r.usb || null;
  const labels = ['Write MB/s', 'Read MB/s'];
  const values = usb && !usb.skipped
    ? [usb.write_mb_s || 0, usb.read_mb_s || 0]
    : [0, 0];

  const ctx = document.getElementById('chartUsb').getContext('2d');
  new Chart(ctx, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        label: 'USB Throughput',
        data: values
      }]
    },
    options: { responsive: true }
  });

})();
</script>

</body>
</html>
"@

    Set-Content -Encoding utf8 -Path $OutHtmlPath -Value $html
}

################################################################################
#
#  Parent Section: Main Runner
#
################################################################################

Section "BenchKit starting"

Write-Host "Root  : $Root"
Write-Host "OutDir : $OutDir"
Write-Host ""

$results = [ordered]@{
    run_id = (Get-Date).ToString("o")
    host   = $env:COMPUTERNAME
    is_admin = (Test-IsAdmin)
    results = [ordered]@{}
}

if (Should-Run "inventory" -and $Inventory) { $results.results["inventory"] = Mod-Inventory }
if (Should-Run "cpu"       -and $CPU)       { $results.results["cpu"]       = Mod-CPU }
if (Should-Run "memory"    -and $Memory)    { $results.results["memory"]    = Mod-Memory }
if (Should-Run "disks"     -and $Disks)     { $results.results["disks"]     = Mod-Disks }
if (Should-Run "usb"       -and $USB)       { $results.results["usb"]       = Mod-USB }
if (Should-Run "nics"      -and $NICs)      { $results.results["nics"]      = Mod-NICs }
if (Should-Run "internet"  -and $Internet)  { $results.results["internet"]  = Mod-Internet }

$resultsPath = Join-Path $OutDir "results.json"
($results | ConvertTo-Json -Depth 12) | Set-Content -Encoding utf8 $resultsPath

$reportPath = Join-Path $OutDir "report.html"
Build-ReportHtml -ResultsJsonPath $resultsPath -OutHtmlPath $reportPath

Section "Done"
Write-Host "Results: $resultsPath"
Write-Host "Report : $reportPath"
Write-Host ""
