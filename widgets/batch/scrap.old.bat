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

CALL p. fileLine -f %wprofile%\config\.unix_id -line 7 --c > %tmpf%
SET /p unixID7=<%tmpf%
SET scrap2="%w%\widgets\bash\notes\RT-scrap-%unixID7%.txt"
if not exist "%w%\widgets\bash" mkdir "%w%\widgets\bash"
if not exist "%w%\widgets\bash\notes" mkdir "%w%\widgets\bash\notes"
if not exist %scrap2% (
    echo %computername% - %distro% >> %scrap2%
    echo ______________________________________________________________________ >> %scrap2%
    echo.  >> %scrap2%
    echo ______________________________________________________________________ >> %scrap2%
)


call n %scrap2%


 
