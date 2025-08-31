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

IF [%1] == [] GOTO:EOF
set doneBox.vbs=%stmp%\doneBox.vbs
echo Const TIMEOUT = 5 > %doneBox.vbs%
echo Set objShell = WScript.CreateObject("WScript.Shell") >> %doneBox.vbs%
echo objShell.Popup %1, TIMEOUT >> %doneBox.vbs%
start %doneBox.vbs%
GOTO:EOF