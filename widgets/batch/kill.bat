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


IF NOT "%1" == "" GOTO QUICK
net view
echo ===================================
echo Enter the computer name to shutdown
set /p cp=kill:
cls
echo %cp%
echo ===================================
set /p do=Type r for restrart or s to shutdown:
cls
echo Shutingdown %cp%
shutdown -%do% -m %cp%
echo ===================================
set /p stop=Hit Enter to stop the shutdown of %cp%
echo Shutdown Aborted
shutdown -a -m %cp%
GOTO END




:QUICK
taskkill /im %1 /f
GOTO END




:END


