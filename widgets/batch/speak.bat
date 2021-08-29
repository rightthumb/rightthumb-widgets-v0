@echo off
set say=%root%\say.vbs
:set /p words=Say what? 
set words=%1 %2 %3 %4 %5 %6 %7 %8 %9
Set WshShell = WScript.CreateObject("WScript.Shell")

echo %WshShell% > %say%
echo strText = ("%words%") > %say%
echo Set objVoice = CreateObject("SAPI.SpVoice") >> %say%
echo objVoice.Speak strText >> %say%

start %say%

