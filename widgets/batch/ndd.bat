 @echo off
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
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
