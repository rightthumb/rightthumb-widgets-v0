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

@REM set PY="D:\techApps\Python\Python36-32\python.exe"
rem set py=python3

if [%1] == [base-e] type %python%\_rightThumb\_base3\_base3_init_example.py > %python%\base-e.py
if [%1] == [] goto:EOF

:START_HERE

if [%1] == [b?] (
    SHIFT
    CALL :START_HERE hasAlias %*
    goto:EOF
)


if not exist "%python%\%1.py" (
    set originalOne=%1
    set searched=0
    GOTO :APP_SEARCH
)

:START_WORKING
rem echo %*
set changeDIR=false
set switchUsed=false
set switchAutoLegacy=false
set switch=
set clean=false
rem set py2=D:\Python27\python.exe
set two=%2

call :DeQuote two
if [%two:~0,1%] == [/] (
        set switchUsed=true
        set switch=%two:~1,100%
    ) else (
        set switch=%2
    )
if [%switch%] == [a] (
        call :TOFOLDER
        if exist %1.py (move %1.py archive)
        if exist %1.py.bak (move %1.py.bak archive)
        goto:EOF
    )

if [%switch%] == [v] set clean=true
if [%switch%] == [/] set clean=true

if [%switch%] == [c] call :fix %1
if [%switch%] == [convert] call :fix %1
if [%switch%] == [r] call :recoverLegacy %1
if [%switch%] == [l] call :labelLegacy %1
call :checkLegacy %1
call :TOBACK
if [%switch%] == [2] (
        if [%switchAutoLegacy%] == [true] (
                call :ver2 %*
            ) else (
                set one = %1&shift&shift
                call :ver2 %one% %*
            )
    ) else (
        if [%switchUsed%] == [false] (
                call :ver3 %*
            ) else (
                set one = %1&shift&shift
                call :ver3 %one% %*
            )
    )


goto:EOF
:APP_SEARCH

    echo.
    echo did you mean


    call p. py-finder -percentage + %1

    rem set /a searched=%searched%+1
    rem if [%searched%] == [1] set plusClose=90
    rem if [%searched%] == [2] set plusClose=80
    rem if [%searched%] == [3] set plusClose=70
    rem if [%searched%] == [4] set plusClose=50

    rem echo pattern: %plusClose%^%%
    rem echo.>"%stmp%\app(file.py)_output.txt"
    rem echo Error: Does not exist>>"%stmp%\app(file.py)_output.txt"
    rem echo.>>"%stmp%\app(file.py)_output.txt"
    rem echo Try:>>"%stmp%\app(file.py)_output.txt"
    rem rem echo %searched% %plusClose%
    rem call p. file -folder %python% -noext -label ;tApps -prefix ;t +close %plusClose% + %1>>"%stmp%\app(file.py)_output.txt"
    rem GOTO:EOF
    rem echo call p. file -folder %python% -noext -label ;tApps -prefix ;t +close %plusClose% + %1>>"%stmp%\app(file.py)_output.txt"
    rem type "%stmp%\app(file.py)_output.txt"
    rem GOTO :POST_ERROR_COUNT_CHECK
goto:EOF

:POST_ERROR_COUNT_CHECK
SET /p apps_found=<"%stmp%\app(file.py)_Count.txt"> nul
set /a apps_found=%apps_found%+1
set /a apps_found=%apps_found%-1
rem echo %apps_found%
if [%apps_found%] == [1] goto :POST_ERROR_HAS_SINGLE
rem GOTO:EOF 
if [%apps_found%] == [0] if %searched% LSS 4 goto :APP_SEARCH
if [%apps_found%] == [0] if [%searched%] == [3] type "%stmp%\app(file.py)_output.txt"
if %apps_found% GTR 0 GOTO :POST_ERROR
goto:EOF
:POST_ERROR


if exist "%stmp%\app(file.py).txt" (
    goto :POST_ERROR_HAS_SINGLE
) else (
    type "%stmp%\app(file.py)_output.txt"
)


goto:EOF
:POST_ERROR_HAS_SINGLE
echo HERE, "%stmp%\app(file.py).txt"
SET /p the_new_app=<"%stmp%\app(file.py).txt"> nul
set argLoop=0
set argsNew=%the_new_app%

goto :BULD_ARGUMENTS
:POST_BULD_ARGUMENTS
rem echo %argsNew%
set /p shouldRun= Did you mean %the_new_app% ?:  
if [%shouldRun%] == [N] GOTO:EOF
if [%shouldRun%] == [NO] GOTO:EOF
if [%shouldRun%] == [n] GOTO:EOF
if [%shouldRun%] == [no] GOTO:EOF
if [%shouldRun%] == [] call :DOCUMENT_AND_START %argsNew%
if [%shouldRun%] == [Y] call :DOCUMENT_AND_START %argsNew%
if [%shouldRun%] == [YES] call :DOCUMENT_AND_START %argsNew%
if [%shouldRun%] == [y] call :DOCUMENT_AND_START %argsNew%
if [%shouldRun%] == [yes] call :DOCUMENT_AND_START %argsNew%

GOTO:EOF
call :START_WORKING %argsNew%


goto:EOF
:DOCUMENT_AND_START
if not exist "%appAliasLog%" (
    echo "timestamp","session","alias","original","folder">>%appAliasLog%
)


call timestamp sdel noEcho
echo "%now%","%Session_ID%","%originalOne%","%1","%python%">>%appAliasLog%
call :START_WORKING %*
goto:EOF
:BULD_ARGUMENTS
SHIFT
set argsNew=%argsNew% %1
if not [%2] == [] goto :BULD_ARGUMENTS
goto:POST_BULD_ARGUMENTS
:TOFOLDER
set changeDIR=true
echo ran
call m back --c
call b py
goto:EOF
:TOBACK
if [%changeDIR%] == [true] call b back
goto:EOF

:ver2
rem cls
if not [%clean%] == [true] (
    echo.
    echo _____________
    echo.
)
%py2% "%python%\%1.py" %*
if not [%clean%] == [true] (
    echo.
    echo _____________
    echo Python 2.7.13
    echo.
)
goto:EOF

:ver3
rem echo %switch%
rem cls
if [%clean%] == [true] (
    echo.
    echo _____________
    echo.
)
call :find_app %*
rem %py% "%python%\%1.py" %*

if [%clean%] == [true] (
    echo.
    echo ____________
    echo Python 3.6.2
    echo.
)
goto:EOF

:fix
call :TOFOLDER
call pyVer %1
set switchUsed=true
goto:EOF

:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
goto:EOF

:labelLegacy
call :TOFOLDER
%py% "%python%\labelFile.py" "%python%\%1.py" "#835B0032-Legacy"
set switchAutoLegacy=true
set switchUsed=true
set switch=2
goto:EOF

:checkLegacy
find /c "#835B0032" "%python%\%1.py" > nul
if not %errorlevel% equ 1 (
        set switchAutoLegacy=true
        set switch=2
    )
goto:EOF

:recoverLegacy
call :TOFOLDER
set fileName=%python%\%1.py
if exist "%fileName%" (
        if exist "%fileName%.bak" (
                del /q "%fileName%"
                type "%fileName%.bak" > "%fileName%"
                del /q "%fileName%.bak"

                
            )
    )
set switchAutoLegacy=true
set switchUsed=true
set switch=2
call :labelLegacy %1
goto:EOF
rem #A1695618-Converted



    :find_app

if exist %python%\%1.py (
    call:run_app %*
) else (
    call:find_app_search
)

    goto:EOF


    :find_app_search

for /f %%f in ('dir /b %python%') do call :find_app_process %%f %*

    goto:EOF

    :find_app_process

if exist %1\%2.py (
    shift
    call :run_app %*
)

    goto:EOF

:run_app
IF NOT ["%lab%"] == [""] (
    TITLE loc-%Session_ID_Suffix% :: %lab% : %1
) else (
    TITLE loc-%Session_ID_Suffix% %1
)
%py% "%python%\%1.py" %*
if exist %myVars%\terminal\%Session_ID%.bat (
    call %myVars%\terminal\%Session_ID%.bat
)
IF NOT ["%lab%"] == [""] (
    TITLE loc-%Session_ID_Suffix%  :: %lab%
) else (
    TITLE loc-%Session_ID_Suffix%
)
goto:EOF




 
