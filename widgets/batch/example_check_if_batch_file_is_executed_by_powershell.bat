@echo off

echo.
echo.
echo Check if batch file is executed by PowerShell
echo.
echo.
call isPWSH
echo isPWSH == %isPWSH%
echo parent == %isPWSHp%