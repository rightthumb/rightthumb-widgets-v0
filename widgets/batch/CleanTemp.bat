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

:Clean Temp Folders

set w=\*
set usr=%USERPROFILE%\Local Settings\Temp%w%
set ie=%USERPROFILE%\Local Settings\Temporary Internet Files\Content.IE5%w%
set ls=D:\Documents and Settings\LocalService\Local Settings\Temp\Temporary Internet Files\Content.IE5%w%
set win=%SystemRoot%\temp%w%
set sys=%SystemRoot%\SYSTEM32\CONFIG\systemprofile\Local Settings\Temporary Internet Files%w%

set switch=/q/s/f
set switch2=/q/s/f/a:r
set switch3=/q/s/f/a:h


cls


@echo off
Title Cleaning Temp Folders: LOOP 
cls

:1
cls
echo loop 1
Title Cleaning Temp Folders: LOOP 1
del "%usr%" %switch%
del "%ie%" %switch%
del "%ls%" %switch%
del "%win%" %switch%
del "%sys%" %switch%

:2
cls
echo loop 2
Title Cleaning Temp Folders: LOOP 2
del "%usr%" %switch%
del "%ie%" %switch%
del "%ls%" %switch%
del "%win%" %switch%
del "%sys%" %switch%


:3
cls
echo loop 3
Title Cleaning Temp Folders: LOOP 3

del "%usr%" %switch2%
del "%ie%" %switch2%
del "%ls%" %switch2%
del "%win%" %switch2%
del "%sys%" %switch2%

:4
cls
echo loop 4
Title Cleaning Temp Folders: LOOP 4
del "%usr%" %switch3%
del "%ie%" %switch3%
del "%ls%" %switch3%
del "%win%" %switch3%
del "%sys%" %switch3%




cls

:end
echo end

 
