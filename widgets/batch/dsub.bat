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

set do=dir /s/b *%1*



IF NOT "%1" == "" GOTO FIND
dir /b
set do=dir /b
GOTO ENDD
:FIND
IF "%2" == "s" GOTO SUB
dir /b %1
set do=dir /b %1
GOTO ENDD

v 3

:SUB
%do%
GOTO ENDD

:ENDD
ENDLOCAL

 
