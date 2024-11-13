@echo off

setlocal
set from=C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settings.json
set to=C:\Users\Scott\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState\settingsBK.json
copy %from% %to% /y
call p. fileBackup -flag lock -runonce -noschedule -f %from%
endlocal

