@set dbg=off

rem ## {R2D2919B742E} ##
rem ###########################################################################
rem What if magic existed?
rem What if a place existed where your every thought and dream come to life.
rem There is only one catch: it has to be written down.
rem Such a place exists, it is called programming.
rem    - Scott Taylor Reph, RightThumb.com
rem ###########################################################################
rem ## {C3P0D40fAe8B} ##

@echo %dbg%

GOTO START
Note anything Help will not work until new modules added



------


call m back
:START

set "invoice_check="
set caseroot=%myTickets%
set html=%caseroot%\html\tickets.htm
set code=%caseroot%\html




set log=%caseroot%\open-%caseID%.txt
set did=Tickets Refreshed

echo. > %html%



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
:if ["%1"] == ["view"] GOTO VIEW
if ["%1"] == ["s"] GOTO SEARCH
if ["%1"] == ["search"] GOTO SEARCH
if ["%1"] == ["css"] GOTO CSS
if ["%1"] == ["view"] GOTO VIEW2
if ["%1"] == ["v"] GOTO VIEW2
if ["%1"] == ["client"] GOTO CLIENT



if ["%1"] == ["help"] pause
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END
if ["%1"] == ["help"] GOTO END

GOTO END



:CLOSE
set did=Closed Ticket %2
echo CLOSE %2
::del "closed-%2.txt" 



if ["%3"] == [""] GOTO close_rename
if NOT ["%3"] == [""] GOTO close_invoice
GOTO END

:close_rename
set invoice_check=false
rename "%caseroot%\open-%2.txt" "closed-%2.txt"

GOTO END
:close_invoice
IF EXIST "%caseroot%\open-%2.txt" GOTO close_invoice_step2
echo ticket already closed
GOTO END
:close_invoice_step2
set invoice_check=true
type "%caseroot%\open-%2.txt" | find /i /v "</span> </span>" > "%caseroot%\closed-%2.txt"
echo ^<br^> ^<span class='invoice' ^> :Invoice# %3 ^</span^> ^<br^> ^</span^> ^</span^> ^<br^>  >>"%caseroot%\closed-%2.txt"
del "%caseroot%\open-%2.txt"
GOTO END

set did=Closed Ticket %2


GOTO END

:OPEN

echo OPEN %2
rename "%caseroot%\closed-%2.txt" "open-%2.txt"
set did=Re-opened Ticket %2
GOTO END

:CLOSED
GOTO END
echo VIEW CLOSED 
type %caseroot%\closed-* > "%html%"
call b back
IF ["%dbg%"] == ["off"] cls

GOTO SKIPEND



:CLOSEALL
GOTO END
echo CLOSEALL
set /p sure=Are you sure you want to close all cases? [y/n]:  
if not ["%sure%"] == ["y"] GOTO END

rename open* closed*
set did=Closed all open Tickets
GOTO END

:EDIT
echo EDIT
set did=Edit /Open Ticket %2


dir /b *%2.txt > ``
set /p editme=<``
del ``
rename *%2.txt open-%2.txt
start "EDIT" %code_editor% %caseroot%\open-%2.txt
GOTO END



------
:SEARCH
echo --------------- > %caseroot%\search.tmp
findstr /i /r  %2 "%caseroot%\*.*" >> %caseroot%\search.tmp
set did=Search Results
GOTO END
------



:ALLDONE
GOTO END
ECHO ALLDONE
set did=All Tickets Closed
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
IF NOT EXIST %html% GOTO ERROR
start "chrome" %chrome% "%html%"
GOTO END


=====================
NOTES
dir /b open* > ``
for /f "tokens=* delims= " %%a in ('dir/b ``') do (
if %%~Za lss 1 GOTO ALLDONE
)

=====================
:CSS
set did=Toggle CSS view

set /p toggle=<%caseroot%\html\toggle.sys
if ["%toggle%"] == ["o "] GOTO CSS_CLOSE
echo 1%toggle%1

:CSS_OPEN
type %caseroot%\html\open.css > %caseroot%\html\style.css
echo o > %caseroot%\html\toggle.sys
echo open
GOTO END

:CSS_CLOSE
type %caseroot%\html\close.css > %caseroot%\html\style.css
echo c > %caseroot%\html\toggle.sys
echo close
GOTO END

:VIEW2
if NOT ["%2"] == [""] GOTO VIEW_TICKET

findstr /i "Session:" %caseroot%\open*

GOTO ENDEND
:VIEW_TICKET
if ["%2"] == ["www"] GOTO VIEW_WWW
if exist %caseroot%\closed-%2.txt findstr /i /v "<" %caseroot%\closed-%2.txt 
if exist %caseroot%\open-%2.txt findstr /i /v "<" %caseroot%\open-%2.txt 
set invoice_search=

findstr /i "Invoice#" %caseroot%\*%2.txt  > invoice_tmp.txt
set /p invoice_search=<invoice_tmp.txt
FOR /F "tokens=6,7 delims== " %%I IN ("%invoice_search%") DO (
ECHO  %%I %%J
)
:del invoice_tmp.txt

:@type %caseroot%\closed-%2.txt | find /i /v "<" 
:@type %caseroot%\open-%2.txt | find /i /v "<" 

GOTO ENDEND
:VIEW_WWW
set did=View myTickets
type %caseroot%\html\header > %html%
type %caseroot%\open-* >> %html%
type %caseroot%\html\footer >> %html%
start "chrome" %chrome% "%html%"
GOTO END

:CLIENT
if ["%2"] == [""] GOTO END
findstr /i "%2" "%caseroot%\open-*.txt" > tmp_client2.txt
type tmp_client2.txt |find /i ") %2" > tmp_client.txt
set clientwww=%caseroot%\html\Client.htm
type %caseroot%\html\header > %clientwww%
for /f "tokens=2 delims=:" %%f in (tmp_client.txt) do ( type D:%%f >> %clientwww% )
type %caseroot%\html\footer >> %clientwww%
del tmp_client.txt
del tmp_client2.txt
start "chrome" %chrome% "%clientwww%"
set did=Client Search %2
GOTO SKIPEND
:END

type %caseroot%\html\header > %html%
type %caseroot%\open-* >> %html%
type %caseroot%\html\footer >> %html%



:SKIPEND
cd %GOBACK%

IF ["%dbg%"] == ["off"] cls
@echo off
echo %did%

if ["%1"] == ["s"] type %caseroot%\search.tmp
if ["%1"] == ["search"] type %caseroot%\search.tmp
if ["%1"] == ["s"] del %caseroot%\search.tmp
if ["%1"] == ["search"] del %caseroot%\search.tmp
if ["%invoice_check%"] == ["false"] echo Ticket closed without Invoice#

GOTO ENDEND
:ERROR
echo ERROR
:ENDEND

 
