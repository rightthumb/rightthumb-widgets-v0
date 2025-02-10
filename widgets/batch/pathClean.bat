@echo off
setlocal enabledelayedexpansion

:: Get the current PATH
set "oldpath=%PATH%"
set "newpath="

:: Loop through each path entry
for %%A in ("%oldpath:;=" "%") do (
    set "found="
    
    :: Check if the path is already in newpath
    for %%B in (!newpath!) do (
        if "%%~B"=="%%~A" set "found=1"
    )

    :: Append if not duplicate
    if not defined found set "newpath=!newpath!;%%~A"
)

:: Remove leading semicolon if exists
if "!newpath:~0,1!"==";" set "newpath=!newpath:~1!"

:: Set the cleaned PATH for the current session only
set PATH=!newpath!

:: Show the new PATH
@REM echo New PATH:
echo !newpath!

@REM pause
