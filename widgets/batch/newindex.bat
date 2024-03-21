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

CALL drivescan
CLS
CALL timestamp default noEcho
SET indexType=
IF [%1] == [/f] (
        SET "indexType=FULL"
    ) ELSE (
        IF [%1] == [/full] (
                SET "indexType=FULL"
            ) ELSE (
                SET "indexType=QUICK"
            )
    )

echo __________________________
echo           %indexType% 
echo      %now%
echo __________________________

:: thisIndexSetting=q // QUICK
:: thisIndexSetting=f // FULL
:: thisIndexSetting=n // NO


CALL :VAR
CALL :DRIVESCAN
GOTO:EOF
:DRIVESCAN
IF EXIST "D:\" SET thisDrive=B & CALL :SETDRIVE
IF EXIST "D:\" SET thisDrive=C & CALL :SETDRIVE
IF EXIST "D:\" SET thisDrive=D & CALL :SETDRIVE
IF EXIST "E:\" SET thisDrive=E & CALL :SETDRIVE
IF EXIST "F:\" SET thisDrive=F & CALL :SETDRIVE
IF EXIST "G:\" SET thisDrive=G & CALL :SETDRIVE
IF EXIST "H:\" SET thisDrive=H & CALL :SETDRIVE
IF EXIST "I:\" SET thisDrive=I & CALL :SETDRIVE
IF EXIST "J:\" SET thisDrive=J & CALL :SETDRIVE
IF EXIST "K:\" SET thisDrive=K & CALL :SETDRIVE
IF EXIST "L:\" SET thisDrive=L & CALL :SETDRIVE
IF EXIST "M:\" SET thisDrive=M & CALL :SETDRIVE
IF EXIST "N:\" SET thisDrive=N & CALL :SETDRIVE
IF EXIST "O:\" SET thisDrive=O & CALL :SETDRIVE
IF EXIST "P:\" SET thisDrive=P & CALL :SETDRIVE
IF EXIST "Q:\" SET thisDrive=Q & CALL :SETDRIVE
IF EXIST "R:\" SET thisDrive=R & CALL :SETDRIVE
IF EXIST "S:\" SET thisDrive=S & CALL :SETDRIVE
IF EXIST "T:\" SET thisDrive=T & CALL :SETDRIVE
IF EXIST "U:\" SET thisDrive=U & CALL :SETDRIVE
IF EXIST "V:\" SET thisDrive=V & CALL :SETDRIVE
IF EXIST "W:\" SET thisDrive=W & CALL :SETDRIVE
IF EXIST "X:\" SET thisDrive=X & CALL :SETDRIVE
IF EXIST "Y:\" SET thisDrive=Y & CALL :SETDRIVE
IF EXIST "Z:\" SET thisDrive=Z & CALL :SETDRIVE
echo __________________________
GOTO:EOF

:SETDRIVE
SET driveIDPath=%thisDrive:~0,1%:\drive.id.sys
IF EXIST "%driveIDPath%" (
        CALL :driveIDPathEXIST
    )

GOTO:EOF

:driveIDPathEXIST
    CALL timestamp default noEcho
    SET /p driveID=<"%driveIDPath%"
    SET thisDMR=%manageDrivesRoot%\%driveID%
    SET thisDMRLabel=%thisDMR%\label.txt
    SET thisDMRLog=%thisDMR%\log.txt
    SET thisDMRLetter=%thisDMR%\letter.txt
    SET thisDMRIndex=%thisDMR%\indexSettings.txt
    SET thisDMRPriority=%thisDMR%\prioritySettings.txt

    SET /p driveLabel=<"%thisDMRLabel%"
    SET /p thisIndexSetting=<"%thisDMRIndex%"
    SET /p thisPrioritySetting=<"%thisDMRPriority%"
    IF [%indexType%] == [QUICK] (
            IF [%thisIndexSetting%] == [Q] (
                    CALL :thisIndex
                ) ELSE (
                    CALL :thisNoIndex
                )
        )
    IF [%indexType%] == [FULL] (
            IF [%thisIndexSetting%] == [Q] (
                    CALL :thisIndex
                ) ELSE (
                    IF [%thisIndexSetting%] == [F] (
                            CALL :thisIndex
                        ) ELSE (
                            CALL :thisNoIndex
                        )
                )
        )
GOTO:EOF

:thisIndex
    echo %now%,%thisDrive:~0,1%,Indexed>> %thisDMRLog%
    echo          %thisDrive:~0,1%:\ %driveLabel%    indexing
    rem dir /s/b %thisDrive:~0,1%:\*.* > "{tmp}"
    call p. files -c -p %thisDrive:~0,1%:\ > "{tmp}"
    type "{tmp}" > %mdrIndex%\%thisPrioritySetting%%driveID%
    echo          %thisDrive:~0,1%:\ %driveLabel%    index complete
    echo.
    IF EXIST "{tmp}" (del "{tmp}")
GOTO:EOF

:thisNoIndex
    echo          %thisDrive:~0,1%:\ %driveLabel%    not indexed
    echo.
GOTO:EOF

:VAR
SET manageDrivesRoot=%scriptroot%\manage_drives\%computername%
SET mdrIndex=%scriptroot%\manage_drives\%computername%\index
IF NOT EXIST %mdrIndex% (mkdir %mdrIndex%)
GOTO:EOF


 
