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


set demote=%1
IF [%1] == [] set /p demote=Demote What? : 
set dev=%USERPROFILE%\Documents\tech\Scripts\DEV
set log=%dev%\demote-log.txt


IF [%demote%] == [] GOTO END|set error=001
GOTO LOG

============================
:LOG
echo ==================== >> %log%
date /t >> %log%
time /t >> %log%
echo %demote% >> %log%
move %demote% %dev% >> %log%
GOTO END

IF [] == [] GOTO 

:END

IF [%error%] == [] GOTO 


 
