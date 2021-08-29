@echo off
if [%py%] == [] CALL %userprofile%\cc.bat
CALL p 7z -p -pn -nd -f %1