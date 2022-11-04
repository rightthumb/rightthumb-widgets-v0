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


if ["%1"] == ["n"] GOTO DO
if not ["%1"] == [""] set thing0=%1
if not ["%2"] == [""] set thing0=%1 %2
if not ["%3"] == [""] set thing0=%1 %2 %3
if not ["%4"] == [""] set thing0=%1 %2 %3 %4
if not ["%5"] == [""] set thing0=%1 %2 %3 %4 %5
if not ["%6"] == [""] set thing0=%1 %2 %3 %4 %5 %6
if not ["%7"] == [""] set thing0=%1 %2 %3 %4 %5 %6 %7
if not ["%8"] == [""] set thing0=%1 %2 %3 %4 %5 %6 %7 %8
if not ["%9"] == [""] set thing0=%1 %2 %3 %4 %5 %6 %7 %8 %9


GOTO SKIP
:DO
set /p thing0=NAME= 

GOTO SKIP
if ["%title%"] == [""] 
if ["%title%"] == [""] 
if ["%1"] == [""] 
if ["%1"] == [""] 

:SKIP
set timestamp=%today%-%time:~0,2%.%time:~3,2%
set ccd.tmp=ccd.tmp
cd>%ccd.tmp%
set /p title_ccd=<%ccd.tmp%
del %ccd.tmp%
title %thing0% %title_ccd%
prompt - 
cls
:END

 
