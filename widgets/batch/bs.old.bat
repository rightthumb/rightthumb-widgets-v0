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

set bmRoot=%scriptroot%\script-bookmarks\%computername%

IF NOT [%1] == [] (
        CALL :RUN %1
    ) ELSE (
        ECHO ERROR: No b search content
    )

GOTO:EOF



:RUN
CALL m back
CALL b b
dir /b *%1*
CALL b back
GOTO:EOF




 
