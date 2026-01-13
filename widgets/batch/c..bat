@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##


CALL:RUN >nul 2>&1
cls
GOTO:EOF
:RUN
set /p Drive=<%userprofile%\.tk421
set widgets=%Drive:~0,1%
set Drive=
rem echo %widgets%
echo Loading...


IF EXIST "%widgets%\" (CALL:START)
IF NOT EXIST "%widgets%\" (CALL:ERROR) 
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
call %widgets%\widgets\batch\resetVars.bat

SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%
call %widgets%\widgets\batch\c.bat %1 
GOTO:EOF