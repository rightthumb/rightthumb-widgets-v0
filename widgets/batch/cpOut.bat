@echo off
if [%1]==[] (
    call cat %tmpf%-cp
) else (
    call cat %tmpf%-%1
)