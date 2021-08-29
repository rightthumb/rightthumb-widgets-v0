@echo off
:c:\index\history

setlocal enabledelayedexpansion
set /a counter=0
set /a %%a = ""
for /f "usebackq delims=" %%a in (c:\index\history) do (
   if "!counter!"=="%1" goto :printme & set /a counter+=1
)
:printme
echo %%a