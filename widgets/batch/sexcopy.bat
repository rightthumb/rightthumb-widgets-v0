@echo off
if ["%1"] == [""] GOTO END
xcopy /s/d/y %1 %2

:END