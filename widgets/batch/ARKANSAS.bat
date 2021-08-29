@echo off
set segment=%1
set thisFile=MS_ARKANSAS.php
%php% %phpFiles%\%thisFile%
echo.

:END