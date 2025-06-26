param(
    [string]$name,
    [int]$port,
    [switch]$auto,
    [string]$saveDir = "$env:USERPROFILE\db.yml"
)

# ----------------- Defaults -----------------
$baseDir = "C:\Mongo"
$defaultPort = 27017
$dataDir = Join-Path $baseDir $name
$configFile = "C:\Mongo\$name.conf"
$logFile = "C:\Mongo\$name.log"
$yamlFile = Join-Path $saveDir "$name.yml"
$adminUser = "admin"

Add-Type -AssemblyName System.Web
$adminPass = [System.Web.Security.Membership]::GeneratePassword(16, 4)

# ----------------- Validation -----------------
if (-not $name) {
    Write-Host "❌ Missing -name"
    exit 1
}
New-Item -ItemType Directory -Force -Path $saveDir | Out-Null

# ----------------- Mongo Check -----------------
if (-not (Get-Command mongod.exe -ErrorAction SilentlyContinue)) {
    Write-Error "[!] MongoDB not found. Install it first."
    exit 1
}

# ----------------- Port Fallback -----------------
if (-not $port) {
    $port = $defaultPort
    while (Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue) {
        $port++
    }
}

# ----------------- Create Folders -----------------
New-Item -ItemType Directory -Force -Path $dataDir | Out-Null
New-Item -ItemType File -Force -Path $logFile | Out-Null

# ----------------- Config File -----------------
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

security:
  authorization: enabled
"@ | Out-File -Encoding UTF8 -FilePath $configFile

# ----------------- Start MongoDB -----------------
Start-Process -FilePath "mongod.exe" -ArgumentList "--config `"$configFile`" --fork" -Wait
Start-Sleep -Seconds 2

# ----------------- Create Admin User -----------------
& mongosh.exe --port $port --eval @"
use admin
db.createUser({
  user: '$adminUser',
  pwd: '$adminPass',
  roles: [ { role: 'root', db: 'admin' } ]
})
"@

# ----------------- Write YAML -----------------
@"
# MongoDB instance created: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
$name:
  type: mongodb
  port: $port
  data: $dataDir
  config: $configFile
  log: $logFile
  start: mongod --config `"$configFile`" --fork
  stop: mongod --config `"$configFile`" --shutdown
  restart: mongod --config `"$configFile`" --shutdown && sleep 1 && mongod --config `"$configFile`" --fork
  users:
    $adminUser:
      password: "$adminPass"
"@ | Out-File -Encoding UTF8 -FilePath $yamlFile

# ----------------- Final Output -----------------
Write-Host "`n[✓] MongoDB instance '$name' running on port $port"
Write-Host "[📝] Config saved: $yamlFile"
Write-Host "`n🔐 Login: mongosh --port $port -u $adminUser -p --authenticationDatabase admin"
