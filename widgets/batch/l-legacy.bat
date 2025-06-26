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

set search=%1
CALL :DeQuote search
set omit=%2
set thisFile=List_Compare.php

if ["%search%"] == ["swap"] GOTO SWAPFILES
if ["%search%"] == ["s"] GOTO SWAPFILES
if ["%search%"] == ["d"] GOTO DELETEFILES
if ["%search%"] == ["delete"] GOTO DELETEFILES
if ["%search%"] == ["f"] GOTO DELETEFILES
if ["%search%"] == ["g"] GOTO DELETEGOOD
if ["%search%"] == ["t"] GOTO DELETETEST

if NOT exist ~Good.txt notepad ~Good.txt
if NOT [%1] == [] GOTO SKIPTESTOPEN
if NOT exist ~Test.txt notepad ~Test.txt
:SKIPTESTOPEN

%php% %phpFiles%\%thisFile%
echo.
GOTO END

:DELETEFILES
if exist ~Test.txt del ~Test.txt
if exist ~Good.txt del ~Good.txt
GOTO END

:DELETEGOOD
if exist ~Test.txt del ~Test.txt
if exist ~Good.txt del ~Good.txt
GOTO END

:DELETETEST
if exist ~Test.txt del ~Test.txt
if exist ~Good.txt del ~Good.txt
GOTO END

:SWAPFILES
rename ~Good.txt ~Good.txt2
rename ~Test.txt ~Good.txt
rename ~Good.txt2 ~Test.txt
GOTO END
:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
GOTO:EOF
:END

 
