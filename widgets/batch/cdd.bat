@echo off
setlocal enabledelayedexpansion

:: Store the original parameter
set "param=%*"

:: Remove quotes from the parameter
set "stripped=!param:"=!"

:: Check for colon in the parameter
set "colonFound=false"
if "!param!" neq "!param::=!" set "colonFound=true"

:: Check if quotes were present and choose the correct cd command
if not "!param!"=="!stripped!" (
    :: Quotes were present
    %py% %widgets%\widgets\python\folder-registration.py
    if "!colonFound!"=="true" (
        cd /d %param%
    ) else (
        cd %param%
    )
    %py% %widgets%\widgets\python\folder-registration.py
) else (
    :: Quotes were not present
    %py% %widgets%\widgets\python\folder-registration.py
    if "!colonFound!"=="true" (
        cd /d "%param%"
    ) else (
        cd "%param%"
    )
    %py% %widgets%\widgets\python\folder-registration.py
)

endlocal
