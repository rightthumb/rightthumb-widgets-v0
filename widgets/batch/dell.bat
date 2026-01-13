@echo off


call o.p last > "%tmpf%.last"
set /p last=<"%tmpf%.last"
echo Delete: %last%
set "shouldDelete="
set /p shouldDelete=Delete? (y/n):

if /i "%shouldDelete%"=="y" (
    del "%last%"
    echo Deleted %last%
) else (
    echo Not deleted %last%
)

set "shouldDelete="