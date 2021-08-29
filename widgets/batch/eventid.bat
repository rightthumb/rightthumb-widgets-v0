@echo off
if [%1] == [] GOTO END
if [%2] == [] GOTO END
set eventid=%1
set source=%2
if not [%3] == [] set source=%2 %3

start "D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe" "http://www.eventid.net/display.asp?eventid=%eventid%&eventno=1274&source=%source%&phase=1"

:END
