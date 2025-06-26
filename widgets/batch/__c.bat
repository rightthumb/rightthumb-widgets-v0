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

CLS
echo Loading...
IF [%1] == [r] SET api=
IF NOT ["%api%"] == ["loaded"] (
        CALL :LOAD
    ) else (
        CLS
    )

CALL :TIMESTAMP

GOTO:EOF
:LOAD
SET /p Drive=<%userprofile%\.tk421
SET widgets=%Drive:~0,1%
SET widgets=%Drive:~0,1%
SET widgets=%Drive:~0,1%
SET widgets=%Drive:~0,1%
SET /p installID=<%widgets%\tech\scripts\instanceID.sys
SET Drive=



::::::: API Paths (Asside from PHP)
SET widgets=%widgets%\tech
SET scriptroot=%widgets%\scripts
SET pssroot=%widgets%\PS_Scripts
SET pss=%widgets%\tech\PS_Scripts
SET scriptrootAlias=%scriptroot%\alias


::::::: PHP Drive

SET log_folder=%scriptroot%\log
SET php=%widgets%\tech\srv\xampp\php\php.exe
SET phpFiles=%scriptroot%\php




::::::: Command Paths
rem SET oldPath=%path%
SET pathAPI=%scriptroot%\;%scriptrootAlias%\
rem SET pathApps=D:\Program Files (x86)\ImageMagick-6.9.2-Q16;D:\ProgramData\Oracle\Java\javapath;D:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;D:\Program Files (x86)\Intel\iCLS Client\;D:\Program Files\Intel\iCLS Client\;D:\WINDOWS\system32;D:\WINDOWS;D:\WINDOWS\System32\Wbem;D:\WINDOWS\System32\WindowsPowerShell\v1.0\;D:\Program Files (x86)\Windows Live\Shared;D:\Program Files\Intel\WiFi\bin\;D:\Program Files\Common Files\Intel\WirelessCommon\;D:\Program Files\Intel\Intel(R) Management Engine Components\DAL;D:\Program Files\Intel\Intel(R) Management Engine Components\IPT;D:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;D:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;D:\Program Files (x86)\Common Files\Acronis\SnapAPI\;D:\Program Files (x86)\Skype\Phone\;D:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\;%USERPROFILE%\AppData\Local\Microsoft\WindowsApps
SET pathPython=%widgets%\tech\scripts\python;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Lib\site-packages;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32;%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts
rem SET pathBuilder=%pathPython%;%path%;%pathAPI%;%pathApps%;
SET pathBuilder=%pathPython%;%path%;%pathAPI%;
SET path=%pathBuilder%
SET pathAPI=
SET pathBuilder=
SET pathPython=

::::::: App shortcuts
rem CALL findExcel
rem CALL findChrome
rem SET lib=D:\_Scott\S_Documents\Projects\self\Library
rem SET acro="c:\Program Files (x86)\Adobe\Acrobat 11.0\Acrobat\Acrobat.exe"
rem SET bzip2="D:\Program Files\GnuWin32\bin\bzip2.exe"
::SET n="D:\Program Files (x86)\Notepad++\notepad++.exe"
::SET n="D:\Program Files (x86)\Notepad++\notepad++.exe"
SET n="D:\Program Files\Sublime Text 3\sublime_text.exe"
SET n=%code_editor%
rem SET w="D:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE"

rem SET py="%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\python.exe"
rem SET py2="D:\Python27\python.exe"
SET py="%widgets%\Apps\Python\Python36-32\python.exe"
SET py2="%widgets%\Apps\Python\Python27\python.exe"
::SET pys="%USERPROFILE%\AppData\Local\Programs\Python\Python35\Scripts"
rem SET pys=%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Scripts
rem SET pytools=%USERPROFILE%\AppData\Local\Programs\Python\Python36-32\Tools\scripts
SET pyroot=%scriptroot%\python
::::::: API Variable Extras
set /p quote=<%scriptroot%\quote.txt
set /p percentage=<%scriptroot%\percentage.txt
set /p percent=<%scriptroot%\percentage.txt
rem SET stemp=%scriptroot%\temp
SET stmp=%scriptroot%\temp
rem SET stemp=%stmp%
rem SET stmpfile=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
rem SET tmpf=%stmpfile%
SET tmpf=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
rem SET stempfile=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
rem SET sql=D:\_Scott\S_Documents\Projects\sql


IF ["%Session_ID%"] == [""] CALL :GENERATE_API_ID
SET api=loaded
CLS
echo.
CALL p. drive -scan
prompt - 

GOTO:EOF


:GENERATE_API_ID
SET /p LastID=<%scriptroot%\ID.sys
rem SET caseroot=API_ID.sys
SET /a Session_ID=%LastID% + 1
echo %Session_ID% > %scriptroot%\ID.sys
CALL timestamp ats2 noEcho
SET timestamp_start=%now%
echo %timestamp_start%
:::::::::::::::::::::::: DOESNT WORK - :: CALL getSID
GOTO:EOF

:TIMESTAMP
CALL timestamp sdel noEcho
set ts=%now%
set timestamp=%now%

CALL timestamp d2 noEcho
set today=%now%
title %today%

CALL timestamp t2 noEcho

GOTO:EOF






 
