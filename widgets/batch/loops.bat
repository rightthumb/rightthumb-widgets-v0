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

set log=%userprofile%\desktop\loops.test.txt
set t=LOOP TEST

:P1
set loops=10
set /a  cnt=%cnt%+1
:title %t% - %cnt% of %loops%
title %t%: %cnt%
:IF [%cnt%] == [%loops%] GOTO ENDP1
@ping 127.0.0.1 -n 10 -l 1> nul
echo %cnt%
GOTO P1
:ENDP1
set cnt=0