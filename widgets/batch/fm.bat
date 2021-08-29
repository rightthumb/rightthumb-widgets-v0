@echo off

set test=true
IF ["%1"] == [""] CALL :FM13

IF ["%1"] == ["13"] CALL :FM13

IF ["%1"] == ["a13"] CALL :FMA13
IF ["%1"] == ["13a"] CALL :FMA13
IF ["%1"] == ["a"] CALL :FMA13

IF ["%1"] == ["12"] CALL :FMA12 %2
IF ["%1"] == ["a12"] CALL :FMA12
IF ["%1"] == ["12a"] CALL :FMA12

IF ["%1"] == ["9"] CALL :FM9
IF ["%1"] == ["old"] CALL :FM9
IF ["%1"] == ["o"] CALL :FM9

echo %test%
GOTO:EOF


:FMA12
set test=%1
"D:\Program Files (x86)\FileMaker\FileMaker Pro 12 Advanced\FileMaker Pro Advanced.exe"
GOTO:EOF

:FM13
"D:\Program Files (x86)\FileMaker\FileMaker Pro 13\FileMaker Pro.exe"
GOTO:EOF

:FMA13
"D:\Program Files (x86)\FileMaker\FileMaker Pro 13 Advanced\FileMaker Pro Advanced.exe"
GOTO:EOF

:FM9
"D:\Program Files (x86)\FileMaker\FileMaker Pro 9\FileMaker Pro.exe"
GOTO:EOF
