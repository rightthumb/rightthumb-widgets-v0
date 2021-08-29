@echo off

IF [%1] == [U] GOTO UPDATE
IF [%1] == [u] GOTO UPDATE


type c:\cpl.txt

GOTO END

:UPDATE
dir /s/b D:\*.cpl > D:\cpl.txt
GOTO END

:END