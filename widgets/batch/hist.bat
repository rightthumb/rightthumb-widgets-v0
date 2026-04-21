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

:c:\index\history

setlocal enabledelayedexpansion
set /a counter=0
set /a %%a = ""
for /f "usebackq delims=" %%a in (c:\index\history) do (
   if "!counter!"=="%1" goto :printme & set /a counter+=1
)
:printme
echo %%a