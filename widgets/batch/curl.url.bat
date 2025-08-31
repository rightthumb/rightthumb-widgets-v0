@echo off
setlocal enabledelayedexpansion

:: Check if curl is available
where curl >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: curl is not available in your PATH.
    echo Please install curl or add it to your system PATH.
    exit /b 1
)

:: Check if URL argument is provided
if "%~1"=="" (
    echo Usage: %~n0 "URL"
    echo Example: %~n0 "http://example.com"
    exit /b 1
)

:: Run curl command and capture output
for /f "delims=" %%i in ('curl -sL -w "%%{url_effective}" -o NUL "%~1"') do set "final_url=%%i"

:: Display results
@REM echo Input URL:   %~1
@REM echo Final URL:   !final_url!
echo !final_url!