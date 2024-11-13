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


set YYYY=%DATE:~10,4%
set MM=%DATE:~4,2%
set DD=%DATE:~7,2%

set HH=%TIME: =0%
set HH=%HH:~0,2%
set MI=%TIME:~3,2%
set SS=%TIME:~6,2%
set FF=%TIME:~9,2%

set theEcho=%2
IF [%1] == [?] call :THEHELP
IF [%1] == [epoch] call :EPOCH
IF [%1] == [csdel] call :CSDEL
IF [%1] == [t] call :THETIME
IF [%1] == [t2] call :THETIMETWO
IF [%1] == [d] call :THEDATE
IF [%1] == [d2] call :THEDATETWO
IF [%1] == [s] call :SINGLE
IF [%1] == [sdel] call :SINGLEDELIM
IF [%1] == [ats] call :THEAT
IF [%1] == [ats2] call :THEAT2
IF [%1] == [sec] call :SEC
IF [%1] == [ms] call :MS
IF [%1] == [msdel] call :MSDELIM
IF [%1] == [msdel2] call :MSDELIMTWO
IF [%1] == [] call :DEFAULT
IF [%1] == [default] call :DEFAULT
IF [%1] == [dt] call :DATETIMEDEFAULT

GOTO:EOF

:THEHELP
set theEcho=noEcho

call :EPOCH
echo epoch  %now%

call :CSDEL
echo csdel  %now%

call :THETIME
echo t      %now%

call :THETIMETWO
echo t2     %now%

call :THEDATE
echo d      %now%

call :THEDATETWO
echo d2     %now%

call :SINGLE
echo s      %now%

call :SINGLEDELIM
echo sdel   %now%

call :THEAT
echo ats    %now%

call :THEAT2
echo ats2   %now%

call :SEC
echo sec    %now%

call :MS
echo ms     %now%

call :MSDELIM
echo msdel  %now%

call :MSDELIMTWO
echo msdel2 %now%
echo.
echo var name = ^%%now^%% 
echo.
echo Example:
echo         timestamp ats noEcho

GOTO:EOF
:EPOCH
%py% "%python%\simpleEpoch.py">%stmp%\simpleEpoch.txt
set /p now=<%stmp%\simpleEpoch.txt
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:CSDEL
set now=%YYYY%-%MM%-%DD%,%HH%:%MI%.%SS%.%FF%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF


:THEDATE
set now=%date:~-4,4%/%date:~-10,2%/%date:~-7,2%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:THEDATETWO
set now=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:THETIME
set now=%time:~0,2%:%time:~3,2%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:THETIMETWO
set now=%time:~0,2%.%time:~3,2%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:DEFAULT
set now=%date:~-4,4%.%date:~-10,2%.%date:~-7,2%@%time:~0,2%:%time:~3,2%
IF NOT [%theEcho%] == [noEcho] (echo { epoch d d2 t t2 s sdel sec ms msdel msdel2 default ; noEcho })
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:DATETIMEDEFAULT
set now=%date:~-4,4%/%date:~-10,2%/%date:~-7,2% %time:~0,2%:%time:~3,2%
IF NOT [%theEcho%] == [noEcho] (echo { d d2 t t2 s sdel sec ms msdel msdel2 default ; noEcho })
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:SINGLE
set now=%YYYY%%MM%%DD%%HH%%MI%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:SINGLEDELIM
set now=%YYYY%.%MM%.%DD%-%HH%.%MI%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:THEAT
set now=%YYYY%.%MM%.%DD%@%HH%.%MI%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:THEAT2
set now=%YYYY%.%MM%.%DD% @ %HH%.%MI%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:SEC
set now=%YYYY%%MM%%DD%%HH%%MI%%SS%%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:MS
set now=%YYYY%%MM%%DD%%HH%%MI%%SS%%FF%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:MSDELIM
set now=%YYYY%.%MM%.%DD%.%HH%.%MI%.%SS%.%FF%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF

:MSDELIMTWO
set now=%YYYY%.%MM%.%DD%-%HH%.%MI%_%SS%.%FF%
IF NOT [%theEcho%] == [noEcho] (echo now = %now%)
GOTO:EOF


    

 
