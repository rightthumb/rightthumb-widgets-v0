@echo off
if [%1] == [] (
	call p cat
) else if [%1] == [-f] (
	shift
	call p cat -f %*
) else (
	call p cat -f %*
)