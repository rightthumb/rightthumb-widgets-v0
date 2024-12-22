@echo off
if [%1] == [d] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [o] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [-] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [--] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [-m] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [-meta] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [m] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
if [%1] == [db] (
    shift
    call:meta %1 %2 %3 %4 %5 %6 %7 %8 %9
    goto:eof
)
call:contents %*

goto:eof

:meta
call p. dirDB -db D:\websites\domains\meta.db %*
goto:eof

:contents
call p. search-indexDB-files -db D:\websites\domains\index.db %*
goto:eof