@echo off
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