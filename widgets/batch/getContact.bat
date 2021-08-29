@echo off
set s=%1
set do=%2
set thisFile=getContact.php
%php% %phpFiles%\%thisFile%
echo.
: copied as g