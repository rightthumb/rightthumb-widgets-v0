@echo off
cls
%py% %widgets%\widgets\python\folder-registration.py
IF [%noTOP%] == [] %py% %widgets%\widgets\python\windows-terminal-header.py