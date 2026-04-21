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

setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do set /A argCount+=1
echo Number of processed arguments: %argCount%

set /a counter=0
for /l %%x in (1, 1, %argCount%) do (
set /a counter=!counter!+1 )