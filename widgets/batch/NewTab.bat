@echo off
prompt - 
tasklist |find /i "Chrome.exe" > ```
set /p check=<```
if ["%check%"] == [""] GOTO OPEN
start %D:\tech\MyScripts\NewTab.vbs
GOTO END
:OPEN
start "D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe" "https://www.google.com/?gws_rd=ssl"

:END
del ```
: ping google.com -t