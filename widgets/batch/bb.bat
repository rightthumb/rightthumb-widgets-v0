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
    call p. script-helper -replace "'%b%' '/' '\\'" > %tmpf%
    SET /p b=<%tmpf%
    rem IF [%2] == [] echo ^%%b^%% = %b%
    IF [%2] == [] echo %b%
GOTO:EOF


 
