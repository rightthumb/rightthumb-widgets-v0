@echo off
::set search=%1 %2 %3 %4 %5 %6 %7 %8 %9
set thisFile=auditFunction.php
%php% %phpFiles%\%thisFile%
echo.
echo.
echo %phpFiles%\%thisFile%
echo.