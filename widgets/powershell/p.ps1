# Define path variables
$documentsPath = [System.Environment]::GetFolderPath([System.Environment+SpecialFolder]::MyDocuments)

$paths = @{
    widgets      = "D:\.rightthumb-widgets"
    PY           = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\python3.exe"
    pip3         = "C:\Users\Scott\AppData\Local\Microsoft\WindowsApps\pip3.exe"
    code_editor  = "C:\Windows\SysWOW64\notepad.exe"
    pip          = "D:\techApps\Python\Python36-32\Scripts\pip.exe"
    pip2         = "D:\techApps\Python\Python27\Scripts\pip.exe"
    py2          = "D:\techApps\Python\Python27\python.exe"
    pyf          = "C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1520.0_x64__qbz5n2kfra8p0\Lib"
    tech_drive   = "D:\.rightthumb-widgets"
    wprofile     = Join-Path $HOME ".rt\profile"
    w            = "D:\.rightthumb-widgets"
    ww           = "D:\.rightthumb-widgets\widgets"
    h            = Join-Path $HOME "\.rt\profile"
    pr           = Join-Path $HOME "\.rt\profile\projects"
    tt           = Join-Path $HOME "\.rt\profile\tables"
    ttt          = "D:\.rightthumb-widgets\widgets\databank\tables"
    p            = "D:\.rightthumb-widgets\widgets\batch\p.bat"
    rt           = Join-Path $HOME "\.rt"
    b            = "D:\.rightthumb-widgets\widgets\bash"
    bash         = "D:\.rightthumb-widgets\widgets\bash"
    s            = "D:\.rightthumb-widgets\widgets\batch"
    bat          = "D:\.rightthumb-widgets\widgets\batch"
    js           = "D:\.rightthumb-widgets\widgets\javascript"
    db           = "D:\.rightthumb-widgets\widgets\databank"
    ps           = "D:\.rightthumb-widgets\widgets\powershell"
    proc         = "D:\techApps\ProcessMonitor\Procmon64.exe"
    ps1          = Join-Path $$documentsPath "\WindowsPowerShell"
    wt           = Join-Path $HOME "\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
    python       = "D:\.rightthumb-widgets\widgets\python"
}

# Set variables with public visibility
foreach ($key in $paths.Keys) {
    Set-Variable -Name $key -Value $paths[$key] -Visibility Public
}

# Define the Python script path
$px = Join-Path $widgets "\widgets\python\$($args[0]).py"

# Run the Python script with the provided arguments
if ($args.Count -gt 0) {
    & $PY $px $args
} else {
    & $PY $px
}
