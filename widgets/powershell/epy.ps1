Set-Variable -Name "widgets" -Value "D:\.rightthumb-widgets" -Visibility Public
Set-Variable -Name "PY" -Value "D:\techApps\Python\Python36-32\python.exe" -Visibility Public
Set-Variable -Name "PY2" -Value "D:\techApps\Python\Python27\python.exe" -Visibility Public
Set-Variable -Name "pip3" -Value "D:\techApps\Python\Python36-32\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "code_editor" -Value "C:\Windows\SysWOW64\notepad.exe" -Visibility Public
Set-Variable -Name "pip" -Value "D:\techApps\Python\Python36-32\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "pip2" -Value "D:\techApps\Python\Python27\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "py2" -Value "D:\techApps\Python\Python27\python.exe" -Visibility Public
Set-Variable -Name "pyf" -Value "D:\techApps\Python\Python36-32" -Visibility Public
Set-Variable -Name "tech_drive" -Value "D:\.rightthumb-widgets" -Visibility Public
Set-Variable -Name "wprofile" -Value "C:\Users\Scott\.rt\profile" -Visibility Public
Set-Variable -Name "w" -Value "D:\.rightthumb-widgets" -Visibility Public
Set-Variable -Name "ww" -Value "D:\.rightthumb-widgets\widgets" -Visibility Public
Set-Variable -Name "h" -Value "C:\Users\Scott\.rt\profile" -Visibility Public
Set-Variable -Name "pr" -Value "C:\Users\Scott\.rt\profile\projects" -Visibility Public
Set-Variable -Name "tt" -Value "C:\Users\Scott\.rt\profile\tables" -Visibility Public
Set-Variable -Name "ttt" -Value "D:\.rightthumb-widgets\widgets\databank\tables" -Visibility Public
Set-Variable -Name "p" -Value "D:\.rightthumb-widgets\widgets\batch\p.bat" -Visibility Public
Set-Variable -Name "rt" -Value "C:\Users\Scott\.rt" -Visibility Public
Set-Variable -Name "b" -Value "D:\.rightthumb-widgets\widgets\bash" -Visibility Public
Set-Variable -Name "bash" -Value "D:\.rightthumb-widgets\widgets\bash" -Visibility Public
Set-Variable -Name "s" -Value "D:\.rightthumb-widgets\widgets\batch" -Visibility Public
Set-Variable -Name "bat" -Value "D:\.rightthumb-widgets\widgets\batch" -Visibility Public
Set-Variable -Name "js" -Value "D:\.rightthumb-widgets\widgets\javascript" -Visibility Public
Set-Variable -Name "db" -Value "D:\.rightthumb-widgets\widgets\databank" -Visibility Public
Set-Variable -Name "ps" -Value "D:\.rightthumb-widgets\widgets\powershell" -Visibility Public
Set-Variable -Name "proc" -Value "D:\techApps\ProcessMonitor\Procmon64.exe" -Visibility Public
Set-Variable -Name "ps1" -Value "C:\Users\Scott\Documents\WindowsPowerShell" -Visibility Public
Set-Variable -Name "wt" -Value "C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json" -Visibility Public
Set-Variable -Name "python" -Value "D:\.rightthumb-widgets\widgets\python" -Visibility Public
$widgets="D:\.rightthumb-widgets"
$PY="D:\techApps\Python\Python36-32\python.exe"
$PY2="D:\techApps\Python\Python27\python.exe"
$pip3="D:\techApps\Python\Python36-32\Scripts\pip.exe"
$code_editor="C:\Windows\SysWOW64\notepad.exe"
$pip="D:\techApps\Python\Python36-32\Scripts\pip.exe"
$pip2="D:\techApps\Python\Python27\Scripts\pip.exe"
$py2="D:\techApps\Python\Python27\python.exe"
$pyf="D:\techApps\Python\Python36-32"
$tech_drive="D:\.rightthumb-widgets"
$wprofile="C:\Users\Scott\.rt\profile"
$w="D:\.rightthumb-widgets"
$ww="D:\.rightthumb-widgets\widgets"
$h="C:\Users\Scott\.rt\profile"
$pr="C:\Users\Scott\.rt\profile\projects"
$tt="C:\Users\Scott\.rt\profile\tables"
$ttt="D:\.rightthumb-widgets\widgets\databank\tables"
$p="D:\.rightthumb-widgets\widgets\batch\p.bat"
$rt="C:\Users\Scott\.rt"
$b="D:\.rightthumb-widgets\widgets\bash"
$bash="D:\.rightthumb-widgets\widgets\bash"
$s="D:\.rightthumb-widgets\widgets\batch"
$bat="D:\.rightthumb-widgets\widgets\batch"
$js="D:\.rightthumb-widgets\widgets\javascript"
$db="D:\.rightthumb-widgets\widgets\databank"
$ps="D:\.rightthumb-widgets\widgets\powershell"
$proc="D:\techApps\ProcessMonitor\Procmon64.exe"
$ps1="C:\Users\Scott\Documents\WindowsPowerShell"
$wt="C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
$python="D:\.rightthumb-widgets\widgets\python"
Set-Variable -Name "widgets" -Value $tech_drive
$widgets=$tech_drive

$px=$widgets+"\widgets\python\" + $args[0] + ".py"


REM Begin Copy
powershell
Set-Content $np+"subl.bat" "@echo off"
Add-Content $np+"subl.bat" "start $nf " + $px
if (!($Env:Path.Contains("Sublime"))) {[System.Environment]::SetEnvironmentVariable("PATH", $Env:Path + ";"+$np, "Machine")}
exit
REM End Copy