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
CALL timestamp default noEcho
echo __________________________
echo      %now%
echo __________________________

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
        SET /p driveID=<"%driveIDPath%"
    ) else (
        CALL :driveIDPathNOTEXIST
    )
CALL timestamp default noEcho
SET thisDMR=%manageDrivesRoot%\%driveID%
SET thisDMRLabel=%thisDMR%\label.txt
SET thisDMRLog=%thisDMR%\log.txt
SET thisDMRLetter=%thisDMR%\letter.txt
SET thisDMRIndex=%thisDMR%\indexSettings.txt
IF EXIST "%thisDMR%" (
        SET /p driveLabel=<"%thisDMRLabel%"
        echo %now%,%thisDrive:~0,1%,Registered>> %thisDMRLog%
        echo %thisDrive:~0,1%>"%thisDMRLetter%"
        IF NOT EXIST "%thisDMRIndex%" (echo F>"%thisDMRIndex%")
    ) ELSE (
        mkdir %thisDMR%
        ping 127.0.0.1 -n 1 > nul
        IF EXIST "%thisDMR%" (
                echo %now%,Created>> %thisDMRLog%
                echo %now%,%thisDrive:~0,1%,Registered>> %thisDMRLog%
                echo N>"%thisDMRIndex%"
                echo %thisDrive:~0,1%>"%thisDMRLetter%"
                echo %thisDrive:~0,1%:\>"%thisDMRLabel%"
                notepad "%thisDMRLabel%"
                ping 127.0.0.1 -n 1 > nul
                SET /p driveLabel=<"%thisDMRLabel%"
            )
    )
echo          %thisDrive:~0,1%:\ %driveLabel%    %driveID%
GOTO:EOF

:driveIDPathNOTEXIST
        SET driveIDtmpFile=tmp001X.txt
        echo '%driveIDtmpFile%'
        CALL %scriptroot%\genguid.bat > %driveIDtmpFile%
        ping 127.0.0.1 -n 1 > nul
        SET /p driveID=<%driveIDtmpFile%
        del /q %driveIDtmpFile%
        echo %driveID%>"%driveIDPath%"
        ping 127.0.0.1 -n 1 > nul
        IF EXIST "%driveIDPath%" (attrib +h "%driveIDPath%")
GOTO:EOF

:VAR
SET manageDrivesRoot=%scriptroot%\manage_drives\%computername%
IF NOT EXIST %manageDrivesRoot% (mkdir %manageDrivesRoot%)
GOTO:EOF


 
