@echo off
@REM call D:\.rightthumb-widgets\widgets\batch\c.bat
@REM call p. fileBackupBackup
%userprofile%\AppData\Local\Microsoft\WindowsApps\python3.exe D:\.rightthumb-widgets\widgets\python\fileBackupBackup.py

:: Related to:
:: bkbk.bat



:: Scheduled!!
:: schtasks /create /tn "bkbk-recover_Evening" /tr "\"D:\.rightthumb-widgets\widgets\batch\bkbk-recover.bat\"" /sc DAILY /st 20:00  /ru SYSTEM

:: schtasks /delete /tn "bkbk-recover_Evening" /f






setlocal EnableDelayedExpansion

:: Extract date components from %date%
:: This assumes your system date format is MM/DD/YYYY or similar. Adjust tokens as needed.

for /f "tokens=1-3 delims=/- " %%a in ("%date%") do (
	set "mm=%%a"
	set "dd=%%b"
	set "yyyy=%%c"
)

:: Handle two-digit year formats (rare)
if "!yyyy!" LSS "100" (
	set /a "yyyy=2000+yyyy"
)

:: Zero-pad if needed
if 1!mm! LSS 110 set "mm=0!mm!"
if 1!dd! LSS 110 set "dd=0!dd!"

:: Combine into ISO format
set "folderDate=!yyyy!-!mm!-!dd!"




c:
cd %userprofile%\.rt\profile\tables\backup_log
set "saveTo=old\!folderDate!"
move *.json !saveTo! >nul 2>&1

call bkbk

:: Create the folder
mkdir "!folderDate!"

:: Output
echo Folder created: !folderDate!