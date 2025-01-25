@echo off
if [%1]==[] (
    call pa > %tmpf%-cp
    set cpOut=%tmpf%-cp
) else (
    call pa > %tmpf%-%1
    set cpOut=%tmpf%-%1
)
echo.
echo Clipboard Saved
echo.