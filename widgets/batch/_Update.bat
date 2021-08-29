@echo off
title Download script updates
set /p y=Do you want to replace the files in live\: 
IF NOT "%y%" == "y" GOTO NO

:YES
IF NOT "%y%" == "yes" GOTO SURE
:SURE
xcopy %systemroot%\system32\*.bat /d
echo Files updated
GOTO END

:NO
echo Action cancelled
GOTO END

:END
pause