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

set to=c:\profile
:mkdir "%to%"
echo.> "%to%\temp"
cls
set "replace= "
netsh wlan show profiles|find "All User Profile" > "%to%\temp"
for /f "tokens=5-10 delims= " %%a in (%to%\temp) do (
	set "line='%%a %%b %%c %%d %%e %%f'"
	setlocal enabledelayedexpansion
	set "line=!line:%replace%%replace%=!"
	set "line=!line:%replace%'='!"
	set "line=!line:'=!"
	netsh wlan export profile name="!line!" folder="%to%"
	endlocal
)
del "%to%\temp"