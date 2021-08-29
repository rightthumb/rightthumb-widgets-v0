@echo off
set s=%1
set do=%2
set thisFile=accc-cancer_member_data.php
%php% %phpFiles%\%thisFile%
echo.
: copied as g