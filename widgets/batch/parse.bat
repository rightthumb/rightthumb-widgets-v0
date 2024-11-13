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

set file=%1
set parse=%2
set count=%3
if NOT ["%1"] == [""] CALL :RUN
if ["%1"] == [""] echo file parse count

set file=
set parse=
set count=
set thisFile=

GOTO:EOF

:RUN
set thisFile=parse.php
%php% %phpFiles%\%thisFile%
echo.
echo.
GOTO:EOF

:EXAMPLE
 > ~out.txt & parse ~out.txt : 1 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt


b bmRoot
ff grow > output.txt & parse output.txt : 1

b dyan
ff test > ~out.txt & parse ~out.txt : 1 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
type obj1.csv > ~out.txt & parse ~out.txt "," 2 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
type tmp.txt |+ #NHC |+ new > ~out.txt & parse ~out.txt "''" 2 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
type Script_TMP.txt |+ name |++ "<Step enable" > ~out.txt & parse ~out.txt "''" 2 > ~dup.txt & dup & del ~dup.txt & del ~out.txt & del ~fin.txt
type Script_TMP.txt |+ name |++ "<Step enable" > ~out.txt & parse ~out.txt "''" 2 > ~dup.txt & dup > scriptNames.txt & del ~dup.txt & del ~out.txt & del ~fin.txt & %code_editor% scriptNames.txt
drivers > ~out.txt & cleanSpaces ~out.txt > ~out2.txt & parse ~out2.txt "," 2  & del ~out*
drivers > ~out.txt & cleanSpaces ~out.txt > ~out2.txt & parse ~out2.txt "," 2  |+ blue

ffff test
fffff test

:END

 
