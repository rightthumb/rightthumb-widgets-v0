@echo off
rem echo %*
rem GOTO:EOF
CALL m back
CALL b tickets
CALL p f -in *.txt -jn + %* > %contextTemp%
CALL b back
rem CALL bb tickets
CALL p context + %*

rem json2DB