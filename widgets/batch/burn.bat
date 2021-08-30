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

CALL p unix


rmdir /s /q %widgets%:\widgets\python\burn\windows
rmdir /s /q %widgets%:\widgets\python\burn\unix
mkdir %widgets%:\widgets\python\burn\windows
mkdir %widgets%:\widgets\python\burn\unix

xcopy /s/d/y/c %widgets%:\widgets\python\src\unix\*.py %widgets%:\widgets\python\burn\unix\
xcopy /s/d/y/c %widgets%:\widgets\python\*.py %widgets%:\widgets\python\burn\windows\



