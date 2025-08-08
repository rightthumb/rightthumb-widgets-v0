:v2

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo off

if [%1] == [HELP] GOTO HELP
if [%1] == [help] GOTO HELP
if [%1] == [h] GOTO HELP


set sroot=D:\tech\MyScripts\log
set p=%sroot%\script-bookmarks\alias\%1.bat
set /p back=<"%p%"

call %p% %*
:END