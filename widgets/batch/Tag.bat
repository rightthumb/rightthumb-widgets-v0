@echo off
if [%1] == [] GOTO END
 
start "D:\Program Files\Internet Explorer\IEXPLORE.EXE" "http://support.dell.com/support/topics/global.aspx/support/my_systems_info/details?c=us&l=en&s=gen&servicetag=%1"

:END

