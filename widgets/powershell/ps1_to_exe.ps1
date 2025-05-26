# Set execution policy for this session
Set-ExecutionPolicy Bypass -Scope Process -Force

# Ensure a PowerShell script is provided
param (
    [string]$ScriptPath
)

if (-not $ScriptPath -or -not (Test-Path $ScriptPath)) {
    Write-Host "Usage: ps1.exe.ps1 <script.ps1>"
    exit 1
}

# Define required executables
$requirements = @("dotnet.exe", "pwsh.exe", "csc.exe", "es.exe")
$indexFile = "C:\index.txt"
$tempIndexFile = "$env:TEMP\c_index.txt"

# Function to check if script is running as Administrator
function Test-Admin {
    $user = [System.Security.Principal.WindowsIdentity]::GetCurrent()
    $principal = New-Object System.Security.Principal.WindowsPrincipal($user)
    return $principal.IsInRole([System.Security.Principal.WindowsBuiltInRole]::Administrator)
}

# Function to add a directory to PATH if not already present
function Add-ToPath {
    param ([string]$dir)
    if (-not [string]::IsNullOrEmpty($dir) -and (Test-Path $dir)) {
        if ($env:Path -notmatch [regex]::Escape($dir)) {
            $env:Path += ";$dir"
            [System.Environment]::SetEnvironmentVariable("Path", $env:Path, [System.EnvironmentVariableTarget]::Machine)
            Write-Host "Added to PATH: $dir"
        } else {
            Write-Host "Already in PATH: $dir"
        }
    }
}

# Function to check if executable exists using `where.exe`
function Find-WithWhere {
    param ([string]$exe)
    $result = where.exe $exe 2>$null
    if ($result) {
        return [System.IO.Path]::GetDirectoryName($result)
    }
    return $null
}

# Function to find executables using Everything Search (`es.exe`)
function Find-WithEverything {
    param ([string]$exe)
    try {
        $path = es.exe $exe | Select-Object -First 1
        if ($path) {
            return [System.IO.Path]::GetDirectoryName($path)
        }
    } catch {
        Write-Host "Error using Everything Search for $exe"
    }
    return $null
}

# Function to search in `C:\index.txt` or temp index
function Find-InIndex {
    param ([string]$exe)
    $searchFile = if (Test-Path $indexFile) { $indexFile } elseif (Test-Path $tempIndexFile) { $tempIndexFile } else { $null }
    
    if ($searchFile) {
        $path = Get-Content $searchFile | Select-String -Pattern $exe | Select-Object -First 1
        if ($path) {
            return [System.IO.Path]::GetDirectoryName($path.ToString())
        }
    }
    return $null
}

# Function to install a package via Chocolatey
function Install-WithChocolatey {
    param ([string]$package)
    if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
        Write-Host "Chocolatey not found. Installing Chocolatey..."
        Set-ExecutionPolicy Bypass -Scope Process -Force
        Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        refreshenv
    }
    Write-Host "Installing $package via Chocolatey..."
    choco install $package -y
}

# Check & install dependencies
foreach ($exe in $requirements) {
    $found = $null

    # Try `where.exe` first
    $found = Find-WithWhere $exe

    # If `where.exe` fails, try Everything Search
    if (-not $found -and (Get-Command es.exe -ErrorAction SilentlyContinue)) {
        $found = Find-WithEverything $exe
    }

    # If `es.exe` fails, try searching the index file
    if (-not $found) {
        $found = Find-InIndex $exe
    }

    # If nothing is found, prompt to index the hard drive
    if (-not $found -and -not (Test-Path $indexFile) -and -not (Test-Path $tempIndexFile)) {
        $answer = Read-Host "Do you want to index your hard drive to auto-detect dependencies? (Y/N)"
        if ($answer -match "^[Yy]$") {
            if (Test-Admin) {
                Write-Host "Indexing hard drive (admin mode)..."
                Get-ChildItem -Path C:\ -Recurse -Filter "*.exe" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName } | Out-File $indexFile
                Write-Host "Index created at C:\index.txt"
            } else {
                Write-Host "Indexing hard drive (user mode)..."
                Get-ChildItem -Path C:\ -Recurse -Filter "*.exe" -ErrorAction SilentlyContinue | ForEach-Object { $_.FullName } | Out-File $tempIndexFile
                Write-Host "Index created at $tempIndexFile"
            }
        }
    }

    # If found, add to PATH
    if ($found) {
        Add-ToPath $found
    } else {
        # If still not found, install via Chocolatey
        $package = $exe -replace ".exe", ""
        Install-WithChocolatey $package
    }
}

# Proceed with conversion to EXE
$BaseName = [System.IO.Path]::GetFileNameWithoutExtension($ScriptPath)
$CSFile = "$BaseName.cs"
$EXEFile = "$BaseName.exe"

# Obfuscate function names
function Generate-ObfuscatedName {
    $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return -join ((1..8) | ForEach-Object { $chars[(Get-Random -Maximum $chars.Length)] })
}

# Read and obfuscate PowerShell script
$ScriptContent = Get-Content $ScriptPath -Raw
$Matches = [regex]::Matches($ScriptContent, 'function\s+([A-Za-z_][A-Za-z0-9_]*)')
$ObfuscatedFunctions = @{}
foreach ($match in $Matches) {
    $origName = $match.Groups[1].Value
    if (-not $ObfuscatedFunctions.ContainsKey($origName)) {
        $ObfuscatedFunctions[$origName] = Generate-ObfuscatedName
    }
    $ScriptContent = $ScriptContent -replace "\b$origName\b", $ObfuscatedFunctions[$origName]
}

# Encode script
$EncodedScript = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($ScriptContent))

# Compile C# wrapper
Set-Content -Path $CSFile -Value @"
using System;
using System.Diagnostics;
using System.IO;
using System.Text;

class Program {
    static void Main() {
        string encodedScript = "$EncodedScript";
        string decodedScript = Encoding.UTF8.GetString(Convert.FromBase64String(encodedScript));
        string tempScriptPath = Path.Combine(Path.GetTempPath(), "obfuscated_script.ps1");

        File.WriteAllText(tempScriptPath, decodedScript);
        Process.Start("powershell.exe", "-ExecutionPolicy Bypass -NoProfile -File " + tempScriptPath).WaitForExit();
    }
}
"@

& "csc.exe" /target:exe /out:$EXEFile /optimize+ /platform:x64 /debug:none /nowarn "$CSFile"
Remove-Item -Force $CSFile
Write-Host "✅ Hardened EXE created: $EXEFile"
