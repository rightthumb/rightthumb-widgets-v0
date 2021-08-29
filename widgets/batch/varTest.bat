@echo off
setlocal enabledelayedexpansion

set argCount=0
for %%x in (%*) do set /A argCount+=1
echo Number of processed arguments: %argCount%

set /a counter=0
for /l %%x in (1, 1, %argCount%) do (
set /a counter=!counter!+1 )