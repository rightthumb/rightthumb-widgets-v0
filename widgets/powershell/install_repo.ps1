# PowerShell script to install Git and clone a repository

# Function to install Git on different platforms
function Install-Git {
    if ($IsWindows) {
        Write-Host "Installing Git on Windows..."
        # Install Git using Chocolatey
        if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
            Set-ExecutionPolicy Bypass -Scope Process -Force
            iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
        }
        choco install git -y
    } elseif ($IsLinux) {
        $distro = (lsb_release -is).ToLower()
        Write-Host "Detected Linux distribution: $distro"

        switch ($distro) {
            'ubuntu' {
                sudo apt-get update
                sudo apt-get install git -y
            }
            'debian' {
                sudo apt-get update
                sudo apt-get install git -y
            }
            'centos' {
                sudo yum install git -y
            }
            'fedora' {
                sudo dnf install git -y
            }
            'arch' {
                sudo pacman -S git --noconfirm
            }
            default {
                Write-Host "Unsupported Linux distribution: $distro"
                exit 1
            }
        }
    } elseif ($IsMacOS) {
        Write-Host "Installing Git on macOS..."
        # Install Git using Homebrew
        if (-not (Get-Command brew -ErrorAction SilentlyContinue)) {
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        }
        brew install git
    } else {
        Write-Host "Unsupported OS."
        exit 1
    }
}

# Function to clone the repository
function Clone-Repository {
    $repoUrl = "https://github.com/rightthumb/rightthumb-widgets-v0"
    $profileRoot = [System.Environment]::GetFolderPath('UserProfile')
    $targetDir = Join-Path -Path $profileRoot -ChildPath "rightthumb-widgets-v0"

    if (-not (Test-Path -Path $targetDir)) {
        git clone $repoUrl $targetDir
    } else {
        Write-Host "Repository already cloned at $targetDir"
    }
}

# Main script
$IsWindows = $false
$IsLinux = $false
$IsMacOS = $false

if ($PSVersionTable.PSVersion.Major -lt 6) {
    Write-Host "This script requires PowerShell 6.0 or higher."
    exit 1
}

if ($env:OS -match "Windows_NT") {
    $IsWindows = $true
} elseif ($env:OSTYPE -match "linux") {
    $IsLinux = $true
} elseif ($env:OSTYPE -match "darwin") {
    $IsMacOS = $true
}

Install-Git
Clone-Repository

