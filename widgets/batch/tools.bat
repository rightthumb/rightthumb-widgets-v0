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

cls
set do=Tools Search
echo %pc% - i am executing (%do%) for you %code_editor%
set base=D:\Tech\Tools
set log=%base%\log.txt
set title=%pc% - Finding Tools for %code_editor%



set delim==========================
title= %title%
cd %base%
set infolder=D:\script-bookmarks\BM-tools.txt
set /p in=<%infolder%
GOTO START
=========================
:START
echo %delim%
set do1=dir /b/s *.exe
echo :exe
%do1%
set do2=dir /b/s *.bat
echo :bats
%do2%


GOTO END
=========================
:END
echo %delim%
echo ^<%pc%^>
echo Just Ran: [%do1%] AND [%do2%]
echo In: %in%\

echo ^</%pc%^>
echo %delim%
title=%title%- Done



 
