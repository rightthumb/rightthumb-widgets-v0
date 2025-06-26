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
rem net view
rem echo ===================================
rem echo Enter the computer name to shutdown
rem set /p cp=kill:
rem cls
rem echo %cp%
rem echo ===================================
rem set /p do=Type r for restrart or s to shutdown:
rem cls
rem echo Shutingdown %cp%
rem shutdown -%do% -m %cp%
rem echo ===================================
rem set /p stop=Hit Enter to stop the shutdown of %cp%
rem echo Shutdown Aborted
rem shutdown -a -m %cp%
GOTO END




:QUICK
taskkill /im %1* /f
GOTO END




:END


 
