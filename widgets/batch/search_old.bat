  @echo %dbgp% off
title index search
cls
echo. -----------------------------------
echo.  Search index of the bellow drives:
dir /b (*
echo. -----------------------------------

:if [%1]==[] %0 DateName ::

IF [%1]==[] set /p search=Search criteria: 
IF [%1]==[] GOTO SEARCH
:SET
set search=%1
IF [%2]==[-] GOTO OUT
GOTO SEARCH


:SEARCH
findstr /r %search% (*
GOTO END

:OUT

set log=%search%.txt
findstr /r %search% (* >  "%log%"
start /max notepad "%log%"
GOTO END


crap


IF [%1]==[-] (IF [%2]==[] set /p search=Search criteria: ) | (IF [%2]==[] GOTO OUT) | IF [%1]==[-] set search=%2 | (GOTO OUT)




IF [%1]==[] set /p search=Search criteria: 
IF [%1]==[] GOTO SEARCH
IF [%1]==[-] set search=%2
IF [%1]==[-] GOTO OUT
IF NOT [%1]==[-] set search=%1
IF [%2]==[] set /p search=Search criteria: 
IF [%2]==[] GOTO OUT
IF [%1]==[-] set search=%2
IF [%2]==[-] GOTO OUT







:END
