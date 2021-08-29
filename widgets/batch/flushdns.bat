@echo off
c
cls
echo this will kill your current connections continue??
pause
ipconfig /release
ipconfig /flushdns
ipconfig /renew
