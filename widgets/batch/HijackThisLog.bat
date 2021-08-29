@echo off
call m stmp
call b sd
set thisFile=HijackThisLog.php
%php% %phpFiles%\%thisFile%
echo.
start "" notepad HijackThis_WhitelistCMD.txt
call b stmp