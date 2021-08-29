@echo off
if [%1] == [] (
		call :ACTION1
	) else (
		call :ACTION2 %*
	)
GOTO:EOF
:ACTION1
cls
echo.
call p touch ?
echo.
GOTO:EOF
:ACTION2
if [%2] == [] (
		call :ACTION3 %1
	) else (
		call :ACTION4 %*
	)
GOTO:EOF



:ACTION3
cls
echo.
call p touch -f %1 -mod now
echo.
GOTO:EOF

:ACTION4
cls
echo.
call p touch %*
echo.
GOTO:EOF