@echo off
cls
setlocal

if [] == [%1] (
	set file=ae.fn.java
) else if [0] == [%1] (
	call:file0 %*
) else (
	set file=%1
)
if [0] == [%1] (
	call p. Parentheses -f %file% -fn -0 | p line -u --c | sort
) else (
	call p. Parentheses -f %file% -fn | p line -u --c | sort
)
goto :eof
:file0
if [] == [%2] (
	set file=ae.fn.java
) else (
	set file=%2
)
goto :eof

endlocal