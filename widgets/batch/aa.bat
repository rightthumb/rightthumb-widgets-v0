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

if [%1] == [] goto:EOF
set switchUsed=false
set switchAutoLegacy=false
set switch=

set two=%2
call :DeQuote two
if [%two:~0,1%] == [/] (
		set switchUsed=true
		set switch=%two:~1,100%
	) else (
		set switch=%2
	)
if [%switch%] == [a] (
		if exist %1.py (move %1.py archive)
		if exist %1.py.bak (move %1.py.bak archive)
		goto:EOF
	)
if [%switch%] == [c] call :fix %1
if [%switch%] == [convert] call :fix %1
if [%switch%] == [r] call :recoverLegacy %1
if [%switch%] == [l] call :labelLegacy %1
call :checkLegacy %1
if [%switch%] == [2] (
		if [%switchAutoLegacy%] == [true] (
				call :ver2 %*
			) else (
				set one = %1&shift&shift
				call :ver2 %one% %*
			)
	) else (
		if [%switchUsed%] == [false] (
				call :ver3 %*
			) else (
				set one = %1&shift&shift
				call :ver3 %one% %*
			)
	)


goto:EOF


:ver2
rem cls
echo.
echo _____________
echo.
%py2% "%pyroot%\%1.py" %*
echo.
echo _____________
echo Python 2.7.13
echo.
goto:EOF

:ver3
rem cls
echo.
echo _____________
echo.
%py% "%pyroot%\%1.py" %*
echo.
echo ____________
echo Python 3.6.2
echo.
goto:EOF

:fix
call pyVer %1.py
set switchUsed=true
goto:EOF

:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
goto:EOF

:labelLegacy
%py% "%pyroot%\labelFile.py" "%pyroot%\%1.py" "#835B0032-Legacy"
set switchAutoLegacy=true
set switchUsed=true
set switch=2
goto:EOF

:checkLegacy
find /c "#835B0032" "%pyroot%\%1.py" > nul
if not %errorlevel% equ 1 (
		set switchAutoLegacy=true
		set switch=2
	)
goto:EOF

:recoverLegacy
set fileName=%pyroot%\%1.py
if exist "%fileName%" (
		if exist "%fileName%.bak" (
				del /q "%fileName%"
				type "%fileName%.bak" > "%fileName%"
				del /q "%fileName%.bak"

				
			)
	)
set switchAutoLegacy=true
set switchUsed=true
set switch=2
call :labelLegacy %1
goto:EOF