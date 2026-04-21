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


set index=%USERPROFILE%\Documents\lo\index.txt
 set search=
 set prefix=
 set postnumone=
 set postnum=

set prefix=    -=Search level:
set postnumone= variable =-
set postnum= variables =-




if NOT [%5] == [] GOTO FIVE
if NOT [%4] == [] GOTO FOUR
if NOT [%3] == [] GOTO THREE
if NOT [%2] == [] GOTO TWO



set search=%1
GOTO ONE

if [%1] == [] GOTO END

:ONE
set titlenote= ( %1)
echo %prefix% ONE %postnumone%
TItle %prefix% ONE %postnumone% (%titlenote% )
findstr /i /r %search% %index%
GOTO END


:TWO
set titlenote= ( %1, %2 )
echo %prefix% TWO%postnum%
title %prefix% TWO%postnum% (%titlenote% )
findstr /i /r %search% %index% | find /i "%2"
GOTO END


:THREE
set titlenote= ( %1, %2, %3 )
echo %prefix% THREE%postnum%
title %prefix% THREE%postnum% (%titlenote% )
findstr /i /r %search% %index% | find /i "%2" | find /i "%3"
GOTO END


:FOUR
set titlenote= ( %1, %2, %3, %4 )
echo %prefix% FOUR%postnum%
title %prefix% FOUR%postnum% (%titlenote% )
findstr /i /r %search% %index% | find /i "%2" | find /i "%3" | find /i "%4"
GOTO END


:FIVE
set titlenote= ( %1, %2, %3, %4, %5 )
echo %prefix% FIVE%postnum%
title %prefix% FIVE%postnum% (%titlenote% )
findstr /i /r %search% %index% | find /i "%2" | find /i "%3" | find /i "%4" | find /i "%5"
GOTO END



:END