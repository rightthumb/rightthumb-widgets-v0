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


rem set /p shouldRun=Run? 

rem IF [%shouldRun%] == [n] GOTO:END
rem IF [%shouldRun%] == [N] GOTO:END
rem IF [%shouldRun%] == [NO] GOTO:END
rem IF [%shouldRun%] == [no] GOTO:END
rem IF [%shouldRun%] == [c] GOTO:END


rem :RUN
rem set /p Drive=<%userprofile%\widgets.txt
rem set widgets=%Drive:~0,1%
rem set Drive=
rem rem echo %widgets%
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
call %widgets%\widgets\batch\resetVars.bat
SET /p Drive=<%userprofile%\widgets.txt
SET widgets=%Drive:~0,1%
call %widgets%\widgets\batch\c.bat %1 
GOTO END
:END
cls


 
