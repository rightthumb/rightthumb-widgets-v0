@echo off

if [%1] == [] (
	call p. file-open -backup secure -alias last
) else (
	call p. file-open -backup secure -alias %*
	rem call cdf
)
