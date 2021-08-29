@echo off
if [%1] == [] (
	type %widgets%widgetsbash\bash-file\headers.txt
) else (
	CALL p file -noext --c -folder %widgets%widgetsbash + %*
)