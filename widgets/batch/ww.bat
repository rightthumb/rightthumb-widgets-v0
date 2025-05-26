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

cls

if not [%1] == [] GOTO ENDX
set log=where.tmp
time /t > %log%

set loop=0
:LOOP
title Loop %loop%
set /a loop=%loop%+1
set /p q=Where is ?:
if [%q%] == [exit] GOTO END
type \index\(pf) | f %q% >> %log%
GOTO LOOP

:END
set /a loop=%loop%-1
echo %loop% >> %log%
time /t >> %log%
cls
echo ======================================
type %log%



:ENDX


 
