 @echo off
set input=%1
set input
set input=%input:"=%
if ["%input%"] == [""] GOTO END
set cnt=0
set log=%temp%\~nd_tmp.txt

dir "%input%" | find "/" > _tmp
set /p modraw=< _tmp
set mod=%modraw:~0,10%
set moddate=%mod:~-4,4%.%mod:~-10,2%.%mod:~-7,2%
del _tmp


if exist "%moddate%-%input%" goto DUPLICATE
goto UNIQUE

:DUPLICATE
echo Duplicate Actions

:LOOP
set /a  cnt=%cnt%+1
set check=%moddate%-%cnt%-%input%

 IF EXIST "%check%" (
     GOTO LOOP
 ) ELSE (
     rename "%input%" "%check%"
     echo %check%
 )

goto END

:UNIQUE
set name=%moddate%-%input%
rename "%input%" "%name%"
echo %name%
goto END


:END
 

:echo %name% > "%log%"
set "cnt="
set "modraw="
set "mod="
set "moddate="
set "check="
set "name="
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
