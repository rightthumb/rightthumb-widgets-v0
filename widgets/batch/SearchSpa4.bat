@echo off
set thisFile=spa_live3.php

set search=
:notepad search_tmp.txt
set /p search=<search_tmp.txt

:START
cls
%php% %phpFiles%\%thisFile%
echo.
:END

:del search_tmp.txt