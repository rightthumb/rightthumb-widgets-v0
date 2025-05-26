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

SET shouldBuildList=True
SET clearList=n


if exist %tmpf% CALL :FOUNDLIST
echo shouldBuildList: %shouldBuildList%
if [%shouldBuildList%] == [True] CALL :BUILDLIST

CALL :PRINTDIRDATA %*

goto:eof







:PRINTDIRDATA
    cls
    echo.

    SET mc=md
    SET ago=2w

    if [%1] == [md] (
            SET mc=md
        ) else if [%1] == [cd] (
            SET mc=cd
        ) else (
            SET ago=%1
        )

    if [%2] == [md] (
            SET mc=md
        ) else if [%2] == [cd] (
            SET mc=cd
        ) else (
            SET ago=%2
        )

    rem echo mc: %mc%
    rem echo ago: %ago%
    rem echo.
    rem echo p dir -ago %ago% %mc% - *.pyc -datepath %mc%
    rem goto:eof

    type %tmpf% | CALL p. dir -ago %ago% %mc% - *.pyc -datepath %mc%

    goto:eof

:FOUNDLIST
    del /q %tmpf%
    rem SET /p clearList=Refresh List?: 
    rem if [%clearList%] == [y] (
    rem         del /q %tmpf%
    rem         echo Freshened List
    rem     ) else (
    rem         SET shouldBuildList=False
    rem     )

    goto:eof

:BUILDLIST
    if exist %myBatch% dir /s/b %myBatch%\ >> %tmpf%
    if exist %batch% dir /s/b %batch%\ >> %tmpf%

    if exist %myPython% dir /s/b %myPython%\ >> %tmpf%
    if exist %python% dir /s/b %python%\ >> %tmpf%

    if exist %powershell% dir /s/b %powershell%\ >> %tmpf%
    if exist %php2% dir /s/b %php2%\ >> %tmpf%

    if exist %exe% dir /s/b %exe%\ >> %tmpf%
    goto:eof

goto:eof




 
