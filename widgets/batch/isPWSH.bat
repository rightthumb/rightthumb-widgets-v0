@echo off

@REM setlocal
CALL :GETPARENT PARENT

IF /I "%PARENT%" == "WindowsTerminal" (
    set isPWSH=no
) ELSE IF /I "%PARENT%" == "cmd" (
    set isPWSH=no
) ELSE IF /I "%PARENT%" == "pwsh" (
    set isPWSH=yes
) ELSE (
    set isPWSH=yes
)
set isPWSHp=%PARENT%
if not [%1] == [] echo isPWSH = %isPWSH%
@REM endlocal

GOTO :EOF

:GETPARENT
:: Fetch parent process name, handling possible errors
SET "PSCMD=$ppid=$pid; for ($i=0; $i -lt 3; $i++) { $ppid=(Get-CimInstance Win32_Process -Filter ('ProcessID='+$ppid)).ParentProcessId }; (Get-Process -EA Ignore -ID $ppid).Name"

for /f "tokens=*" %%i in ('powershell -NoProfile -ExecutionPolicy Bypass -Command "%PSCMD%"') do SET %1=%%i
GOTO :EOF
