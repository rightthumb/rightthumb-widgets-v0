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


if [%1] == [] (
    CALL p. ls -m
)
if [%1] == [m] (
    CALL p. ls -m
)

if [%1] == [d] (
    CALL:DO_A %*
)

GOTO:EOF



:DO_A
    if [%2] == [] (
        CALL:DO_B
    ) else (
        CALL:DO_C %*
    )
GOTO:EOF



:DO_B
    rem echo 2 Days
    CALL p. ls -s md -g ago -c ago name md -ago 2d
GOTO:EOF



:DO_C
    SHIFT
    

    echo %1 %2 %3 %4 %5 %6 %7 %8 %9 | findstr /C:"-cago" 1>nul

    if errorlevel 1 (
      rem echo. got one - pattern not found
      SET "autoGROUP=   "
    ) ELSE (
      SET "autoGROUP=   "
      rem SET autoGROUP=  -s cd -g ago
      rem echo. got zero - found pattern
    )

    rem pause
    IF NOT [%9] == [] GOTO:DO_C_9
    IF NOT [%8] == [] GOTO:DO_C_8
    IF NOT [%7] == [] GOTO:DO_C_7
    IF NOT [%6] == [] GOTO:DO_C_6
    IF NOT [%5] == [] GOTO:DO_C_5
    IF NOT [%4] == [] GOTO:DO_C_4
    IF NOT [%3] == [] GOTO:DO_C_3
    IF NOT [%2] == [] GOTO:DO_C_2
    IF NOT [%1] == [] GOTO:DO_C_1
    echo ERROR
GOTO:EOF

:DO_C_9
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4 %5 %6 %7 %8 %9 %autoGROUP%
GOTO:EOF
:DO_C_8
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4 %5 %6 %7 %8 %autoGROUP%
GOTO:EOF
:DO_C_7
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4 %5 %6 %7 %autoGROUP%
GOTO:EOF
:DO_C_6
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4 %5 %6 %autoGROUP%
GOTO:EOF
:DO_C_5
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4 %5 %autoGROUP%
GOTO:EOF
:DO_C_4
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3 %4  %autoGROUP%
GOTO:EOF
:DO_C_3
    CALL p. ls -s md -g ago -c ago name md %1 %2 %3  %autoGROUP%
GOTO:EOF
:DO_C_2
    CALL p. ls -s md -g ago -c ago name md %1 %2  %autoGROUP%
GOTO:EOF
:DO_C_1
    CALL p. ls -s md -g ago -c ago name md %1 %autoGROUP%
GOTO:EOF


 
