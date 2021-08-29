@echo off
set thisFile=dataSendTest.php


echo. > ~relevant.txt
for /F "tokens=*" %%A in  ( '%php% %phpFiles%\%thisFile%' ) do  (
   %%A
   
)
