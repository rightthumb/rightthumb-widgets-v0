@echo off


if [%1]==[] (
	echo.
	echo ob wt
	echo ob https://sds.sh/
	echo.
	echo.
	echo ob https://sds.sh/  -fn md
	echo ob https://sds.sh/  -fn cd
	echo ob c.bat  -fn cd
	echo ob c.bat  -fn md -t fd
	echo.
	echo.
	echo Off Topic But Possible: ob 1w -fn ago -t fd
	echo.
	echo.
	

	goto :eof
)

call p. script-helper -i %* | call cp