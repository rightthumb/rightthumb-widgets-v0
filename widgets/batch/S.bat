@echo off

set index_file=%scriptroot%\*.*

if [%1] == [] GOTO:EOF

set search=%1

if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO




GOTO ONE

if [%1] == [] GOTO NULL

:ONE
echo Search level: ONE variable
findstr /i /r /s  %search% %index_file%
GOTO END


:TWO
echo Search level: TWO variables
findstr /i /r /s  %search% %index_file% | find /i "%2"
GOTO END


:THREE
echo Search level: THREE variables
findstr /i /r /s  %search% %index_file% | find /i "%2" | find /i "%3"
GOTO END


:FOUR
echo Search level: FOUR variables
findstr /i /r /s  %search% %index_file% | find /i "%2" | find /i "%3" | find /i "%4"
GOTO END


:FIVE
echo Search level: FIVE variables
findstr /i /r /s  %search% %index_file% | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5"
GOTO END

:NULL
echo Search level: #NULL variable
type %index_file%
GOTO END



:END 
