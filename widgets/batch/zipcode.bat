@echo off
if [%1] == [] GOTO END
 
start "D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe" "http://zipinfo.com/cgi-local/zipsrch.exe?zip=%1"

:END
