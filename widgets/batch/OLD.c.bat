@echo off
IF "%1" == "a" GOTO AUTO
IF "%1" == "" GOTO SALLY
IF "%1" == "h" GOTO HELP
IF "%1" == "help" GOTO HELP
IF "%1" == "?" GOTO HELP
IF "%1" == "/?" GOTO HELP
GOTO SALLY
:AUTO
call name2 %username% %computername%
GOTO SALLY
:HELP
cls

echo --------------------

echo e note.bat = edit title and echo text
echo --------------------
echo name [new] = change display name on c.bat
:echo me [new] = change display name on c.bat

echo --------------------
pause


:SALLY
call %systemroot%/system32/sally.bat