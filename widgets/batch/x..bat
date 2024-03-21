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

%py% %widgets%\widgets\python\folder-registration.py

echo.
echo Reminder run   r.t   once a week.
echo.

rem call p. fileBackup -f %wprofile%\projects\project-log.txt

SET ORIGINAL_Session_ID=%Session_ID%

IF [%1] == [r] SET reclaim_tickets=yes
doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1

SET BackupRunOnce=N
CALL p. checkForRunOnceBackups

SET runOnceStatus=NO
SET /p runOnceStatus=<%myVars%\hasRunOnceScheduled

IF [%runOnceStatus%] == [YES] CALL :RunOnceBackupAsk





rem pause

rem echo %Session_ID%
rem echo %myVars%\ID.sys
IF NOT EXIST %myVars%\ID.sys SET myVars=D:\.rightthumb-widgets\hosts\VULCAN\vars
IF NOT EXIST %myVars%\ID.sys (
    echo NOT EXIST %myVars%\ID.sys
    goto:eof
)

CALL :IDTEST
CALL :IDTEST


if not [%computername%] == [VULCAN] GOTO :SKIP1
if %Session_ID% LSS 5000 (
    echo Session_ID: %Session_ID% BAD
    echo.
    goto:eof
)
:SKIP1



CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE
CALL :TESTFILE

CALL :FILENAME
IF EXIST "%file%" (
    echo File exists: %file%
    echo %Session_ID%
    goto:eof
)
if not [%computername%] == [VULCAN] GOTO :SKIP2
if %Session_ID% LSS 5000 (
    echo Session_ID: %Session_ID% BAD
    echo.
    goto:eof
)
:SKIP2
set html=%myTickets%\html
IF NOT EXIST %html% MD %html%
set timestamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2% @ %time:~0,2%:%time:~3,2%
set timestamp_end=Session:%Session_ID% CLOSE %timestamp%
set start_stamp=%timestamp_start% 
set timestamp_start=Session:%Session_ID% OPEN %start_stamp%
echo ^<div class='box' ^> >> "%file%"
echo ^<div class='item' ^> >> "%file%"
echo Session: %Session_ID% (%start_stamp%- %timestamp%) isAdmin:%isAdmin% %project%>> "%file%"
echo ^</div^> >> "%file%"
echo ^<br^> >> "%file%"
echo ^<div class='guid' ^> %instanceID%^</div^>>> ^<br^> >> "%file%"
echo ^<div class='sid' ^> %machineID%^</div^>>> ^<br^> >> "%file%"
echo ^<div class='details' ^> >> "%file%"





if not ["%lab%"] == [""] echo ^<div class='laboratory' ^> %lab% >> ^</div^> >> "%file%"





echo ^<br^> >> "%file%"
echo ^<pre^> >> "%file%"

CALL p. singleLine -f "%stmp%\unclaimed_tickets_history\history-%ORIGINAL_Session_ID%.txt" > "%fileTempData%"  2>&1
rem doskey /history > "%fileTempData%"

type "%fileTempData%" | p. passFilter >> "%file%"
type "%file%" > "%fileTempData%"
del "%fileTempData%"
rem doskey /history >> "%file%"
echo ^</pre^> >> "%file%"
echo ^<br^> ^</div^> ^</div^> ^<br^> >> "%file%"

rem del "%stmp%\unclaimed_tickets_history\history-%ORIGINAL_Session_ID%.txt"


rem echo.
rem echo x
rem echo %open_timestamp%
rem echo x

















rem call p. autoBackup -ago 1d
echo %Session_ID%
echo %myVars%\ID.sys
rem pause
echo "%file%"
rem set /p test=pause
GOTO KILL

=================

call b s
cd

echo code_in > name.txt
echo pc_code > pc.txt
set /p n=<name.txt
set /p pc=<pc.txt
GOTO KILL
GOTO END
:KILL






:END
@echo on

type %html%\header > %html%\tickets.htm
::type %myTickets%\open-* >> %html%\tickets.htm
call b myTickets
dir /b open-* |sort >~openTickets.txt
for /F "tokens=*" %%A in  (~openTickets.txt) do  (
   ECHO Processing Ticket File %%A.... 
   type %%A  >> %html%\tickets.htm
)

type %html%\footer >> %html%\tickets.htm

::del /Q /F %scriptroot%\Session_%Session_ID%.sys
IF EXIST ~openTickets.txt (del ~openTickets.txt)

 

rem echo BackupRunOnce: %BackupRunOnce%
IF [%BackupRunOnce%] == [Y] (

    echo BackupRunOnce: STARTED
    call:autoBackup_A
    rem call p. autoBackup -date "%open_timestamp2%" -include_once
) ELSE (
    echo BackupRunOnce: SKIPPED
    call:autoBackup_B
    rem call p. autoBackup -date "%open_timestamp2%"
)

if not [%ORIGINAL_Session_ID%] == [%Session_ID%] ( CALL p. ticket_transfer -old %ORIGINAL_Session_ID% -new %Session_ID%)

rem pause
echo.
echo.
IF [%reclaim_tickets%] == [yes] CALL p. unclaimed_tickets
exit
:RunOnceBackupAsk
if [%skip_backup%] == [YES] (
call c
echo skip_backup
) else (
    SET /p roAsk=Backup run once? (n)  
    IF NOT [%roAsk%] == [] SET BackupRunOnce=Y
)
goto:eof

:FILENAME
if ["%project%"] == [""] set name=closed-%Session_ID%.txt
if NOT ["%project%"] == [""] set name=open-%Session_ID%.txt
set file=%myTickets%\%name%
set fileTempData=%myTickets%\tempFile.txt

goto:eof

:TESTFILE
if [%computername%] == [VULCAN] CALL :TESTFILE2
:TESTFILE2
CALL :FILENAME
IF EXIST "%file%" (
    SET /p LastID=<%myVars%\ID.sys
    SET /a Session_ID=%LastID% + 1
    if %Session_ID% GTR 5000 ( CALL :UPDATE_ID_FILE )
)
goto:eof

:IDTEST
if [%computername%] == [VULCAN] (
    CALL :IDTEST_HOME
) else (
    CALL :IDTEST_ALT
)
:IDTEST_HOME
if %Session_ID% LSS 5000 (
    echo Session_ID: %Session_ID% BAD
    SET /p LastID=<%myVars%\ID.sys
    SET /a Session_ID=%LastID% + 1
    if %Session_ID% GTR 5000 ( CALL :UPDATE_ID_FILE )
    echo Session_ID: %Session_ID% NEW
    echo.
)
:IDTEST_ALT
CALL :TEST_FILE

if [%fileError%] == [True] (
    echo Session_ID: %Session_ID% BAD
    SET /p LastID=<%myVars%\ID.sys
    SET /a Session_ID=%LastID% + 1
    CALL :UPDATE_ID_FILE
    
    echo.
    CALL :IDTEST_ALT
)
goto:eof
:TEST_FILE
SET fileError=False
CALL :FILENAME
IF EXIST "%file%" (
    SET fileError=True
)
goto:eof

:UPDATE_ID_FILE
if [%Session_ID%] == [] (
    SET Session_ID=%Session_ID_BK%
) else (
    echo %Session_ID% > %myVars%\ID.sys
)
goto:eof
:autoBackup_A
rem if [%skip_backup%] == [YES] (
rem     echo skip_backup
rem ) else (
rem     call p. autoBackup -date "%open_timestamp2%" -include_once
rem )
goto:eof
:autoBackup_B
rem if [%skip_backup%] == [YES] (
rem     echo skip_backup
rem ) else (
rem     call p. autoBackup -date "%open_timestamp2%"
rem )
goto:eof


 
