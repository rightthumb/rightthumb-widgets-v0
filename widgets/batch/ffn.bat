@echo off

if [%1] == [] GOTO CLEAR
GOTO START

:CLEAR
set indexindex=
GOTO END

:START
set search=%1
findstr /i /r /m "%search%" "%indexindex%"
:END
echo.