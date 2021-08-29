@echo off
title Runas utility :: scott is cool
cls
set /p c=Enter Computer:
set /p u=Enter Username:
set /p do=Enter Comand:
runas /netonly /user:"%c%\%u%" "%do%"
echo done