@echo off

set demote=%1
IF [%1] == [] set /p demote=Demote What? : 
set dev=D:\Users\Scott\Documents\tech\Scripts\DEV
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
