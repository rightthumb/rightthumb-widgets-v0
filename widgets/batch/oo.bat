@echo off 


if [%2] == [] (
	rem echo.
) else (
	call p. file-open -path -alias %1
	call cdf
	goto:eof
)

if [%1] == [] (
	call p. file-open -backup secure -alias last
) else (
	call p. file-open -backup secure -alias %*
	call cdf
)

rem call p. file-open -backup -single %*