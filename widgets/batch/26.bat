

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo off

set search=%1
set index=D:\index\massage\26

if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO
if NOT [%1] == [] GOTO ONE



GOTO ONE

if [%1] == [] GOTO END

:ONE
echo Search level: ONE variable
findstr /i /r %search% "%index%"
GOTO END


:TWO
echo Search level: TWO variables
findstr /i /r %search% "%index%" | find /i "%2"
GOTO END


:THREE
echo Search level: THREE variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3"
GOTO END


:FOUR
echo Search level: FOUR variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3" | find /i "%4"
GOTO END


:FIVE
echo Search level: FIVE variables
findstr /i /r %search% "%index%" | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5"
GOTO END



:END 
echo ------------