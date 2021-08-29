@echo off
if [%1] == [] GOTO END
 
start "D:\Users\Scott\AppData\Local\Google\Chrome\Application\chrome.exe" "http://en.wikipedia.org/wiki/Area_code_%1"

:END
