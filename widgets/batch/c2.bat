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


call "%USERPROFILE%\.rt\profile\vars\config.bat"
call "%USERPROFILE%\.rt\profile\vars\personal.bat"
GOTO:GET_STRAIT_TO_LOADING
GOTO:EOF


:GET_STRAIT_TO_LOADING
	IF [%1] == [test] @echo on
	set tool=%widgets%\install\installer.py
	set tool.sh=%widgets%\widgets\bash\101-auto-setup.sh
	set help.txt=%widgets%\install\README.TXT
	set README=%widgets%\install\README.TXT
	set t=%py% %tool%


	SET reclaim_tickets=no
	SET PYTHON_BASE=3
	DOSKEY /LISTSIZE=999
	SET noClear=FALSE
	if [%1] == [c] SET noClear=TRUE
	if [%1] == [test] SET noClear=TRUE

	CALL:CLEAR_SCREEN
	IF NOT [%Session_ID%] == [] (
		echo Loading...
	)
	rem echo ... saving history
	IF NOT [%Session_ID%] == [] (
		doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
		CALL:BUILD_TICKET >nul 2>&1
	)
	rem echo ... history saved

	IF [%1] == [r] SET api=

	IF NOT ["%api%"] == ["loaded"] (
		CALL :LOAD
	) else (
		CALL:CLEAR_SCREEN
	)
	CALL :TIMESTAMP >nul 2>&1
	CALL:CLEAR_SCREEN
GOTO:EOF



:CLEAR_SCREEN
	IF NOT [%noClear%] == [TRUE] (
		CLS
	)
GOTO:EOF



:TIMESTAMP
	CALL timestamp d noEcho
	SET open_timestamp=%now%
	CALL timestamp dt noEcho
	SET open_timestamp2=%now%
	CALL timestamp sdel noEcho
	SET ts=%now%
	CALL timestamp t noEcho
	SET nowTime=%now%
	SET today=%timestamp_start%  - %nowTime%
	if not ["%lab%"] == [""] (
		rem title %lab% - %Session_ID%
		title %lab% - local
	) else (
		title local
		rem title %today%
	)
	CALL timestamp t2 noEcho
GOTO:EOF




:GENERATE_API_ID
	SET /p LastID=<"%myVars%\ID.sys"
	SET /a Session_ID=%LastID% + 1
	SET Session_ID_BK=%Session_ID%
	echo %Session_ID% > "%myVars%\ID.sys"
	CALL timestamp ats2 noEcho
	SET timestamp_start=%now%
GOTO:EOF



:LOAD
			if not exist "%USERPROFILE%\.rt\profile\vars\instanceID.sys" (
				p genuuid -strip be > "%USERPROFILE%\.rt\profile\vars\instanceID.sys"
			)
			SET /p quote=<"%USERPROFILE%\.rt\profile\vars\quote.txt"
			SET /p percentage=<"%USERPROFILE%\.rt\profile\vars\percentage.txt"
			SET Drive=

			::::::: PHP Drive
			rem if EXIST D:\xampp\php\php.exe (
			rem     SET php=D:\xampp\php\php.exe
			rem ) else (
			rem     SET php=D:\techApps\xampp\php\php.exe
			rem )
			::::::: App shortcuts
			::::::: API Variable Extras
			set "computername2=%computername: =_%"
			SET hostDefault=hosts\{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}

			rem SET thisHost=hosts\%computername2%
			rem SET thisHost=%USERPROFILE%\.rt\profile
			rem SET myHome=%widgets%\%thisHost%

			SET thisHost=%wprofile%
			SET myHome=%thisHost%

			SET myVars=%myHome%\vars
			SET myBookmarks=%myHome%\bookmarks
			SET myTickets=%myHome%\tickets
			SET myIndexes=%myHome%\indexes
			SET i=%myHome%\indexes
			SET day=%myHome%\daily
			SET myTables=%myHome%\tables
			SET myDatabases=%myHome%\databases
			SET myInfo=%myHome%\info
			SET myProjects=%myHome%\projects
			SET mywidgets=%myHome%\widgets
			SET myNotes=%myHome%\notes
			SET myWebApp=%myHome%\WebApp
			SET webapp=%myWebApp%
			SET myBatch=%myHome%\widgets\batch
			SET myPython=%myHome%\widgets\python
			SET myPowershell=%myHome%\widgets\powershell
			SET myPhp=%myHome%\widgets\php
			SET stmp=%myHome%\temp
			SET myTxt=%myHome%\txt
			SET mdt=%myVars%\mdt.txt
			SET m3Data=%i%\Movie_Drive_t3.dirCache
			SET mcData=%i%\Movies_Cloud.dirCache
			SET dID={65E57A88-6471-E426-D878-AD55F117A804}
			SET mID={D86E7BD3-2C52-0C57-9DA2-447309490DB4}
			SET m3ID={D644A899-89BB-9748-8339-3FC5F75B8A16}
			SET pubID={C7DA4040-A42C-0372-B54A-8E40F835D3E1}
			SET privID={5B55D9AE-6C90-B44B-2071-5376CBB2AAAE}
			IF NOT EXIST "%widgets%\hosts" (md %widgets%\hosts) 
			IF NOT EXIST "%myHome%" (
					md "%myHome%"
					echo Building profile on USB
					xcopy /s/d/y/c "%widgets%\%hostDefault%\*.*" "%myHome%"\>nul
				)
			IF NOT EXIST "%myVars%" (md "%myVars%") 
			IF NOT EXIST "%myBookmarks%" (md "%myBookmarks%") 
			IF NOT EXIST "%myTickets%" (md "%myTickets%") 
			IF NOT EXIST "%myIndexes%" (md "%myIndexes%") 
			IF NOT EXIST "%myIndexes%\archive" (md "%myIndexes%\archive") 
			IF NOT EXIST "%myTables%" (md "%myTables%") 
			IF NOT EXIST "%myDatabases%" (md "%myDatabases%") 
			IF NOT EXIST "%myInfo%" (md "%myInfo%") 
			IF NOT EXIST "%myProjects%" (md "%myProjects%") 
			IF NOT EXIST "%mywidgets%" (md "%mywidgets%") 
			IF NOT EXIST "%myNotes%" (md "%myNotes%") 
			IF NOT EXIST "%myWebApp%" (md "%myWebApp%")
			IF NOT EXIST "%myBatch%" (md "%myBatch%") 
			IF NOT EXIST "%myPython%" (md "%myPython%") 
			IF NOT EXIST "%myPowershell%" (md "%myPowershell%") 
			IF NOT EXIST "%myPhp%" (md "%myPhp%") 
			IF NOT EXIST "%stmp%" (md "%stmp%")
			IF NOT EXIST %myTxt% (md %myTxt%) 
			SET batch=%widgets%\widgets\batch
			SET bash=%widgets%\widgets\bash
			SET python=%widgets%\widgets\python
			SET powershell=%widgets%\widgets\powershell
			SET php2=%widgets%\widgets\php
			SET exe=%widgets%\widgets\exe\exe
			SET exeB=%widgets%\widgets\exe
			SET data=%widgets%\widgets\data
			SET myImports=%python%\_rightThumb
			IF NOT EXIST %widgets% (md %widgets%) 
			IF NOT EXIST %batch% (md %batch%)
			IF NOT EXIST %python% (md %python%) 
			IF NOT EXIST %powershell% (md %powershell%) 
			IF NOT EXIST %php2% (md %php2%) 
			IF NOT EXIST %exe% (md %exe%)
			CALL :run_process_exe_folders

			::::::: Command Paths
			SET javabin=C:\Program Files\Java\jdk-18.0.2

			SET appPaths="%batch%";"%python%";"%myBatch%";"%myPython%";"%exe_folders%";"%USERPROFILE%"
			if exist "%pyf%\Scripts" ( SET appPaths=%appPaths%;%pyf%\Scripts )
			SET pathPython=%USERPROFILE%
			if exist "%pyf2%\Lib" ( SET SET pathPython=%pyf2%;%pyf2%\Lib;%pyf2%\Lib\site-packages;%pyf2%;%pyf2%\Scripts )
			CALL %batch%\originalPath.bat
			SET originalPath=%Path%
			SET pathBuilder=%appPaths%;%pathPython%;%originalPath%;%pathPython%;%javabin%
			IF EXIST "D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64" (
				SET "pathBuilder=%pathBuilder%;D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64"
			)
			SET path=%pathBuilder%
			SET pathBuilder=
			SET pathPython=

			SET phpFiles=%php2%


			SET /p quote=<%USERPROFILE%\.rt\profile\vars\quote.txt
			SET /p percentage=<%USERPROFILE%\.rt\profile\vars\percentage.txt

			SET tmpf.htm="%stmp%\13cf9da8b39d.htm"
			SET tmpf="%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}"
			SET tmpf0="%stmp%\{B820137A-79B8-45E3-BCBD-A6CAC50892D0}"
			SET tmpf1="%stmp%\{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}"
			SET tmpf2="%stmp%\{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}"
			SET tmpf3="%stmp%\{F139D191-FA1A-44D5-855C-7E5141B30E0D}"
			SET tmpf4="%stmp%\{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}"
			SET tmpf5="%stmp%\{201D82D6-2DC0-4552-A598-54F5481399A1}"
			SET tmpf6="%stmp%\{26B3B9C6-0A59-432A-9386-D432B53001CB}"
			SET tmpf7="%stmp%\{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}"
			SET tmpf8="%stmp%\{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}"
			SET tmpf9="%stmp%\{DF1D4EBC-838E-419C-9C58-943C1767391A}"
			SET tmpfl="%stmp%\{79E8C4B0-2AAA-2083-B812-AD1B9283B30A}"
			SET ideas="%stmp%\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}"
			SET pips="%stmp%\pips.txt"
			SET disc="%stmp%\disc.txt"
			SET todoo="%stmp%\todo.txt"
			SET todo="%myHome%\projects\todo.txt"
			set open="%myHome%\projects\open_projects.txt"
			SET lastP="%myHome%\projects\project-log.txt"
			SET scrap="%myHome%\projects\project-log.txt"
			SET documentation="%widgets%\widgets\document"ation
			SET instructions="%documentation%\instructions".txt
			SET imports="%documentation%\python_imports.py"
			SET basic_scripts="%documentation%\algorithms.txt"
			SET algorithms="%documentation%\algorithms.txt"
			SET behavior="%myHome%\projects\behavior.txt"
			SET DB="%widgets%\hosts\MSI\tables\clients_databases.txt"
			set appAliasLog="%myTables%\app_alias_record.csv"
			SET behave=%behavior%
			SET hacks=%hack%
			SET sites="%widgets%\widgets\javascript\my_website_projects.js"
			SET minecraft="%widgets%\widgets\javascript\minecraft.txt"
			SET idea="%stmp%\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}"
			SET contextTemp="%stmp%\{21E8D046-A855-EE9B-B772-9EECBD922D87}"
			SET battery="%widgets%\widgets\vbs\battery.vbs"
			SET fileBackup="%myTables%\fileBackup_log.json"
			SET bkLog="%myTables%\fileBackup_log.json"
			SET HOSTS=D:\Windows\System32\drivers\etc\hosts
			SET databank=%widgets%\widgets\databank
			SET dbTables=%databank%\tables
			SET mData="%dbTables%\movie.cache"
			SET tiktok="%widgets%\widgets\databank\tables\tikTok.txt"
			SET archive7z=%widgets%\widgets\archive_7z_files
			SET distro="%myHome%\config\.distro"
			if not exist "%myHome%\config" mkdir "%myHome%\config"
			if not exist %distro% CALL p. this_distro > %distro%
			SET /p distro=<%distro%
			IF NOT EXIST %archive7z% (md %archive7z%) 
				net session >nul 2>&1
				if %errorLevel% == 0 (
					SET isAdmin=True
				) else (
					SET isAdmin=False
				)
			if not exist "%stmp%" mkdir "%stmp%"
			if not exist "%stmp%\unclaimed_tickets" mkdir "%stmp%\unclaimed_tickets"
			if not exist "%stmp%\unclaimed_tickets_history" mkdir "%stmp%\unclaimed_tickets_history"
			SET dircache="%myTables%\dirCache.json"
			SET dircachep="%myTables%\dirCacheP.json"
			CALL theUSB
			set qi="%myIndexes%\0A{465C1A34-D22F-184E-F713-F8E5149E212D}"
			echo %code_editor%>"%myVars%\notepad.txt"

			::::::: API Paths (Asside from PHP)
			SET scriptroot=%batch%
			IF ["%Session_ID%"] == [""] CALL :GENERATE_API_ID
			SET api=loaded
			CALL:CLEAR_SCREEN
			echo.
			prompt - 
GOTO:EOF



:BUILD_TICKET_HISTORY
	doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
	rem CALL:BUILD_TICKET >nul 2>&1
GOTO:EOF



:BUILD_TICKET
	if ["%project%"] == [""] set name=closed-%Session_ID%.txt
	if NOT ["%project%"] == [""] set name=open-%Session_ID%.txt
	set file=%stmp%\unclaimed_tickets\%name%
	set fileTempData="%myTickets%\tempFile.txt"
	set timestamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2% @ %time:~0,2%:%time:~3,2%
	echo ^<div class='box' ^> > "%file%"  2>&1
	echo ^<div class='item' ^> >> "%file%"  2>&1
	echo Session: %Session_ID% (%timestamp_start% - %timestamp%) isAdmin:%isAdmin% %project%>> "%file%"  2>&1
	echo ^</div^> >> "%file%"  2>&1
	echo ^<br^> >> "%file%"  2>&1
	echo ^<div class='guid' ^> %instanceID%^</div^>>> ^<br^> >> "%file%"  2>&1
	echo ^<div class='sid' ^> %machineID%^</div^>>> ^<br^> >> "%file%"  2>&1
	echo ^<div class='details' ^> >> "%file%"
	if not ["%lab%"] == [""] echo ^<div class='laboratory' ^> %lab% >> ^</div^> >> "%file%"  2>&1
	echo ^<br^> >> "%file%"  2>&1
	echo ^<pre^> >> "%file%"  2>&1
	echo. >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"
	CALL p. singleLine -f "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt" > "%fileTempData%"  2>&1
	type "%fileTempData%" | p. passFilter >> "%file%"  2>&1
	type "%file%" > "%fileTempData%"  2>&1
	del "%fileTempData%"
	echo ^</pre^> >> "%file%"  2>&1
	echo ^<br^> ^</div^> ^</div^> ^<br^> >> "%file%"  2>&1
goto:eof


:run_process_exe_folders
	set exe_folders=%exeB%
	for /f %%f in ('dir /s/b %exeB%') do if exist %%f\*.exe call:process_exe_folders %%f
goto:eof


:process_exe_folders
	set exe_folders=%exe_folders%;%1
goto:eof