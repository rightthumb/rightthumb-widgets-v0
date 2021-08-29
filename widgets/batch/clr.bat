@echo off
:http://ss64.com/nt/color.html
echo does not work
if ["%1"] == [""] GOTO END
if not exist ~ echo  " >~ & clr string "
if not exist ~ GOTO END
findstr /a:1 "%1" ~
:END