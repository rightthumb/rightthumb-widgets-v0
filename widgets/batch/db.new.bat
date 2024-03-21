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

SET blank_db_path=%widgets%\widgets\databank\blank.db
IF EXIST %blank_db_path% (
    echo %blank_db_path%
    CALL:CP_blank %*
    GOTO:EOF
)
GOTO:EOF

:CP_blank
    IF NOT [%1] == [] CALL:copy_with_name %1
    IF [%1] == [] CALL:copy_without_name 
GOTO:EOF

:copy_with_name
    IF EXIST %1 CALL p. print_color -color red -text  "Error: %1, already exists"
    rem IF EXIST %1 echo 
    IF NOT EXIST %1 (
        echo %1>%tmpf%
        copy  %blank_db_path% %1>nul
        CALL p. print_color -text  "created %1" -color green
        CALL p. paths -f %1
    )
GOTO:EOF

:copy_without_name
    IF EXIST blank.db CALL p. print_color -color red -text  "Error: blank.db, already exists"
    rem IF EXIST blank.db echo Error: blank.db, already exists
    IF NOT EXIST blank.db (
        echo blank.db>%tmpf%
        xcopy /d/c %blank_db_path%>nul
        CALL p. print_color -text  "created blank.db" -color green
        CALL p. paths -f blank.db
    )

    
GOTO:EOF

 
