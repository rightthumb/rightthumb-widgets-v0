@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

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

 
