@echo off
setlocal enabledelayedexpansion

rem Check for the 'uu' variable and call functions 'm back' and 'b' if it's set
if not "%uu%" == "" (
    call m back > nul
    call b %uu% > nul
)

rem Handling the case when no arguments are provided
if "%~1" == "" (
    echo -ago 3d
    call p. files -ago 3d + *.md --c | .mx u..
) else (
    rem Calculate the length of the first argument
    call :strlen "%~1"
    
    rem Check if the length of the argument is 1 (likely a single digit)
    if !length! == 1 (
        echo -ago %1d
        call p. files -ago %1d + *.md --c | .mx u..
    ) else (
        echo -ago %1
        call p. files -ago %1 + *.md --c | .mx u..
    )
)

rem Check again for the 'uu' variable and call 'b back' if it's set
if not "%uu%" == "" (
    call b back > nul
)

goto:eof

:strlen
rem Calculate the length of a string
call p. string-length -string %~1 > %tmpf%
set /p length=<%tmpf%
set /a length=%length%
goto:eof
