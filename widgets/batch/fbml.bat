@echo off


set index=%scriptroot%\fbml.txt

if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO
if [%1] == [] GOTO OPEN



GOTO ONE




:ONE
echo Search level: ONE variable
findstr /i /r %1 "%index%"
GOTO END


:TWO
echo Search level: TWO variables
findstr /i /r %1 "%index%" | find /i "%2"
GOTO END


:THREE
echo Search level: THREE variables
findstr /i /r %1 "%index%" | find /i "%2" | find /i "%3"
GOTO END


:FOUR
echo Search level: FOUR variables
findstr /i /r %1 "%index%" | find /i "%2" | find /i "%3" | find /i "%4"
GOTO END


:FIVE
echo Search level: FIVE variables
findstr /i /r %1 "%index%" | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5"
GOTO END

:OPEN
start notepad %index%

:END 
