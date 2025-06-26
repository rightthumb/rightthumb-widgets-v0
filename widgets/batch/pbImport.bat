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

set id=%1
set do=%2
set test=%3
set all=%1 %2 %3 %4 %5 %6 %7
if ["%id%"] == [""] GOTO HELPME
set thisFile=pbImport.php
if ["%2"] == ["\import"] GOTO IMPORT
if ["%3"] == ["\import"] GOTO IMPORT
if ["%2"] == ["import"] GOTO IMPORT
if ["%3"] == ["import"] GOTO IMPORT
%php% %phpFiles%\%thisFile%
GOTO END
:IMPORT
call b dyan
%php% %phpFiles%\%thisFile% > import.csv
start "" "http://www.pillerbeauty.com/dbScript.php?script=pbImport"
GOTO END

:HELPME
echo.
echo ================================
echo HELP:
echo.
echo pbImport \cat
echo pbImport \cat ^> ~out.txt ^& parse ~out.txt "," "1,3"  ^& del ~out.txt
echo.
echo pbImport 2018 GEQ \import
echo.
echo pbImport 2018 GEQ
echo pbImport 1001-1005        ... (id_cat ^>= 1002 ^& id_cat ^<= 1005)
echo pbImport 1001-1005 NEQ    ... (id_cat ^> 1002 ^& id_cat ^< 1005)
echo pbImport 2018 EQU
echo pbImport 2018 EQU \cat
echo pbImport 2018 EQU \test
echo pbImport 1001-1005 EQU \test2
echo pbImport 1001-1005 EQU \test
echo.
echo pbImport 0 NEQ \test ^> ~out.txt ^& parse ~out.txt "," 2  ^& del ~out.txt 
echo pbImport 2018 GEQ  ^> ~out.txt ^& parse ~out.txt "," "1,4"  ^& del ~out.txt
echo pbImport 0 NEQ  ^> ~out.txt ^& parse ~out.txt "," 4  ^& del ~out.txt
echo.
echo EQU - Equal
echo NEQ - Not equal
echo. 
echo LSS - Less than ^<
echo LEQ - Less than or Equal ^<=
echo. 
echo GTR - Greater than ^>
echo GEQ - Greater than or equal ^>=
echo.
echo E:\tech\scripts\php\pbImport.php
echo.
echo ================================
echo.
echo.
:END

 
