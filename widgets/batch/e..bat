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

rem if not [%3] == [] (
rem         call p. fileBackup -open -i "%batch%\%1.bat" %2 %3
rem     ) else if not [%2] == [] (
rem         call p. fileBackup -open -i "%batch%\%1.bat" %2
rem     ) else (
rem         call p. fileBackup -open -i "%batch%\%1.bat"
rem )
rem start "EDIT" %code_editor% "%batch%\%1.bat"
call p. file-open -backup -f "%batch%\%1.bat"
rem echo "%batch%\%1.bat"