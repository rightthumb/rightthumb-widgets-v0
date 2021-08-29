@echo off
title Save this folder on your desktop
set /p y=Do you want to save this folder on your desktop: 
IF NOT "%y%" == "y" GOTO NO

:YES
IF NOT "%y%" == "yes" GOTO SURE
:SURE
mkdir "%userprofile%\Desktop\-Scripts"
xcopy *.bat "%userprofile%\Desktop\-Scripts\" /d
echo Files updated
GOTO END

:NO
echo Action cancelled
GOTO END

:END
pause