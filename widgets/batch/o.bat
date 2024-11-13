@echo off

if [%1] == [o] (
	call p. file-open %*
	goto :eof
)

if [%1] == [-f] (
	call p. file-open -backup secure %*
	goto :eof
)
if [%1] == [] (
	call p. file-open -backup secure -alias last
) else (
	call p. file-open -backup secure -alias %*
	rem call cdf
)
