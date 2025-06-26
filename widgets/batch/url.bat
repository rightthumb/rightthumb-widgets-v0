@echo off

@echo off
if not "%~2"=="" (
    CALL p. site. -a %1 -url %2 -add
) else (
    CALL p. site. -a %*
)

goto:eof

call p. site -f %1
