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


if [%2] == [] (
    CALL :ONE %1
) else (
    CALL :TWO %1 %2
)

GOTO:EOF
:ONE
type %1 | p. line --c -make " q ;'{};' " | p. execute
GOTO:EOF
:TWO
type %1 | p. line --c -make " q ;'{};' | p. line --c + %2 " | p. execute
GOTO:EOF

 
