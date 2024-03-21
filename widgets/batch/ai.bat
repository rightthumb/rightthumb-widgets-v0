@echo off
if [%1] == [] (
	call p. vps-ai-sds
) else (
	call:run %*
)

:run

if [%1] == [-q] (
call p. vps-ai-sds %*
) else (
call p. vps-ai-sds -p %*
)
goto:eof

rem @echo off
rem if [%1] == [] (
rem     call p. ai-prompt
rem ) else (
rem     call p. ai-prompt -prompt %*
rem )
