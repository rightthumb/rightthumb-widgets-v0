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

echo                         Find Task and Kill
echo                           By:Scott Reph
echo                           813-690-1260
set tmp=%temp%\task.tmp
set tmps=%temp%\tasks.tmp
set out=%temp%\taskout.tmp
title Find a task
tasklist > "%tmp%"

if not [%1] == [] set t=%1
if not [%1] == [] GOTO AUTOFIND
set /p l=List? (n):
if /I "%l%" == "y" GOTO list

echo ================================================
echo. 
echo. 

:start
set /p t=Enter Task::
type "%tmp%" | find /I "%t%" > "%out%"
type "%tmp%" | find /I "%t%"
Set PARSEARG="eol=; tokens=1,2* delims=exe, "
For /F %PARSEARG% %%a in (%out%) Do SET search=%%a
if /I "%search%" == "" GOTO error

:ASK
set /p k=Kill? (n):
if /I "%k%" == "y" GOTO kill
GOTO exit

:AUTOFIND
type "%tmp%" | find /I "%t%"
GOTO ASK

:error
echo not found
pause
GOTO exit
:kill
call kill %t%*
%tkill%
GOTO exit
:list
set /p s=Sort? (n):
if /I "%s%" == "y" GOTO sort
:listb
notepad "%tmp%"
GOTO start
:sort
sort "%tmp%" /o "%tmps%" 
notepad "%tmps%"
GOTO start
echo.
pause
goto exit

if [] == [] GOTO 

:exit

 
