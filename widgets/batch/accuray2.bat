@echo off

set segment=%1
set thisFile=MS_Accuray2.php
%php% %phpFiles%\%thisFile%
:cls

echo.

:END