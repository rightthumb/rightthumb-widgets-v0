@echo off
set /p continue= Would you like to reindex this folder and subfolders? 
if %continue% == ["Y"] GOTO Start
if %continue% == ["Yes"] GOTO Start
GOTO CNL
:Start
dir /s/b > index.txt
GOTO END
:CNL
echo CNL
:END