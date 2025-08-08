@echo off

if [%1] == [] (
	call p. file-open -print -sub -backup secure -alias last
) else (
	call p. file-open -print -sub -backup secure -alias %*
	rem call cdf
)