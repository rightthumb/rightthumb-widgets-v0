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

SET checkID=%1
if [%2] == [] (
        SET "folder="
    ) else (
        SET folder=%2
    )
rem echo %*
SET found=False
SET foundFolder=False
:DRIVESCAN
IF EXIST "D:\" SET thisDrive=B& CALL :SCANTHIS
IF EXIST "D:\" SET thisDrive=C& CALL :SCANTHIS
IF EXIST "D:\" SET thisDrive=D& CALL :SCANTHIS
IF EXIST "E:\" SET thisDrive=E& CALL :SCANTHIS
IF EXIST "F:\" SET thisDrive=F& CALL :SCANTHIS
IF EXIST "G:\" SET thisDrive=G& CALL :SCANTHIS
IF EXIST "H:\" SET thisDrive=H& CALL :SCANTHIS
IF EXIST "I:\" SET thisDrive=I& CALL :SCANTHIS
IF EXIST "J:\" SET thisDrive=J& CALL :SCANTHIS
IF EXIST "K:\" SET thisDrive=K& CALL :SCANTHIS 
IF EXIST "L:\" SET thisDrive=L& CALL :SCANTHIS 
IF EXIST "M:\" SET thisDrive=M& CALL :SCANTHIS 
IF EXIST "N:\" SET thisDrive=N& CALL :SCANTHIS 
IF EXIST "O:\" SET thisDrive=O& CALL :SCANTHIS 
IF EXIST "P:\" SET thisDrive=P& CALL :SCANTHIS
IF EXIST "Q:\" SET thisDrive=Q& CALL :SCANTHIS
IF EXIST "R:\" SET thisDrive=R& CALL :SCANTHIS
IF EXIST "S:\" SET thisDrive=S& CALL :SCANTHIS
IF EXIST "T:\" SET thisDrive=T& CALL :SCANTHIS
IF EXIST "U:\" SET thisDrive=U& CALL :SCANTHIS
IF EXIST "V:\" SET thisDrive=V& CALL :SCANTHIS
IF EXIST "W:\" SET thisDrive=W& CALL :SCANTHIS
IF EXIST "X:\" SET thisDrive=X& CALL :SCANTHIS
IF EXIST "Y:\" SET thisDrive=Y& CALL :SCANTHIS
IF EXIST "Z:\" SET thisDrive=Z& CALL :SCANTHIS
goto:eof

:SCANTHIS
    if [%found%] == [True] goto:eof
    SET thisDriveID=%thisDrive%:\drive.id.sys
    IF EXIST %thisDriveID% (
            CALL :CHECKINFILE
        )
    goto:eof

:CHECKINFILE
    find /c "%checkID%" "%thisDriveID%" > nul
    if not %errorlevel% equ 1 (
            SET found=True

            %thisDrive%:
            cd\
            
            if [%folder%] == [] (
                    SET foundFolder=True
                    echo Found: %thisDrive%:
                ) else (
                    CALL :THEFOLDER
                )
        )
    goto:eof

:THEFOLDER
    IF EXIST %thisDrive%:\%folder% (
            SET foundFolder=True
            cd %thisDrive%:\%folder%
            echo Found: %thisDrive%:\%folder%
        ) else (
            echo Found: %thisDrive%:
        )
    goto:eof

goto:eof


 
