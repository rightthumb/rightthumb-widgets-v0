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

cls
echo Synchronizing python libraries
IF [%1] == [] call sync
cls
echo Initiating drive scan
echo.
call p. drive -scan
set /p USB=USB Drive: 

set usbDrive=%USB:~0,1%
echo %usbDrive%
rem GOTO:EOF
SET stmp=%myHome%\temp


rem %widgets%\techApps\Python\
rem %usbDrive%:\techApps\Python\

IF NOT EXIST %widgets%\techApps\xampp (GOTO:EOF)

IF NOT EXIST %usbDrive%:\techApps (md %usbDrive%:\techApps)
IF NOT EXIST %usbDrive%:\techApps\xampp (md %usbDrive%:\techApps\xampp)
IF NOT EXIST %usbDrive%:\techApps\Python (md %usbDrive%:\techApps\Python)
IF NOT EXIST %usbDrive%:\techApps\Python\Python27 (md %usbDrive%:\techApps\Python\Python27)
IF NOT EXIST "%usbDrive%:\techApps\Python\Python36-32" (md "%usbDrive%:\techApps\Python\Python36-32")
IF NOT EXIST "%usbDrive%:\techApps\Notepad++" (md "%usbDrive%:\techApps\Notepad++")
IF NOT EXIST "%usbDrive%:\techApps\Sublime Text 2.0.2 x64" (md "%usbDrive%:\techApps\Sublime Text 2.0.2 x64")
IF NOT EXIST %usbDrive%:\techApps\ProcessMonitor (md %usbDrive%:\techApps\ProcessMonitor)


xcopy /s/d/y/c %widgets%\techApps\xampp\*.* %usbDrive%:\techApps\xampp\
xcopy /s/d/y/c %widgets%\techApps\Python\Python27\*.* %usbDrive%:\techApps\Python\Python27\
xcopy /s/d/y/c "%widgets%\techApps\Python\Python36-32\*.*" "%usbDrive%:\techApps\Python\Python36-32\"
xcopy /s/d/y/c "%widgets%\techApps\Notepad++\*.*" "%usbDrive%:\techApps\Notepad++\"
xcopy /s/d/y/c "%widgets%\techApps\Sublime Text 2.0.2 x64\*.*" "%usbDrive%:\techApps\Sublime Text 2.0.2 x64\"
xcopy /s/d/y/c %widgets%\techApps\ProcessMonitor\*.* %usbDrive%:\techApps\ProcessMonitor\


IF NOT EXIST %usbDrive%:\widgets (md %usbDrive%:\widgets)
IF NOT EXIST %usbDrive%:\tech\srv (md %usbDrive%:\tech\srv)

IF NOT EXIST %usbDrive%:\tech\hosts (md %usbDrive%:\tech\hosts)
IF NOT EXIST %usbDrive%:\%hostDefault% (md %usbDrive%:\%hostDefault%)

xcopy /s/d/y/c %widgets%\%hostDefault%\*.* %usbDrive%:\%hostDefault%\

xcopy /s/d/y/c %widgets%\widgets\*.* %usbDrive%:\widgets\
rem xcopy /s/d/y/c %widgets%\widgets\*.* %usbDrive%:\widgets\




xcopy /d/y/c %widgets%\tech\*.* %usbDrive%:\tech\
xcopy /d/y/c %widgets%\widgets\*.* %usbDrive%:\widgets\
xcopy /d/y/c %widgets%\tech\srv\*.* %usbDrive%:\tech\srv\



 
