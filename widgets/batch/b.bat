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



call result call p b -a %*
rem echo %result%
call:VALIDATE ":" %result%
if [%valid%] == [yes] (
  %result:~0,2%
  cd "%result%"
  cd
) else (
  p error -err Bookmark does not exist
)
goto:eof
:VALIDATE
echo.%2 | findstr /C:"%1" 1>nul
if errorlevel 1 (
  set valid=no
) ELSE (
  set valid=yes
)
goto:eof
rem THE END *************************************************************


SETLOCAL ENABLEDELAYEDEXPANSION
SET count=1
FOR /F "tokens=* USEBACKQ" %%F IN (`p b -a %*`) DO (
  SET result!count!=%%F
  SET result=%%F
  SET /a count=!count!+1
)
ENDLOCAL
echo %var1%
cd %var1%

goto:eof
CALL p b -a %* > "%stmp%\bookmark.tmp"
set /p back=<"%stmp%\bookmark.tmp"
echo %back%
cd %back%

goto:eof
CALL p b -save -a %* 
set /p back=<"%stmp%\bookmark.tmp"
set drive_letter=%back:~0,2%
%drive_letter%
cd "%back%"

GOTO:EOF

IF [%1] == [HELP] GOTO HELP
IF [%1] == [help] GOTO HELP
IF [%1] == [?] GOTO HELP
IF NOT EXIST %myBookmarks%\ MD %myBookmarks%\
set p=%myBookmarks%\BM-%1.txt
IF NOT EXIST "%p%" (echo Not Valid & GOTO END)
set /p back=<"%p%"
call set back=%%back:{A8693D4B-8A80-898F-83F0-E806D2F36800}=%widgets%%%
call set back=%%back:{6FAB5628-94A1-410A-82D1-1D42A2A11750}=%userprofile%%%
call set back=%%back:{C12F266D-71B9-40D2-98B9-424B42D2DBAC}=%thisHost%%%
rem echo "%back%"
IF NOT EXIST "%back%" (echo No Longer EXISTS & echo "%back%" & GOTO END)

set bname=%1

IF [%2] == [var] GOTO VAR
IF [%2] == [v] GOTO VAR
IF not [%2] == [] GOTO CHECKVAR
IF [%1] == [HELP] GOTO HELP


set drive_letter=%back:~0,2%
%drive_letter%
cd "%back%"
GOTO END


:CHECKVAR
IF [%2] == [-e] dir "%back%\*.exe" /s/b 
IF [%2] == [-run] set run="%back%\%3"
IF [%2] == [-run] echo run= %run%



GOTO END
:HELP
echo.==================================
echo examples: 7z represents bookmark
echo.
echo. bm to var:     b 7z var
echo. bm to var:     b 7z v
echo. bm cd change:     b 7z 
echo. bm list exe:      b 7z -e
echo. bm file as var:   b 7z -run 7z.exe

echo. 
GOTO END

:VAR
set v=%back%
echo v= %v%
GOTO END



:END
goto:eof



