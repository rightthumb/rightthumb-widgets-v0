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

set say=%root%\say.vbs
:set /p words=Say what? 
set words=%1 %2 %3 %4 %5 %6 %7 %8 %9
Set WshShell = WScript.CreateObject("WScript.Shell")

echo %WshShell% > %say%
echo strText = ("%words%") > %say%
echo Set objVoice = CreateObject("SAPI.SpVoice") >> %say%
echo objVoice.Speak strText >> %say%

start %say%



 
