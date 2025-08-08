@echo off

if [%1]==[] (
	CALL p. on -session %Session_ID% -folder %cd%
) else (
	CALL p. on -session %Session_ID% -delete
)