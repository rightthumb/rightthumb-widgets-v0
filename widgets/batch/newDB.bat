@echo off
SET blank_db_path="%widgets%\widgets\databank\blank.db"
IF EXIST [%blank_db_path%] (
	CALL:CP_blank %*
)
GOTO:EOF

:CP_blank
	IF NOT [%1] == [] CALL:copy_with_name %1
	IF [%1] == [] CALL:copy_without_name 
:copy_with_name
xcopy /d/c %blank_db_path% %1

:copy_without_name
xcopy /d/c %blank_db_path%