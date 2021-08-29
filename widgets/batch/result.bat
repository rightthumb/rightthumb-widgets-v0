@echo off

%*>"%stmp%\result.tmp"
set /p result=<"%stmp%\result.tmp"
rem echo %result%

GOTO:EOF
SETLOCAL ENABLEDELAYEDEXPANSION
SET count=1
FOR /F "tokens=* USEBACKQ" %%F IN (`%*`) DO (
  SET result!count!=%%F
  SET /a count=!count!+1
	set result=%result1%
)
ENDLOCAL

GOTO:EOF

