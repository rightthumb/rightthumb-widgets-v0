@echo off

if [%2] == [] (
	set runSet=null
	goto:eof
)

set "runSet="
call %* > "%stmp%\runSet.txt"
set /p runSet=<"%stmp%\runSet.txt"