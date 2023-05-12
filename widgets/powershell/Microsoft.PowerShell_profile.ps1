Set-Variable -Name "widgets" -Value "D:\.rightthumb-widgets" -Visibility Public
Set-Variable -Name "PY" -Value "D:\techApps\Python\Python36-32\python.exe" -Visibility Public
Set-Variable -Name "PY2" -Value "D:\techApps\Python\Python27\python.exe" -Visibility Public
Set-Variable -Name "pip3" -Value "D:\techApps\Python\Python36-32\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "code_editor" -Value "C:\Windows\SysWOW64\notepad.exe" -Visibility Public
Set-Variable -Name "php" -Value "D:\php\php.exe" -Visibility Public
Set-Variable -Name "pip" -Value "D:\techApps\Python\Python36-32\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "pip2" -Value "D:\techApps\Python\Python27\Scripts\pip.exe" -Visibility Public
Set-Variable -Name "py2" -Value "D:\techApps\Python\Python27\python.exe" -Visibility Public
Set-Variable -Name "pyf" -Value "D:\techApps\Python\Python36-32" -Visibility Public
Set-Variable -Name "tech_drive" -Value "C:\rightthumb-widgets-v0" -Visibility Public
Set-Variable -Name "wprofile" -Value "C:\Users\Scott\.rt\profile" -Visibility Public
Set-Variable -Name "w" -Value "D:\.rightthumb-widgets" -Visibility Public
Set-Variable -Name "ww" -Value "D:\.rightthumb-widgets\widgets" -Visibility Public
Set-Variable -Name "h" -Value "C:\Users\Scott\.rt\profile" -Visibility Public
Set-Variable -Name "pr" -Value "C:\Users\Scott\.rt\profile\projects" -Visibility Public
Set-Variable -Name "tt" -Value "C:\Users\Scott\.rt\profile\tables" -Visibility Public
Set-Variable -Name "ttt" -Value "C:\rightthumb-widgets-v0\widgets\databank\tables" -Visibility Public
Set-Variable -Name "p" -Value "D:\.rightthumb-widgets\widgets\batch\p.bat" -Visibility Public
Set-Variable -Name "rt" -Value "C:\Users\Scott\.rt" -Visibility Public
Set-Variable -Name "b" -Value "C:\rightthumb-widgets-v0\widgets\bash" -Visibility Public
Set-Variable -Name "bash" -Value "C:\rightthumb-widgets-v0\widgets\bash" -Visibility Public
Set-Variable -Name "s" -Value "C:\rightthumb-widgets-v0\widgets\batch" -Visibility Public
Set-Variable -Name "bat" -Value "C:\rightthumb-widgets-v0\widgets\batch" -Visibility Public
Set-Variable -Name "js" -Value "C:\rightthumb-widgets-v0\widgets\javascript" -Visibility Public
Set-Variable -Name "db" -Value "C:\rightthumb-widgets-v0\widgets\databank" -Visibility Public
Set-Variable -Name "ps" -Value "C:\rightthumb-widgets-v0\widgets\powershell" -Visibility Public
Set-Variable -Name "proc" -Value "D:\techApps\ProcessMonitor\Procmon64.exe" -Visibility Public
Set-Variable -Name "ps1" -Value "C:\Users\Scott\Documents\WindowsPowerShell" -Visibility Public
Set-Variable -Name "wt" -Value "C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json" -Visibility Public
Set-Variable -Name "python" -Value "D:\.rightthumb-widgets\widgets\python" -Visibility Public
$widgets="D:\.rightthumb-widgets"
$PY="D:\techApps\Python\Python36-32\python.exe"
$PY2="D:\techApps\Python\Python27\python.exe"
$pip3="D:\techApps\Python\Python36-32\Scripts\pip.exe"
$code_editor="C:\Windows\SysWOW64\notepad.exe"
$php="D:\php\php.exe"
$pip="D:\techApps\Python\Python36-32\Scripts\pip.exe"
$pip2="D:\techApps\Python\Python27\Scripts\pip.exe"
$py2="D:\techApps\Python\Python27\python.exe"
$pyf="D:\techApps\Python\Python36-32"
$tech_drive="C:\rightthumb-widgets-v0"
$wprofile="C:\Users\Scott\.rt\profile"
$w="D:\.rightthumb-widgets"
$ww="D:\.rightthumb-widgets\widgets"
$h="C:\Users\Scott\.rt\profile"
$pr="C:\Users\Scott\.rt\profile\projects"
$tt="C:\Users\Scott\.rt\profile\tables"
$ttt="C:\rightthumb-widgets-v0\widgets\databank\tables"
$p="D:\.rightthumb-widgets\widgets\batch\p.bat"
$rt="C:\Users\Scott\.rt"
$b="C:\rightthumb-widgets-v0\widgets\bash"
$bash="C:\rightthumb-widgets-v0\widgets\bash"
$s="C:\rightthumb-widgets-v0\widgets\batch"
$bat="C:\rightthumb-widgets-v0\widgets\batch"
$js="C:\rightthumb-widgets-v0\widgets\javascript"
$db="C:\rightthumb-widgets-v0\widgets\databank"
$ps="C:\rightthumb-widgets-v0\widgets\powershell"
$proc="D:\techApps\ProcessMonitor\Procmon64.exe"
$ps1="C:\Users\Scott\Documents\WindowsPowerShell"
$wt="C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json"
$python="D:\.rightthumb-widgets\widgets\python"
Set-Variable -Name "widgets" -Value $tech_drive
$widgets=$tech_drive


Set-Variable -Name "p" -Value $widgets+"\widgets\python"
Set-Alias -Name p -Value $HOME"\Documents\WindowsPowerShell\p.ps1"
Set-Alias -Name d -Value $HOME"\Documents\WindowsPowerShell\d.ps1"
Set-Alias -Name dd -Value $HOME"\Documents\WindowsPowerShell\dd.ps1"
Set-Alias -Name b -Value $HOME"\Documents\WindowsPowerShell\b.ps1"
Set-Alias -Name m -Value $HOME"\Documents\WindowsPowerShell\m.ps1"
Set-Alias -Name which -Value $HOME"\Documents\WindowsPowerShell\which.ps1"
Set-Alias -Name epy -Value $HOME"\Documents\WindowsPowerShell\epy.ps1"
Set-Alias -Name pss -Value $HOME"\Documents\WindowsPowerShell\pss.ps1"
Set-Alias -Name py -Value "python3"


$p=$widgets+"\widgets\python"
$addPath = $widgets+"\widgets\python"
$regexAddPath = [regex]::Escape($addPath)
$arrPath = $env:Path -split ';' | Where-Object {$_ -notMatch 
"^$regexAddPath\\?"}
$env:Path = ($arrPath + $addPath) -join ';'



$widgets="C"
if (  Test-Path $env:userprofile\.tk421  ) {
	$widgets=(cat $env:userprofile\.tk421) -join "`n"
}


# if (  Test-Path "D:\Program Files\Sublime Text 3\sublime_text.exe"  ) {

# 	$code_editor="D:\Program Files\Sublime Text 3\sublime_text.exe"
# 	$np="D:\Program Files\Sublime Text 3\"
# 	$nf="sublime_text.exe"

# } elseif (  Test-Path $widgets+"\Sublime Text Build 3211\sublime_text.exe"  ) {

# 	$code_editor=$widgets+"\Sublime Text Build 3211\sublime_text.exe"
# 	$np=$widgets+"\Sublime Text Build 3211\"
# 	$nf="sublime_text.exe"

# } else {
# 	$code_editor="D:\Windows\system32\notepad.exe"
# 	$np="D:\Windows\system32\"
# 	$nf="notepad.exe"
# }
# echo $widgets
# echo $n
# if (!(Test-Path $env:userprofile\.tk421) -and !(Test-Path $userfile)) {

# echo "Peanut Butter Jelly Time"
# Chocolatey profile
$ChocolateyProfile = "$env:ChocolateyInstall\helpers\chocolateyProfile.psm1"
if (Test-Path($ChocolateyProfile)) {
  Import-Module "$ChocolateyProfile"
}
Set-Variable -Name "n" -Value $n
echo "echo test | py `$p\app.py"
echo ""
