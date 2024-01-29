 
$pathsToSet = @(
    "D:\.rightthumb-widgets",
    "D:\.rightthumb-widgets\widgets",
    "D:\.rightthumb-widgets\widgets\powershell",
    "D:\techApps\Python\Python36-32",
    "D:\techApps\Python\Python27",
    "C:\Users\Scott\.rt\profile"
)

foreach ($path in $pathsToSet) {
    if (Test-Path $path) {
        Set-Variable -Name ([System.IO.Path]::GetFileName($path)) -Value $path -Visibility Public
    } else {
        Write-Warning "Path $path does not exist."
    }
}

$documentsPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::MyDocuments)


$aliasesToSet = @{
    p = "$documentsPath\WindowsPowerShell\p.ps1"
    d = "$documentsPath\WindowsPowerShell\d.ps1"
    dd = "$documentsPath\WindowsPowerShell\dd.ps1"
    # b = "$documentsPath\WindowsPowerShell\b.ps1"
    # m = "$documentsPath\WindowsPowerShell\m.ps1"
    which = "$documentsPath\WindowsPowerShell\which.ps1"
    epy = "$documentsPath\WindowsPowerShell\epy.ps1"
    pss = "$documentsPath\WindowsPowerShell\pss.ps1"
    py = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"


    # widgets = "D:\.rightthumb-widgets"
    # PY2 = "D:\techApps\Python\Python27\python.exe"
    # pip3 = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\pip3.exe"
    # code_editor = "C:\Program Files\Microsoft VS Code\Code.exe"
    # php = "D:\xampp\php\php.exe"
    # pip = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\pip3.exe"
    # pip2 = "D:\techApps\Python\Python27\Scripts\pip.exe"
    # pyf = "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib"
    # tech_drive = "D:\.rightthumb-widgets"
    # wprofile = "C:\Users\Scott\.rt\profile"
    # w = "D:\.rightthumb-widgets"
    # ww = "D:\.rightthumb-widgets\widgets"
    # h = "C:\Users\Scott\.rt\profile"
    # pr = "C:\Users\Scott\.rt\profile\projects"
    # tt = "C:\Users\Scott\.rt\profile\tables"
    # ttt = "D:\.rightthumb-widgets\widgets\databank\tables"
    # rt = "C:\Users\Scott\.rt"
    # bash = "D:\.rightthumb-widgets\widgets\bash"
    # s = "D:\.rightthumb-widgets\widgets\batch"
    # bat = "D:\.rightthumb-widgets\widgets\batch"
    # js = "D:\.rightthumb-widgets\widgets\javascript"
    # db = "D:\.rightthumb-widgets\widgets\databank"
    # ps = "D:\.rightthumb-widgets\widgets\powershell"
    # proc = "D:\techApps\ProcessMonitor\Procmon64.exe"
    # ps1 = "C:\Users\Scott\Documents\WindowsPowerShell"
    # wt = "C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
    # npp = "C:\Program Files\Sublime Text\sublime_text.exe"

}

function m {
    param (
        [string]$a
    )

    $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
    $pyscript = "D:\.rightthumb-widgets\widgets\python\m.py"

    # Build the command to execute
    $command = "$pythonPath $pyscript -a $a"

    # Execute the command and capture its output
    $path = Invoke-Expression $command
    Write-Host $path
}

function b {
    param (
        [string]$a
    )

    $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
    $pyscript = "D:\.rightthumb-widgets\widgets\python\b.py"

    # Build the command to execute
    $command = "$pythonPath $pyscript -a $a"

    # Execute the command and capture its output
    $path = Invoke-Expression $command

    # Change the current directory to the output directory
    Set-Location -Path $path -PassThru
}

# Get-WmiObject Win32_DiskDrive | Select-Object Model, DeviceID | py $p\pwsh-table.py
# Get-WmiObject Win32_DiskDrive | Select-Object Model, DeviceID | pp pwsh-table



function ppp {
    [CmdletBinding()]
    param (
        [string]$r,
        [string]$TheArgs,

        [Parameter(ValueFromPipeline=$true)]
        [Alias("InputObject")]
        [PSObject]$Data

    )
    
    begin {
        $list = New-Object 'System.Collections.Generic.List[PSObject]'
        $isTable = $false
    }
    
    process {
        $list.Add($Data)
        if ($Data -is [System.Data.DataTable]) {
            $isTable = $true
        }
    }
    
    end {
        $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
        $pyscript = "D:\.rightthumb-widgets\widgets\python\$r.py"
    
        if ((Test-Path $pythonPath -PathType Leaf) -and (Test-Path $pyscript)) {
            $scriptInput = if ($isTable) { $list | Format-Table -AutoSize | Out-String } else { $list | Out-String }
    
            try {
                # Pipe the script input directly to the Python script
                $scriptInput | & $pythonPath $pyscript + $TheArgs
    
            } catch {
                Write-Error "Failed to execute Python script: $_"
            }
        }
        else {
            Write-Error "Python executable or script file not found"
        }
    }
    
}



function pp {
    [CmdletBinding()]
    param (
        [string]$r,

        [Parameter(ValueFromPipeline=$true)]
        [Alias("InputObject")]
        [PSObject]$Data

    )
    
    begin {
        $list = New-Object 'System.Collections.Generic.List[PSObject]'
        $isTable = $false
    }
    
    process {
        $list.Add($Data)
        if ($Data -is [System.Data.DataTable]) {
            $isTable = $true
        }
    }
    
    end {
        $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
        $pyscript = "D:\.rightthumb-widgets\widgets\python\$r.py"
    
        if ((Test-Path $pythonPath -PathType Leaf) -and (Test-Path $pyscript)) {
            $scriptInput = if ($isTable) { $list | Format-Table -AutoSize | Out-String } else { $list | Out-String }
    
            try {
                # Pipe the script input directly to the Python script
                $scriptInput | & $pythonPath $pyscript
    
            } catch {
                Write-Error "Failed to execute Python script: $_"
            }
        }
        else {
            Write-Error "Python executable or script file not found"
        }
    }
    
}



function p3 {
    Param (
        [string]$r,
        [string[]]$AdditionalArgs
    )
    $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
    if (Test-Path $pythonPath -PathType Leaf) {
        # Run the Python script using the specified Python executable and script file
        $pyscript = "D:\.rightthumb-widgets\widgets\python\$r.py"
        Write-Host $AdditionalArgs
        & $pythonPath $pyscript $AdditionalArgs
    }
    else {
        Write-Host "Python executable not found at the specified path."
    }
}

function p2 {
    [CmdletBinding()]
    Param (
        [string]$scriptFile
    )
    
    $pythonPath = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"

    if (Test-Path $pythonPath -PathType Leaf) {
        if ($PSCmdlet.MyInvocation.ExpectingInput) {
            # Read input from the pipeline
            $inputData = $input | Out-String

            # Run the Python script using the specified Python executable and script file
            $pyscript = "D:\.rightthumb-widgets\widgets\python\$scriptFile.py"
            $inputData | & $pythonPath $pyscript
        }
        else {
            Write-Host "No data received from the pipeline. Provide input via pipeline to use this function."
        }
    }
    else {
        Write-Host "Python executable not found at the specified path."
    }
}




foreach ($alias in $aliasesToSet.GetEnumerator()) {
    Set-Alias -Name $alias.Key -Value $alias.Value 
    Set-Variable $alias.Key -Value $alias.Value  -Visibility Public
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
$p = "D:\.rightthumb-widgets\widgets\python"
Write-Output "echo test | py `$p\line.py"

function tb0 {
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
function tb {
    [CmdletBinding()]
    param (
        [Parameter(ValueFromPipeline=$true)]
        [Alias("InputObject")]
        [PSObject]$Data
    )
    
    begin {
        $table = @()
    }
    
    process {
        $table += $Data
    }
    
    end {
        $table | Format-Table -AutoSize | Out-String
    }
}
