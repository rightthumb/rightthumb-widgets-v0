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
	echo provide path to opt folder
	goto:eof
)
echo unable to change ownership in linux
goto:eof
set distro_opt=%1
call :DeQuote distro_opt
echo %distro_opt%
echo.
echo.
if not exist %distro_opt%\RightThumb   mkdir %distro_opt%\RightThumb
if not exist %distro_opt%\RightThumb\tech   mkdir %distro_opt%\RightThumb\tech
if not exist %distro_opt%\RightThumb\widgets   mkdir %distro_opt%\RightThumb\widgets
if not exist %distro_opt%\RightThumb\widgets\python   mkdir %distro_opt%\RightThumb\widgets\python
if not exist %distro_opt%\RightThumb\widgets\python\src   mkdir %distro_opt%\RightThumb\widgets\python\src
if not exist %distro_opt%\RightThumb\widgets\python   mkdir %distro_opt%\RightThumb\widgets\python

if not exist %distro_opt%\RightThumb\widgets\bash   mkdir %distro_opt%\RightThumb\widgets\bash

if not exist %distro_opt%\RightThumb\widgets\databank   mkdir %distro_opt%\RightThumb\widgets\databank




xcopy /s/d/y/c %programs%\python\*.* %distro_opt%\RightThumb\widgets\python\

xcopy /s/d/y/c %programs%\bash\*.* %distro_opt%\RightThumb\widgets\bash\

xcopy /s/d/y/c %programs%\databank\*.* %distro_opt%\RightThumb\widgets\databank\


goto:EOF


:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
goto:EOF