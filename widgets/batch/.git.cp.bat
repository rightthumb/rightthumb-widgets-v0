@echo off
REM ===============================
REM Run Git-force-push PowerShell script with arguments
REM ===============================

cd > %tmpf%
cd /d %widgets%


set SCRIPT_PATH="%widgets%\widgets\powershell\Git-force-push.ps1"

REM Call PowerShell with execution policy bypass (so it runs unsigned scripts)
powershell.exe -NoProfile -ExecutionPolicy Bypass -File %SCRIPT_PATH% --branch main --remote origin --retries 3


set /p back=<%tmpf%
cd /d %back%
