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

set file=test.txt
setlocal enabledelayedexpansion

set /a counter=2
set %%a = ""

for /f "usebackq delims=" %%a in (%file%) do (
echo %%a
) 
:printme 


:if "!counter!"=="%1" set line=%%a & goto :printme set /a counter+=2









GOTO END
@echo off

for /f %%a in (test.txt) do (
  echo %%a
  exit /b
)



GOTO END
@echo off
set f=D:\script-bookmarks\Clean
cd %f%
set log=%f%\clean.txt
echo ---------------------------------------- >> %log%
date /t  >> %log%
time /t  >> %log%
call CleanTemp.bat >> %log%


:END