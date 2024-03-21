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


IF NOT EXIST %myBookmarks%\ MD %myBookmarks%\
set p=%myBookmarks%\BM-%1.txt

IF [%2] == [] (
    CALL p. m -alias %*
) else (
    CALL p. m -alias %* --c
)


rem cd > "%tmpf%"
rem set /p pp=<"%tmpf%"
rem call set pp=%%pp:%widgets%={A8693D4B-8A80-898F-83F0-E806D2F36800}%%
rem call set pp=%%pp:%userprofile%={6FAB5628-94A1-410A-82D1-1D42A2A11750}%%
rem call set pp=%%pp:%thisHost%={C12F266D-71B9-40D2-98B9-424B42D2DBAC}%%
rem rem CALL :DeQuote pp
rem echo %pp%>"%p%"


SET /p back=<"%p%"> nul
rem call set back=%%back:{A8693D4B-8A80-898F-83F0-E806D2F36800}=%widgets%%%
:END

GOTO:EOF
:DeQuote
for /f "delims=" %%A in ('echo %%%1%%') do set %1=%%~A
GOTO:EOF


rem @echo off
rem set myBookmarks=%scriptroot%\script-bookmarks\%computername%
rem IF NOT EXIST %myBookmarks%\ MD %myBookmarks%\
rem set p=%myBookmarks%\BM-%1.txt
rem cd > "%p%"
rem set /p back=<"%p%"
rem :END


 
