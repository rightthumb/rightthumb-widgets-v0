@echo off
setlocal enabledelayedexpansion

if "%~1"=="" (
    echo Usage: pathRemove.bat "FolderToRemove"
    exit /b
)

set "remove=%~1"
set "oldpath=%PATH%"
set "newpath="

:: Loop through each path entry
for %%A in ("%oldpath:;=" "%") do (
    if /I not "%%~A"=="%remove%" (
        set "newpath=!newpath!;%%~A"
    )
)

:: Remove leading semicolon if exists
if "!newpath:~0,1!"==";" set "newpath=!newpath:~1!"

:: Set the cleaned PATH for the current session only
set PATH=!newpath!

:: Show the new PATH
@REM echo Updated PATH:
@REM echo !newpath!

