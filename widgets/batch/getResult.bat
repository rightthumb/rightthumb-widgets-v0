@echo off
set doThis=%1
IF [%1] == [] GOTO:EOF
CALL :DeQuote doThis
%doThis%>{6E5894A5FBA8}
set /p result=<{6E5894A5FBA8}

IF EXIST {6E5894A5FBA8} (
		del {6E5894A5FBA8}
	)
set doThis=

GOTO:EOF

:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
GOTO:EOF

