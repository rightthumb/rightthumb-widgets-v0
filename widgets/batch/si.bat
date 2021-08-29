@echo off

if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO



set search=%1
GOTO ONE
echo Search level: ONE
if [%1] == [] GOTO END

:ONE
findstr /r %search% \index\i
GOTO END


:TWO
echo Search level: TWO
findstr /r %search% \index\i | find /i "%2"
GOTO END


:THREE
echo Search level: THREE
findstr /r %search% \index\i | find /i "%2" | find /i "%3"
GOTO END


:FOUR
echo Search level: FOUR
findstr /r %search% \index\i | find /i "%2" | find /i "%3" | find /i "%4"
GOTO END


:FIVE
echo Search level: FIVE
findstr /r %search% \index\i | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5"
GOTO END



:END 
