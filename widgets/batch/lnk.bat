@echo off
if [%2] == [] (
	call p. link -f %1
) else (
	call p. link -src %1 -dst %2
)
