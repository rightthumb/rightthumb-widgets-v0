@echo off
call p. windowsExtendedPath -f %*

echo.
set shouldDel=n
set /p shouldDel=Del? [y/n]: 
if %shouldDel%==y (
    echo.
    call p. windowsExtendedPath -f %* -del
)

:: winExt.bat