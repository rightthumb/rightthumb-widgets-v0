@echo off
set thisFile=spa_live2.php

set search=
set /p search=Search for: 
if ["%search%"] == [""] GOTO END

:START
cls
%php% %phpFiles%\%thisFile%
echo.
:END