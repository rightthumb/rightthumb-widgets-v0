@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##


IF NOT EXIST "D:\tech\MyScripts\log\logs\" (mkdir D:\tech\MyScripts\log\logs)

set log=D:\tech\MyScripts\log\logs\LOG.%1.txt
echo ----------------------- >> "%log%"
echo %date% - %time% >> "%log%"
echo (%1)  >> "%log%"
call %1  >> "%log%"


 
 
