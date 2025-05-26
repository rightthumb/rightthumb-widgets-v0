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

set getDate=N
IF ["%1"] == ["d"] set getDate=Y
IF EXIST D:\ set "foundDrive=B" & CALL :FOUND B %getDate%
IF EXIST D:\ set "foundDrive=C" & CALL :FOUND C %getDate%
IF EXIST D:\ set "foundDrive=D" & CALL :FOUND D %getDate%
IF EXIST E:\ set "foundDrive=E" & CALL :FOUND E %getDate%
IF EXIST F:\ set "foundDrive=F" & CALL :FOUND F %getDate%
IF EXIST G:\ set "foundDrive=G" & CALL :FOUND G %getDate%
IF EXIST H:\ set "foundDrive=H" & CALL :FOUND H %getDate%
IF EXIST I:\ set "foundDrive=I" & CALL :FOUND I %getDate%
IF EXIST J:\ set "foundDrive=J" & CALL :FOUND J %getDate%
IF EXIST K:\ set "foundDrive=K" & CALL :FOUND K %getDate%
IF EXIST L:\ set "foundDrive=L" & CALL :FOUND L %getDate%
IF EXIST M:\ set "foundDrive=M" & CALL :FOUND M %getDate%
IF EXIST N:\ set "foundDrive=N" & CALL :FOUND N %getDate%
IF EXIST O:\ set "foundDrive=O" & CALL :FOUND O %getDate%
IF EXIST P:\ set "foundDrive=P" & CALL :FOUND P %getDate%
IF EXIST Q:\ set "foundDrive=Q" & CALL :FOUND Q %getDate%
IF EXIST R:\ set "foundDrive=R" & CALL :FOUND R %getDate%
IF EXIST S:\ set "foundDrive=S" & CALL :FOUND S %getDate%
IF EXIST T:\ set "foundDrive=T" & CALL :FOUND T %getDate%
IF EXIST U:\ set "foundDrive=U" & CALL :FOUND U %getDate%
IF EXIST V:\ set "foundDrive=V" & CALL :FOUND V %getDate%
IF EXIST W:\ set "foundDrive=W" & CALL :FOUND W %getDate%
IF EXIST X:\ set "foundDrive=X" & CALL :FOUND X %getDate%
IF EXIST Y:\ set "foundDrive=Y" & CALL :FOUND Y %getDate%
IF EXIST Z:\ set "foundDrive=Z" & CALL :FOUND Z %getDate%


GOTO:EOF


:FOUND
set foundDrive=%1
set getDate=%2
IF [%2] == [Y] (
        set testTMP=Access denied
        set result=Access denied
        CALL getResult "attrib -H %foundDrive%:\drive.id.sys"
IF ["%result%"] == ["Access denied"] (
        set testTMP=Access denied
    ) else (
        set testTMP=%result:~,13%
    )
echo %testTMP%
        IF ["%testTMP%"] == ["Access denied"] (
                set getDate=N
                echo Not Admin
            )
    )

IF [%getDate%] == [Y] CALL :GETIDDATE %foundDrive%
IF [%getDate%] == [N] CALL :GETID %foundDrive%


echo %foundDrive%:\ %foundDriveId% %foundDriveIdDate%
set foundDrive=
set foundDriveId=
set foundDriveIdDate=
set result=
GOTO:EOF


:GETIDDATE
set foundDrive=%1
IF EXIST %foundDrive%:\drive.id.sys (
        attrib -H %foundDrive%:\drive.id.sys
        CALL getResult "dir %foundDrive%:\drive.id.sys |+ drive.id.sys"
        attrib +H %foundDrive%:\drive.id.sys
        set /p foundDriveId=<%foundDrive%:\drive.id.sys
        ::set foundDriveIdDate=%result:~1,9%
        set foundDriveIdDate=%result:~6,4%.%result:~,2%.%result:~3,2%
    ) else (
        genGUID>%foundDrive%:\drive.id.sys
        attrib +H %foundDrive%:\drive.id.sys
    )
GOTO:EOF


:GETID
set foundDrive=%1
IF EXIST %foundDrive%:\drive.id.sys (
        set /p foundDriveId=<%foundDrive%:\drive.id.sys
    ) else (
        genGUID>%foundDrive%:\drive.id.sys
    )
GOTO:EOF




 
