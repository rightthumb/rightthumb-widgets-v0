@echo off
if [%1] == [] (
	call p. site -d -f last
) else (
	call p. site -d -f %* 
)
