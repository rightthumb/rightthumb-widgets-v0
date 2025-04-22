param(
    [string]$name,
    [int]$port,
    [switch]$auto,
    [string]$save = "$(Get-Location)\mongoDB_settings.yml"
)

# ---------- Help Menu ----------
if (-not $name -and -not $PSBoundParameters.ContainsKey('port') -and -not $auto -and -not $save) {
    Write-Host "Usage:"
    Write-Host "  .\init-mongo.ps1 -name mongo2 [-port 27018] [-auto] [-save .\mongoDB_settings.yml]"
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  -name     MongoDB instance name (required)"
    Write-Host "  -port     Optional port (auto-increments if omitted)"
    Write-Host "  -auto     Fully automated mode"
    Write-Host "  -save     Optional YAML config file"
    Write-Host ""
    Write-Host "Example:"
    Write-Host "  .\init-mongo.ps1 -name mongo2 -auto"
    exit
}

# ---------- Defaults ----------
$baseDir = "C:\Mongo"
$defaultPort = 27017
$dataDir = Join-Path $baseDir $name
$configFile = "C:\Mongo\$name.conf"
$logFile = "C:\Mongo\$name.log"

# ---------- Validate ----------
if (-not $name) {
    Write-Error "Missing -name"
    exit 1
}

# ---------- MongoDB Installed? ----------
if (-not (Get-Command mongod.exe -ErrorAction SilentlyContinue)) {
    Write-Host "[!] MongoDB is not installed."
    Write-Host "    Please install from: https://www.mongodb.com/try/download/community"
    exit 1
}

# ---------- Auto Port Fallback ----------
if (-not $port) {
    $port = $defaultPort
    while (Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue) {
        $port++
    }
}

# ---------- Prepare Data ----------
if (Test-Path $dataDir) {
    Write-Host "[!] Instance already exists: $name"
} else {
    Write-Host "[+] Creating data directory: $dataDir"
    New-Item -ItemType Directory -Path $dataDir -Force | Out-Null
}

# ---------- Generate Config ----------
@"
systemLog:
  destination: file
  path: $logFile
  logAppend: true

storage:
  dbPath: $dataDir

net:
  bindIp: 127.0.0.1
  port: $port
"@ | Out-File -Encoding UTF8 -FilePath $configFile

Write-Host "[+] Written config: $configFile"

# ---------- Start MongoDB ----------
Write-Host "[+] Starting MongoDB instance: $name"
Start-Process -FilePath "mongod.exe" -ArgumentList "--config `"$configFile`" --fork" -NoNewWindow -Wait

# ---------- Save to YAML ----------
Add-Content -Path $save -Value "`n# Created on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
Add-Content -Path $save -Value "$name:"
Add-Content -Path $save -Value "  port: $port"
Add-Content -Path $save -Value "  data_dir: $dataDir"
Add-Content -Path $save -Value "  config: $configFile"
Add-Content -Path $save -Value "  log_file: $logFile"

# ---------- Summary ----------
Write-Host ""
Write-Host "[✓] MongoDB instance '$name' started"
Write-Host "    Port     : $port"
Write-Host "    Data Dir : $dataDir"
Write-Host "    Log File : $logFile"
Write-Host "    Config   : $configFile"
Write-Host ""
Write-Host "[📝] Settings saved to: $save"
