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

set loop=0
:LOOP
IF [%1] == [loop] (title LOOP: %loop%)
netstat -a -n |- 0.0.0.0:0 |-- "*:*" |- UDP |- 127.0.0. |- [::] |- State>~whoishere.txt
set thisFile=whoisherePart1.php
IF [%1] == [loop] (%php% %phpFiles%\%thisFile%>~whoishere%loop%.txt)
IF [%1] == [] (%php% %phpFiles%\%thisFile%)

set /a loop=%loop% + 1
IF [%1] == [loop] (GOTO LOOP)
echo.