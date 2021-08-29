:v2
@echo off

if [%1] == [HELP] GOTO HELP
if [%1] == [help] GOTO HELP
if [%1] == [h] GOTO HELP


set sroot=D:\tech\MyScripts\log
set p=%sroot%\script-bookmarks\alias\%1.bat
set /p back=<"%p%"

call %p% %*
:END