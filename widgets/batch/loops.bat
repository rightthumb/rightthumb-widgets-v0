@echo off
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