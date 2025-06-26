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

set input=%1
set input=%input:"=%
if ["%input%"] == [""] GOTO END
set log=%temp%\~nd_tmp.txt

dir "%input%" | find "/" > _tmp
set /p modraw=< _tmp
set mod=%modraw:~0,10%
set moddate=%mod:~-4,4%.%mod:~-10,2%.%mod:~-7,2%
del _tmp

echo %moddate% - %input%

:END
 

set modraw=
set mod=
set moddate=
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


 
