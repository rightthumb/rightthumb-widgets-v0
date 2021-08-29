@echo off

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
