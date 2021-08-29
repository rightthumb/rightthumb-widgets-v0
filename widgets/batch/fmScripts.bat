@echo off
set file=%1
set search=%2
set thisFile=fmScripts.php
%php% %phpFiles%\%thisFile%
echo.
echo.
::auditFM