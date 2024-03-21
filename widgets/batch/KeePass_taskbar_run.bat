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

set "id="
call "%userprofile%\rr.bat"
set /p id=Enter ID: 
if [%id%] == [] (
    set id=me
)
call p. fileBackup -open -f %w%\widgets\keys\p\%id%.kdbx
start "C:\Program Files\KeePass Password Safe 2\KeePass.exe" "%w%\widgets\keys\p\%id%.kdbx"
rem start "%techApps%\KeePass-2.49\KeePass.exe" "%w%\widgets\keys\p\%id%.kdbx"

 
