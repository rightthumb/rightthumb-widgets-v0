@echo off
call c
call p. on -delete -session %Session_ID%
if [%1] == [lock] call p. lock-files
if [%1] == [l] call p. lock-files
@REM if [%1] == [] call pin
title=Closing Queue
call p. lock-wait -wait x
call p. lock-wait -lock x
call p. lock-files -timer




::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
call p. day-divisible -save %tmpf%-day-divisible -divisible 2
set /p dayDivisible=<%tmpf%-day-divisible
if [%dayDivisible%] == [Yes] goto check_if_already_backed_up_today

goto End_Of_LogBackup

:check_if_already_backed_up_today
setlocal
:: Create the directory if it does not exist
if not exist "%tt%\bk" mkdir "%tt%\bk"

:: Set today's date in YYYY-MM-DD format
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (
	set year=%%c
	set month=%%a
	set day=%%b
)
set todaysDate=%year%-%month%-%day%

:: Check if the directory for today exists, if not, set bkBackupLog to false
if not exist "%tt%\bk\today" (
	set bkBackupLog=false
) else (
	set bkBackupLog=true
)

:: Perform operations based on bkBackupLog
if "%bkBackupLog%"=="false" (
	call :checkToday
) else (
	echo fileBackup.json already backed up today
)
echo %todaysDate% > "%tt%\bk\today"
endlocal
goto End_Of_LogBackup

:: Define the checkToday subroutine
:checkToday
set /p checkToday=<"%tt%\bk\today"
call :trimSpaces checkToday

if "%checkToday%"=="%todaysDate%" (
	echo fileBackup.json already backed up today <====================================== Already
) else (
	call p. bk -f %tt%\fileBackup.json -fo %tt%\bk
	echo fileBackup.json backed up <------------------------------------------ First
)
goto:eof

:: Trim function to remove leading and trailing spaces
:trimSpaces
setlocal enabledelayedexpansion
set "str=!%1!"
for /f "tokens=* delims= " %%a in ("!str!") do set "str=%%a"
for /f "tokens=* delims= " %%a in ("!str!") do endlocal & set "%1=%%a"
goto :eof

:: End of script
:End_Of_LogBackup
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::




rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

title=Closing

%py% %widgets%\widgets\python\folder-registration.py

call %userprofile%\.rt\profile\vars\config.bat
rem call %widgets%\widgets\batch\resetVars.bat
call %widgets%\widgets\batch\c.bat %1 
title=Closing
echo.
echo Reminder run   r.t   once a week.
echo.
rem call p. fileBackup -f %wprofile%\projects\project-log.txt
goto:skipper

:del_session
if exist "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt" (
	call rm "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"
)
goto:eof

:skipper
SET ORIGINAL_Session_ID=%Session_ID%
if [%burn_this%] == [yes] (
	title Closed
	call:del_session
	call p. lock-wait -unlock x
	call p. lock-wait -unlock x
	@REM call p. ctrl-w
	echo Exit Script Complete
	exit
	goto:eof

)
IF [%1] == [r] SET reclaim_tickets=yes
doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1

SET BackupRunOnce=N
CALL p. checkForRunOnceBackups

SET runOnceStatus=NO
SET /p runOnceStatus=<%myVars%\hasRunOnceScheduled

IF [%runOnceStatus%] == [YES] CALL :RunOnceBackupAsk

set skip_backup=NO




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
call p. fileBackup -f "%file%"
rem doskey /history >> "%file%"
echo ^</pre^> >> "%file%"
echo ^<br^> ^</div^> ^</div^> ^<br^> >> "%file%"

rem del "%stmp%\unclaimed_tickets_history\history-%ORIGINAL_Session_ID%.txt"


rem echo.
rem echo x
rem echo %open_timestamp%
rem echo x
















rem call p. autoBackup -date "%open_timestamp2%" -include_once
rem call p. autoBackup -ago 1d

echo %Session_ID%
echo %myVars%\ID.sys
rem pause
echo "%file%"
rem set /p test=pause
GOTO KILL

=================

call b s x
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
call g myTickets
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
	call p. autoBackup -date "%open_timestamp2%" -include_once
	call:clearBackupFiles
) ELSE (
	echo BackupRunOnce: SKIPPED
	call:autoBackup_B
	call p. autoBackup -date "%open_timestamp2%"
	call:clearBackupFiles
)

if not [%ORIGINAL_Session_ID%] == [%Session_ID%] ( CALL p. ticket_transfer -old %ORIGINAL_Session_ID% -new %Session_ID%)

rem pause
echo.
echo.
IF [%reclaim_tickets%] == [yes] CALL p. unclaimed_tickets
rem call:autoBackup_B
rem if not [%timer%] == [] if not [%lab%] == [] (
rem     echo %lab%>%myTickets%\timer-%Session_ID%.lab
rem )

call lab-timer
call p. ticketTimeline
title=Closed
call p. lock-wait -unlock x
call p. lock-wait -unlock x
@REM call p. ctrl-w
echo Exit Script Complete
exit
goto:eof
:RunOnceBackupAsk
if [%skip_backup%] == [YES] (
call c
echo skip_backup
) else (
	call:RunOnceBackupAsk2
)
goto:eof

	SET /p roAsk=Backup run once? (n)  
	IF NOT [%roAsk%] == [] SET BackupRunOnce=Y
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
if [%skip_backup%] == [YES] (
	echo skip_backup
) else (
	call p. autoBackup -date "%open_timestamp2%" -include_once
	call:clearBackupFiles
)
goto:eof
:autoBackup_B
if [%skip_backup%] == [YES] (
	echo skip_backup
) else (
	echo autoBackup running...
	call p. autoBackup -date "%open_timestamp2%"
	call:clearBackupFiles
)
goto:eof
:clearBackupFiles
	move %myTables%\fileBackupSchedule.json  %myTables%\log_backup\fileBackupSchedule.json 
	move %myTables%\myFileLocations.json  %myTables%\log_backup\myFileLocations.json 
	call ndp %myTables%\log_backup\fileBackupSchedule.json
	call ndp %myTables%\log_backup\myFileLocations.index
	echo {} > %myTables%\myFileLocations.index
	echo [] > %myTables%\fileBackupSchedule.json
goto:eof