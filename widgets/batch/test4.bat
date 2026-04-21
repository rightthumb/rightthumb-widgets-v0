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

if exist "D:\drive.id.sys" set extDrive=B & CALL :SETDRIVE
if exist "D:\drive.id.sys" set extDrive=C & CALL :SETDRIVE
if exist "D:\drive.id.sys" set extDrive=D & CALL :SETDRIVE
if exist "E:\drive.id.sys" set extDrive=E & CALL :SETDRIVE
if exist "F:\drive.id.sys" set extDrive=F & CALL :SETDRIVE
if exist "G:\drive.id.sys" set extDrive=G & CALL :SETDRIVE
if exist "H:\drive.id.sys" set extDrive=H & CALL :SETDRIVE
if exist "I:\drive.id.sys" set extDrive=I & CALL :SETDRIVE
if exist "J:\drive.id.sys" set extDrive=J & CALL :SETDRIVE
if exist "K:\drive.id.sys" set extDrive=K & CALL :SETDRIVE
if exist "L:\drive.id.sys" set extDrive=L & CALL :SETDRIVE
if exist "M:\drive.id.sys" set extDrive=M & CALL :SETDRIVE
if exist "N:\drive.id.sys" set extDrive=N & CALL :SETDRIVE
if exist "O:\drive.id.sys" set extDrive=O & CALL :SETDRIVE
if exist "P:\drive.id.sys" set extDrive=P & CALL :SETDRIVE
if exist "Q:\drive.id.sys" set extDrive=Q & CALL :SETDRIVE
if exist "R:\drive.id.sys" set extDrive=R & CALL :SETDRIVE
if exist "S:\drive.id.sys" set extDrive=S & CALL :SETDRIVE
if exist "T:\drive.id.sys" set extDrive=T & CALL :SETDRIVE
if exist "U:\drive.id.sys" set extDrive=U & CALL :SETDRIVE
if exist "V:\drive.id.sys" set extDrive=V & CALL :SETDRIVE
if exist "W:\drive.id.sys" set extDrive=W & CALL :SETDRIVE
if exist "X:\drive.id.sys" set extDrive=X & CALL :SETDRIVE
if exist "Y:\drive.id.sys" set extDrive=Y & CALL :SETDRIVE
if exist "Z:\drive.id.sys" set extDrive=Z & CALL :SETDRIVE
GOTO AFTERDRIVE
:SETDRIVE
set driveFound=false
set thisIsScriptDrive=false

set /p extId=<"%extDrive:~0,1%:\drive.id.sys"
IF [%extId%] == [] GOTO:EOF
IF [%extId%] == [{D644A899-89BB-9748-8339-3FC5F75B8A16}] set driveFound=t3
IF [%extId%] == [{EFFBC611-F9AD-7993-43D3-48D509090FB5}] set driveFound=b32
IF [%extId%] == [{653103B6-8D0D-2686-6F0B-5E686CEF3AE6}] set driveFound=l119

IF [%driveFound%] == [false] GOTO:EOF
IF [%driveFound%] == [t3] (
	echo %extDrive:~0,1%> %userprofile%\3T_drive.txt
	set t3Drive=%extDrive:~0,1%
	set t3=%extDrive:~0,1%
	)
IF [%driveFound%] == [l119] (
	echo %extDrive:~0,1%> %userprofile%\l119_drive.txt
	set l119=%extDrive:~0,1%
	)
IF [%driveFound%] == [b32] (
	set thisIsScriptDrive=true
	)
:::::::
IF [%thisIsScriptDrive%] == [true] (
	::::::: Script Root
	echo %extDrive:~0,1%> %userprofile%\php_drive.txt
	set widgets=%extDrive:~0,1%
	set widgets=%extDrive:~0,1%
	set widgets=%extDrive:~0,1%
	)

GOTO:EOF
:::::::::::::::::::::::::::::::::::::::::::
:AFTERDRIVE