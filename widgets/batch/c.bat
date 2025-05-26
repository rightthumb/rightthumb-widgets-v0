@echo off
chcp 65001 > nul
REM ## {R2D2919B742E} ##
REM ###########################################################################
REM What IF magic existed?
REM What IF a place existed where your every thought and dream come to life.
REM There is only one catch: it has to be written down.
REM Such a place exists, it is called programming.
REM    - Scott Taylor Reph, RightThumb.com
REM ###########################################################################
REM ## {C3P0D40fAe8B} ##

set "PATHEXT=.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PYW"
@REM :CLEAR_SCREEN





@REM                 %stmp%\pin_ask





:: e fileLocks

if [%isPWSH%] == [yes] (
    echo pwsh
    CLS
)

IF [%1] == [c] (
    SET "MainArg=simple"
) ELSE IF [%1] == [simple] (
    SET "MainArg=simple"
) else (
    SET "MainArg=None"
)

CALL %USERPROFILE%\.rt\profile\vars\config.bat
if [%wprofile%] == [] SET wprofile=%USERPROFILE%\.rt\profile
CALL %wprofile%\vars\personal.bat
SET fileLocks=%wprofile%\fileLocks
if not exist "%fileLocks%" mkdir "%fileLocks%"
CALL:GET_STRAIT_TO_LOADING

:: Tail of script

@REM CALL p. terminal-session-registration -session %Session_ID%

GOTO:EOF


:GET_STRAIT_TO_LOADING
    IF [%1] == [test] @echo on
    SET tool=%widgets%\install\installer.py
    SET tool.sh=%widgets%\widgets\bash\101-auto-setup.sh
    SET help.txt=%widgets%\install\README.TXT
    SET README=%widgets%\install\README.TXT
    SET t=%py% %tool%


    SET reclaim_tickets=no
    SET PYTHON_BASE=3
    DOSKEY /LISTSIZE=999
    SET noClear=FALSE
    REM IF [%1] == [c] SET noClear=TRUE
    IF [%1] == [c] SET noTOP=TRUE
    IF [%1] == [t] SET "noTOP="
    IF [%1] == [tt] SET noTOP=TRUE
    IF [%1] == [top] SET "noTOP="
    IF [%1] == [cc] SET "noTOP="
    IF [%1] == [test] SET noClear=TRUE

    IF [%Session_ID%] == [] (
        ECHO Loading...
    )
    REM ECHO ... saving history
    IF NOT [%Session_ID%] == [] (
        doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
        CALL:BUILD_TICKET >nul 2>&1
    )
    REM ECHO ... history saved

    IF [%1] == [r] SET api=

    IF NOT ["%api%"] == ["loaded"] (
        CALL :LOAD
        @REM SET > %wprofile%\config\._Var_Cache_.bat
    ) else (
        CALL:CLEAR_SCREEN
    )
    CALL :TIMESTAMP >nul 2>&1
GOTO:EOF



:CLEAR_SCREEN

    IF NOT [%noClear%] == [TRUE] (
        REM prompt - 
        CLS
        @REM IF [%noTOP%] == [] %py% %widgets%\widgets\python\windows-terminal-header.py
        IF [%noTOP%]==[] IF [%pterm%]==[] %py% %widgets%\widgets\python\windows-terminal-header.py
        %py% %widgets%\widgets\python\folder-registration.py
        REM ECHO %noTOP%
    )
    if [%pterm%] == [true] cls
    if [%pterm%] == [true] goto:theEndOfTheFile
GOTO:EOF



:TIMESTAMP
    CALL timestamp d noEcho >nul 2>&1
    SET open_timestamp=%now%
    CALL timestamp dt noEcho >nul 2>&1
    SET open_timestamp2=%now%
    CALL timestamp sdel noEcho >nul 2>&1
    SET ts=%now%
    CALL timestamp t noEcho >nul 2>&1
    SET nowTime=%now%
    SET today=%timestamp_start%  - %nowTime%
    call SET "Session_ID_Suffix=%%Session_ID:~-3%%"
    IF NOT ["%lab%"] == [""] (
        TITLE loc-%Session_ID_Suffix% :: %lab%
    ) else (
        TITLE loc-%Session_ID_Suffix%
    )
    CALL timestamp t2 noEcho >nul 2>&1
GOTO:EOF




:GENERATE_API_ID
    SET /p LastID=<%myVars%\ID.sys
    SET /a Session_ID=%LastID% + 1
    SET Session_ID_BK=%Session_ID%
    ECHO %Session_ID% > %myVars%\ID.sys
    CALL timestamp ats2 noEcho >nul 2>&1
    CALL p. files -folder %myVars% -rrr > nul
    SET timestamp_start=%now%
GOTO:EOF



:LOAD
            IF NOT EXIST "%wprofile%\vars\instanceID.sys" (
                p genuuid -strip be > "%wprofile%\vars\instanceID.sys"
            )
            SET /p quote=<"%wprofile%\vars\quote.txt"
            SET /p percentage=<"%wprofile%\vars\percentage.txt"

            SET Drive=

            ::::::: PHP Drive
            REM IF EXIST D:\xampp\php\php.exe (
            REM     SET php=D:\xampp\php\php.exe
            REM ) else (
            REM     SET php=D:\techApps\xampp\php\php.exe
            REM )
            ::::::: App shortcuts
            ::::::: API Variable Extras
            SET "computername2=%computername: =_%"
            SET hostDefault=hosts\{D599DDFE-28B1-4CBD-B300-78DB4BCA7DF5}

            REM SET thisHost=hosts\%computername2%
            REM SET thisHost=%wprofile%
            REM SET myHome=%widgets%\%thisHost%

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
            SET last=%wprofile%\tables\file-open.last
            REM IF NOT EXIST %widgets%\hosts (mkdir %widgets%\hosts) 
            REM IF NOT EXIST %myHome% (
            REM         md %myHome%
            REM         ECHO Building profile on USB
            REM         xcopy /s/d/y/c %widgets%\%hostDefault%\*.* %myHome%\>nul
            REM     )
            IF NOT EXIST %myVars% (mkdir %myVars%) 
            IF NOT EXIST %myBookmarks% (mkdir %myBookmarks%) 
            IF NOT EXIST %myTickets% (mkdir %myTickets%) 
            IF NOT EXIST %myIndexes% (mkdir %myIndexes%) 
            IF NOT EXIST %myIndexes%\archive (mkdir %myIndexes%\archive) 
            IF NOT EXIST %myTables% (mkdir %myTables%) 
            IF NOT EXIST %myDatabases% (mkdir %myDatabases%) 
            IF NOT EXIST %myInfo% (mkdir %myInfo%) 
            IF NOT EXIST %myProjects% (mkdir %myProjects%) 
            IF NOT EXIST %mywidgets% (mkdir %mywidgets%) 
            IF NOT EXIST %myNotes% (mkdir %myNotes%) 
            IF NOT EXIST %myWebApp% (mkdir %myWebApp%)
            IF NOT EXIST %myBatch% (mkdir %myBatch%) 
            IF NOT EXIST %myPython% (mkdir %myPython%) 
            IF NOT EXIST %myPowershell% (mkdir %myPowershell%) 
            IF NOT EXIST %myPhp% (mkdir %myPhp%) 
            IF NOT EXIST %stmp% (mkdir %stmp%) 
            IF NOT EXIST %myTxt% (mkdir %myTxt%) 
            SET batch=%widgets%\widgets\batch
            SET bash=%widgets%\widgets\bash
            SET python=%widgets%\widgets\python
            SET powershell=%widgets%\widgets\powershell
            SET php2=%widgets%\widgets\php
            SET exe=%widgets%\widgets\exe\exe
            SET exeB=%widgets%\widgets\exe
            SET data=%widgets%\widgets\data
            SET bin=%widgets%\widgets\bin
            SET binWin=%widgets%\widgets\bin\Win
            SET myImports=%python%\_rightThumb
            SET filemeta=%exeB%\File_Metadata
            IF NOT EXIST %widgets% (mkdir %widgets%) 
            IF NOT EXIST %batch% (mkdir %batch%)
            IF NOT EXIST %python% (mkdir %python%) 
            IF NOT EXIST %powershell% (mkdir %powershell%) 
            IF NOT EXIST %php2% (mkdir %php2%) 
            IF NOT EXIST %exe% (mkdir %exe%)
            CALL :run_process_exe_folders

            ::::::: Command Paths
            SET javabin=C:\Program Files\Java\jdk-18.0.2

            SET appPaths=%binWin%;%myPython%;%exe_folders%;%USERPROFILE%;%filemeta%;C:\Users\Scott\AppData\Roaming\npm
            IF EXIST "%pyf%\Scripts" ( SET appPaths=%appPaths%;%pyf%\Scripts )
            SET pathPython=%USERPROFILE%
            IF EXIST "%pyf2%\Lib" ( SET SET pathPython=%pyf2%;%pyf2%\Lib;%pyf2%\Lib\site-packages;%pyf2%;%pyf2%\Scripts )
            CALL %batch%\originalPath.bat
            SET originalPath=%Path%
            SET pathBuilder=%appPaths%;%pathPython%;%pathPython%;%originalPath%;%javabin%
            IF EXIST "D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64" (
                SET "pathBuilder=%pathBuilder%;D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29910\bin\Hostx64\x64"
            )
            SET path=%pathBuilder%
            
            SET pathBuilder=
            SET pathPython=



            call pathAddPre C:\Users\Scott\.cargo\bin
            call pathAdd C:\Program Files\MongoDB\Server\8.0\bin
            call pathAddPre %batch%
            call pathAddPre %myBatch%

            call pathAdd %python%
            call pathRemove C:\QMK_MSYS\mingw64\bin
            call pathRemove C:\Python313
            call pathRemove D:\techApps\Python\Python36-32


            SET phpFiles=%php2%


            SET /p quote=<%wprofile%\vars\quote.txt
            SET /p percentage=<%wprofile%\vars\percentage.txt

            SET tmpf.htm=%stmp%\13cf9da8b39d.htm
            SET tmpf=%stmp%\{8E3F33E4-86AB-AB1E-6219-801DE111D9AF}
            SET tmpf0=%stmp%\{B820137A-79B8-45E3-BCBD-A6CAC50892D0}
            SET tmpf1=%stmp%\{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}
            SET tmpf2=%stmp%\{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}
            SET tmpf3=%stmp%\{F139D191-FA1A-44D5-855C-7E5141B30E0D}
            SET tmpf4=%stmp%\{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}
            SET tmpf5=%stmp%\{201D82D6-2DC0-4552-A598-54F5481399A1}
            SET tmpf6=%stmp%\{26B3B9C6-0A59-432A-9386-D432B53001CB}
            SET tmpf7=%stmp%\{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}
            SET tmpf8=%stmp%\{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}
            SET tmpf9=%stmp%\{DF1D4EBC-838E-419C-9C58-943C1767391A}
            SET tmpfl=%stmp%\{79E8C4B0-2AAA-2083-B812-AD1B9283B30A}
            SET t0=%stmp%\{B820137A-79B8-45E3-BCBD-A6CAC50892D0}
            SET t1=%stmp%\{C0FA8E56-8426-46BB-9CE8-4A14C51EA261}
            SET t2=%stmp%\{5FBF34C0-9A95-4C7E-BA53-44F84ECECCB5}
            SET t3=%stmp%\{F139D191-FA1A-44D5-855C-7E5141B30E0D}
            SET t4=%stmp%\{AA8EC8E1-EA9D-460D-A593-7B0FAEB9243E}
            SET t5=%stmp%\{201D82D6-2DC0-4552-A598-54F5481399A1}
            SET t6=%stmp%\{26B3B9C6-0A59-432A-9386-D432B53001CB}
            SET t7=%stmp%\{C03C0132-CFFC-4E3A-8F0F-614BB95164C7}
            SET t8=%stmp%\{4CCA3EBD-4535-42B7-9C75-05EFAACB00E0}
            SET t9=%stmp%\{DF1D4EBC-838E-419C-9C58-943C1767391A}
            SET tl=%stmp%\{79E8C4B0-2AAA-2083-B812-AD1B9283B30A}
            SET ideas=%stmp%\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}
            SET pips=%stmp%\pips.txt
            SET disc=%stmp%\disc.txt
            SET todoo=%stmp%\todo.txt
            SET todo=%myHome%\projects\todo.txt
            SET open=%myHome%\projects\open_projects.txt
            SET lastP=%myHome%\projects\project-log.txt
            SET scrap=%myHome%\projects\project-log.txt
            SET documentation=%widgets%\widgets\documentation
            SET instructions=%documentation%\instructions.txt
            SET imports=%documentation%\python_imports.py
            SET algorithms=%documentation%\algorithms.txt
            SET basic_scripts=%documentation%\algorithms.txt
            SET behavior=%myHome%\projects\behavior.txt
            SET DB=%widgets%\hosts\MSI\tables\clients_databases.txt
            SET appAliasLog=%myTables%\app_alias_record.csv
            SET behave=%behavior%
            SET hacks=%hack%
            SET sites=%widgets%\widgets\javascript\my_website_projects.js
            SET minecraft=%widgets%\widgets\javascript\minecraft.txt
            SET idea=%stmp%\{6EF01C5C-E6A8-585D-F946-1C9BC46C1D7A}
            SET contextTemp=%stmp%\{21E8D046-A855-EE9B-B772-9EECBD922D87}
            SET battery="%widgets%\widgets\vbs\battery.vbs"
            SET fileBackup=%myTables%\fileBackup_log.json
            SET bkLog=%myTables%\fileBackup_log.json
            SET HOSTS=D:\Windows\System32\drivers\etc\hosts
            SET databank=%widgets%\widgets\databank
            SET dbTables=%databank%\tables
            SET mData=%dbTables%\movie.cache
            SET tiktok=%widgets%\widgets\databank\tables\tikTok.txt
            SET archive7z=%widgets%\widgets\archive_7z_files
            SET distro=%myHome%\config\.distro
            IF NOT EXIST "%myHome%\config" mkdir "%myHome%\config"
            IF NOT EXIST %distro% CALL p. this_distro > %distro%
            SET /p distro=<%distro%
            IF NOT EXIST %archive7z% (mkdir %archive7z%) 
                net session >nul 2>&1
                IF %errorLevel% == 0 (
                    SET isAdmin=True
                ) else (
                    SET isAdmin=False
                )
            IF NOT EXIST %stmp% mkdir %stmp%
            IF NOT EXIST "%stmp%\unclaimed_tickets" mkdir "%stmp%\unclaimed_tickets"
            IF NOT EXIST "%stmp%\unclaimed_tickets_history" mkdir "%stmp%\unclaimed_tickets_history"
            SET dircache=%myTables%\dirCache.json
            SET dircachep=%myTables%\dirCacheP.json
            CALL theUSB
            SET qi=%myIndexes%\0A{465C1A34-D22F-184E-F713-F8E5149E212D}
            ECHO %code_editor%>"%myVars%\notepad.txt"

            IF NOT EXIST "%userprofile%\cc.bat" (
                COPY "%bat%\rr.bat" "%userprofile%\cc.bat"
                IF ERRORLEVEL 1 (
                    ECHO "There was an error copying the file."
                    REM exit /b 1
                )
            )

            ::::::: API Paths (Asside from PHP)
            SET scriptroot=%batch%
            IF ["%Session_ID%"] == [""] CALL :GENERATE_API_ID
            SET api=loaded
            CALL:CLEAR_SCREEN
            REM ECHO.
            REM cls
            prompt └─ 
            REM prompt - 
            if exist "%stmp%\pin_ask" (
                CALL:SET_PIN
            )
            @REM CALL fixPath
GOTO:EOF

:SET_PIN
IF [%MainArg%] == [None] (
    call :Possible_isPWSH
    call :Possible_Pin
    call :Possible_Call_Parent
)
GOTO:EOF

:Possible_Pin
    if not [%isPWSH%] == [yes] (
        call pin
    )
GOTO:EOF

:Possible_isPWSH
    if [%isPWSH%] == [] (
        call isPWSH
        goto :eof
    )
GOTO:EOF

:Possible_Call_Parent
    set "SCRIPT_DIR=%~dp0"
    set "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
    if not "%SCRIPT_DIR:~-1%"=="%batch%" (
        call c simple
        @REM echo Called C
    ) 
GOTO:EOF





:BUILD_TICKET_HISTORY
    doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
    REM CALL:BUILD_TICKET >nul 2>&1
GOTO:EOF



:BUILD_TICKET
    IF ["%project%"] == [""] SET name=closed-%Session_ID%.txt
    IF NOT ["%project%"] == [""] SET name=open-%Session_ID%.txt
    SET file=%stmp%\unclaimed_tickets\%name%
    SET fileTempData=%myTickets%\tempFile.txt
    SET timestamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2% @ %time:~0,2%:%time:~3,2%
    ECHO ^<div class='box' ^> > "%file%"  2>&1
    ECHO ^<div class='item' ^> >> "%file%"  2>&1
    ECHO Session: %Session_ID% (%timestamp_start% - %timestamp%) isAdmin:%isAdmin% %project%>> "%file%"  2>&1
    ECHO ^</div^> >> "%file%"  2>&1
    ECHO ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='guid' ^> %instanceID%^</div^>>> ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='sid' ^> %machineID%^</div^>>> ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='details' ^> >> "%file%"
    IF NOT ["%lab%"] == [""] ECHO ^<div class='laboratory' ^> %lab% >> ^</div^> >> "%file%"  2>&1
    ECHO ^<br^> >> "%file%"  2>&1
    ECHO ^<pre^> >> "%file%"  2>&1
    ECHO. >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"
    CALL p. singleLine -f "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt" > "%fileTempData%"  2>&1
    TYPE "%fileTempData%" | p. passFilter >> "%file%"  2>&1
    TYPE "%file%" > "%fileTempData%"  2>&1
    DEL "%fileTempData%"
    ECHO ^</pre^> >> "%file%"  2>&1
    ECHO ^<br^> ^</div^> ^</div^> ^<br^> >> "%file%"  2>&1
goto:eof


:run_process_exe_folders
    SET exe_folders=%exeB%
    for /f %%f in ('dir /s/b %exeB%') do IF EXIST %%f\*.exe call:process_exe_folders %%f
goto:eof


:process_exe_folders
    SET exe_folders=%exe_folders%;%1
goto:eof
 
:theEndOfTheFile