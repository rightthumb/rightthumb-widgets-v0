@echo off
setlocal enabledelayedexpansion

set "input=%~1"

:: Check if input ends with .exe
if /i "%input:~-4%"==".exe" (
    set "processName=%input%"
) else (
    set "processName=%input%.exe"
)

:: Kill the process
taskkill /im "!processName!" /f
