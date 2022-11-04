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


call m back --c
call b myTickets > nul


:notepad %myTickets%\bill.tmp.txt
:IF NOT EXIST "%myTickets%\bill.tmp.txt" echo error
:IF NOT EXIST "%myTickets%\bill.tmp.txt" GOTO END

IF NOT EXIST "%myTickets%\~"  (call t v > ~ & call bill)
IF NOT EXIST "%myTickets%\~" GOTO END

rem goto:eof


set thisFile=bill_log_format4.php

%php% %phpFiles%\%thisFile%
IF EXIST %myTickets%\bill.tmp.out.csv (start "excel" %excel% %myTickets%\bill.tmp.out.csv)
rem IF EXIST %myTickets%\bill.tmp.out.csv (start "excel" n %myTickets%\bill.tmp.out.csv)
IF NOT EXIST %myTickets%\bill.tmp.out.csv echo ERROR
IF EXIST "%myTickets%\bill.tmp.txt" del "%myTickets%\bill.tmp.txt"
IF EXIST "%myTickets%\~" del "%myTickets%\~"
echo.
:start go.vbs



:END 
call b back > nul
 
 
 
 
 


 
