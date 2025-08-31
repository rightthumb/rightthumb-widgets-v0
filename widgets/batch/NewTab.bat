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

prompt - 
tasklist |find /i "Chrome.exe" > ```
set /p check=<```
if ["%check%"] == [""] GOTO OPEN
start %D:\tech\MyScripts\NewTab.vbs
GOTO END
:OPEN
start "%USERPROFILE%\AppData\Local\Google\Chrome\Application\chrome.exe" "https://www.google.com/?gws_rd=ssl"

:END
del ```
: ping google.com -t