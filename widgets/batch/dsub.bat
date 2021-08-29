@echo off
set do=dir /s/b *%1*



IF NOT "%1" == "" GOTO FIND
dir /b
set do=dir /b
GOTO ENDD
:FIND
IF "%2" == "s" GOTO SUB
dir /b %1
set do=dir /b %1
GOTO ENDD

v 3

:SUB
%do%
GOTO ENDD

:ENDD
ENDLOCAL