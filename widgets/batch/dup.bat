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



set thisFile=duplicates.php

if ["%1"] == ["d"] GOTO DELETEFILES
if ["%1"] == ["delete"] GOTO DELETEFILES
if not exist ~dup.txt notepad ~dup.txt
:echo %file%
%php% %phpFiles%\%thisFile%
GOTO END

:DELETEFILES
if exist ~dup.txt del ~dup.txt

:END

 
