@echo off
set pinID=%1
set url=%2
set thisFile=pageDescription.php
%php% %phpFiles%\%thisFile%
echo.
: copied as g