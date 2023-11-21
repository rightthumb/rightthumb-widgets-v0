@echo off
if [%1] == [] (
	call p indexDB-files
) else (
	call p indexDB-files -db %1
)