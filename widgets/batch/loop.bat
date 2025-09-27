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

set cnt=0
if [%2] == [] GOTO ERROR
if [%1] == [] GOTO ERROR
set number=%1
cls
:LOOP
set /a  cnt=%cnt%+1
echo LOOP: %cnt%
title %1 - Loop %cnt% of %1
call %2 %3 %4 %5 %6 %7 %7 %8 %9
echo.
if [%cnt%] == [%number%] GOTO END
GOTO LOOP

:ERROR
echo LOOP # command param
:END