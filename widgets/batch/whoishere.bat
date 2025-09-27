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

netstat -a -n |- 0.0.0.0:0 |-- "*:*" |- UDP |- 127.0.0. |- [::] |- State>~whoishere.txt
set thisFile=whoisherePart1.php
%php% %phpFiles%\%thisFile%>~whoishere2.txt
echo.
echo.> ~ipOwner.txt
for /F "tokens=*" %%A in  ( ~whoishere2.txt ) do  (
   ECHO Processing %%A
   call netblock %%A >> ~ipOwner.txt
)
pause
set thisFile=whoisherePart2.php
%php% %phpFiles%\%thisFile%
echo.
::IF EXIST ~whoishere.txt (del ~whoishere.txt)
::IF EXIST ~whoishere2.txt (del ~whoishere2.txt)
::IF EXIST ~ipOwner.txt (del ~ipOwner.txt)