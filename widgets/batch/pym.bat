@echo off
set alias=%myPython%\%1.py
echo %alias%
goto :eof
%py% %alias% %*