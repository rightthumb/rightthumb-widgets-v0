@echo off
echo.>extList.txt
for /f "tokens=* delims= " %%a in (i) do (
echo %%~xa>>extList.txt
)