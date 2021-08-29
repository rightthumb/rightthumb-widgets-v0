@echo off
set do=%1
set thisFile=do.php
CALL :dequote do

%do% > do.sys
%php% %phpFiles%\%thisFile%
echo.
echo.
Goto :eof
:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
Goto :eof
: copied as g


pbImport \cat ^> ~out.txt ^& parse ~out.txt ^",^" ^"1,3^"  & del ~out.txt