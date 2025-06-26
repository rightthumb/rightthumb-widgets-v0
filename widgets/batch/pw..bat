@echo off
setlocal enabledelayedexpansion

:: Use PowerShell to securely input a password
for /f %%A in ('powershell -command "$password = Read-Host -Prompt 'Enter your password' -AsSecureString; [System.Runtime.InteropServices.Marshal]::PtrToStringAuto([System.Runtime.InteropServices.Marshal]::SecureStringToBSTR($password))"') do set "password=%%A"

:: Display the entered password
echo Password entered: !password!

endlocal
