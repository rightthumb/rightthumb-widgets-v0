@echo off
CALL C:\Users\Scott\.rt\profile\vars\config.bat
CALL C:\Users\Scott\.rt\profile\vars\personal.bat

SET batch=%widgets%\widgets\batch
SET python=%widgets%\widgets\python
SET myBatch=%myHome%\widgets\batch
SET myPython=%myHome%\widgets\python
SET appPaths=%batch%;%python%;%myBatch%;%myPython%

SET path=%path%;%appPaths%
SET "appPaths="
@REM if exist %wprofile%\config\._Var_Cache_.bat (
@REM     type %wprofile%\config\._Var_Cache_.bat | D:\.rightthumb-widgets\widgets\batch\.mx.bat SET
@REM )


CALL :GENERATE_API_ID
GOTO:EOF

:GENERATE_API_ID
    SET /p LastID=<%userprofile%\.rt\profile\vars\ID.sys
    SET /a Session_ID=%LastID% + 1
    SET Session_ID_BK=%Session_ID%
    ECHO %Session_ID% > %userprofile%\.rt\profile\vars\ID.sys
    CALL timestamp ats2 noEcho >nul 2>&1
    CALL p. files -folder %userprofile%\.rt\profile\vars -rrr > nul
    @REM SET timestamp_start=%now%
GOTO:EOF
