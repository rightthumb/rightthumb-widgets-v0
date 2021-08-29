@echo off

call m back
call b myTickets

:notepad %myTickets%\bill.tmp.txt
:IF NOT EXIST "%myTickets%\bill.tmp.txt" echo error
:IF NOT EXIST "%myTickets%\bill.tmp.txt" GOTO END

IF NOT EXIST "%myTickets%\~"  (call t v > ~ & call bill)
IF NOT EXIST "%myTickets%\~" GOTO END



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

 call b back
 
 
 
 
 
 
