@echo off

set segment=%1
set thisFile=MS_Accuray.php
%php% %phpFiles%\%thisFile%
echo.

:END