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
set changeDIR=false
set switchUsed=false
set switchAutoLegacy=false
set switch=
set clean=false
rem set py2=D:\Python27\python.exe
set two=%2
call :DeQuote two
if [%two:~0,1%] == [/] (
		set switchUsed=true
		set switch=%two:~1,100%
	) else (
		set switch=%2
	)
if [%switch%] == [a] (
		call :TOFOLDER
		if exist %1.py (move %1.py archive)
		if exist %1.py.bak (move %1.py.bak archive)
		goto:EOF
	)

if [%switch%] == [v] set clean=true
if [%switch%] == [/] set clean=true

if [%switch%] == [c] call :fix %1
if [%switch%] == [convert] call :fix %1
if [%switch%] == [r] call :recoverLegacy %1
if [%switch%] == [l] call :labelLegacy %1
call :checkLegacy %1
call :TOBACK
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
:TOFOLDER
set changeDIR=true
call m back
call b mypy
goto:EOF
:TOBACK
if [%changeDIR%] == [true] call b back
goto:EOF

:ver2
rem cls
if not [%clean%] == [true] (
	echo.
	echo _____________
	echo.
)
%py2% "%myPython%\%1.py" %*
if not [%clean%] == [true] (
	echo.
	echo _____________
	echo Python 2.7.13
	echo.
)
goto:EOF

:ver3
rem echo %switch%
rem cls
if [%clean%] == [true] (
	echo.
	echo _____________
	echo.
)
%py% "%myPython%\%1.py" %*
if [%clean%] == [true] (
	echo.
	echo ____________
	echo Python 3.6.2
	echo.
)
goto:EOF

:fix
call :TOFOLDER
call pyVer %1.py
set switchUsed=true
goto:EOF

:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
goto:EOF

:labelLegacy
call :TOFOLDER
%py% "%myPython%\labelFile.py" "%myPython%\%1.py" "#835B0032-Legacy"
set switchAutoLegacy=true
set switchUsed=true
set switch=2
goto:EOF

:checkLegacy
find /c "#835B0032" "%myPython%\%1.py" > nul
if not %errorlevel% equ 1 (
		set switchAutoLegacy=true
		set switch=2
	)
goto:EOF

:recoverLegacy
call :TOFOLDER
set fileName=%myPython%\%1.py
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