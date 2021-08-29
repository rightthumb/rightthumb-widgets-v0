@echo off
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

