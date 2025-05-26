@echo off

if [%1] == [] (
    CALL a.BTN--wt--ctrlw-toggle
    goto:eof
)


setlocal
set folder=D:\.rightthumb-widgets
set single=%folder%\.folder.meta.single
set multi=%folder%\.folder.meta.multi
set file=%folder%\.folder.meta

call p. cat -f "%file%" + aleen --c > "%stmp%\a.w.status" 2>nul
set /p status=<"%stmp%\a.w.status"

rem Checking if the length of status is over 4 characters
set "has_length="
call :strlen status len
if %len% GTR 4 set "has_length=true"

if defined has_length (
    type "%single%" > "%file%"
    echo Single
) else (
    type "%multi%" > "%file%"
    echo Multi
)
endlocal
exit /b

:strlen
setlocal EnableDelayedExpansion
set "s=!%~1!"
if not defined s (
    endlocal & set "%~2=0"
    exit /b
)
set "len=0"
for /l %%i in (12,-1,0) do (
    set /a "len|=1<<%%i"
    for %%j in (!len!) do if "!s:~%%j,1!"=="" set /a "len&=~1<<%%i"
)
endlocal & set "%~2=%len%"
exit /b
