@echo off
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

