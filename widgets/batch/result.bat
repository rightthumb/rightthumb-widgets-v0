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

rem echo  %*
%*>"%stmp%\result.tmp"
set /p result=<"%stmp%\result.tmp"  >nul 2>&1
rem echo %result%

GOTO:EOF
SETLOCAL ENABLEDELAYEDEXPANSION
SET count=1
FOR /F "tokens=* USEBACKQ" %%F IN (`%*`) DO (
  SET result!count!=%%F
  SET /a count=!count!+1
	set result=%result1%
)
ENDLOCAL

GOTO:EOF