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

:: type c.bat | p. line -m "{} " + set =  --c | p. line --c - "= " rem ::
:: type c.bat | p. line - \ if ;.;. set rem echo goto call cls ")" prompt -ln
rem 026 :HARDRELOAD
rem 105 :RELOADVARS
rem 110 :VARS
rem 144 :CLEARDRIVE
rem 208 :AFTERDRIVE
rem 323 :SKIPID
rem 330 :STARTC
rem 336 :END
rem 353 :NOCLEAR
rem 364 :FORCEDRIVE
rem 376 :DRIVESCHECKED
rem %USERPROFILE%\Desktop\2018.02.13\varCleanup.txt




::::::: Date and Time Stuff
set thisday=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
set now=%time:~0,2%:%time:~3,2%
set timestamp=%thisday%-%time:~0,2%.%time:~3,2%
set ts=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%-%time:~0,2%.%time:~3,2%
set today=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%


IF ["%1"] == [""] call :STARTC
IF ["%1"] == ["hr"] call :HARDRELOAD
IF ["%1"] == ["r"] call :RELOADVARS
call :END

GOTO:EOF

:: ------------------------------------------- ::
:HARDRELOAD
echo HARD RELOAD
set pathUSB=
set Drive=
set log_folder=
set phpFiles=
set pathT3=
set scriptrootAlias=
set pathAPI=
set pathBuilder=
set quote=
set LastID=
set caseroot=
set Session_ID=
set timestamp_start=
set pathT3=
set pathAPI=
set pathBuilder=
set LastID=
set timestamp_start=
set drivesCheckedAlready=
set path=%oldPath%
set thisSID=
set thisGUID=
set instanceID
::::
set path2=
set acro=
set api=
set back=
set bmRoot=
set bname=
set bumpapp1=
set bzip2=
set caseroot=
set chrome=
set chrome1=
set chrome2=
set chrome3=
set Drive=
set widgets=
set drivesCheckedAlready=
set drive_letter=
set excel=
set excel1=
set excel2=
set indexindex=
set log_folder=
set n=
set n=
set now=
set p=
set pathUSB=
set pc=
set php=
set widgets=
set phpFiles=
set runone=
set widgets=
set scriptroot=
set scriptrootAlias=
set search=
set Session_ID=
set t3=
set t3Drive=
set t3set=
set thisday=
set thisFile=
set timestamp=
set today=
set ts=
set ts2=
set verDate=
set widgets=
::::
call :RELOADVARS
GOTO:EOF


:RELOADVARS
set api=
call :VARS
GOTO:EOF

:VARS
IF ["%api%"] == ["loaded"] GOTO END

::::::: DRIVE SCAN
:::::::::::::::::::::::::::::::::::::::::::
rem GOTO SKIP_THIS_SECTION_001
CALL :CLEARDRIVE
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

:CLEARDRIVE
set t3=0
set l119=0
set widgets=0
set cloudPub=0
set cloudPriv=0
set cloudJr=0

GOTO:EOF

:SETDRIVE
set driveFound=false
set thisIsScriptDrive=false

set /p extId=<"%extDrive:~0,1%:\drive.id.sys"
IF [%extId%] == [] GOTO:EOF
IF [%extId%] == [{D644A899-89BB-9748-8339-3FC5F75B8A16}] set driveFound=t3
IF [%extId%] == [{EFFBC611-F9AD-7993-43D3-48D509090FB5}] set driveFound=b32
IF [%extId%] == [{653103B6-8D0D-2686-6F0B-5E686CEF3AE6}] set driveFound=l119
IF [%extId%] == [{C7DA4040-A42C-0372-B54A-8E40F835D3E1}] set driveFound=cloudPub
IF [%extId%] == [{5B55D9AE-6C90-B44B-2071-5376CBB2AAAE}] set driveFound=cloudPriv

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
IF [%driveFound%] == [cloudPub] (
    echo %extDrive:~0,1%> %userprofile%\cloudPub_drive.txt
    set cloudPub=%extDrive:~0,1%
    )
IF [%driveFound%] == [cloudPriv] (
    echo %extDrive:~0,1%> %userprofile%\cloudPriv_drive.txt
    set cloudPriv=%extDrive:~0,1%
    )
IF [%driveFound%] == [b32] (
    set thisIsScriptDrive=true
    )
:::::::
IF [%thisIsScriptDrive%] == [true] (
    ::::::: Script Root
    echo %extDrive:~0,1%> %userprofile%\.tk421
    set widgets=%extDrive:~0,1%
    set widgets=%extDrive:~0,1%
    set widgets=%extDrive:~0,1%
    set installId=%extId%
    )
set thisIsScriptDrive=
set driveFound=
set extId=

GOTO:EOF
:::::::::::::::::::::::::::::::::::::::::::

rem :SKIP_THIS_SECTION_001




:AFTERDRIVE
IF EXIST %widgets%\ (
        set widgets=%widgets%
        set widgets=%widgets%
        set widgets=%widgets%
        set /p installId=<%widgets%\tech\scripts\instanceID.sys
    ) else (
        set /p Drive=<%userprofile%\.tk421
        set widgets=%Drive:~0,1%
        set widgets=%Drive:~0,1%
        set widgets=%Drive:~0,1%
        set widgets=%Drive:~0,1%
        set /p installId=<%widgets%\tech\scripts\instanceID.sys
        set Drive=
    )

rem IF [%widgets%] == [0] (
rem     set /p Drive=<%userprofile%\.tk421
rem     set widgets=%Drive:~0,1%
rem     set widgets=%Drive:~0,1%
rem     set widgets=%Drive:~0,1%
rem     set widgets=%Drive:~0,1%
rem     set /p installId=<%widgets%\tech\scripts\instanceID.sys
rem     set Drive=
rem     )




::::::: API Paths (Asside from PHP)
set scriptroot=%widgets%\tech\scripts
set widgets=%widgets%\tech
set pssroot=%widgets%\tech\PS_Scripts
set pss=%widgets%\tech\PS_Scripts
set scriptrootAlias=%scriptroot%\alias


::::::: PHP Drive

set log_folder=%scriptroot%\log
set php=%widgets%\tech\srv\xampp\php\php.exe
set phpFiles=%scriptroot%\php




::::::: Command Paths
::set pathAdminTools=D:\tech\FTP_Share\Tech\Apps\tech\batch_files\batch\admtool2
::set pathCygwin=D:\PROGRA~1\GNUWIN32\BIN
::;%userprofile%
set oldPath=%path%
set pathAPI=%scriptroot%\;%scriptrootAlias%\
set pathApps=D:\Program Files (x86)\ImageMagick-6.9.2-Q16;D:\ProgramData\Oracle\Java\javapath;D:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;D:\Program Files (x86)\Intel\iCLS Client\;D:\Program Files\Intel\iCLS Client\;D:\WINDOWS\system32;D:\WINDOWS;D:\WINDOWS\System32\Wbem;D:\WINDOWS\System32\WindowsPowerShell\v1.0\;D:\Program Files (x86)\Windows Live\Shared;D:\Program Files\Intel\WiFi\bin\;D:\Program Files\Common Files\Intel\WirelessCommon\;D:\Program Files\Intel\Intel(R) Management Engine Components\DAL;D:\Program Files\Intel\Intel(R) Management Engine Components\IPT;D:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;D:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;D:\Program Files (x86)\Common Files\Acronis\SnapAPI\;D:\Program Files (x86)\Skype\Phone\;D:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps
rem set pathPython=%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib\;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts\
set pathPython=%widgets%\tech\scripts\python;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib\site-packages;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts
set pathBuilder=%pathPython%;%path%;%pathAPI%;%pathApps%;
set path=%pathBuilder%


::::::: App shortcuts
call findExcel
call findChrome
set lib=D:\_Scott\S_Documents\Projects\self\Library
set acro="c:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Acrobat.exe"
set bzip2="D:\Program Files\GnuWin32\bin\bzip2.exe"
::set n="D:\Program Files (x86)\Notepad++\notepad++.exe"
::set n="D:\Program Files (x86)\Notepad++\notepad++.exe"
set n="D:\Program Files\Sublime Text 3\sublime_text.exe"
set n=%code_editor%
set w="D:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"
::set py="%USERPROFILE%\AppData\Local\Programs\Python\Python35\python.exe"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
rem set py="%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\python.exe"
rem set py2="D:\Python27\python.exe"
set py="%widgets%\Apps\Python\Python36-32\python.exe"
set py2="%widgets%\Apps\Python\Python27\python.exe"
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::set pys="%USERPROFILE%\AppData\Local\Programs\Python\Python35\Scripts"
set pys=%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts
set pytools=%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Tools\scripts
set pyroot=%scriptroot%\python
::::::: API Variable Extras
set /p quote=<%scriptroot%\quote.txt
set /p percentage=<%scriptroot%\percentage.txt
set /p percent=<%scriptroot%\percentage.txt
set /p instanceID=<%scriptroot%\instanceID.sys
set stemp=%scriptroot%\temp
set stmp=%scriptroot%\temp
set stmpfile=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
set stempfile=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
set sql=D:\_Scott\S_Documents\Projects\sql

::::::: Date and Time Stuff
set thisday=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
set now=%time:~0,2%:%time:~3,2%
set timestamp=%thisday%-%time:~0,2%.%time:~3,2%
set ts=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%-%time:~0,2%.%time:~3,2%
set today=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%


::::::: GENERATE API ID
IF NOT ["%Session_ID%"] == [""] GOTO SKIPID
set /p LastID=<%scriptroot%\ID.sys
set caseroot=API_ID.sys
set /a Session_ID=%LastID% + 1
echo %Session_ID% > %scriptroot%\ID.sys
set timestamp_start=%thisday% @ %now%
echo %timestamp_start%
call getSID
:SKIPID
GOTO:EOF





:STARTC
IF [%api%] == [] call :RELOADVARS
call :VARS
GOTO:EOF


:END

::::::: Title
IF [%api%] == [] (title %thisday%)
IF [%1] == [r] (title %thisday%)
IF [%1] == [t] (title %thisday%)


::::::: CLEANUP, OTHER
IF NOT EXIST %stemp% (md %stemp%)
set pathT3=
set pathAPI=
set pathBuilder=
set LastID=
IF [%1] == [v] (GOTO NOCLEAR)
prompt - 
cls
:NOCLEAR



::::::: Check Drives
call %widgets%\tech\scripts\updateDate.bat
set /p verDate=<%widgets%\tech\scripts\verDate.txt
IF [%1] == [drive] (GOTO FORCEDRIVE)
IF [%1] == [v] (GOTO DRIVESCHECKED)
IF [%drivesCheckedAlready%] == [y] GOTO DRIVESCHECKED
IF [%1] == [c] GOTO DRIVESCHECKED
:FORCEDRIVE
echo __________________________
echo      %verDate%
echo __________________________
IF NOT [%widgets%] == [0]     (echo          %widgets% 32BTN)
IF NOT [%t3%] == [0]           (echo          %t3%: T3)
IF NOT [%l119%] == [0]         (echo          %l119%: 119L)
IF NOT [%cloudPub%] == [0]     (echo          %cloudPub%: cloudPub)
IF NOT [%cloudPriv%] == [0]    (echo          %cloudPriv%: cloudPriv)
echo __________________________
cls
call drivescan
:DRIVESCHECKED
set drivesCheckedAlready=y
set api=loaded
echo.
GOTO:EOF

::::::: DONE

:::::::::::::::NOTES FOR SCRIPT WRITING

::::::: Command Results to Variable
::for /f "delims=" %%i in ('command') do set output=%%i

::::::: NEW PHP
::set thisFile=
::%php% %phpFiles%\%thisFile%
:::::::








 
