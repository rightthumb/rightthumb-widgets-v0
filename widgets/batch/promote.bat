@echo off

set Promote=%1
IF [%1] == [] set /p Promote=Promote What? : 
set LIVE=D:\tech\MyScripts
set log=%LIVE%\Promote-log.txt


IF [%Promote%] == [] GOTO END|set error=001
GOTO LOG

============================
:LOG
echo ==================== >> %log%
date /t >> %log%
time /t >> %log%
echo %Promote% >> %log%
move %Promote% %LIVE% >> %log%
GOTO END

:IF [] == [] GOTO 

:END

:IF [%error%] == [] GOTO 
echo [%1 has been promoted to the production enviroment.]