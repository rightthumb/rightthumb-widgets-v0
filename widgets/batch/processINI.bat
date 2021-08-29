@echo off
set thisFile=processINI.php

for /F "tokens=*" %%A in  ( '%php% %phpFiles%\%thisFile%' ) do  (
  set %%A
   
)
