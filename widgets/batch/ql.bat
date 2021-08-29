@echo off
set do=ql_tmp.bat

edit %do%
tyoe %do%
:LOOP
set /p on=ITEM? 
IF [%on%] == [exit] GOTO ENDLOOP
IF [%on%] == [] GOTO LOOP

call %do% "%on%"


GOTO LOOP
:ENDLOOP

:END