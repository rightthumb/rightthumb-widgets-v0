@echo off

if [%1]==[] (
	CALL p. on -session %Session_ID% -folder %cd%
	CALL p. tag -trigger expires 1w -fo .
) else (
	CALL p. on -session %Session_ID% -delete
	CALL p. tag -trigger expires 1w -fo . -delete
)