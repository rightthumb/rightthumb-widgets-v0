<#
BenchKit (PowerShell) - Modular benchmark runner you can scavenge from later

Examples:

  .\benchkit.ps1 -All

  .\benchkit.ps1 -Only "cpu,memory,nics"

  .\benchkit.ps1 -Usb -UsbPath "E:\"

  .\benchkit.ps1 -GitSetup

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

    [switch]$NoGraphs
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
        if (",$Only," -notlike "*,$Key,*") { return $false }
    }

    if ($Skip) {
        if (",$Skip," -like "*,$Key,*") { return $false }
    }

    return $true
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
#  - Separate from Git system
#  - Registry maps command -> choco/winget package IDs
#
################################################################################

# ---------------------------
# Child Section: Registries
# ---------------------------

$PkgChoco = @{}
$PkgWinget = @{}

# Common tools (optional)
# Note: we don’t force-install; we only attempt if -Install and installer exists.

$PkgChoco["speedtest"] = "speedtest"          # Ookla
$PkgWinget["speedtest"] = "Ookla.Speedtest"   # winget ID

$PkgChoco["iperf3"] = "iperf3"
$PkgWinget["iperf3"] = "ESnet.iperf3"         # may vary; registry keeps it editable

# SMART (optional)
$PkgChoco["smartctl"] = "smartmontools"
$PkgWinget["smartctl"] = "smartmontools.smartmontools"  # may vary; keep as an editable entry



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

    # Framework suite
    "pts"          = "https://github.com/phoronix-test-suite/phoronix-test-suite"     # :contentReference[oaicite:19]{index=19}

    # Core tools
    "fio"          = "https://github.com/axboe/fio"                                   # :contentReference[oaicite:20]{index=20}
    "iperf3"       = "https://github.com/esnet/iperf"                                # :contentReference[oaicite:21]{index=21}

    # Internet speed
    "librespeed"   = "https://github.com/librespeed/speedtest"                       # :contentReference[oaicite:22]{index=22}
    "librespeedcli"= "https://github.com/librespeed/speedtest-cli"                   # :contentReference[oaicite:23]{index=23}

    # Extras
    "stress-ng"    = "https://github.com/ColinIanKing/stress-ng"                      # :contentReference[oaicite:24]{index=24}
    "smartmontools"= "https://github.com/smartmontools/smartmontools"                 # :contentReference[oaicite:25]{index=25}

    # Report charts
    "chartjs"      = "https://github.com/chartjs/Chart.js"                            # :contentReference[oaicite:26]{index=26}
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

    $cpu = Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed
    $mem = Get-CimInstance Win32_ComputerSystem | Select-Object TotalPhysicalMemory
    $os  = Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber



    return [ordered]@{
        os = $os
        cpu = $cpu
        memory = $mem
    }
}



function Mod-CPU {

    Section "Module: cpu (WinSAT cpuformal if available)"

    # WinSAT exists on many Windows versions, but Microsoft notes it can be altered/unavailable after 8.1 :contentReference[oaicite:27]{index=27}
    $winsatPath = Join-Path $env:WINDIR "System32\winsat.exe"

    $cpu = Get-CimInstance Win32_Processor | Select-Object Name, NumberOfCores, NumberOfLogicalProcessors, MaxClockSpeed



    $winsatOut = ""
    if (Test-Path $winsatPath) {
        $winsatOut = & $winsatPath cpuformal 2>&1 | Out-String
    } else {
        $winsatOut = "winsat.exe not found"
    }



    return [ordered]@{
        info = $cpu
        winsat = $winsatOut
    }
}



function Mod-Memory {

    Section "Module: memory (DIMM + WinSAT mem if available)"

    $memTotalGB = [math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2)

    $dimms = Get-CimInstance Win32_PhysicalMemory |
        Select-Object BankLabel, Manufacturer, PartNumber, Capacity, Speed, ConfiguredClockSpeed



    $winsatPath = Join-Path $env:WINDIR "System32\winsat.exe"
    $winsatOut = ""
    if (Test-Path $winsatPath) {
        $winsatOut = & $winsatPath mem 2>&1 | Out-String
    } else {
        $winsatOut = "winsat.exe not found"
    }



    return [ordered]@{
        total_gb = $memTotalGB
        dimms = $dimms
        winsat = $winsatOut
    }
}



function Mod-Disks {

    Section "Module: disks (WinSAT disk + PhysicalDisk info)"

    $disks = Get-PhysicalDisk | Select-Object FriendlyName, MediaType, Size, HealthStatus, OperationalStatus



    $winsatPath = Join-Path $env:WINDIR "System32\winsat.exe"
    $seqRead  = ""
    $seqWrite = ""

    if (Test-Path $winsatPath) {
        $seqRead  = & $winsatPath disk -seq -read  2>&1 | Out-String
        $seqWrite = & $winsatPath disk -seq -write 2>&1 | Out-String
    } else {
        $seqRead  = "winsat.exe not found"
        $seqWrite = "winsat.exe not found"
    }



    return [ordered]@{
        physical = $disks
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
    $writeMBps = [math]::Round($SizeMB / $sw.Elapsed.TotalSeconds, 2)



    # Read (USB -> PC)
    $back = Join-Path $env:TEMP "bench_usb_test_back.bin"
    $sw = [Diagnostics.Stopwatch]::StartNew()
    Copy-Item -Force $dst $back
    $sw.Stop()
    $readMBps = [math]::Round($SizeMB / $sw.Elapsed.TotalSeconds, 2)



    # Cleanup only what we created
    Remove-Item -Force -ErrorAction SilentlyContinue $src, $back, $dst
    Remove-Item -Force -ErrorAction SilentlyContinue $targetDir



    return [ordered]@{
        path = $UsbPath
        size_mb = $SizeMB
        write_mb_s = $writeMBps
        read_mb_s = $readMBps
    }
}



function Mod-NICs {

    Section "Module: nics (link speed)"

    $nics = Get-NetAdapter |
        Select-Object Name, InterfaceDescription, Status, LinkSpeed, MacAddress



    return [ordered]@{
        adapters = $nics
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
#  Parent Section: HTML Report + Charts
#
################################################################################

function Build-ReportHtml {

    param(
        [Parameter(Mandatory=$true)][string]$ResultsJsonPath,
        [Parameter(Mandatory=$true)][string]$OutHtmlPath
    )

    if ($NoGraphs) { return }



    Section "Report: HTML + Chart.js"

    $html = @'
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

  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>

  <h1>BenchKit Report</h1>

  <div class="card">
    <h2>Raw JSON</h2>
    <pre id="raw"></pre>
  </div>

  <div class="card">
    <h2>USB Example Chart</h2>
    <p>If you ran USB test, it will chart read/write MB/s.</p>
    <canvas id="chartUsb"></canvas>
  </div>

<script>
(async function () {

  const resp = await fetch('results.json');
  const data = await resp.json();

  document.getElementById('raw').textContent = JSON.stringify(data, null, 2);



  // ---------------------------------------------------------------------------
  // USB chart starter
  // ---------------------------------------------------------------------------

  const usb = data.results.usb || null;

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
    options: {
      responsive: true
    }
  });

})();
</script>

</body>
</html>
'@

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
