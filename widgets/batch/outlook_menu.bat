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

cls
set l=D:\Program Files (x86)\Microsoft Office\root\Office16\OUTLOOK.EXE
IF ["%1"] == [""] GOTO HELP
IF ["%1"] == ["h"] GOTO HELP
IF ["%1"] == ["/?"] GOTO HELP
IF ["%1"] == ["?"] GOTO HELP
IF [%1] == [a] set item=appointment
IF [%1] == [c] set item=contact
IF [%1] == [e] set item=note
IF [%1] == [n] set item=stickynote
IF [%1] == [j] set item=activity
IF [%1] == [t] set item=task
GOTO START

:HELP
echo =================
echo NEW Outlook Item Menu
echo [a] Appointment
echo [c] Contact
echo [e] Email
echo [n] Stickynote
echo [j] Journal
echo [t] Task
echo =================

GOTO END



:START
title %item%
echo New %item%
"%l%" /c ipm.%item%
GOTO END


:END