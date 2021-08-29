@echo off


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