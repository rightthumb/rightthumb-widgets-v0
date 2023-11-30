@echo off
call m back > nul
call b 2023 > nul
if [%1] == [] (
	call p files -ago 3d + *.md --c | .mx u..
) else (
	call p files -ago %1 + *.md --c | .mx u..
)
call b back > nul