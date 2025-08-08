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


goto check_Permissions

:check_Permissions    
	net session >nul 2>&1
	if %errorLevel% == 0 (
		rem echo Success: Administrative permissions confirmed.
	) else (
		echo Failure: Current permissions inadequate.
		goto:eof
	)
	

rem title Fix Printer
echo Fixing Printer
echo ------------------
net stop spooler
dir /s %systemroot%\system32\spool\printers\*.shd
dir /s %systemroot%\system32\spool\printers\*.spl
del %systemroot%\system32\spool\printers\*.shd
del %systemroot%\system32\spool\printers\*.spl
net start spooler
echo ------------------
rem pause