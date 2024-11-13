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


if [%1] == [] GOTO CLEAR
GOTO START

:CLEAR
set indexindex=
GOTO END

:START
call ftmp %1 %2 %3 %4 %5 %6 %7 %8 %9

:END
echo.

 
