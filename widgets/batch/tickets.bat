@echo off

set %tIDROOT%


set /p LastID=<tID.sys
set /a  tID=%LastID%+1
set file=open-%tID%.txt


echo LOOP: %tID%
echo Ticket: %tID%
title Creating Ticket: %tID% 

echo %1 > 

set /p note=Note:

echo %x%


:END

