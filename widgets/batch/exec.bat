@echo off
if [%1] == [] (
	call p. execute-py
) else (
	call p. execute-py -snip %*
)