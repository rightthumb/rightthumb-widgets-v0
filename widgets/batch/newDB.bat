@echo off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

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