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


mode 50,9
::mode 50,900
CALL %userprofile%\cc v
CALL b scripttmp
cd

SET cnt=0
SET search=online
SET thisFile=offline_check.php
SET netDWNfile=%stmp%\~dwnCheck.txt
SET offlineWWWfile=%stmp%\~dwnCount.txt
CALL :PHP
GOTO LOOP



:LOOP
SET /a  cnt=%cnt%+1
TITLE Loop: %cnt%
CALL :PING
COLOR 1f
CALL :PHP
IF EXIST %offlineWWWfile% (SET /p offline_www=<%offlineWWWfile%)
IF NOT EXIST %offlineWWWfile% (SET offline_www=0)
IF NOT [%offline_www%] == [0] CALL :OFFLINE
IF [%offline_www%] == [0] (SET dwnTime=0)
CALL pause1 5
::CALL :LOOP
GOTO LOOP

:OFFLINE
SET /a dwnTime=%dwnTime% + 1
IF %dwnTime% LSS 5 CALL :LOOP
CALL :PING
TITLE Node OFFLINE
:::::::::start D:\tech\MyScripts\#_vbs.vbs
:::::::::start cmd /c D:\tech\MyScripts\#_offline.bat
SET count=
CALL :blink

:blink

SET count=%count%-
COLOR fc
CALL pause1 1
COLOR cf
CALL pause1 1
IF NOT ["%count%"] == ["-------"] (CALL :blink)
CALL :LOOP

:PHP
%php% %phpFiles%\%thisFile%
GOTO:EOF

:PING
IF EXIST %netDWNfile% del /q %netDWNfile%
IF EXIST %offlineWWWfile% del /q %offlineWWWfile%
echo.> %netDWNfile%
SET "net_down_check="
ping google.com -n 1 -i 254 | find "Reply" | find /v "unreachable"> %netDWNfile%
ping 4.2.2.3 -n 1 -i 254 | find "Reply" | find /v "unreachable">> %netDWNfile%
ping 8.8.8.8 -n 1 -i 254 | find "Reply" | find /v "unreachable">> %netDWNfile%
echo down>> %netDWNfile%
SET /p net_down_check=<%netDWNfile%
IF NOT [%net_down_check:~0,5%] == [Reply] CALL :DOWN
echo.> %netDWNfile%
GOTO:EOF

:DOWN
cls
echo.
echo.
echo.
COLOR cf
TITLE INTERNET IS DOWN!!
ECHO                 INTERNET IS DOWN!!

CALL pause1 1
COLOR fc
CALL pause1 1
COLOR cf
CALL pause1 1
COLOR fc
CALL :LOOP