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

set sw=
if ["%2"] == ["s"] set sw=/S


reg query %1 %sw%>%contextTemp% 2>&1 && CALL:SUCCESS %* || CALL:FAIL %*
GOTO:EOF
:SUCCESS
type %contextTemp%
GOTO:EOF
:FAIL
GOTO:EOF

rem https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/reg-query
rem https://www.robvanderwoude.com/regsearch.php

rem q HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment Path


rem REG Query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /V /F Path /S /E
rem REG Query "HKCU\SOFTWARE" /V /F windowsterminal /S /E
rem REG Query "HKCU\SOFTWARE" /V /F buffersize /S /E

rem REG Query HKLM\Software /K /F windowsterminal /S /E

