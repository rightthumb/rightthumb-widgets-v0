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

if [%1] == [] (
    %py%
) else (
    goto:stuff %*
    goto:eof
)

:stuff
if exist "%python%\%1.py" (
    %py% "%python%\%1.py"
) else (
    @REM type D:\.rightthumb-widgets\widgets\python\0-index.list  --c + %* | p. pipe-cleaner -ext
    @REM CALL p. py-finder  + $@ -percentage
    @REM CALL p. file -prefix -noext --c -folder %widgets%\widgets\python + %*
    call p. cat -f D:\.rightthumb-widgets\widgets\python\0-index.list + %*
)

rem @echo off
rem if [%1] == [] (
rem     %py%
rem ) else if exist %widgets%\widgets\python\%1.py (
rem     set subject=%1
rem     shift
rem     %py% %widgets%\widgets\python\%subject%.py %*
rem ) else (
rem     CALL p. file -noext --c -folder %widgets%\widgets\python + %*
rem )



 
 
