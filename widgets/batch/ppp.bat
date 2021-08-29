@echo off
IF ["%1"] == [""] GOTO ASK
set project=%1 %2 %3 %4 %5 %6 %7 %8 %9
GOTO END
:ASK
set /p project=Project: 

:END

title %today%-%time% %project%
call grn
