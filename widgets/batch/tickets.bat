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