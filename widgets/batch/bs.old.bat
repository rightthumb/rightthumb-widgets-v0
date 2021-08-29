@echo off
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


