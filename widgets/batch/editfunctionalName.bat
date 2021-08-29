@echo off
IF [%1] == [] (echo file action name to from)
IF [%1] == [] (GOTO END)

set fileName=%1

::change, add, delete: "c", "a", "d"
set action=%2
set name=%3
set changeTo=%4
set changeFrom=%5

set thisFile=editfunctionalName.php
%php% %phpFiles%\%thisFile%
echo.
:END