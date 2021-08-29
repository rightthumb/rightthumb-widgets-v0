@echo off
:also ps

setlocal

:: --- Configuration --->

:: Temp-/Infofile path/name
set info=%temp%\info.txt
set info=info.txt

:: IrfanView
set iview="D:\Program Files\IrfanView\i_view32.exe"

:: <--- Configuration ---

%iview% %1 /info=%info%

for /f "tokens=4,6" %%a in ('type %info% ^| find.exe /i "Image dimensions"') do (set /a width=%%a) & (set /a height=%%b)

echo %1 - W:%width% x H:%height%
:echo File: %1
:echo Width: %width% Pixel
:echo Height: %height% Pixel
:echo.


GOTO END
:END