@echo off
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
