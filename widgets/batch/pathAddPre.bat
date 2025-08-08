@echo off
if "%~1"=="" (
	echo Usage: append_path.bat "C:\your\path"
	exit /b 1
)

set path=%~1;%path%