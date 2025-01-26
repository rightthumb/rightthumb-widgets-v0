@echo off


if [%1] == [] (
	call:name index.db
	call p. indexDB-files
) else (
	call:name %1
	call p. indexDB-files -db %1
)
goto:eof
:name
if exist %1 (
	call nd %1
)
goto:eof