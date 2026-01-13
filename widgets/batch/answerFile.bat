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

set file=%1

setlocal EnableDelayedExpansion
<"!file!" (
  for /f %%i in ('type "!file!" ^| find /c /v ""') do set /a n=%%i && for /l %%j in (1 1 %%i) do (
	set /p line_%%j=
  )
)

echo *** number of lines: !n!
echo *** line contents:
for /l %%i in (1 1 !n!) do echo !line_%%i!

rem Endlocal
rem setlocal disableDelayedExpansion
for /l %%i in (1 1 !n!) do set VAR_%%i=!line_%%i!

echo.
echo !VAR_1!