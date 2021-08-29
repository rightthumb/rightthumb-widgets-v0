@echo off

if [%2] == [] (
	CALL :ONE %1
) else (
	CALL :TWO %1 %2
)

GOTO:EOF
:ONE
type %1 | p line --c -make " q ;'{};' " | p execute
GOTO:EOF
:TWO
type %1 | p line --c -make " q ;'{};' | p line --c + %2 " | p execute
GOTO:EOF