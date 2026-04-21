@echo off
setlocal enabledelayedexpansion

:: initialize variables
set "shifter="
set "shifter1="

:: first argument
set "shifter1=%~1"
shift

:loop
if "%~1"=="" goto endloop
if "!shifter!"=="" (
	set "shifter=%~1"
) else (
	set "shifter=!shifter! %~1"
)
shift
goto loop

:endloop
:: export variables globally
endlocal & (
	set "shifter1=%shifter1%"
	set "shifter=%shifter%"
)