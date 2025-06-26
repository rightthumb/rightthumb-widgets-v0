@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

REM Loop through all files in the current directory of the batch file
for %%f in (*) do (
    REM Check if the file is not the batch file itself
    if %%f NEQ %~nx0 (
        REM Rename the file by adding an underscore to the beginning
        ren "%%f" "_%%f"
    )
)

ENDLOCAL
