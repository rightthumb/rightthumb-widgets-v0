@echo off
SET FILE="{AABD68C1-8CCB-431A-A785-59A2C03EBFAB}.txt"
echo test > %file% && GOTO:SUCCESS || GOTO:FAIL
GOTO:EOF

:SUCCESS
ECHO SUCCESS
del %FILE%>nul
GOTO:EOF

:FAIL
ECHO FAIL
GOTO:EOF