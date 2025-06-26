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


PROMPT - 
ECHO %1>~path.txt    
FOR /F "tokens=1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26 delims=\" %%A in (~path.txt) DO (
IF NOT [%%A]==[] SET myVar=%%A
IF NOT [%%B]==[] SET myVar=%%B
IF NOT [%%C]==[] SET myVar=%%C
IF NOT [%%D]==[] SET myVar=%%D
IF NOT [%%E]==[] SET myVar=%%E
IF NOT [%%F]==[] SET myVar=%%F
IF NOT [%%G]==[] SET myVar=%%G
IF NOT [%%H]==[] SET myVar=%%H
IF NOT [%%I]==[] SET myVar=%%I
IF NOT [%%J]==[] SET myVar=%%J
IF NOT [%%K]==[] SET myVar=%%K
IF NOT [%%L]==[] SET myVar=%%L
IF NOT [%%M]==[] SET myVar=%%M
IF NOT [%%N]==[] SET myVar=%%N
IF NOT [%%O]==[] SET myVar=%%O
IF NOT [%%P]==[] SET myVar=%%P
IF NOT [%%Q]==[] SET myVar=%%Q
IF NOT [%%R]==[] SET myVar=%%R
IF NOT [%%S]==[] SET myVar=%%S
IF NOT [%%T]==[] SET myVar=%%T
IF NOT [%%U]==[] SET myVar=%%U
IF NOT [%%V]==[] SET myVar=%%V
IF NOT [%%X]==[] SET myVar=%%X
IF NOT [%%X]==[] SET myVar=%%X
IF NOT [%%Y]==[] SET myVar=%%Y
IF NOT [%%Z]==[] SET myVar=%%Z

)
DEL ~path.txt /F /Q

set "a=%myVar%
echo %a%
if ["%a:~-5%"] == ["     "] GOTO 5
GOTO next
:5
set myvar2=%a:~0,-5%.7z
GOTO spaces_check_done
:next
if ["%a:~-4%"] == ["    "] GOTO 4
GOTO next
:4
set myvar2=%a:~0,-4%.7z
GOTO spaces_check_done
:next
if ["%a:~-3%"] == ["   "] GOTO 3
GOTO next
:3
set myvar2=%a:~0,-3%.7z
GOTO spaces_check_done
:next
if ["%a:~-2%"] == ["  "] GOTO 2
GOTO next
:2
set myvar2=%a:~0,-2%.7z
GOTO spaces_check_done
:next
if ["%a:~-1%"] == [" "] GOTO 1
GOTO none
:1
set myvar2=%a:~0,-1%.7z
GOTO spaces_check_done
:none
set myvar2=%a%.7z
GOTO spaces_check_done
:spaces_check_done
echo "%myvar2%" %1

"c:\Program Files (x86)\7-Zip\7z.exe" a "%myvar2%" %1


 
