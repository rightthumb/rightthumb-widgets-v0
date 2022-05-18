@echo off
call m back --c
call b w > nul
if [%1] == [] (
    call:one
) else (
    call:two %*
)
call b back > nul
goto:eof
:one
call p files -w --c -ago 10h | p line --c -make "git add {}" | p execute
goto:eof
:two
call p files -w --c -ago %* | p line --c -make "git add {}" | p execute
goto:eof
