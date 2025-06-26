@echo off
cls
:RESTART

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo off
:if not exist "%systemroot%\system32\-monitor.bat" xcopy  /y %0 %systemroot%\system32\
mode 30,2
call %userprofile%\cc v
call b scripttmp
cd



:VAR
set notice=%1 is:
set a_delay=5
set b_delay=1
set on_color=1f
set off_color=8f
set check_color=f8
set b_color=f0
set blink_0_color=fc
set blink_1_color=cf
set log=%stmp%\offline-log.txt
set log2=%stmp%\offline-log.csv
set log3=%stmp%\offline-log-skip.csv
set last=
set netDWNfile=%stmp%\~~%1.txt
:==========================================

rem prompt -
GOTO LOOP
:DOWN
color cf
ECHO INTERNET IS DOWN!!
@ping 127.0.0.1 -n %b_delay% -l 10> nul
color fc
:loop

if exist %netDWNfile% del /q %netDWNfile%
if exist %offlineWWWfile% del /q %offlineWWWfile%
echo.> %netDWNfile%
set "net_down_check="
ping google.com -n 1 -i 254 | find "Reply"> %netDWNfile%
ping 4.2.2.3 -n 1 -i 254 | find "Reply">> %netDWNfile%
ping 8.8.8.8 -n 1 -i 254 | find "Reply">> %netDWNfile%
set /p net_down_check=<%netDWNfile%
if not "%net_down_check:~0,5%" == "Reply" GOTO DOWN
echo.> %netDWNfile%

:GOTO RESTART
:color %check_color%
set status=
cls

echo Checking Connection
title Checking Connection
:echo finding %1
:echo Check 1

FOR /F "tokens=1 delims= " %%B IN ('PING -l 1 -n 1 -w 8000 %1') DO IF "%%B"=="Reply" set status=ONLINE

cls

if "%status%"=="" GOTO test2
GOTO skipoffline
:test2
echo "%1","%date:~-4,4%.%date:~-10,2%.%date:~-7,2%","%time:~0,2%:%time:~3,2%" >> "%log3%"
echo Check 2
FOR /F "tokens=1 delims= " %%B IN ('PING -l 1 -n 1 -w 8000 %1') DO IF "%%B"=="Reply" set status=ONLINE
if "%status%"=="" GOTO test3
GOTO skipoffline
:test3
echo Check 3

FOR /F "tokens=1 delims= " %%B IN ('PING -l 1 -n 1 -w 8000 %1') DO IF "%%B"=="Reply" set status=ONLINE

if "%status%"=="" GOTO offline

:skipoffline
:==========================================
:online
if "%last%"=="off" GOTO NOWON
GOTO skipNOWON
:NOWON
::start %scriptroot%\#_vbs.vbs
if %loop% LSS 2 GOTO skipNOWON
:1:42 PM 7/30/2014
cls
echo %loop%
color 2f
@ping 127.0.0.1 -n %b_delay% -l 10> nul
@ping 127.0.0.1 -n %b_delay% -l 10> nul
echo %1 - %date:~-4,4%.%date:~-10,2%.%date:~-7,2% - %offtime% - %time:~0,2%:%time:~3,2% >> "%log%"
echo "%1","%date:~-4,4%.%date:~-10,2%.%date:~-7,2%","%offtime%","%time:~0,2%:%time:~3,2%" >> "%log2%"
set offtime=
:skipNOWON
set loop=0
set last=on
color %on_color%
title + %notice% %status%
echo %notice% %status%
:echo. 
:echo.
:echo %log%
@ping 127.0.0.1 -n %a_delay% -l 10> nul
GOTO loop

:==========================================
:offline
if exist %netDWNfile% del /q %netDWNfile%
if exist %offlineWWWfile% del /q %offlineWWWfile%
echo.> %netDWNfile%
set "net_down_check="
ping google.com -n 1 -i 254 | find "Reply"> %netDWNfile%
ping 4.2.2.3 -n 1 -i 254 | find "Reply">> %netDWNfile%
ping 8.8.8.8 -n 1 -i 254 | find "Reply">> %netDWNfile%
set /p net_down_check=<%netDWNfile%
if not "%net_down_check:~0,5%" == "Reply" GOTO DOWN
echo.> %netDWNfile%

title Node Offline
set /a loop=%loop% + 1
set status=OFFLINE
if "%last%"=="on" GOTO NOWOFF
if "%last%"=="" GOTO NOWOFF
GOTO skipNOWOFF
:NOWOFF
set offtime=%time:~0,2%:%time:~3,2%
:::::::::::start %scriptroot%\#_vbs.vbs
:::::::::start cmd /c %scriptroot%\#_offline.bat
:skipNOWOFF
set last=off
if "%send1%"=="" GOTO send
GOTO sent
:send
:==========================================
set from=scott@techreph.com
set to=scott.reph@gmail.com
set cell=8136901260@mymetropcs.com
set subject=%1 is OFFLINE
set message=%1 is OFFLINE
set server=192.168.255.22
set user=TechREPH
set pass=8136901260
:sendEmail -f %from% -t %to% -u "%subject%" -m "%message%" -s "%server%" -o username=%user% -o password=%pass%
sendEmail -f %from% -t %cell% -u "%subject%" -m "%message%" -s "%server%" -o username=%user% -o password=%pass%
:==========================================
set send1=no
cls
:sent
color %off_color%
:title - %notice% %status%
echo %notice% %status%



set count=
  :blink

  set count=%count%-
color %blink_0_color%
@ping 127.0.0.1 -n %b_delay% -l 10> nul
color %blink_1_color%
@ping 127.0.0.1 -n %b_delay% -l 10> nul

  if not "%count%"=="-------" %then% GOTO blink

color %off_color%
@ping 127.0.0.1 -n %a_delay% -l 10> nul

GOTO loop


:netsh interface show interface 
:netsh wlan show networks
:netsh wlan show all |+ ssid |- number |- bssid |- name |++ "     "


 
