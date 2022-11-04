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

set tmp0=``.txt
set tmp=`.txt
set file=%1
if [%2] == [all] GOTO ALLLINES
findstr /n /v ":1:2:3:4***" %file% > %tmp0%
findstr "%2:" "%tmp0%" > %tmp%

for /F "tokens=2 delims=:" %%b in (%tmp%) do set line=%%b
for /F "tokens=1 delims=:" %%a in (%tmp%) do set number=%%a

del %tmp%
del %tmp0%
if not [%number%] == [%2] GOTO BAD

:GOOD
echo %line%

GOTO END
:BAD
set line=line not available
echo line not available
GOTO END
:ALLLINES
findstr /n /v ":1:2:3:4***" %file% 
GOTO END



:END



 
