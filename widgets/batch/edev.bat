@echo off

set root=%scriptroot%\dev


:BAT

start notepad "%root%\%1.bat" 
GOTO END

:END
 echo %root%\%1