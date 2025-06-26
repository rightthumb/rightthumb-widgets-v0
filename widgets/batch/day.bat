@echo off
if "%1"=="" (
	call p. day
) else (
	set theDay=%1
	set theD=d
	call p. day -ago %theDay%%theD%
	@REM call p. day -ago %theDay%%theD%
)
