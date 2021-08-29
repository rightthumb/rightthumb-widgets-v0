@echo off

IF NOT EXIST "D:\tech\MyScripts\log\logs\" (mkdir D:\tech\MyScripts\log\logs)

set log=D:\tech\MyScripts\log\logs\LOG.%1.txt
echo ----------------------- >> "%log%"
echo %date% - %time% >> "%log%"
echo (%1)  >> "%log%"
call %1  >> "%log%"
