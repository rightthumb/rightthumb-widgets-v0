@echo off

if [%2] == [] (
    call p callable2 -f %~1
) else (
    call p callable2 -f %~1 --c %~2 %~3 %~4 %~5 %~6 %~7 %~8 %~9
)
