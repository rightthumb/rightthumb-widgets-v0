param(
    [string]$name,
    [int]$port,
    [switch]$auto,
    [string]$save = "$(Get-Location)\postgres_settings.yml"
)

# ---------------- Help Menu ----------------
if (!$name -and !$PSBoundParameters.ContainsKey("port") -and !$auto -and !$save) {
    Write-Host "Usage:"
    Write-Host "  .\init-postgres.ps1 -name pg1 [-port 5433] [-auto] [-save 'C:\path\to\settings.yml']"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -name    PostgreSQL instance name (required)"
    Write-Host "  -port    Optional port (auto-increments if omitted)"
    Write-Host "  -auto    Fully automated mode"
    Write-Host "  -save    Alternate YAML config file (default: .\postgres_settings.yml)"
    exit
}

# ---------------- Defaults ----------------
$baseDir = "C:\Postgres"
$defaultPort = 5432
$dataDir = Join-Path $baseDir $name
$logFile = Join-Path $baseDir "${name}_logfile.log"
$configFile = Join-Path $dataDir "postgresql.conf"

# ---------------- Validation ----------------
if (-not $name) {
    Write-Error "Missing -name"
    exit 1
}

# ---------------- PostgreSQL Check ----------------
if (-not (Get-Command initdb -ErrorAction SilentlyContinue)) {
    Write-Host "[+] PostgreSQL is not installed."
    Write-Host "    Please install PostgreSQL manually from https://www.postgresql.org/download/windows/"
    exit 1
}

# ---------------- Auto Port Detection ----------------
if (-not $port) {
    $port = $defaultPort
    while (Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue) {
        $port++
    }
}

# ---------------- Password Generation ----------------
Add-Type -AssemblyName System.Web
$pass = [System.Web.Security.Membership]::GeneratePassword(24, 4)

# ---------------- Data Directory ----------------
if (Test-Path $dataDir) {
    Write-Host "[!] Instance already exists: $name"
} else {
    Write-Host "[+] Creating data directory: $dataDir"
    New-Item -ItemType Directory -Force -Path $dataDir | Out-Null
    & initdb.exe -D $dataDir
}

# ---------------- Configuration ----------------
(gc $configFile) -replace '#port = .*', "port = $port" |
    ForEach-Object { $_ -replace "#listen_addresses =.*", "listen_addresses = 'localhost'" } |
    Set-Content $configFile

Add-Content -Path (Join-Path $dataDir 'pg_hba.conf') -Value "host all all 127.0.0.1/32 md5"
Add-Content -Path (Join-Path $dataDir 'pg_hba.conf') -Value "host all all ::1/128 md5"

# ---------------- Start PostgreSQL ----------------
Write-Host "[+] Starting PostgreSQL instance..."
& pg_ctl.exe -D $dataDir -l $logFile start

# ---------------- Set Password ----------------
Start-Sleep -Seconds 3
& psql.exe -p $port -c "ALTER USER postgres WITH PASSWORD '$pass';"

# ---------------- Save to YAML ----------------
Add-Content -Path $save -Value "`n# Created on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Add-Content -Path $save -Value "$name:"
Add-Content -Path $save -Value "  port: $port"
Add-Content -Path $save -Value "  password: `"$pass`""
Add-Content -Path $save -Value "  data_dir: $dataDir"
Add-Content -Path $save -Value "  config: $configFile"
Add-Content -Path $save -Value "  log_file: $logFile"

# ---------------- Summary ----------------
Write-Host "`n[✓] PostgreSQL instance '$name' started"
Write-Host "    Port     : $port"
Write-Host "    Password : $pass"
Write-Host "    Data Dir : $dataDir"
Write-Host "    Log File : $logFile"
Write-Host "    Config   : $configFile"
Write-Host ""
Write-Host "[📝] Settings saved to: $save"
