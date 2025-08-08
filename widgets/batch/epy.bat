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

rem echo "%python%\%1.py"

if not [%3] == [] (
	call p. fileBackup -open -i "%python%\%1.py" %2 %3 -python
) else if not [%2] == [] (
	call p. fileBackup -open -i "%python%\%1.py" %2 -python
) else (
	call p. fileBackup -open -i "%python%\%1.py" -python
) 


rem start "EDIT" %code_editor% "%python%\%1.py"
call p. file-open -app %code_editor% -f "%python%\%1.py"