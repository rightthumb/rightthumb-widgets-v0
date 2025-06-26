@echo off

CALL m back --c
CALL b vmware > nul
IF [%1] == [-n] (
	call:new %2
	goto:eof
) ELSE IF [%1] == [-new] (
	call:new %2
	goto:eof
)
CALL d
goto:eof

:new
	mkdir %1
	cd %1
	echo created: %1
	cd
	cd..
goto:eof


:test
	echo %1
goto:eof
