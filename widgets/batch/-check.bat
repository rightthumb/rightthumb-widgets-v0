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

IF "%1" == "" GOTO SETG

:SETONE
set token=%1
GOTO START

:SETG
set token=google.com
GOTO START

:START
%widgets%
:==========================================
set notice=%1 is:
set delay=5
set b_delay=2
set b_color=70
set logdir=%widgets%\tech\logs\
set log=%logdir%%1,Connection-log.txt


:==========================================
if "%token%"=="" GOTO copythis
if "%token%"=="log" GOTO openlog
if "%token%"=="clearlog" GOTO clearlog
if not exist %logdir% mkdir %logdir%

:==========================================
echo ======================= >> "%log%"
echo Test Started >> "%log%"
date /t >> "%log%"
time /t >> "%log%"


:==========================================

prompt -
:loop
set status=
cls

echo Checking Connection
title Checking Connection
echo finding %1

FOR /F "tokens=1 delims= " %%B IN ('PING -l 1 -n 1 -w 800 %1') DO IF "%%B"=="Reply" set status=ONLINE

cls
time /t
if "%status%"=="" GOTO offline

GOTO online
:==========================================
:backonline
echo backonline
echo ======================= >> "%log%"
echo %1 is %status% >> "%log%"
date /t >> "%log%"
time /t >> "%log%"
set status2=

:==========================================
:online
if "%status2%"=="OFFLINE" GOTO backonline
color 7
title %notice% %status%
echo %status%

@ping 127.0.0.1 -n %delay% -l 10> nul
GOTO loop

:==========================================
:offline
set status=OFFLINE

if "%status2%"=="OFFLINE" GOTO offline2


:nowoffline
echo nowoffline
echo ======================= >> "%log%"
echo %1 is %status% >> "%log%"
date /t >> "%log%"
time /t >> "%log%"
set status2=OFFLINE

:==========================================
:offline2
color %b_color%
title %notice% %status%
echo %status%


set count=
  :blink

  set count=%count%-
color 7
@ping 127.0.0.1 -n %b_delay% -l 10> nul
color %b_color%
@ping 127.0.0.1 -n %b_delay% -l 10> nul
  if not "%count%"=="---" %then% GOTO blink
@ping 127.0.0.1 -n %delay% -l 10> nul

GOTO loop


:clearlog
del \q "%logdir%"
pause
GOTO end


:openlog
explorer "%logdir%"
GOTO end

:copythis
xcopy %0 %systemroot%\system32\ /ys
GOTO end

:end

 
