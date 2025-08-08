@echo off

if not [%2] == [] (
	call:makelink %*
	goto:eof
)

wsl
cd
goto:eof
:makelink
@echo off
setlocal enabledelayedexpansion

:: Check for administrative privileges
net session >nul 2>&1
if %errorLevel% neq 0 (
	echo Please run as administrator.
	pause
)

:: Check if source (src) and destination (dst) are provided
if "%~1"=="" OR "%~2"=="" (
	echo Usage: script_name.bat [source] [destination]
)

:: Set src and dst from command line arguments
set "src=%~1"
set "dst=%~2"

:: Detect if src is a file or a directory
if exist "%src%\" (
	echo Source is a directory
	echo Attempting to create symbolic link for directory...
	mklink /D "%dst%" "%src%"
	if errorlevel 1 (
		echo Failed to create symbolic link for directory.
		echo Attempting to copy directory...
		xcopy /E /I "%src%" "%dst%"
	)
) else if exist "%src%" (
	echo Source is a file
	echo Attempting to create hard link for file...
	mklink /H "%dst%" "%src%"
	if errorlevel 1 (
		echo Failed to create hard link for file.
		echo Attempting to copy file...
		copy "%src%" "%dst%"
	)
) else (
	echo Error: Source not found.
)

echo Done.
endlocal
goto:eof