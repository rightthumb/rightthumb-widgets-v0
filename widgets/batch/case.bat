: view per case

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo off
set dbg=

%dbg%@echo off
GOTO START
Note anything Help will not work until 2 new label modules are added



------



:START


set wasat=%bookmarks%\case.back.txt
cd> %wasat%
set caseroot=%scriptroot%\case
set html=%caseroot%\html\home.htm
set code=%caseroot%\html
set /p GOBACK=< %wasat%
set /p LastID=<%caseroot%ID.sys
set /a caseID=%LastID% + 1
echo %caseID% > %caseroot%ID.sys
set log=%caseroot%\open-%caseID%.txt
set did=Cases Refreshed

echo. > %html%


call b case
:OPTIONS
if ["%1"] == ["help"] @echo on
if ["%1"] == ["done"] GOTO ALLDONE
if ["%1"] == ["d"] GOTO ALLDONE
if ["%1"] == ["ad"] GOTO ALLDONE
if ["%1"] == ["edit"] GOTO EDIT
if ["%1"] == ["e"] GOTO EDIT
if ["%1"] == ["r"] GOTO END
if ["%1"] == ["refresh"] GOTO END
if ["%1"] == ["open"] GOTO OPEN
if ["%1"] == ["o"] GOTO OPEN
if ["%1"] == ["c"] GOTO CLOSE
if ["%1"] == ["close"] GOTO CLOSE
if ["%1"] == ["closed"] GOTO CLOSED
if ["%1"] == ["a"] GOTO CLOSEALL
if ["%1"] == ["ca"] GOTO CLOSEALL
if ["%1"] == ["view"] GOTO VIEW
if ["%1"] == ["s"] GOTO SEARCH
if ["%1"] == ["search"] GOTO SEARCH

if ["%1"] == ["help"] pause
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END



title Case: %caseID%

set /p todo=ToDo: 
set /p note=Note:
set /p JS=<case_include.txt



echo ======================= >> "%log%"
    echo ^<br^> >> "%log%"
echo %date% - %time%: >> "%log%"
    echo ^<br^> >> "%log%"


echo Case: %caseID% - ^<b^>  %todo% >> "%log%"
    echo ^</b^> >> "%log%

    echo ^<br^> >> "%log%"
echo %note% >> "%log%"

    echo ^<br^> >> "%log%"
set did=Created Case %caseID%
GOTO END


:CLOSE

echo CLOSE %2
del "closed-%2.txt" 

rename "open-%2.txt" "closed-%2.txt"
set did=Closed Case %2
GOTO END

:OPEN
echo OPEN %2
rename "closed-%2.txt" "open-%2.txt"
set did=Re-opened Case %2
GOTO END

:CLOSED
echo VIEW CLOSED 
type %caseroot%\closed-* > "%html%"
call b back
%dbg%cls

GOTO SKIPEND



:CLOSEALL
echo CLOSEALL
set /p sure=Are you sure you want to close all cases? [y/n]:  
if not ["%sure%"] == ["y"] GOTO END

rename open* closed*
set did=Closed all open Cases
GOTO END

:EDIT
echo EDIT
set did=Edit /Open Case %2


dir /b *%2.txt > ``
set /p editme=<``

rename *%2.txt open-%2.txt
start notepad %caseroot%\open-%2.txt

GOTO END



------
:SEARCH
echo ========= > %caseroot%\search.tmp
findstr /i /r  %2 "%caseroot%\*.*" >> %caseroot%\search.tmp

GOTO END
------



:ALLDONE
ECHO ALLDONE
set did=All Cases Closed
echo ======================= > "%html%"
    echo ^<br^> >> "%html%"
echo %date% - %time%: >> "%html%"
    echo ^<br^> >> "%html%"

    echo ^<b^> >> "%html%
echo All Tasks have been completed >> "%html%"
    echo ^</b^> >> "%html%
    echo ^<br^> >> "%html%"

    echo ^<br^> >> "%html%"
GOTO SKIPEND

:VIEW
start "%USERPROFILE%\AppData\Local\Google\Chrome\Application\chrome.exe" "%html%"
GOTO END


=====================
NOTES
dir /b open* > ``
for /f "tokens=* delims= " %%a in ('dir/b ``') do (
if %%~Za lss 1 GOTO ALLDONE
)

=====================

:END


%dbg%@echo on
dir /b open* > ``
for /f "tokens=* delims= " %%a in ('dir/b ``') do (
if %%~Za lss 1 GOTO ALLDONE
)
%dbg%dir open*
echo ""

type %caseroot%\case_include.txt > "%html%"
type %caseroot%\open-* > "%html%"




:SKIPEND
cd %GOBACK%

%dbg%cls
@echo off
echo %did%

if ["%1"] == ["s"] type %caseroot%\search.tmp
if ["%1"] == ["search"] type %caseroot%\search.tmp



 
