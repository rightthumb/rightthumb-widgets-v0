$pathsToSet = @(
    "D:\.rightthumb-widgets",
    "D:\techApps\Python\Python36-32",
    "D:\techApps\Python\Python27",
    "D:\.rightthumb-widgets\widgets",
    "C:\Users\Scott\.rt\profile"
)

foreach ($path in $pathsToSet) {
    if (Test-Path $path) {
        Set-Variable -Name ([System.IO.Path]::GetFileName($path)) -Value $path -Visibility Public
    } else {
        Write-Warning "Path $path does not exist."
    }
}

function choco. {
    param (
        [Parameter(Mandatory=$true)]
        [string[]]$Packages
    )
    
    $hostname = $env:COMPUTERNAME
    foreach ($chocoPackage in $Packages) {
        Write-Host "Starting installation of $chocoPackage on $hostname..."

        try {
            choco install -y $chocoPackage
            Write-Host "Installation of $chocoPackage successful on $hostname."
            Invoke-WebRequest -Uri "https://shell.sds.sh/install/choco/" -Method POST -ContentType "application/x-www-form-urlencoded" -Body "hostname=$hostname&choco=$chocoPackage"
        } catch {
            Write-Host "Failed to install $chocoPackage on $hostname."
        }
    }
}


# Aliases
$aliasesToSet = @{
    p = "$HOME\Documents\WindowsPowerShell\p.ps1"
    d = "$HOME\Documents\WindowsPowerShell\d.ps1"
    dd = "$HOME\Documents\WindowsPowerShell\dd.ps1"
    b = "$HOME\Documents\WindowsPowerShell\b.ps1"
    m = "$HOME\Documents\WindowsPowerShell\m.ps1"
    which = "$HOME\Documents\WindowsPowerShell\which.ps1"
    epy = "$HOME\Documents\WindowsPowerShell\epy.ps1"
    pss = "$HOME\Documents\WindowsPowerShell\pss.ps1"
    py = "python3"
}

foreach ($alias in $aliasesToSet.GetEnumerator()) {
    Set-Alias -Name $alias.Key -Value $alias.Value
}

# Add Path to $env:Path
$addPath = "D:\.rightthumb-widgets\widgets\python"
if (Test-Path $addPath -PathType Container) {
    $env:Path += ";$addPath"
}

# Chocolatey Profile
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path $ChocolateyProfile) {
    Import-Module "$ChocolateyProfile"
}



## Login Welcome Message and Hush Login: Start


# Check if .hushlogin_ps1 exists and write the command if not
if (-not (Test-Path "$env:USERPROFILE\.rt\.hushlogin_ps1")) {
    Write-Host "echo test | py `"$p\app.py`""
}

# Define a 'Hush' function to toggle or enforce hush
function Hush {
    param (
        [switch]$Force
    )

    $hushFile = "$env:USERPROFILE\.rt\.hushlogin_ps1"

    if ($Force) {
        if (-not (Test-Path $hushFile)) {
            New-Item -ItemType File -Path $hushFile -Force | Out-Null
        }
    } else {
        if (Test-Path $hushFile) {
            Remove-Item $hushFile
        } else {
            New-Item -ItemType File -Path $hushFile -Force | Out-Null
        }
    }
}

## Login Welcome Message and Hush Login: End




function tb {
    [CmdletBinding()]
    param (
        [Parameter(ValueFromPipeline=$true)]
        [Alias("InputObject")]
        [PSObject]$Data
    )
    
    process {
        $Data | Format-Table -AutoSize | Out-String
    }
}
