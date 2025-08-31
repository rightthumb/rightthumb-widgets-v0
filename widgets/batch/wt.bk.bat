@echo off

setlocal
set from=%USERPROFILE%\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
set to=%USERPROFILE%\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settingsBK.json
copy %from% %to% /y
call p. fileBackup -flag lock -runonce -noschedule -f %from%
endlocal