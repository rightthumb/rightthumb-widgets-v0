@echo off

if [%1] == [] GOTO CLEAR
GOTO START

:CLEAR
set indexindex=
GOTO END

:START
call ftmp %1 %2 %3 %4 %5 %6 %7 %8 %9

:END
echo.