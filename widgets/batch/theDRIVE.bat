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

SET "theDRIVE="

SET FIND_DRIVE=%1
CALL :DRIVESCAN
if [%2] == [error] CALL :ERROR_CHECK
GOTO:EOF
:DRIVESCAN
IF EXIST "D:\" SET thisDrive=B & CALL :SETDRIVE
rem IF EXIST "D:\" SET thisDrive=C & CALL :SETDRIVE
rem IF EXIST "D:\" SET thisDrive=D & CALL :SETDRIVE
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
SET "testPath="




  

GOTO:EOF


:ERROR_CHECK
IF [%theDrive%] == [] (
        CALL :ERROR_FAIL
    )
GOTO:EOF
:ERROR_FAIL
SET theDrive=Error
rem echo %theDrive%
GOTO:EOF

:SETDRIVE
IF NOT [%theDRIVE%] == [] GOTO:EOF
SET testPath=%thisDrive:~0,1%:\drive.id.sys

IF EXIST "%testPath%" (
        CALL :DRIVECHECK %1
    )
GOTO:EOF
:DRIVECHECK
SET /p thisDriveID=<%testPath%
rem echo %thisDriveID% %1 %thisDrive:~0,1%
rem echo %thisDriveID% %FIND_DRIVE% %thisDrive:~0,1%
if [%thisDriveID%] == [%FIND_DRIVE%] (
    SET theDRIVE=%thisDrive:~0,1%
    )
GOTO:EOF


 
