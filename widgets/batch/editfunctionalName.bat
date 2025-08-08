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