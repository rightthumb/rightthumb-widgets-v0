@echo off
REM Check if Python is installed
python --version >NUL 2>&1
if errorlevel 1 (
    echo Python is not installed or not in the PATH. Exiting.
    exit /b 1
)

REM Install the packages
%pip3% install -r full_requre.txt

if errorlevel 1 (
    echo There was a problem installing the packages. Exiting.
    exit /b 1
)

echo All packages installed successfully!
pause
exit /b 0
