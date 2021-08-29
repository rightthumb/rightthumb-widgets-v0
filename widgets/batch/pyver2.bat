@echo off
rem call m back
rem call b pyroot
rem set pyFile=%pyroot%\%1.py
set pyFile=%1
set thisFile=pyVer.php
%php% %phpFiles%\%thisFile%
echo.
rem call b back

