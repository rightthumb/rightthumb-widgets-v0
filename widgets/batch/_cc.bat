@echo off
set /p Drive=<%userprofile%\.tk421
set widgets=%Drive:~0,1%
set Drive=
rem echo %widgets%
echo Loading...


IF NOT EXIST %widgets%:\ (GOTO ERROR) 
IF EXIST %widgets%:\ (GOTO START) 
:ERROR
prompt - 
cls
IF [] == [y] GOTO END
echo USB Drive Failure
set errorDisplayOnce=y
GOTO END
:START
call %widgets%:\tech\scripts\c.bat %1 
GOTO END
:END
