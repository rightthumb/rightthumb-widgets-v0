@echo off
cls

echo Starting kill loop 


:LOOP
taskkill /im rundll3* /f
taskkill /im iexplore.exe /f
GOTO LOOP
