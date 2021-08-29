@echo off
set tmp0=``.txt
set tmp=`.txt
set file=%2
findstr /n /v "::::***" "%file%" > %tmp0%
findstr "%1:" "%tmp0%" > %tmp%

for /F "tokens=2 delims=:" %%b in (%tmp%) do set line=%%b
for /F "tokens=1 delims=:" %%a in (%tmp%) do set number=%%a

del %tmp%
del %tmp0%
if not [%number%] == [%1] GOTO BAD

:GOOD
echo %line%
echo %number%
GOTO END
:BAD
set line=line not available
echo line not available
GOTO END


:END