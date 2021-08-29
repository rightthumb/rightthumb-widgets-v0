@echo off
CALL D:\Users\Scott\cc.bat

echo conversion issue
CALL p json2DB -build -app -i %1
echo b issue
CALL b db
echo dba issue
CALL p dba -app %1
PAUSE
PAUSE


