@echo off

CALL:RUN >nul 2>&1
cls
GOTO:EOF
:RUN
set /p Drive=<%userprofile%\.tk421
set widgets=%Drive:~0,1%
set Drive=
rem echo %widgets%
echo Loading...


IF EXIST "%widgets%:\" (CALL:START)
IF NOT EXIST "%widgets%:\" (CALL:ERROR) 
GOTO:EOF
:ERROR
prompt - 
cls
IF [] == [y] GOTO:EOF
echo USB Drive Failure
set errorDisplayOnce=y
GOTO:EOF
:START

rem disable
call %widgets%:\widgets\batch\resetVars.bat

SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%
call %widgets%:\widgets\batch\c.bat %1 
GOTO:EOF
