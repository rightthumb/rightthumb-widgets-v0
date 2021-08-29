@echo off

rem set search=%1
rem set index=\index\i

if NOT [%5] == [] CALL FIVE %*
if NOT [%4] == [] CALL FOUR %*
if NOT [%3] == [] CALL THREE %*
if NOT [%2] == [] CALL TWO %*





if not [%1] == [] CALL :ONE %*
GOTO:EOF

:ONE
echo Search level: ONE variable
@echo off
start explorer /select, %1
GOTO:EOF


:TWO
echo Search level: TWO variables
start explorer /select, "%1 %2"
GOTO:EOF


:THREE
echo Search level: THREE variables
start explorer /select, "%1 %2 %3"
GOTO:EOF


:FOUR
echo Search level: FOUR variables
start explorer /select, "%1 %2 %3 %4"
GOTO:EOF


:FIVE
echo Search level: FIVE variables
start explorer /select, "%1 %2 %3 %4 %5"
GOTO:EOF



:END 
