@echo off

if not [%2] == [] (
	lnk %1 %2
	goto:eof
)

wsl
cd
