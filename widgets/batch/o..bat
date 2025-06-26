@echo off

if [%1] == [] (
	call p. file-open -print -alias last
) else (
	call p. file-open -print -alias %*
	rem call cdf
)
