@echo off
if [%1] == [] (
	call pa | call p. auto-remove-prefix
) else (
	call p. auto-remove-prefix %*
)