@echo off
if "%~1"=="" (
	echo Usage: pathAdd "C:\your\path"
	exit /b 1
)

set path=%path%;%~1

:: pathAdd2 for powershell version