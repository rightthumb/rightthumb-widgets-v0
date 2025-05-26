@echo off
rem call pa | call  p line --c -make "- {}" | call cp
if [%1] == [] (
	call p. files -folder %python% -r -rr + *.py
) else (
	call p. files -folder %python% -r -rr + *.py %*
)
