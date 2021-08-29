@echo off
IF "%1" == "p" (set prmpt=%2)


if /I "%prmpt%" == "" GOTO P1
:N1
prompt -
call note.bat
GOTO END

set e=Error
echo %e%

:P1
call note.bat


GOTO N1
cls
echo %e%
:END
