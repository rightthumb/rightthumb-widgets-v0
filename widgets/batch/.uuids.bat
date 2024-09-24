@echo off
if "%1" == "" goto :ten
if not "%1" == "" goto :other %1

goto :eof

:ten
CALL p. genuuid -cnt 10 
goto :eof

:other
call CALL p. genuuid -cnt %1
goto :eof


 
