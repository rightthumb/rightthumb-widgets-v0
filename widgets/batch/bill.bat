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

echo Generating invoice
set "invoice_client="
if not [%1] == [] set invoice_client=%1
if not [%invoice_client%] == [] echo invoice: %invoice_client%

call m back --c
call b 0 > nul
call b myTickets > nul
call t v > ~
call p. b0 -print -date > %myTickets%\folder.txt
set /p csv_export=<%tmpf%

rem echo "=if((E2<15),15,E2)"
rem echo "=IF(AND(E2>0,E2<15),15,IF(AND(E2>15,E2<30),30,IF(AND(E2>30,E2<45),45,IF(AND(E2>45,E2<60),60,IF(AND(E2>60,E2<75),75,IF(AND(E2>75,E2<90),90,IF(AND(E2>90,E2<105),105,IF(AND(E2>105,E2<120),120,IF(AND(E2>120,E2<135),135,IF(AND(E2>135,E2<150),150,IF(AND(E2>150,E2<165),165,IF(AND(E2>165,E2<180),180,IF(AND(E2>180,E2<195),195,IF(AND(E2>195,E2<210),210,IF(AND(E2>210,E2<225),225,IF(AND(E2>225,E2<240),240,IF(AND(E2>240,E2<255),255,IF(AND(E2>255,E2<270),270,IF(AND(E2>270,E2<285),285,IF(AND(E2>285,E2<300),300,IF(AND(E2>300,E2<315),315,IF(AND(E2>315,E2<330),330,IF(AND(E2>330,E2<345),345,IF(AND(E2>345,E2<360),360,IF(AND(E2>360,E2<375),375,IF(AND(E2>375,E2<390),390,IF(AND(E2>390,E2<405),405,IF(AND(E2>405,E2<420),420,IF(AND(E2>420,E2<435),435,IF(AND(E2>435,E2<450),450,IF(AND(E2>450,E2<465),465,IF(AND(E2>465,E2<480),480,IF(AND(E2>480,E2<495),495,IF(AND(E2>495,E2<510),510,IF(AND(E2>510,E2<525),525,IF(AND(E2>525,E2<540),540,IF(AND(E2>540,E2<555),555,IF(AND(E2>555,E2<570),570,IF(AND(E2>570,E2<585),585,IF(AND(E2>585,E2<600),600,IF(AND(E2>600,E2<615),615,IF(AND(E2>615,E2<630),630,IF(AND(E2>630,E2<645),645,IF(AND(E2>645,E2<660),660,IF(AND(E2>660,E2<675),675,IF(AND(E2>675,E2<690),690,IF(AND(E2>690,E2<705),705,IF(AND(E2>705,E2<720),720,IF(AND(E2>720,E2<735),735,IF(AND(E2>735,E2<750),750,IF(AND(E2>750,E2<765),765,IF(AND(E2>765,E2<780),780,IF(AND(E2>780,E2<795),795,IF(AND(E2>795,E2<810),810,IF(AND(E2>810,E2<825),825,IF(AND(E2>825,E2<840),840,IF(AND(E2>840,E2<855),855,IF(AND(E2>855,E2<870),870,IF(AND(E2>870,E2<885),885,IF(AND(E2>885,E2<900),900,IF(AND(E2>900,E2<915),915,IF(AND(E2>915,E2<930),930,IF(AND(E2>930,E2<945),945,E2)))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))))"
:notepad %myTickets%\bill.tmp.txt
:IF NOT EXIST "%myTickets%\bill.tmp.txt" echo error
:IF NOT EXIST "%myTickets%\bill.tmp.txt" GOTO END

rem IF NOT EXIST "%myTickets%\~"  (call t v > ~ & call bill)
rem IF NOT EXIST "%myTickets%\~" GOTO END

rem goto:eof

set thisFile=bill_log_format6b.php
rem if [%1] == [t] set thisFile=bill_log_format5.php
rem if [%1] == [top] set thisFile=bill_log_format5.php
rem if [%1] == [b] set thisFile=bill_log_format6b.php
rem if [%1] == [bottom] set thisFile=bill_log_format6b.php


rem %php% %phpFiles%\%thisFile%
rem goto:eof

%php% %phpFiles%\%thisFile% > %tmpf%
set /p invoice_csv=<%tmpf%
rem timeout /t 3
rem echo done waiting
echo %invoice_csv%
rem call o "%invoice_csv%"
rem IF EXIST %invoice_csv% (start "excel" %excel% %invoice_csv%)
IF EXIST %invoice_csv% (start excel %invoice_csv%  >nul 2>&1)
rem IF EXIST %myTickets%\bill.tmp.out.csv (start "excel" %excel% %myTickets%\bill.tmp.out.csv)
rem IF EXIST %myTickets%\bill.tmp.out.csv (start "excel" n %myTickets%\bill.tmp.out.csv)
IF NOT EXIST %myTickets%\bill.tmp.out.csv echo ERROR
IF EXIST "%myTickets%\bill.tmp.txt" del "%myTickets%\bill.tmp.txt"
IF EXIST "%myTickets%\~" del "%myTickets%\~"
echo.
:start go.vbs



:END
call b back > nul
 
 
 
 
 


 
