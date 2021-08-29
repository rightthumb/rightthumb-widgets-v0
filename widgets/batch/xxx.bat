@echo off
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