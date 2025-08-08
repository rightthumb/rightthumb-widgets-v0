@echo off

if "%1"=="" (
	call p. file  -f 101   -noext _ -rr --s --c
	goto :eof
)

call p. files -folder %ww%\bash\101 --c -fp + %* | p cat