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

set LOOP=
set VARONE=%1
set index=D:\index\massage\26


if ["%1"] == [""] GOTO LOOP

GOTO CHECK

:LOOPB
pause
CLS
:LOOP

set VARONE=
set LOOP=yes
set /p VARONE= 26 - 


GOTO ONE

GOTO END

:CHECK
set VARONE =%1
set VARTWO =%2
set VARTHREE =%3
set VARFOUR =%4
set VARFIVE =%5
if NOT ["%VARFIVE%"] == [""] GOTO FIVE
if NOT ["%VARFOUR%"] == [""] GOTO FOUR
if NOT ["%VARTHREE%"] == [""] GOTO THREE
if NOT ["%VARTWO%"] == [""] GOTO TWO
if NOT ["%VARONE%"] == [""] GOTO ONE

GOTO END




GOTO ONE

if [%1] == [] GOTO END

:ONE
if ["%VARONE%"] == ["x"] GOTO END
echo Search level: ONE variable
findstr /i /r "%VARONE%" "%index%"
if NOT ["%LOOP%"] == [yes] GOTO LOOPB
GOTO END


:TWO
echo Search level: TWO variables
findstr /i /r "%VARONE%" "%index%" | find /i "%VARTWO%"
GOTO END


:THREE
echo Search level: THREE variables
findstr /i /r "%VARONE%" "%index%" | find /i "%VARTWO%" | find /i "%VARTHREE%"
GOTO END


:FOUR
echo Search level: FOUR variables
findstr /i /r "%VARONE%" "%index%" | find /i "%VARTWO%" | find /i "%VARTHREE%" | find /i "%VARFOUR%"
GOTO END


:FIVE
echo Search level: FIVE variables
findstr /i /r "%VARONE%" "%index%" | find /i "%VARTWO%" | find /i "%VARTHREE%" | find /i "%VARFOUR%" | find /i "%VARFIVE%"
GOTO END






set VARONE =
set VARTWO =
set VARTHREE =
set VARFOUR =
set VARFIVE =
set LOOP=
:END