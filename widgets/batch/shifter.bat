@echo off
setlocal enabledelayedexpansion

set "shifter="

shift

:loop
if "%1"=="" goto endloop
set "shifter=!shifter! "%1""
shift
goto loop

:endloop
endlocal & set "shifter=%shifter:~1%"







rem @echo off
rem setlocal enabledelayedexpansion

rem set "shifter="

rem shift

rem :loop
rem if "%1"=="" goto endloop
rem set "shifter=!shifter! %1"
rem shift
rem goto loop

rem :endloop
rem endlocal & set "shifter=%shifter:~1%"