@echo off
cls
set search=%1 %2 %3 %4 %5 %6 %7 %8 %9
set thisFile=med.php
%php% %phpFiles%\%thisFile% > ~tmp.txt
findstr /r "[A-Za-z]" ~tmp.txt
del ~tmp.txt
echo.
