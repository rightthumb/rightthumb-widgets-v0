@echo off
setlocal enabledelayedexpansion

REM === Input validation ===
if "%~1"=="" exit /b 1

set "newPath=%~1"
REM Remove trailing backslash
if "%newPath:~-1%"=="\" set "newPath=%newPath:~0,-1%"

REM === Check if already exists using registry ===
for /f "tokens=3*" %%A in ('reg query "HKCU\Environment" /v PATH 2^>nul') do set "oldPath=%%B"
echo !oldPath! | find /I "%newPath%" >nul
if not errorlevel 1 exit /b 0

REM === PowerShell: Append, Deduplicate, and Set PATH (User) ===
powershell -NoProfile -Command ^
	"$p=[Environment]::GetEnvironmentVariable('PATH','User');" ^
	"$p=($p -split ';') + '%newPath%';" ^
	"$p=$p | Where-Object { $_ -ne '' } | Select-Object -Unique;" ^
	"[Environment]::SetEnvironmentVariable('PATH',($p -join ';'),'User')"

endlocal
exit /b 0