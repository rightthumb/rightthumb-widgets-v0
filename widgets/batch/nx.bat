@echo off
setlocal EnableDelayedExpansion

rem Execute the command
if exist "%batch%\%1.bat" (
    call %*
) else (
    %*
)

rem Check error level and notify accordingly
if !errorlevel! equ 0 (
    call notify "Success: %*"
) else (
    call notify2 "Failed: %*"
)
