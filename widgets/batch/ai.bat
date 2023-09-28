@echo off
if [%1] == [] (
    call p ai-simple
) else (
    call p ai-simple -prompt %*
)