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

rem :set /p n=<name.txt
rem :set /p pc=<pc.txt
rem cls

rem IF NOT "%1" == "" GOTO FIND
rem dir /b
rem set do=dir /b
rem GOTO END

rem :FIND
rem IF "%2" == "s" GOTO SUB
rem set do=dir /b | find /i "%1"
rem %do%
rem GOTO END

rem :SUB
rem dir /s/b *%1*
rem set do=dir /s/b *%1*
rem GOTO END

rem :END
rem if errorlevel==1 set error=1
rem if errorlevel==2 set error=2
rem if errorlevel==3 set error=3
rem if errorlevel==4 set error=4
rem if errorlevel==5 set error=5                          
rem if errorlevel==6 set error=6
rem if errorlevel==7 set error=7
rem if errorlevel==8 set error=8
rem if errorlevel==9 set error=9


%py% %widgets%\widgets\python\folder-registration.py
rem echo --------
rem :echo ^<%pc%^>
rem :echo Just Ran:
rem :echo %do%
rem cd
rem :echo ^</%pc%^>
rem echo Files:
rem echo.
if [%1] == [-subject] (
    echo %2 >> .subjects
    echo Saved: %2 to .subjects
    GOTO:EOF
)
if [%1] == [-s] (
    echo %2 >> .subjects
    echo Saved: %2 to .subjects
    GOTO:EOF
)
if [%1] == [-copy] (
    call :ACTION3 %*
    GOTO:EOF
)
if [%1] == [-cp] (
    call :ACTION3 %*
    GOTO:EOF
)
if [%1] == [-links] (
    call :ACTION3 %*
    GOTO:EOF
)
if [%1] == [-link] (
    call :ACTION3 %*
    GOTO:EOF
)

if [%1] == [-l] (
    call :ACTION3 %*
    GOTO:EOF
)

if [%1] == [-f] (
    call :ACTION3 %*
    GOTO:EOF
)
if [%1] == [-folder] (
    call :ACTION3 %*
    GOTO:EOF
)

if [%1] == [] (
        call :ACTION1
    ) else (
        call :ACTION2 %*
    )
GOTO:EOF
:ACTION1
cls
echo.
call p. file_folder
echo.
GOTO:EOF

:ACTION2
cls
echo.
call p. file_folder + %*
echo.
GOTO:EOF

:ACTION3
cls
echo.
call p. file_folder %*
echo.
GOTO:EOF



 
 
