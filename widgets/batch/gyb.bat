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

:loop
ipconfig /flushdns>tmp
ping google.com -l 1 -n 1 -w 500| find /i "reply" > g.tmp
ping yahoo.com -l 1 -n 1  -w 500| find /i "reply" > y.tmp
start  /min a.gyb
set /p g=<g.tmp
set /p y=<y.tmp
ping yahoo.com -l 1 -n 1 >tmp
type  b.tmp | find /i "name" > b2.tmp
set /p b=<b2.tmp

if ["%g:~0,5%%"] == ["Reply"] GOTO gYES
GOTO gNO
:gYES
set google=Y
GOTO gDONE
:gNO
set google=N
:gDONE

if ["%y:~0,5%%"] == ["Reply"] GOTO yYES
GOTO yNO
:yYES
set yahoo=Y
GOTO yDONE
:yNO
set yahoo=N
:yDONE

if ["%b:~0,4%%"] == ["Name"] GOTO bYES
GOTO bNO
:bYES
set bing=Y
GOTO bDONE
:bNO
set bing=N
:bDONE
echo Google(icmp)=%google% Yahoo(icmp)=%yahoo% Bing(dns)=%bing% 
set /p loopthis=Run Again: 
set google=
set yahoo=
set bing=
set g=
set y=
set b=

del g.tmp
del y.tmp
del b.tmp
del b2.tmp
if ["%loopthis%"] == ["n"] GOTO END
if ["%loopthis%"] == ["N"] GOTO END
set loopthis=
GOTO loop
:END
set loopthis=

 
