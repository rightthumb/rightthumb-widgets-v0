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


 
