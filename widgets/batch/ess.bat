@echo off
:: Enable Delayed Expansion for Proper Variable Handling
setlocal enabledelayedexpansion

:: Default to 1
set "nDays=1"

:: Check if %1 is a number
if not "%1"=="" (
	set /a testval=%1 2>nul
	if "!testval!"=="%1" set "nDays=%1"
)

:: Display Values for Debugging
@REM echo Input Days: %1
@REM echo Parsed Days: %nDays%

:: Display Files
echo.
echo Files:
echo.
es.exe dm:last%nDays%days type:file | p. line --c - %es% backup logs temp | p. files --c | sort | p. line %*
echo.
echo.

:: Display Folders
echo Folders:
echo.
es.exe dm:last%nDays%days type:folder | p. line --c - %es% backup logs temp | p. isFolder | sort | p. line %*
echo.
echo.
echo.

endlocal