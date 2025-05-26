@echo off
if [%1] == [] (
	call p. site -u -f last
) else (
	call p. site -u -f %* 
)

 
