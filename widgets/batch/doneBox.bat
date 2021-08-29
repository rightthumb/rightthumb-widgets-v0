@echo off
IF [%1] == [] GOTO:EOF
set doneBox.vbs=%stmp%\doneBox.vbs
echo Const TIMEOUT = 5 > %doneBox.vbs%
echo Set objShell = WScript.CreateObject("WScript.Shell") >> %doneBox.vbs%
echo objShell.Popup %1, TIMEOUT >> %doneBox.vbs%
start %doneBox.vbs%
GOTO:EOF