@echo off
call m back --c
call:vars %*

if [%gitfilesrepo%] == [] (
    call b w > nul
) else (
    call b %gitfilesrepo% > nul
)


if [%gitfilesago%] == [] (
    call:one
) else (
    call:two %gitfilesago%
)
call b back > nul
goto:eof
:one
call p. files -backup -w --c -ago 10h  | p. line --c -make "git add {}" | p. execute
goto:eof
:two
call p. files -backup -w --c -ago %*  | p. line --c -make "git add {}" | p. execute
goto:eof
:three
call p. files -backup -w --c -ago %1  | p. line --c -make "git add {}" | p. execute
goto:eof

:vars
if not [%1] == [] call:checkvar %1
if not [%2] == [] call:checkvar %2
goto:eof
:checkvar
set testvar=%1

:: Extract the first character
set "firstChar=%testvar:~0,1%"

:: Check if the character is a number
if "%firstChar%" geq "0" if "%firstChar%" leq "9" (
    set gitfilesago=%testvar%
) else (
    set gitfilesrepo=%testvar%
)
set "testvar="
set "firstChar="
goto:eof
