@echo off
if [%1] == [] (
    call b 0
) else (
    call o %*
)