@echo off
set url=%1
set thisFile=getTable.php
%php% %phpFiles%\%thisFile%
echo.
echo.
: copied as g