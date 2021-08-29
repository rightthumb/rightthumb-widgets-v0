@echo off
set segment=%1
set thisFile=MS_Gamma.php
%php% %phpFiles%\%thisFile%
echo.

:END