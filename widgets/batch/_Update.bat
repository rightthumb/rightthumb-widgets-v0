@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

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

 
