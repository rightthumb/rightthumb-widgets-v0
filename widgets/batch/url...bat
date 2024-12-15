@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

call p. open-url -url %*

goto:eof


rem alias u.bat

if [%1] == [] (
    call p. url
    goto:eof
)

setlocal enabledelayedexpansion

set theScript=%USERPROFILE%\Downloads\URL-SCRIPT.py

REM Check if URL or code is provided
if "%~1"=="" (
    echo ERROR: no URL, ex: u ^<url^> [args...]
    exit /b 1
)

REM Check if %1 ends in .py and append it if not
set filename=%~1
if /I not "%~x1"==".py" (
    set filename=%~1.py
)

REM Form the URL
set URL=https://rightthumb.com/apps/code/py/%filename%

REM Download the script using PowerShell and hide output
powershell -Command "Invoke-WebRequest -Uri '%URL%' -OutFile '%theScript%' >$null 2>&1"

REM Form the remaining arguments string
set args=%*
set args=!args:%~1=!

REM Run the Python file
python "%theScript%" !args!

REM Delete the Python file
del "%theScript%"

endlocal
