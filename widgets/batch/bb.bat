@echo off
set pp=%myBookmarks%\BM-%1.txt
rem echo %pp%

IF NOT EXIST "%pp%" (
		echo Not Valid
	) else (
		call :action
	)
set p=
set pp=
GOTO:EOF

:action
	rem type %pp%
	SET /p p=<"%pp%"
	rem echo %p%
	call set p=%%p:{A8693D4B-8A80-898F-83F0-E806D2F36800}=%widgets%%%
	call set p=%%p:{6FAB5628-94A1-410A-82D1-1D42A2A11750}=%userprofile%%%
	call set p=%%p:{C12F266D-71B9-40D2-98B9-424B42D2DBAC}=%thisHost%%%
	SET b=%p%
	IF [%2] == [] echo ^%%b^%% = %b%
GOTO:EOF
