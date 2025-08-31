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


if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO



set search=%1
GOTO ONE
echo Search level: ONE
if [%1] == [] GOTO END

:ONE
findstr /r /i %1 \index\ports.txt
GOTO END


:TWO
echo Search level: TWO
findstr /r /i %1 \index\ports.txt
findstr /r /i %2 \index\ports.txt
GOTO END


:THREE
echo Search level: THREE
findstr /r /i %1 \index\ports.txt
findstr /r /i %2 \index\ports.txt
findstr /r /i %3 \index\ports.txt
GOTO END


:FOUR
echo Search level: FOUR
findstr /r /i %1 \index\ports.txt
findstr /r /i %2 \index\ports.txt
findstr /r /i %3 \index\ports.txt
findstr /r /i %4 \index\ports.txt
GOTO END


:FIVE
echo Search level: FIVE
findstr /r /i %1 \index\ports.txt
findstr /r /i %2 \index\ports.txt
findstr /r /i %3 \index\ports.txt
findstr /r /i %4 \index\ports.txt
findstr /r /i %5 \index\ports.txt
"%4" | find /i "%5"
GOTO END



:END