@echo off
set location =%1
set thisFile=weather.php
%php% %phpFiles%\%thisFile%
echo.
echo.
: copied as g