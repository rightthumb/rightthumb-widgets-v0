@echo off
if [%1] == [] (
    call p ai-prompt
) else (
    call p ai-prompt -prompt %*
)