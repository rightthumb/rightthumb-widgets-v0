@echo off
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