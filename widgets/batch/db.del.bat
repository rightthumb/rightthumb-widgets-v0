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

SET /p last_db=<%tmpf%
SET Should_DEL=n
IF NOT EXIST %last_db% CALL p. print_color -text  "The file does not exist" -color red
IF EXIST %last_db% CALL:file_exists
GOTO:EOF

del %last_db%

:file_exists
SET ASK=NO
SET /p ASK=Delete %last_db% ? 
rem IF [%ASK%] == [] GOTO:SHOULD_DEL_FILE
IF [%ASK%] == [y] GOTO:SHOULD_DEL_FILE
IF [%ASK%] == [yes] GOTO:SHOULD_DEL_FILE
CALL p. print_color -text  "NO, the file '%last_db%' was NOT deleted" -color red
GOTO:EOF
:SHOULD_DEL_FILE
del %last_db%
CALL p. print_color -text  "YES, the file '%last_db%' WAS deleted" -color red
GOTO:EOF


 
