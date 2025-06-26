@REM @echo off

IF NOT [%Session_ID%] == [] (
doskey /history >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"  2>&1
CALL:BUILD_TICKET >nul 2>&1
)

cls

GOTO:EOF

:BUILD_TICKET
    IF ["%project%"] == [""] SET name=closed-%Session_ID%.txt
    IF NOT ["%project%"] == [""] SET name=open-%Session_ID%.txt
    SET file=%stmp%\unclaimed_tickets\%name%
    SET fileTempData=%myTickets%\tempFile.txt
    SET timestamp=%date:~-4,4%.%date:~-10,2%.%date:~-7,2% @ %time:~0,2%:%time:~3,2%
    ECHO ^<div class='box' ^> > "%file%"  2>&1
    ECHO ^<div class='item' ^> >> "%file%"  2>&1
    ECHO Session: %Session_ID% (%timestamp_start% - %timestamp%) isAdmin:%isAdmin% %project%>> "%file%"  2>&1
    ECHO ^</div^> >> "%file%"  2>&1
    ECHO ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='guid' ^> %instanceID%^</div^>>> ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='sid' ^> %machineID%^</div^>>> ^<br^> >> "%file%"  2>&1
    ECHO ^<div class='details' ^> >> "%file%"
    IF NOT ["%lab%"] == [""] ECHO ^<div class='laboratory' ^> %lab% >> ^</div^> >> "%file%"  2>&1
    ECHO ^<br^> >> "%file%"  2>&1
    ECHO ^<pre^> >> "%file%"  2>&1
    ECHO. >> "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt"
    CALL p. singleLine -f "%stmp%\unclaimed_tickets_history\history-%Session_ID%.txt" > "%fileTempData%"  2>&1
    TYPE "%fileTempData%" | p. passFilter >> "%file%"  2>&1
    TYPE "%file%" > "%fileTempData%"  2>&1
    DEL "%fileTempData%"
    ECHO ^</pre^> >> "%file%"  2>&1
    ECHO ^<br^> ^</div^> ^</div^> ^<br^> >> "%file%"  2>&1
goto:eof