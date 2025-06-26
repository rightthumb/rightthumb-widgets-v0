param(
    [string]$name,
    [int]$port,
    [switch]$auto,
    [string]$saveDir = "$env:USERPROFILE\db.yml"
)

# ----------------- Defaults -----------------
$baseDir = "C:\Postgres"
$defaultPort = 5432
$dataDir = Join-Path $baseDir $name
$logFile = Join-Path $baseDir "${name}_logfile.log"
$configFile = Join-Path $dataDir "postgresql.conf"
$yamlFile = Join-Path $saveDir "$name.yml"

# ----------------- Validate -----------------
if (-not $name) {
    Write-Host "❌ Missing -name"
    exit 1
}

New-Item -ItemType Directory -Force -Path $saveDir | Out-Null

# ----------------- PostgreSQL Check -----------------
if (-not (Get-Command initdb.exe -ErrorAction SilentlyContinue)) {
    Write-Error "[!] PostgreSQL not found. Install it first."
    exit 1
}

# ----------------- Port Selection -----------------
if (-not $port) {
    $port = $defaultPort
    while (Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue) {
        $port++
    }
}

# ----------------- Password -----------------
Add-Type -AssemblyName System.Web
$pass = [System.Web.Security.Membership]::GeneratePassword(24, 4)

# ----------------- Init Instance -----------------
if (-not (Test-Path $dataDir)) {
    New-Item -ItemType Directory -Force -Path $dataDir | Out-Null
    & initdb.exe -D $dataDir
}

# ----------------- Config -----------------
(Get-Content $configFile) -replace '#port = .*', "port = $port" |
    ForEach-Object { $_ -replace "#listen_addresses =.*", "listen_addresses = 'localhost'" } |
    Set-Content $configFile

Add-Content -Path (Join-Path $dataDir 'pg_hba.conf') -Value "host all all 127.0.0.1/32 md5"

# ----------------- Start -----------------
& pg_ctl.exe -D $dataDir -l $logFile start
Start-Sleep -Seconds 2
& psql.exe -p $port -c "ALTER USER postgres WITH PASSWORD '$pass';"

# ----------------- Write YAML -----------------
@"
# PostgreSQL instance created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
$name:
  type: postgresql
  port: $port
  data: $dataDir
  config: $configFile
  log: $logFile
  start: pg_ctl -D `"$dataDir`" -l `"$logFile`" start
  stop: pg_ctl -D `"$dataDir`" stop
  restart: pg_ctl -D `"$dataDir`" -l `"$logFile`" restart
  users:
    postgres:
      password: "$pass"
"@ | Out-File -Encoding UTF8 -FilePath $yamlFile

Write-Host "`n[✓] PostgreSQL instance '$name' running on port $port"
Write-Host "[📝] Config saved: $yamlFile"
