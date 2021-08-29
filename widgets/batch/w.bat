@echo off
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
