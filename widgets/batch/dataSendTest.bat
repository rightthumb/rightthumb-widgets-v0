@echo off
call m stemp
call b sd
set thisFile=dataSendTest.php
%php% %phpFiles%\%thisFile%
echo.
call b stemp