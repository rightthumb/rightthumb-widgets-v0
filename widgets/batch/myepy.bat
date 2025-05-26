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



SET do=True
SET askX=X
IF NOT EXIST "%myPython%\%1.py" (
    CALL :NEW %1
)
rem echo END
rem GOTO:EOF

IF [%do%] == [True] (
    IF NOT EXIST "%myPython%\%1.py" copy %template% %myPython%\%1.py>nul
    call p. fileBackup -open -i "%myPython%\%1.py"
    start "EDIT" %code_editor% "%myPython%\%1.py"
)

GOTO:EOF



:NEW
    CALL :ASK
    rem echo %askX%
    IF [%askX%] == [n] (
        SET do=False
        echo aborted
        GOTO:EOF
    ) ELSE (
        echo Created
        CALL :GETLATEST
        rem echo %template%
        rem echo %myPython%\%1.py
        rem echo copy %template% %myPython%\%1.py
        copy %template% %myPython%\%1.py>nul
        GOTO:EOF
    )
    GOTO:EOF

:ASK
    rem SET askX=X
    SET /P askX=Create?: 
    GOTO:EOF
:GETLATEST
    SET testBase=1

    CALL :LOOP

    
    GOTO:EOF

:LOOP

    SET template="%myImports%\_base%PYTHON_BASE%\_base%PYTHON_BASE%_init_example.py"
    GOTO:EOF

    rem THIS WAS ASSUMING THERE WAS ONLY A EXAMPLE FILE FOR THE LATEST VERSION

    rem CHANGED IT TO THE VARIABLE SET IN c.bat

    rem echo HERE
    SET answer=0
    SET /a testBase=%testBase%+1
    IF EXIST "%myImports%\_base%testBase%\" SET answer=1
    IF ["%answer%"] == ["1"] (
        SET template="%myImports%\_base%testBase%\_base%testBase%_init_example.py"
    )
    IF NOT [%testBase%] == [100] CALL :LOOP
    GOTO:EOF

:END


 
