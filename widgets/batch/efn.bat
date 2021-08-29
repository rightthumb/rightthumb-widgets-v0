@echo off
IF [%1] == [] (echo file action name from to)
IF [%1] == [] (GOTO END)

set fileName=%1

::change, add, delete: "c", "a", "d"
set action=%2
set name=%3
set changeFrom=%4
set changeTo=%5
set thisFile=editfunctionalName.php
%php% %phpFiles%\%thisFile%
echo.
:END
::: editfunctionalName