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

IF [%1] == [r] SET reclaim_tickets=yes
IF [%2] == [r] SET reclaim_tickets=yes
CALL jDate

IF [%1] == [] (
    SET /a xDate=%jDate% - 2
) else (
    SET /a xDate=%jDate% - %1
)


rem GOTO:EOF

CALL gDate %xDate%
SET xDate=
rem ECHO %gDate%
rem GOTO:EOF
SET open_timestamp2=%gDate%
echo %open_timestamp2%
pause
CALL X

 
