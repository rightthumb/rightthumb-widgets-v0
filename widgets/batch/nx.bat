@echo off
%*
if %errorlevel% equ 0 (
    call notify "Success: %*"
) else (
    call notify2 "Failed: %*"
)
