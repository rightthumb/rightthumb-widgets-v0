@echo off
set url=%1
set do=%2
set thisFile=url.php
%php% %phpFiles%\%thisFile%
echo.
echo.
: copied as g