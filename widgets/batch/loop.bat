@echo off
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
