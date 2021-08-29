@echo off
call b spamoritz
set thisFile=spa_live4wl.php


:START
cls
%php% %phpFiles%\%thisFile%
echo.
:END