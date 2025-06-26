@echo off
if [%1] == [o] (
	call p. file-open -sub %*
	goto :eof
)

if [%1] == [-f] (
	call p. file-open -sub -backup secure %*
	goto :eof
)
if [%1] == [] (
	call p. file-open -sub -backup secure -alias last
) else (
	call p. file-open -sub -backup secure -alias %*
	rem call cdf
)
