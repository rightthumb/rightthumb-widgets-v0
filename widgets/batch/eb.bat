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

if not [%3] == [] (
		call p. fileBackup -open -i "%bash%\%1.sh" %2 %3
	) else if not [%2] == [] (
		call p. fileBackup -open -i "%bash%\%1.sh" %2
	) else (
		call p. fileBackup -open -i "%bash%\%1.sh"
)
start "EDIT" %code_editor% "%bash%\%1.sh"