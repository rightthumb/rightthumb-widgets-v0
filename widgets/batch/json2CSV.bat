@echo off
set file=%1
set last_field_name=%2
set thisFile=json2CSV.php
%php% %phpFiles%\%thisFile%
echo.
echo.
: copied as g