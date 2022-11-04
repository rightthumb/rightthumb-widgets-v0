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

SET "shouldRun="
SET /p shouldRun=Close Chrome? 

IF [%shouldRun%] == [n] GOTO:END
IF [%shouldRun%] == [N] GOTO:END
IF [%shouldRun%] == [NO] GOTO:END
IF [%shouldRun%] == [no] GOTO:END
IF [%shouldRun%] == [No] GOTO:END

taskkill /im chrome.exe /f

start chrome.exe --profile-directory=Default --disable-web-security --disable-site-isolation-trials --allow-running-insecure-content  "http://www.google.com/"

:END
cls
GOTO:EOF

 
