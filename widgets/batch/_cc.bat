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

set /p Drive=<%userprofile%\.tk421
set widgets=%Drive:~0,1%
set Drive=
rem echo %widgets%
echo Loading...


IF NOT EXIST %widgets%\ (GOTO ERROR) 
IF EXIST %widgets%\ (GOTO START) 
:ERROR
prompt - 
cls
IF [] == [y] GOTO END
echo USB Drive Failure
set errorDisplayOnce=y
GOTO END
:START
call %widgets%\tech\scripts\c.bat %1 
GOTO END
:END