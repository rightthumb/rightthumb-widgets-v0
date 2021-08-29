@echo off
title Install script updates
set /p y=Do you want to replace the files in System32: 
IF NOT "%y%" == "y" GOTO NO

:YES
IF NOT "%y%" == "yes" GOTO SURE
:SURE
xcopy *.bat %systemroot%\system32\ /d
echo Files updated
GOTO END

:NO
echo Action cancelled
GOTO END

:END
pause