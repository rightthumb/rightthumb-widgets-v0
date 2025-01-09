@echo off
REM Check if the argument (%1) is provided
if "%~1"=="" (
    echo Usage: PythonPathSetup.bat "path_to_python.exe"
    exit /b 1
)

set py=%1

REM Extract the base directory from the provided path
set "PYTHON_DIR=%~dp1"

REM Remove the trailing backslash if it exists
if "%PYTHON_DIR:~-1%"=="\" set "PYTHON_DIR=%PYTHON_DIR:~0,-1%"

REM Append the base directory and the Scripts subdirectory to the PATH
echo Adding "%PYTHON_DIR%" and "%PYTHON_DIR%\Scripts" to PATH...
setx PATH "%PATH%;%PYTHON_DIR%;%PYTHON_DIR%\Scripts"

echo PATH updated successfully!
pause
